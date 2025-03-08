import serial
import os
from flask import Blueprint, jsonify
from twilio.rest import Client
from config import Config

bp = Blueprint('main', __name__)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def send_sms_alert(message):
    client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=Config.TWILIO_PHONE_NUMBER,
        to=Config.FARMER_PHONE_NUMBER
    )

@bp.route('/read-soil', methods=['GET'])
def read_soil_moisture():
    ser.write(b'READ\n')
    data = ser.readline().decode('utf-8').strip()
    
    try:
        moisture = int(data)
        if moisture < Config.THRESHOLD:  # Below threshold, start watering
            ser.write(b'ON\n')
            send_sms_alert(f"Low moisture detected: {moisture}. Watering started.")
            return jsonify({"moisture": moisture, "status": "Watering started"})
        else:
            ser.write(b'OFF\n')
            return jsonify({"moisture": moisture, "status": "Soil is wet enough"})
    except ValueError:
        return jsonify({"error": "Invalid sensor data"}), 500

@bp.route('/control-pump/<state>', methods=['GET'])
def control_pump(state):
    if state.upper() == "ON":
        ser.write(b'ON\n')
        return jsonify({"status": "Pump turned ON"})
    elif state.upper() == "OFF":
        ser.write(b'OFF\n')
        return jsonify({"status": "Pump turned OFF"})
    return jsonify({"error": "Invalid state"}), 400
