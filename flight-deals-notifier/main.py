from datetime import datetime, timedelta

from dotenv import load_dotenv

from data_manager import DataManager

from flight_search import FlightSearch

from flight_data import FlightData

from notification_manager import NotificationManager


load_dotenv()


# 1. Configuration

ORIGIN_CITY_IATA = "CAI"


# 2. Initialize Classes

data_manager = DataManager()

flight_search = FlightSearch()

notification_manager = NotificationManager()


# 3. Fetch Google Sheet Data

sheet_data = data_manager.get_destination_data()


# 4. Check and fill missing or Knowledge Graph IATA codes

updated = False

for row in sheet_data:

    if not row.get("iataCode") or row.get("iataCode").startswith("/m/"):

        city_name = row["city"]

        iata_code = flight_search.get_destination_code(city_name)

        row["iataCode"] = iata_code

        updated = True

        print(f"Found code for {city_name}: {iata_code}")


if updated:

    data_manager.destination_data = sheet_data

    data_manager.update_destination_codes()

    print("✅ Google Sheet updated with missing IATA codes!")

else:

    print("All rows already have valid IATA codes.")


# 5. Define Travel Dates (Tomorrow to +7 Days)

tomorrow = datetime.now() + timedelta(days=30)

outbound_date = tomorrow.strftime("%Y-%m-%d")

return_date = (tomorrow + timedelta(days=7)).strftime("%Y-%m-%d")


print(f"\nSearching flights from {ORIGIN_CITY_IATA} {outbound_date}\n")


# 6. Loop Destinations, Search Flights, & Compare Prices

for destination in sheet_data:

    dest_code = destination.get("iataCode")

    target_price = destination.get("lowestPrice", float("inf"))

    city_name = destination.get("city")

    if not dest_code or dest_code == "N/A":

        print(f"Skipping {city_name}: Invalid IATA code.")

        continue

    print(f"✈️ Checking flights to {city_name} ({dest_code})...")

    raw_flight_data = flight_search.check_flights(

        origin_city_code=ORIGIN_CITY_IATA,

        destination_city_code=dest_code,

        from_time=outbound_date,

        
    )

    # print(raw_flight_data) 

    cheapest_flight = FlightData.find_cheapest_flight(raw_flight_data)

    if cheapest_flight.price == "N/A":

        print(f"No flights found for {city_name} ({dest_code}).")

        continue

    if cheapest_flight.price < target_price:

        msg = (

            f"🔥 DEAL FOUND for {city_name}!\n"

            f"   Price: ${cheapest_flight.price} (Target: ${target_price})\n"

            f"   Fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}\n"

            f"   Departure time : {cheapest_flight.outbound_date} , Arrival time : {cheapest_flight.return_date}\n"

            f"   Stops: {cheapest_flight.stops}"

        )

        print(msg)

        notification_manager.send_sms(msg)

    else:

        print(f"No deal for {city_name}: Cheapest found is ${cheapest_flight.price} (Target: ${target_price})")