import random, schedule, time

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

webToonDictionary = {
  'Sunday': ["Lore Olympus","The Remarried Empress"],
  'Monday': ["The Boxer","It's Mine"]
}

client = Client(twilio_account, twilio_token)
client.messages.create (
    to= cellphone,
    from_= twilio_number,
    body="This is a test"
)
