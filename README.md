# Binance Futures Trading Bot

This project was developed as part of a Python Developer internship assignment.

It is a simple command-line application built using Python that places Market and Limit orders on the Binance Futures Testnet.

## Features

- Place Market Orders
- Place Limit Orders
- Supports BUY and SELL orders
- Command-line interface using argparse
- Input validation
- Logging of API requests and responses
- Error handling

## Technologies Used

- Python 3
- python-binance
- python-dotenv

## Installation

Clone the repository

```bash
git clone https://github.com/Nithin3117/binance-futures-trading-bot.git
```

Go to the project folder

```bash
cd binance-futures-trading-bot
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project folder and add your Binance Testnet API credentials.

```text
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Running the Project

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

## Output

The application displays:

- Order ID
- Order Status
- Executed Quantity (if available)
- Average Price (if available)

All API requests, responses, and errors are also saved in `logs/trading.log`.

## Requirements

- Python 3.x
- Binance Futures Testnet Account
- Binance Testnet API Key and Secret Key

## Note

- This project is developed for the Binance Futures Testnet.
- The `.env` file is not included in this repository for security reasons.
- Use your own Testnet API credentials to run the project.

## Author

**Nithin**
