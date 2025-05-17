import time

from models.market_impact import calculate_market_impact
from models.slippage import SlippageModel
from models.maker_taker import MakerTakerModel

def run_simulation(orderbook):

    top_bid = orderbook['bids'][0] if orderbook['bids'] else None
    top_ask = orderbook['asks'][0] if orderbook['asks'] else None
    print(f"Top Bid: {top_bid} | Top Ask: {top_ask}")

    # Exchange :  (OKX)
    # Spot Asset :  (Any available on the selected exchange)
    # Order Type (market)
    # Quantity : Trade size (~100 USD equivalent)
    # Volatility (market parameter -- see exchanges' docs)
    # Fee Tier (based on exchange documentation)

    # start_time = time.time()

    # trade_size = input_data.quantity_usd
    # volatility = input_data.volatility
    # fee_tier = input_data.fee_tier

    # market_impact = calculate_market_impact(trade_size)

    # slippageModel = SlippageModel()
    # slippage = slippageModel.predict(trade_size, volatility) * trade_size  # scale by trade size

    # maker_taker_model = MakerTakerModel()
    # maker_proportion = maker_taker_model.predict(trade_size, volatility)

    # fees = calculate_fee(trade_size, fee_tier)

    # net_cost = slippage + fees + market_impact

    # latency = time.time() - start_time

    return {
        "message" : "hi"
    }

    # return {
    #     "expected_slippage_usd": round(slippage, 4),
    #     "expected_fees_usd": round(fees, 4),
    #     "expected_market_impact_usd": round(market_impact, 4),
    #     "net_cost_usd": round(net_cost, 4),
    #     "maker_proportion": round(maker_proportion, 4),
    #     "internal_latency_seconds": round(latency, 5),
    # }
