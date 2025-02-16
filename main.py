import requests
import board
import time
import os

from adafruit_seesaw.seesaw import Seesaw
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

i2c_bus = board.I2C()
ss = Seesaw(i2c_bus, addr=0x36)

count = 0

while(count < 10):
    #Getting sensor measurements
    moisture = ss.moisture_read()
    temp = ss.get_temp()

    #Getting current date
    now = str(datetime.now())

    #Formatting request body
    data = {
        "date": now,
        "moisture": moisture,
        "temperature": temp
    }

    url = os.getenv('API_URI')

    #attempting api request
    try:
        headers = {"Content-Type": "application/json; charset=utf-8"}
        response = requests.post(url, headers=headers, json=data)

        count += 1
        time.sleep(3)
            
    except requests.exceptions.RequestException as e:
        count += 1
        time.sleep(3)

    
    


