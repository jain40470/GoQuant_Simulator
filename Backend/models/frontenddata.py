from pydantic import BaseModel

class FrontendData(BaseModel):
    exchange: str
    spotAsset: str
    orderType: str
    quantity: float
    volatility: float
    feeTier: str
    marketSide: str