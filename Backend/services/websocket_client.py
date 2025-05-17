import asyncio
import websockets
import json
from services.orderbook_processor import update_orderbook

async def connect_to_websocket():
    uri = "wss://ws.gomarket-cpp.goquant.io/ws/l2-orderbook/okx/BTC-USDT-SWAP"
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                while True:
                    message = await websocket.recv()
                    data = json.loads(message)
                    update_orderbook(data)
        except Exception as e:
            print(f"WebSocket Error: {e}")
            await asyncio.sleep(5)
