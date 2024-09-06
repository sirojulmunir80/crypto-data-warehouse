# 🚀 Crypto Data Warehouse with PostgreSQL & Python

This project creates a **Crypto Data Warehouse** by extracting real-time cryptocurrency data from the WazirX API, transforming it, and loading it into a PostgreSQL database. It follows the ETL (Extract, Transform, Load) process, allowing for easy data analysis and querying of cryptocurrency trends.

## 🔍 Project Overview

The goal of this project is to build a data warehouse for real-time cryptocurrency data. It allows you to:

- Extract data from the **WazirX API**.
- Transform and clean the data using **Python** and **Pandas**.
- Load the transformed data into a **PostgreSQL** database.
- Perform SQL queries to analyze trends in cryptocurrency prices, volume, and other key metrics.

## 🛠️ Technologies Used

- **Python**: For scripting the ETL process.
- **PostgreSQL**: Database to store cryptocurrency data.
- **Pandas**: For data transformation and cleaning.
- **Requests**: To make API calls to WazirX.

## 📊 Data Sources

The cryptocurrency data is sourced from the [WazirX API](https://api-wazirx-com.translate.goog/sapi/v1/tickers/24hr?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc), which provides 24-hour statistics for all available cryptocurrency pairs.

## ⚙️ Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/sirojulmunir80/crypto-data-warehouse.git
cd crypto-data-warehouse

### 2. Install Dependencies
```bash
pip install psycopg2 pandas requests

### 3. Set Up PostgreSQL Database
#### 1. reate a new PostgreSQL database:
```bash
CREATE DATABASE crypto_data;
#### 2. Create the necessary tables for storing the crypto data:
```bash
CREATE TABLE IF NOT EXISTS crypto_tickers (
    symbol VARCHAR(50),
    base_asset VARCHAR(50),
    quote_asset VARCHAR(50),
    open_price FLOAT,
    low_price FLOAT,
    high_price FLOAT,
    last_price FLOAT,
    volume FLOAT,
    bid_price FLOAT,
    ask_price FLOAT,
    timestamp TIMESTAMP,
    CONSTRAINT unique_symbol_timestamp UNIQUE (symbol, timestamp)
);









