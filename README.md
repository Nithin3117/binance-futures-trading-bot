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

## Setup

1. Clone the repository.
2. Install the required packages using:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Binance Futures Testnet API credentials.

```text
API_KEY=your_api_key
API_SECRET=your_api_secret
```

4. Activate your virtual environment and run the project.

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

- A Binance Futures Testnet account has already been created.
- Valid Testnet API Key and Secret Key are available.
- Futures permission is enabled for the API Key.
- Python 3 and the required packages are installed.

## Output

The application displays:

- Order ID
- Order Status
- Executed Quantity (if available)
- Average Price (if available)

API requests, responses, and errors are stored in `logs/trading.log`.

## Note

- This project works only with the Binance Futures Testnet.
- The `.env` file is not included in this repository for security reasons.

## Author

**Nithin Bollineni**
