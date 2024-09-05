import psycopg2

def load_data(df, conn_params):
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO crypto_tickers (symbol, base_asset, quote_asset, open_price, low_price, high_price, 
                                        last_price, volume, bid_price, ask_price, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['symbol'], row['baseAsset'], row['quoteAsset'], row['openPrice'], row['lowPrice'], row['highPrice'],
            row['lastPrice'], row['volume'], row['bidPrice'], row['askPrice'], row['timestamp']
        ))
    conn.commit()
    cursor.close()
    conn.close()
