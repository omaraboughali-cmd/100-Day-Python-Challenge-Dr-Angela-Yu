class FlightData:

    def __init__(self, price, origin_airport, destination_airport, outbound_date, return_date, stops=0):

        self.price = price

        self.origin_airport = origin_airport

        self.destination_airport = destination_airport

        self.outbound_date = outbound_date

        self.return_date = return_date

        self.stops = stops

    @staticmethod

    def find_cheapest_flight(data):

        """Parses raw JSON data from SerpApi and returns a FlightData object."""

        if not data:

            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

        all_options = data.get("best_flights", []) + data.get("other_flights", [])

        if not all_options:

            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

        cheapest_option = min(all_options, key=lambda x: x.get("price", float("inf")))

        price = cheapest_option.get("price", "N/A")

        flights = cheapest_option.get("flights", [])

        if not flights:

            return FlightData(price, "N/A", "N/A", "N/A", "N/A", "N/A")

        origin = flights[0]["departure_airport"].get("id", "N/A")

        destination = flights[-1]["arrival_airport"].get("id", "N/A")

        outbound_date = flights[0]["departure_airport"].get("time", "N/A")

        return_date = flights[-1]["arrival_airport"].get("time", "N/A")

        stops = len(cheapest_option.get("layovers", []))

        return FlightData(price, origin, destination, outbound_date, return_date, stops)