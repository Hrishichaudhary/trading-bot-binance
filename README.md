# Binance Futures Trading Bot (CLI)

## 📌 Overview
This project is a simplified trading bot built in Python that simulates order placement on Binance Futures (USDT-M). It supports both MARKET and LIMIT orders via a command-line interface (CLI), with proper validation, logging, and modular structure.

---

## 🚀 Features
- Place **MARKET** and **LIMIT** orders
- Supports both **BUY** and **SELL**
- CLI-based input using argparse
- Input validation
- Structured modular code (client, orders, validators, logging)
- Logging of requests, responses, and errors

---

## 🗂️ Project Structure
```
trading_bot/
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

---

## ⚙️ Setup Instructions

1. Clone the repository:
```bash
git clone <your-repo-link>
cd trading_bot

2. Install dependencies:
    pip install -r requirements.txt

▶️ How to Run

🔹 MARKET Order:
    python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

🔹 LIMIT Order:
    python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## 📊 Market Order Output
![Market Order](assets/market_order.png)

## 📊 Limit Order Output
![Limit Order](assets/limit_order.png)

## 📊 Log Output
![Log Output](output/Log-Output.png)
        
👤 Author

Hrishikesh K. Chaudhary

