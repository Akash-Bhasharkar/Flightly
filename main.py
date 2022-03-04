
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager




data = DataManager()
data.update()
data_list = data.get_data()

flight_search = FlightSearch()
notification  = NotificationManager(data_list)
flight_data = FlightData()

email_list = data.get_users()


flight_data.offers(notification, email_list, data_list)

response = input("Want to sign up for exiciting flight deals ?")

while response.lower() == "yes" : 
   first_name = input("Enter first name : ")
   last_name = input("Enter last name : ")
   email = input("Enter email : ")
   email_confirm = input("Comfirm email : ")
   if email == email_confirm :
      response = "no"
      user_data = (first_name, last_name, email)
      data.add_user(user_data)
   else :
        print("Email not matched!")
        again = input("Want to try again? : ")
        response = again
