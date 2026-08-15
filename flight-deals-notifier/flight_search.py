import os

import requests

from dotenv import load_dotenv


load_dotenv()


IATA_FALLBACKS = {

    "Paris": "CDG",

    "Tokyo": "NRT",

    "New York": "JFK",
    
}


class FlightSearch:

    def __init__(self):

        self.api_key = os.environ.get("API_KEY")

        self.url = "https://serpapi.com/search.json"

    def get_destination_code(self, city_name):

        """Fetches 3-letter IATA code via local lookup or SerpApi autocomplete."""

        city_clean = city_name.strip().title()

        if city_clean in IATA_FALLBACKS:

            return IATA_FALLBACKS[city_clean]

        params = {

            "engine": "google_flights_autocomplete",

            "q": city_name,

            "api_key": self.api_key

        }

        try:

            response = requests.get(self.url, params=params)

            response.raise_for_status()

            data = response.json()

            for suggestion in data.get("suggestions", []):

                code = suggestion.get("id", "")

                if len(code) == 3 and code.isalpha():

                    return code.upper()

        except Exception as e:

            print(f"Error fetching IATA for {city_name}: {e}")

        return "N/A"

    def check_flights(self, origin_city_code, destination_city_code, from_time):

        """Queries SerpApi for Google Flights data between two locations."""

        params = {

            "engine": "google_flights",

            "departure_id": origin_city_code,

            "arrival_id": destination_city_code,

            "outbound_date": from_time,

            'type' : 2,

            "currency": "USD",

            "hl": "en",

            "api_key": self.api_key , 

            'deep_search' : True

        }

        response = requests.get(self.url, params=params)

        response.raise_for_status()

        return response.json()