import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class SlippageModel:

    def __init__(self):

        X = np.random.rand(1000,3) 
        trade_size = X[:,0]
        volatility = X[:,1]
        liquidity =  (1 - X[:, 2])  # lower liquidity -> higher slippage
        noise = np.random.rand(1000) # noise to avoid overfitting to a perfect pattern
        Y = trade_size * 0.01 + volatility * 0.02 +  liquidity*0.03 + noise*0.001

        # In real case : we will be training the model on real data.

        self.model = Sequential()
        self.model.add(Dense(64, input_dim=3, activation='relu')) 
        self.model.add(Dense(32, activation='relu')) 
        self.model.add(Dense(1, activation='linear')) 

        self.model.compile(optimizer=Adam(), loss='mean_squared_error')
        self.model.fit(X,Y, epochs=100, batch_size=10, verbose=0)
        
    def predict_slippage(self, trade_size_usd: float, volatility: float,liquidity : float) -> float:

        X_input = np.array([[trade_size_usd, volatility,liquidity]])  
        
        return self.model.predict(X_input)[0][0]  