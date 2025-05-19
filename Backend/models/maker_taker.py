import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class MakerTakerModel:

    def __init__(self):
        X = np.random.rand(1000, 3)   # b/w 0 to 1
        trade_size = X[:, 0]
        volatility = X[:, 1]
        liquidity = 1 - X[:, 2]  
        noise = np.random.rand(1000)   # noise to avoid overfitting to a perfect pattern

        # maker proportion roughly inversely related to trade size & volatility
        Y = (1 - trade_size) * 0.4 + (1 - volatility) * 0.3 + liquidity * 0.3 + noise * 0.05
        Y = np.clip(Y, 0, 1)

        self.model = Sequential()
        self.model.add(Dense(64, input_dim=3, activation='relu'))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(optimizer=Adam(), loss='binary_crossentropy')
        self.model.fit(X, Y, epochs=100, batch_size=10, verbose=0)

    def predict_maker_taker(self, trade_size_usd: float, volatility: float, liquidity: float) -> float:
        X_input = np.array([[trade_size_usd, volatility, liquidity]])
        pred = self.model.predict(X_input)[0][0]
        return float(pred)
