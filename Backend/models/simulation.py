import time

from models.market_impact import calculate_market_impact
from models.slippage import SlippageModel
from models.maker_taker import MakerTakerModel


# INPUT
# exchange 
# spotAsset
# orderType
# quantity
# volatility
# feeTier
# marketSide

# Exchange :  (OKX)
# Spot Asset :  (Any available on the selected exchange)
# Order Type (market)
# Quantity : Trade size (~100 USD equivalent)
# Volatility (market parameter -- see exchanges' docs)
# Fee Tier (based on exchange documentation)


def run_simulation(input_data , orderbook):

    top_bid = orderbook['bids'][0] if orderbook['bids'] else None
    top_ask = orderbook['asks'][0] if orderbook['asks'] else None
    print(f"Top Bid: {top_bid} | Top Ask: {top_ask}")

    trade_size = input_data.quantity
    volatility = input_data.volatility
    fee_tier = input_data.feeTier

    start_time = time.time()

    # market_impact = calculate_market_impact(trade_size)

    # slippageModel = SlippageModel()
    # slippage = slippageModel.predict(trade_size, volatility) * trade_size 

    # maker_taker_model = MakerTakerModel()
    # maker_proportion = maker_taker_model.predict(trade_size, volatility)

    # fees = calculate_fee(trade_size, fee_tier)

    # net_cost = slippage + fees + market_impact

    latency = time.time() - start_time

    return {
        "slippage": "slippage",
        "fees": "Hiiii",
        "marketImpact": "market_impact",
        "netCost": "Hiii",
        "makerTakerRatio": "maker_proportion",
        "internalLatency": latency,
    }
