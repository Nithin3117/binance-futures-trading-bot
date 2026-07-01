# Binance Futures Trading Bot

A simple Python application to place Market and Limit orders on the Binance Futures Testnet (USDT-M).

## Features

- Place Market Orders
- Place Limit Orders
- Supports BUY and SELL orders
- Command Line Interface using argparse
- Input validation
- Logging of requests, responses, and errors
- Error handling

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

## Setup

1. Clone the repository

```bash
git clone <repository-url>
```

2. Create and activate a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file

```text
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Run Examples

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

## Assumptions

- Binance Futures Testnet account is active.
- API Key and Secret Key are valid.
- Futures permission is enabled for the API.
