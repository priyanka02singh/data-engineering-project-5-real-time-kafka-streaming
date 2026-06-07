from kafka import KafkaConsumer 
import json 
import psycopg2

consumer = KafkaConsumer(
    'crypto_prices',    
    bootstrap_servers='localhost:9092', 
    auto_offset_reset='earliest', 
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
) 

conn = psycopg2.connect(
    host="localhost",
    database="crypto_db",
    user="airflow",
    password="airflow"
)

cursor = conn.cursor()

print("Listening for crypto prices...") 

for message in consumer:

    data = message.value

    timestamp = data['timestamp']
    price = data['bitcoin_price_usd']

    cursor.execute(
        """ 
        INSERT INTO crypto_prices (timestamp, bitcoin_price_usd) 
        VALUES (%s, %s) 
        """, 
        (timestamp, price)
    )

    conn.commit()

    print(f"Inserted: {data}")
