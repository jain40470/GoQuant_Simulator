
def calculate_market_impact(trade_size_usd: float, alpha: float = 0.001, beta: float = 0.0001) -> float:  
    
    """
    Almgren-Chriss model to estimate market impact based on trade size.
    Parameters : 
         trade_size_usd: The trade size in USD
         alpha: Linear coefficient (default 0.001)
         beta: Quadratic coefficient (default 0.0001)
    Output : 
         The estimated market impact (how much price moves)
    """
         
    return alpha * trade_size_usd + beta * trade_size_usd**2


