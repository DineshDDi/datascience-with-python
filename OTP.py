import random
from twilio.rest import Client

otp = random.randint(0000, 9999)
print(otp)
account = 'Find from your twilio account'
auth = 'Find from your twilio account'
client = Client(account,auth)

message = client.message.create(
    body= "Your OTP is"+ str(otp),
    from_= "56567",
    to = "9176528966"
)

print(message.sid)



