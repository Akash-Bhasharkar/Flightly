import requests
from flight_search import FlightSearch
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class DataManager(FlightSearch):
   
   def __init__(self) : 
       super().__init__()
       self.headers = {
                      "Authorization": os.getenv("AUTH")
       }

       self.api_id = os.getenv("API_ID")

   
   def get_data(self) :
       res = requests.get(url = self.api_id , headers = self.headers)
       res.raise_for_status()
       return res.json()["prices"]

   def update(self) :
       city_list = self.get_data()
       for city in city_list :
            
            parameters = {
                                "price" : {
                                    "iataCode" : self.get_code(city["city"])
                                }
                         }
            res = requests.put(url = f"{self.api_id}/{city['id']}", json = parameters, headers = self.headers)   
            res.raise_for_status()
   
   def add_user(self, user_data) :
       parameters = {
                     "user" : {
                               "firstName" : user_data[0],
                               "lastName" : user_data[1],
                               "email" : user_data[2]
                              }
                    }
       
       res = requests.post(url = "https://api.sheety.co/dc3a224edc1989e87a76468b2c3a74f1/flightDeals/users", json = parameters, headers = self.headers)   
       res.raise_for_status()

   def get_users(self) : 
       res = requests.get(url = "https://api.sheety.co/dc3a224edc1989e87a76468b2c3a74f1/flightDeals/users", headers = self.headers)   
       res.raise_for_status()
       user_list = res.json()["users"]
       email_list = [item["email"] for item in user_list]
       return email_list

