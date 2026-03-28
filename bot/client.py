class MockClient:
    def new_order(self, **kwargs):
        return {
            "orderId": 123456,
            "status": "FILLED",
            "executedQty": kwargs.get("quantity"),
            "avgPrice": kwargs.get("price", "MARKET_PRICE")
        }

def get_client():
    return MockClient()