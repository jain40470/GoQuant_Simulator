from fastapi import FastAPI
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from services.websocket_client import connect_to_websocket
from services.orderbook_processor import get_orderbook_snapshot
from models.simulation import run_simulation
from models.frontenddata import FrontendData
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

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


@app.websocket("/ws/simulate")
async def websocket_simulate(websocket: WebSocket):
    await websocket.accept()
    try:
        # Receive input data from frontend as JSON string
        input_text = await websocket.receive_text()
        input_data = json.loads(input_text)

        while True:
            orderbook_snapshot = get_orderbook_snapshot()
            if not orderbook_snapshot["bids"] or not orderbook_snapshot["asks"]:
                await websocket.send_json({"error": "Orderbook not ready yet. Please wait..."})
            else:
                # Run simulation with current input and live orderbook
                result = run_simulation(input_data, orderbook_snapshot)
                await websocket.send_json(result)
            await asyncio.sleep(1)  # send updates every second

    except WebSocketDisconnect:
        print("Client disconnected from simulation websocket")
    except Exception as e:
        print(f"Error in /ws/simulate: {e}")
        await websocket.close()
        
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(connect_to_websocket())
