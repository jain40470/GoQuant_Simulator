
# 🚀 GoQuant Simulator

**GoQuant Simulator** is a real-time modular simulator built to estimate trading costs like slippage, market impact, and maker-taker fee proportions using live orderbook data from the GoQuant WebSocket feed.
It provides a fast, interactive way to simulate different trade parameters and observe their impact on net cost and execution efficiency.The backend streams **continuous real-time simulation updates every second** based on the latest live orderbook snapshots combined with user inputs, enabling highly responsive and realistic trade cost estimations.


## 🧠 Features

- 📡 **Real-time Orderbook Feed**: Live L2 data via GoQuant WebSocket (OKX BTC-USDT-SWAP).
- 🧮 **Deep Learning Models**: Keras-based models estimate:
  - Maker-Taker Proportions
  - Slippage
- 📊 **Market Impact Modeling**: Almgren–Chriss-style quadratic cost model.
- 🧪 **Simulate Different Trade Scenarios**: Trade size, volatility, fee tiers, and market sides.
- 🧾 **Cost Breakdown**: Outputs slippage, fees, market impact, net cost, and latency.

## 📁 Project Structure

```
GoQuant_Simulator/
├── backend/                 # FastAPI backend with strategy logic and APIs
│   ├── main.py              # Entry point for FastAPI
│   └──services/
│   ├── websocket_client.py      # WebSocket connector 
│   └── orderbook_processor.py   # Realtime L2 orderbook snapshot processor     
|   ├── models/
│   ├── simulation.py            # Main simulation logic
│   ├── frontenddata.py          # Pydantic model for incoming simulation request
│   ├── slippage.py              # DL-based slippage estimator
│   ├── maker_taker.py           # DL-based maker-taker estimator
│   └── market_impact.py         # Almgren-Chriss market impact function
├── frontend/                # React frontend
│   ├── src/
│   └── ...
├── GOquant_Simulator.ipynb  # Jupyter notebook for rough work.
├── README.md
└── requirements.txt         # Python dependencies 

```

---

## 🖥️ Frontend UI

Frontend application built with **React** and **Vite**, enables users to input trading parameters and view real-time simulations of expected trading costs on the OKX exchange.

## Features

- Input trading parameters such as order type, quantity, market side, volatility, and fee tier.
- Real-time cost simulation results based on advanced financial models.
- Clear breakdown of costs including slippage, fees, market impact, and more.

## GoQuant_Simulator/Backend

Backend provides an API to simulate trading costs based on live order book data fetched via WebSocket.

## Features

- Connects to a WebSocket feed to receive real-time order book data.
- Handles CORS for seamless integration with frontend apps running locally.
- Exposes REST API endpoints to accept frontend parameters and return simulation results.
- Calculates trading cost metrics using advanced models on live market data.
- Streams real-time continuous simulation updates over a WebSocket endpoint, allowing the frontend to receive live cost metrics every second during the simulation session.


### 🧠 Models Behind the Scenes

### Slippage Model
- **Purpose:** Estimates the expected slippage or price deviation caused by executing an order relative to the available market liquidity.
- **Inputs:** Trade size (USD), volatility, liquidity
- **Output:** Predicted slippage (price impact cost)
- **Training:** Uses synthetic data combining trade size, volatility, and liquidity with added noise to avoid overfitting.
- **Implementation:** `SlippageModel` class with a Keras neural network.

### Maker-Taker Model
- **Purpose:** Predicts the probability that a trade will execute as a **maker** (adding liquidity) vs a **taker** (removing liquidity).
- **Inputs:** Trade size (normalized), volatility (normalized), liquidity (normalized)
- **Output:** Probability (0 to 1) representing maker proportion
- **Training:** Trained on synthetic patterns where maker probability inversely correlates with trade size and volatility, positively correlates with liquidity.
- **Implementation:** `MakerTakerModel` class with a Keras neural network.

### Market Impact Model
- **Purpose:** Estimates the market impact cost using the Almgren-Chriss quadratic cost function.
- **Inputs:** Trade size (USD)
- **Output:** Estimated market impact cost
- **Formula:**
  ```python
  impact = alpha * trade_size + beta * trade_size**2
  ```
---

## Input Parameters


| Parameter      | Description                                              |
|----------------|----------------------------------------------------------|
| **Exchange**   | Currently supports: OKX                                  |
| **Spot Asset** | Select any asset available on the chosen exchange        |
| **Order Type** | Market (additional types may be supported in the future) |
| **Quantity**   | Approximate USD equivalent (e.g., ~100 USD)              |
| **Market Side**| Buy or Sell side of the order                            |
| **Volatility** | Market volatility parameter (see exchange documentation) |
| **Fee Tier**   | Fee tier based on the exchange's official fee schedule   |

## Output Parameters


| Parameter                  |            Description                                 |
|----------------------------|--------------------------------------------------------|
| **Expected Slippage**      | Estimated price deviation due to order execution       |               
| **Expected Fees**          | Calculated transaction costs based on fee tier         |
| **Expected Market Impact** | Estimated effect of order size on market price         |        
| **Net Cost**               | Total cost combining slippage, fees, and impact        |
| **Maker/Taker Proportion** | Predicted ratio of maker versus taker order fills      |
| **Internal Latency**       | Processing delay measured                              | 



## ⚙️ How It Works


### ✅ Inputs from Frontend

```json
{
  "exchange": "OKX",
  "spotAsset": "BTC-USDT",
  "orderType": "market",
  "quantity": 10000,
  "volatility": 0.05,
  "feeTier": "Tier 2",
  "marketSide": "buy"
}
```

## 🧪 Sample Output

The backend exposes a WebSocket endpoint at `/ws/simulate` that accepts frontend simulation parameters as JSON and streams real-time simulation updates every second based on live orderbook data.

```json
{
  "slippage": 0.0013,
  "fees": 0.35,
  "marketImpact": 0.58,
  "netCost": 0.9313,
  "makerTakerRatio": 0.6247,
  "internalLatency": 0.0124
}
```

---

## 🚀 Getting Started

### 🔧 Backend Setup

```bash
git clone https://github.com/jain40470/GoQuant_Simulator
cd GoQuant_Simulator
pip install -r requirements.txt
uvicorn main:app --reload
```

Make sure the frontend is running at one of the allowed origins:
- `http://localhost:5173`
- `http://127.0.0.1:3000`

### 🧩 Frontend Setup


```bash
git clone https://github.com/jain40470/GoQuant_Simulator/Frontend
cd Frontend
npm install
npm run dev
```

---

## 📡 WebSocket Feed

- Source: `wss://ws.gomarket-cpp.goquant.io/ws/l2-orderbook/okx/BTC-USDT-SWAP`
- Auto reconnect logic built-in
- Orderbook maintained in-memory for accurate simulation snapshots

---

## 📚 Tech Stack

- **Backend**: FastAPI, WebSockets, TensorFlow/Keras
- **Frontend**: React.js (Vite), TailwindCSS
- **Data**: Real-time L2 orderbook (OKX)

---

## 📝 License

This project is licensed under the MIT License.
