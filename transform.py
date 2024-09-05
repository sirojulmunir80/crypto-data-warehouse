from utils import convert_timestamp

def transform_data(df):
    df['openPrice'] = df['openPrice'].astype(float)
    df['lowPrice'] = df['lowPrice'].astype(float)
    df['highPrice'] = df['highPrice'].astype(float)
    df['lastPrice'] = df['lastPrice'].astype(float)
    df['volume'] = df['volume'].astype(float)
    df['bidPrice'] = df['bidPrice'].astype(float)
    df['askPrice'] = df['askPrice'].astype(float)
    df['timestamp'] = df['at'].apply(convert_timestamp)
    return df[['symbol', 'baseAsset', 'quoteAsset', 'openPrice', 'lowPrice', 'highPrice', 
               'lastPrice', 'volume', 'bidPrice', 'askPrice', 'timestamp']]
