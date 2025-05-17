import React, { useState } from 'react';

const InputPanel = ({ onSubmit }) => {

  const [formData, setFormData] = useState({
    exchange: 'OKX',
    spotAsset: 'BTC/USDT',
    orderType: 'market',
    quantity: 100,
    volatility: 'medium',
    feeTier: 'Tier 1',
    marketSide: 'buy',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };


  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Input Parameters</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block font-medium">Exchange</label>
          <select name="exchange" value={formData.exchange} onChange={handleChange} className="w-full p-2 border rounded">
            <option value="OKX">OKX</option>
          </select>
        </div>

        <div>
          <label className="block font-medium">Spot Asset</label>
          <select name="spotAsset" value={formData.spotAsset} onChange={handleChange} className="w-full p-2 border rounded">
            <option value="BTC/USDT">BTC/USDT</option>
            <option value="ETH/USDT">ETH/USDT</option>
            <option value="SOL/USDT">SOL/USDT</option>
          </select>
        </div>

        <div>
          <label className="block font-medium">Order Type</label>
          <select name="orderType" value={formData.orderType} onChange={handleChange} className="w-full p-2 border rounded">
            <option value="market">Market</option>
          </select>
        </div>

        <div>
          <label className="block font-medium">Order Side</label>
          <select name="marketSide" value={formData.marketSide} onChange={handleChange} className="w-full p-2 border rounded">
            <option value="buy">Buy</option>
            <option value="sell">Sell</option>
          </select>
        </div>

        <div>
          <label className="block font-medium">Quantity (USD)</label>
          <input type="number" name="quantity" value={formData.quantity} onChange={handleChange} className="w-full p-2 border rounded" />
        </div>

        <div>
        <label className="block font-medium">Volatility</label>
        <input
            type="number"
            name="volatility"
            value={formData.volatility}
            onChange={handleChange}
            className="w-full p-2 border rounded"
            step="0.01"
            placeholder="e.g. 0.05"
            />
        </div>

        <div>
          <label className="block font-medium">Fee Tier</label>
          <select name="feeTier" value={formData.feeTier} onChange={handleChange} className="w-full p-2 border rounded">
            <option value="Tier 1">Tier 1</option>
            <option value="Tier 2">Tier 2</option>
            <option value="Tier 3">Tier 3</option>
          </select>
        </div>

        <button type="submit" className="bg-green-600 text-green px-4 py-2 rounded hover:bg-blue-700">Submit</button>

      </form>
    </div>
  );
};

export default InputPanel;
