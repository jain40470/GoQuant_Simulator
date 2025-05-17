import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


class MakerTakerModel:

    def __init__(self):
        
        X = np.random.rand(1000,2)  # b/w 0 to 1
        trade_size = X[:,0]  
        volatility = X[:,1]
        noise = np.random.rand(1000) # noise to avoid overfitting to a perfect pattern
        Y = (1-trade_size) * 0.5 + (1 - volatility) * 0.3 + noise*0.1  # will be in range of 0 to 1
        # maker proportion roughly inversely related to trade size & volatility
        Y = np.clip(Y, 0, 1)  # ensure proportions are between 0 and 1

        self.model = Sequential()
        self.model.add(Dense(64, input_dim=2, activation='relu')) 
        self.model.add(Dense(32, activation='relu'))  
        self.model.add(Dense(1, activation='sigmoid'))  

        self.model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

        self.model.fit(X,Y, epochs=100, batch_size=10, verbose=0)

    def predict_maker_taker(self, trade_size_usd: float, volatility: float) -> float:

        X_input = np.array([[trade_size_usd, volatility]]) 
        return self.model.predict(X_input)[0][0] 