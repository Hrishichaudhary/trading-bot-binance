import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging
import logging

setup_logging()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)

    client = get_client()

    print("\n📤 Order Request:")
    print(vars(args))

    response = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    logging.info(f"Order Response: {response}")

    print("\n✅ Order Success:")
    print({
        "orderId": response.get("orderId"),
        "status": response.get("status"),
        "executedQty": response.get("executedQty"),
        "avgPrice": response.get("avgPrice")
    })

except Exception as e:
    logging.error(str(e))
    print(f"\n❌ Error: {str(e)}")