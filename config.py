import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
    FARMER_PHONE_NUMBER = os.getenv("FARMER_PHONE_NUMBER")

    MOISTURE_SENSOR_PIN = 21  
    RELAY_PIN = 20  
    THRESHOLD = 400  # Adjust based on sensor calibration
