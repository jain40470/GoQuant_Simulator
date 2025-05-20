from fastapi import FastAPI
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from services.websocket_client import connect_to_websocket
from services.orderbook_processor import get_orderbook_snapshot
from models.simulation import run_simulation
from models.frontenddata import FrontendData
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from models.slippage import SlippageModel
from models.maker_taker import MakerTakerModel

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],               
    allow_headers=["*"],              
)

@app.get("/")
def root():
    return {"message": "GoQuant Simulator Backend"}


@app.websocket("/ws/simulate")
async def websocket_simulate(websocket: WebSocket):
    await websocket.accept()
    try:
    
        input_text = await websocket.receive_text()
        try:
            input_obj = FrontendData.parse_raw(input_text)
            input_data = input_obj.dict() 
        except Exception as parse_error:
            await websocket.send_json({"error": f"Invalid input: {str(parse_error)}"})
            await websocket.close()
            return

        while True:
            orderbook_snapshot = get_orderbook_snapshot()
            if not orderbook_snapshot["bids"] or not orderbook_snapshot["asks"]:
                await websocket.send_json({"error": "Orderbook not ready yet. Please wait..."})
            else:
                # Run simulation with current input and live orderbook
                result = run_simulation(input_data, orderbook_snapshot, maker_taker_model, slippage_model)
                await websocket.send_json(result)
            await asyncio.sleep(1)  # send updates every second

    except WebSocketDisconnect:
        print("Client disconnected from simulation websocket")
    except Exception as e:
        print(f"Error in /ws/simulate: {e}")
        await websocket.close()
        
@app.on_event("startup")
async def startup_event():
    global maker_taker_model, slippage_model
    maker_taker_model = MakerTakerModel()
    slippage_model = SlippageModel()
    asyncio.create_task(connect_to_websocket())
