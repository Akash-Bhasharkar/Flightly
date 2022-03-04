from flight_search import FlightSearch
from datetime import datetime, timedelta


class FlightData(FlightSearch):
      
      def __init__(self) : 
          super().__init__()
          today = datetime.now() + timedelta(days = 1)
          date_from = today.strftime("%d/%m/%Y")
          self.message_date = today.strftime("%Y-%m-%d")
          date_to = (today + timedelta(days = 6 * 30)).strftime("%d/%m/%Y")

          self.dates = (date_from, date_to)

      def structure(self, city_list) : 
          
          for city in city_list :
              city_iata = city["iataCode"]
              city_price = city["lowestPrice"]
              
              flight_available = self.search_flight(self.dates, city_iata, city_price)
              if len(flight_available) != 0 : 
                 return f"Low price alert! Fly from London-STN to {city['city']}-{city_iata}, from {self.message_date} to {flight_available[1]} only at ${flight_available[0]}."
          return False

      def offers(self, note, email_list, city_list) :
        for city in city_list :
                  city_iata = city["iataCode"]
                  city_price = city["lowestPrice"]
              
                  flight_available = self.search_flight(self.dates, city_iata, city_price)
                  print(flight_available)
                  if len(flight_available) != 0 : 
                     single_message = f"Low price alert! Fly from London-STN to {city['city']}-{city_iata}, from {self.message_date} to {flight_available[1]} only at ${flight_available[0]}.\n"
                     with open("Flight offers.txt", mode = "a") as file : 
                          file.write(single_message)
        for item in email_list :
              with open("Flight offers.txt", mode = "r") as file : 
                   message = file.read()  
                   note.send_mail(message, email = item)
        open("Flight offers.txt", mode = "w")   
          
          

    