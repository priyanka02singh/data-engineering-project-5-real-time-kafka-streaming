import psycopg2 

# Connect to Postgres 

conn = psycopg2.connect(
    host="postgres_db", 
    database="crypto_db", 
    user="airflow", 
    password="airflow" 
) 

cursor = conn.cursor() 

# Read latest raw records 

cursor.execute("""
    SELECT timestamp, bitcoin_price_usd 
    FROM crypto_prices 
    ORDER BY timestamp ASC 
""") 

rows = cursor.fetchall() 

# Calculate price changes 

previous_price = None 

for row in rows:
    timestamp = row[0] 
    current_price = row[1] 

    if previous_price is None:
        price_change = 0
    else:
        price_change = current_price - previous_price
    
    # Insert into analytics table 
    cursor.execute("""
        INSERT INTO crypto_price_analytics 
        (timestamp, bitcoin_price_usd, price_change) 
        VALUES (%s, %s, %s)
    """, (timestamp, current_price, price_change)) 

    previous_price = current_price 

# Commit changes 

conn.commit() 

print("Transformation complete!") 

# Close connections 
cursor.close()
conn.close()
