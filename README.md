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
