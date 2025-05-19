import React from 'react';

const OutputPanel = ({ data }) => {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Output Parameters</h2>
      {data ? (
 <ul className="grid grid-cols-1 gap-4 text-lg text-green-900">
 {[
   { label: 'Slippage :', value: data.slippage },
   { label: 'Expected Fees :', value: data.fees },
   { label: 'Market Impact :', value: data.marketImpact },
   { label: 'Net Cost :', value: data.netCost },
   { label: 'Maker/Taker Proportion :', value: data.makerTakerRatio },
   { label: 'Internal Latency :', value: data.internalLatency },
 ].map((item, index) => (
   <li
     key={index}
     className="bg-white p-4 rounded-md shadow-sm flex flex-col"
   >
     <span className="font-semibold text-lg">{item.label}</span>
     <span className="text-green-800 font-bold text-xl mt-1 break-words">
       {item.value}
     </span>
   </li>
 ))}
</ul>
      ) : (
        <p className="text-gray-500">Submit input to get results.</p>
      )}
    </div>
  );
};

export default OutputPanel;
