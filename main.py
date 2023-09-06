import requests #import requests module
from twilio.rest import Client #import twilio Client module
import timer

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACedc455f2accadd670f3r42f4bf4c852d"
auth_token = "3f7d2be27f051516a102c12be11059a278"
client = Client(account_sid, auth_token)



MY_LATITUDE = 145 #Enter your location's latitude
MY_LONGITUDE = -37.8 #Enter your location's longitude
USER_PHONE_NUMBER = "+61429587343" #Enter the mobile number where you want to receive the notifications
TWILIO_ACCOUNT_MOBILE_NUMBER = "+12215377122"

# 'accuracy' variable determines the area where you want to cath the ISS. Bigger number means larger area in the sky.
accuracy = 10

# Send GET request to ISS API to get current longitude and latitude
data = requests.get("http://api.open-notify.org/iss-now.json").json()

# Convert longitude and latitudes into floting point numbers
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Run the program in infinite loop
while True:
    #Wait 5 secs
    timer.sleep(5)
    # Check if the ISS station is within the range
    if  (MY_LATITUDE - accuracy <= iss_latitude <= MY_LATITUDE + accuracy) and (MY_LONGITUDE - accuracy <= iss_longitude <= MY_LONGITUDE + accuracy):
        print("ISS is over the user")
        #Notify the user by sending SMS
        message = client.messages \
        .create(
            body='ISS is above you, Look Up!',
            from_= TWILIO_ACCOUNT_MOBILE_NUMBER,
            to= USER_PHONE_NUMBER
        )



