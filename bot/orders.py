from binance.enums import *
from binance.exceptions import BinanceAPIException
from bot.client import get_client
from bot.validators import validate_order
from bot.logging_config import logger


client = get_client()


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": str(quantity)
        }

        if order_type.upper() == "LIMIT":
            params["price"] = str(price)
            params["timeInForce"] = TIME_IN_FORCE_GTC

        logger.info(f"Order Request: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"Order Response: {response}")

        print("\nOrder Placed Successfully")
        print(f"Order ID : {response.get('orderId')}")
        print(f"Status   : {response.get('status')}")

        if response.get("executedQty"):
            print(f"Executed Quantity : {response.get('executedQty')}")

        if response.get("avgPrice"):
            print(f"Average Price     : {response.get('avgPrice')}")
    
    except BinanceAPIException as e:
        logger.error(e.message)
        print(f"\nBinance Error: {e.message}")

    except Exception as e:
        logger.error(str(e))
        print(f"\nError: {e}")