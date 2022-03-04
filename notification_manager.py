from flight_data import FlightData
import smtplib
class NotificationManager(FlightData):
      
      def __init__(self, city_list) :
          super().__init__()
          
          self.is_available = self.structure(city_list)
          if self.is_available != False :
             self.send_mail(self.is_available)

      def send_mail(self, message, email = "Your_email") :
          with smtplib.SMTP("smtp.gmail.com") as connection :
               connection.starttls()
               connection.login(user = "Your_email", password = "Password")
               connection.sendmail(
                            from_addr = "Your_email",
                            to_addrs = "Your_email",
                            msg = f"Subject:Flight Update\n\n{message}"
                    )