orderbook_snapshot = {"bids": [], "asks": []}

def update_orderbook(data):
    global orderbook_snapshot
    orderbook_snapshot["bids"] = data.get("bids", [])
    orderbook_snapshot["asks"] = data.get("asks", [])

def get_orderbook_snapshot():
    return orderbook_snapshot
