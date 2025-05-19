import time

from models.market_impact import calculate_market_impact
from models.slippage import SlippageModel
from models.maker_taker import MakerTakerModel


# Input_data
# exchange: str
# spotAsset: str
# orderType: str
# quantity: float
# volatility: float
# feeTier: str
# marketSide: str


def run_simulation(input_data , orderbook):

    slippage_model = SlippageModel()
    maker_taker_model = MakerTakerModel()

    FEE_TIERS = {
    "Tier 1": {"maker": 0.0002, "taker": 0.0007},
    "Tier 2": {"maker": 0.00015, "taker": 0.0005},
    "Tier 3": {"maker": 0.0001, "taker": 0.0003},
    }

    start_time = time.time()

    top_bid = orderbook['bids'][0] if orderbook['bids'] else None
    top_ask = orderbook['asks'][0] if orderbook['asks'] else None
  
    trade_size_usd = input_data.quantity  # already in usd

    # if not 
    # exec_price = top_ask[0] if market_side == "buy" else top_bid[0]
    # trade_size_usd = quantity * exec_price

    volatility = input_data.volatility
    market_side = input_data.marketSide.lower()  # "buy" or "sell"
    order_type = input_data.orderType.lower()

    fee_tier = FEE_TIERS.get(input_data.feeTier, FEE_TIERS["Tier 1"])
    is_taker = order_type == "market"
    fee_rate = fee_tier["taker"] if is_taker else fee_tier["maker"]

    if market_side == 'buy':
        liquidity = sum([float(ask[1]) for ask in orderbook['asks']])
    elif market_side == 'sell':
        liquidity = sum([float(bid[1]) for bid in orderbook['bids']])


    slippage = slippage_model.predict_slippage(trade_size_usd, volatility, liquidity)
    maker_proportion = maker_taker_model.predict_maker_taker(trade_size_usd,volatility,liquidity) 
    market_impact = calculate_market_impact(trade_size_usd)

    fees = fee_rate * trade_size_usd
    net_cost = slippage + market_impact + fees

    latency = time.time() - start_time

    return {
        "slippage": float(slippage),
        "fees": float(fees),
        "marketImpact": float(market_impact),
        "netCost": float(net_cost),
        "makerTakerRatio": float(maker_proportion),
        "internalLatency": float(latency),
    }
