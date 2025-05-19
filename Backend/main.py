from fastapi import FastAPI
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from services.websocket_client import connect_to_websocket
from services.orderbook_processor import get_orderbook_snapshot
from models.simulation import run_simulation
from models.frontenddata import FrontendData

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],               # Allow all HTTP methods
    allow_headers=["*"],               # Allow all headers
)

@app.get("/")
def root():
    return {"message": "GoQuant Simulator Backend"}

@app.post("/simulate")
def simulate(input : FrontendData):
    orderbook_snapshot = get_orderbook_snapshot()
    if not orderbook_snapshot["bids"] or not orderbook_snapshot["asks"]:
        return {"error": "Orderbook snapshot is empty. Please wait for websocket data."}
    print(input)
    result = run_simulation(input,orderbook_snapshot)
    return result

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(connect_to_websocket())
