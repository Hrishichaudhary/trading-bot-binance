# Binance Futures Trading Bot (CLI)

## 📌 Overview
This project is a simplified trading bot built in Python that simulates order placement on Binance Futures (USDT-M). It supports both MARKET and LIMIT orders via a command-line interface (CLI), with proper validation, logging, and modular structure.

---

## 🚀 Features
- Place **MARKET** and **LIMIT** orders
- Supports both **BUY** and **SELL**
- CLI-based input using argparse
- Input validation and error handling
- Structured modular code (client, orders, validators, logging)
- Logging of requests, responses, and errors to a log file

---

## 🗂️ Project Structure
```
trading_bot/
│
├── assets/
│ ├── market_order.png
│ ├── limit_order.png
│ └── Log-Output.png
│
├── bot/
│ ├── init.py
│ ├── client.py # Client (Mock / API wrapper)
│ ├── orders.py # Order placement logic
│ ├── validators.py # Input validation
│ ├── logging_config.py
│
├── cli.py # CLI entry point
├── requirements.txt
├── README.md
├── bot.log # Sample log output
```

## ⚙️ Setup Instructions

### 1. Clone the repository:
    git clone https://github.com/Hrishichaudhary/trading-bot-binance.git
    cd trading-bot

### 2. Install dependencies:
    pip install -r requirements.txt

# ▶️ How to Run

### MARKET Order:
        python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
    
### LIMIT Order:
        python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

# Sample Outputs:

## 📊 Market Order Output:
![Market Order](assets/market_order.png)

## 📊 Limit Order Output:
![Limit Order](assets/limit_order.png)

## 📝 Logging

### All API interactions and responses are logged in:
        bot.log

## 📊 Log Output:
![Log Output](assets/Log-Output.png)

## ⚠️ Assumptions

* Binance Futures Testnet API access was restricted (KYC and environment limitations).
* A mock client is used to simulate order execution.
* The system is fully structured and ready for real API integration when valid credentials are available.

## 📌 Notes

* The project demonstrates real-world backend design practices.
* API layer is abstracted for easy replacement with real Binance API.
* Logging ensures traceability of all operations.

## 👤 Author

### Hrishikesh Kumar Chaudhary
###### 📧 hrishikesh.kr.chaudhary16@gmail.com

###### 📞 +91 8100448947