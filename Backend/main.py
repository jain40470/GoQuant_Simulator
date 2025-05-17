from fastapi import FastAPI
import asyncio
from services.websocket_client import connect_to_websocket
from services.orderbook_processor import get_orderbook_snapshot
from models.simulation import run_simulation

app = FastAPI()

@app.get("/")
def root():
    return {"message": "GoQuant Simulator Backend"}

@app.post("/simulate")
def simulate():
    orderbook_snapshot = get_orderbook_snapshot()
    if not orderbook_snapshot["bids"] or not orderbook_snapshot["asks"]:
        return {"error": "Orderbook snapshot is empty. Please wait for websocket data."}
    result = run_simulation(orderbook_snapshot)
    return result

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(connect_to_websocket())
