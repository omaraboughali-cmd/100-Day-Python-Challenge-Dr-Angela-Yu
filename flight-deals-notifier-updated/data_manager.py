import requests


SHEETY_ENDPOINT = "https://api.sheety.co/8bd626147e5c625d6dc93203a45aa408/flightDeals/sheet1"

SHEETY_ENDPOINT_1 = 'https://api.sheety.co/8bd626147e5c625d6dc93203a45aa408/flightDeals/users'

class DataManager:

    def __init__(self):

        self.destination_data = []

        self.headers = {

            # "Authorization": "Bearer YOUR_TOKEN"

        }

    def get_destination_data(self):

        """Fetches all rows from the Google Sheet."""

        response = requests.get(url=SHEETY_ENDPOINT, headers=self.headers)

        response.raise_for_status()

        data = response.json()

        self.destination_data = data.get("sheet1", data.get("prices", []))

        return self.destination_data

    def update_destination_codes(self):

        """Updates row entries in Google Sheets with newly found IATA codes."""

        for city in self.destination_data:

            new_data = {

                "sheet1": {

                    "iataCode": city["iataCode"]

                }

            }

            response = requests.put(

                url=f"{SHEETY_ENDPOINT}/{city['id']}",

                json=new_data,

                headers=self.headers

            )

            response.raise_for_status()

    def get_user_data(self):

        
                response = requests.get(url=SHEETY_ENDPOINT_1, headers=self.headers)
        
                response.raise_for_status()
        
                data = response.json()

                # print(data)

                self.user_data = data.get("users", data.get("users", []))

                return self.user_data
                
                