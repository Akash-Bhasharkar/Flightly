
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class FlightSearch:
    
    def __init__(self) :
        
        self.api_key = os.getenv("API_KEY")
        self.api_name = "https://tequila-api.kiwi.com"
        self.headers_flight = {
                        "apikey" : self.api_key
        }

    def search_flight(self, dates, iata_code, lowest_price) :
        parameters = {
                           
                           "fly_from" : "STN",
                           "fly_to" : iata_code,
                           "date_from" : dates[0],
                           "date_to" : dates[1],
                           "curr" : "USD",
                           "price_to" : lowest_price
        }
        res = requests.get(url = f"{self.api_name}/v2/search", headers = self.headers_flight, params = parameters)
        res.raise_for_status()
        data = res.json()
        data_list = data["data"]
        print(data_list)
        if len(data_list) != 0 :
           price = data_list[0]["price"]
           date_till = data_list[0]["route"][0]["utc_arrival"].split("T")[0]
           return (price, date_till)
        else :
           return ()

    def get_code(self, city) :
        parameters = {
                           "term" : city
        }
        res = requests.get(url = f"{self.api_name}/locations/query", params = parameters, headers = self.headers_flight)
        res.raise_for_status()
        data = res.json()
        return data["locations"][0]["code"]