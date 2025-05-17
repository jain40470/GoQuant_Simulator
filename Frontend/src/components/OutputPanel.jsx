import React from 'react';

const OutputPanel = ({ data }) => {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Output Parameters</h2>
      {data ? (
        <ul className="space-y-2">
          <li><strong>Expected Slippage:</strong> {data.slippage}</li>
          <li><strong>Expected Fees:</strong> {data.fees}</li>
          <li><strong>Expected Market Impact:</strong> {data.marketImpact}</li>
          <li><strong>Net Cost:</strong> {data.netCost}</li>
          <li><strong>Maker/Taker Proportion:</strong> {data.makerTakerRatio}</li>
          <li><strong>Internal Latency:</strong> {data.internalLatency}</li>
        </ul>
      ) : (
        <p className="text-gray-500">Submit input to get results.</p>
      )}
    </div>
  );
};

export default OutputPanel;
