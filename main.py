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

headers = {"Content-Type": "application/json; charset=utf-8"}
url = os.getenv('API_URI')

count = 0

while(count < 10):
    #Getting sensor measurements
    moisture = ss.moisture_read()
    temp = ss.get_temp()

    #Getting current date
    now = datetime.now()
    year = now.year
    month = now.month

    #Formatting month
    if(month < 10):
        month = f"0{month}"

    #Formatting request body
    data = {
        "date": str(now),
        "moisture": moisture,
        "temperature": rount(((temp * 1.8) + 32), 2),
        "month_year": f"{month}-{year}"
    }

    #attempting api request
    try:
        requests.post(url, headers=headers, json=data)

        count += 1
        time.sleep(3)
            
    except requests.exceptions.RequestException as e:
        count += 1
        time.sleep(3)

    
    


