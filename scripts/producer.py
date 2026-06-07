from kafka import KafkaProducer 
import requests
import json 
import time 
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092', 
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
) 

URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

while True:

    try:
 
        response = requests.get(URL) 
        data = response.json()

        bitcoin_price = data['bitcoin']['usd']

        message = {
            "timestamp": str(datetime.now()),
            "bitcoin_price_usd": bitcoin_price
        }

        producer.send('crypto_prices', value=message)

        print(f"Sent: {message}")

    except Exception as e:
        print(f"Error occurred: {e}")

    time.sleep(5)
    
