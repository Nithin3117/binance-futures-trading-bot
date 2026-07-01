import argparse

from bot.orders import place_order


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="BUY or SELL")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit price")

    args = parser.parse_args()

    place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )


if __name__ == "__main__":
    main()