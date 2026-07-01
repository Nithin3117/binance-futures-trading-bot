# Binance Futures Trading Bot

This project was developed as part of a Python Developer internship assignment.

It is a simple command-line application built using Python that places Market and Limit orders on the Binance Futures Testnet.

## Features

- Place Market Orders
- Place Limit Orders
- Supports BUY and SELL orders
- Command-line interface using argparse
- Input validation
- Logging of API requests, responses, and errors
- Exception handling

## Technologies Used

- Python 3
- python-binance
- python-dotenv

## Running the Project

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

## Output

The application displays:

- Order ID
- Order Status
- Executed Quantity (if available)
- Average Price (if available)

All API requests, responses, and errors are saved in `logs/trading.log`.

## Requirements

- Python 3.x
- Binance Futures Testnet Account
- Binance Testnet API Key
- Binance Testnet Secret Key

## Note

- This project works with the Binance Futures Testnet.
- Create a `.env` file and add your own Testnet API Key and Secret Key.
- The `.env` file is not included in this repository for security reasons.

## Author

**Nithin Bollineni**
