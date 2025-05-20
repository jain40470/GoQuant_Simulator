import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


class SlippageModel:

    def __init__(self):

        print("I am here at Slippage")
    
        X = np.random.rand(1000, 3)
        trade_size = X[:, 0]
        volatility = X[:, 1]
        liquidity = 1 - X[:, 2]    # lower liquidity -> higher slippage
        noise = np.random.rand(1000) * 0.001  # small noise
        
        Y = trade_size * 0.01 + volatility * 0.02 + liquidity * 0.03 + noise

        self.model = Sequential()
        self.model.add(Dense(64, input_dim=3, activation='relu'))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(1, activation='linear'))

        self.model.compile(optimizer=Adam(), loss='mean_squared_error')

        self.model.fit(X, Y, epochs=100, batch_size=10, verbose=0)

    def predict_slippage(self, trade_size_usd: float, volatility: float, liquidity: float) -> float:
        trade_size_scaled = trade_size_usd / (trade_size_usd + 1)  # scales between 0 and 1 for any positive number
        volatility_scaled = volatility / (volatility + 1)
        liquidity_scaled = 1 - (liquidity / (liquidity + 1))  #
        X_input = np.array([[trade_size_scaled, volatility_scaled, liquidity_scaled]])
        prediction = self.model.predict(X_input, verbose=0)[0][0]
        return float(prediction)
  