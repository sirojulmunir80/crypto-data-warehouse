from extract import extract_data
from transform import transform_data
from load import load_data

url = "https://api-wazirx-com.translate.goog/sapi/v1/tickers/24hr?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc"
conn_params = {
    'dbname': 'crypto_data',
    'user': 'postgres',
    'password': 'xxxxxxx',
    'host': 'localhost',
    'port': '5432'
}

if __name__ == "__main__":
    df = extract_data(url)
    cleaned_data = transform_data(df)
    load_data(cleaned_data, conn_params)
