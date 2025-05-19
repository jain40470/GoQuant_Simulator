import React, { useState } from 'react';
import InputPanel from './components/InputPanel';
import OutputPanel from './components/OutputPanel';
import axios from 'axios';
import './App.css'

const App = () => {

  const [outputData, setOutputData] = useState("null");
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');

  const handleSubmit = async (inputData) => {
    try {
      setLoading(true);
      setErrorMsg('');
      const response = await axios.post('http://localhost:8000/simulate', inputData);
      console.log(response.data)
      setOutputData(response.data);
    } catch (error) {
      console.error('Error fetching output data:', error);
      setErrorMsg("Failed to fetch data from the backend. Please try again" + error);
      setOutputData(null);
    } finally {
      setLoading(false);
    }
  };

  // 

  return (
    <>

<div className="flex justify-center items-center py-10 px-100">
  
  <div 
    className="grid grid-cols-2 gap-8 w-full max-w-6xl"
    style={{ gridTemplateRows: '1fr 6fr' }}
  >
    <div className="bg-white shadow rounded-lg p-6 flex flex-col justify-center items-center text-green-600 text-2xl font-semibold col-span-2">
      GoQuant Market Simulator
    </div>

    <div className="bg-green-100 rounded-lg p-6 shadow flex flex-col">
      <InputPanel onSubmit={handleSubmit} />
    </div>
    <div className="bg-green-50 rounded-lg p-6 shadow flex flex-col">
      <OutputPanel data={outputData} />
    </div>

  </div>

  {errorMsg && (
  <div className="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-red-600 text-white px-6 py-4 rounded shadow-lg z-50 max-w-sm w-full text-center">
    {errorMsg}
    <button
      onClick={() => setErrorMsg('')}
      className="ml-4 text-black font-bold hover:text-gray-200"
      aria-label="Close error popup"
    >
      &times;
    </button>
  </div>

  
)}

{loading && (
  <div className="fixed top-4 left-1/2 transform -translate-x-1/2 bg-green-300 text-black px-4 py-2 rounded shadow">
    Loading...
  </div>
)}

</div>



    </>
    

  );
};

export default App;
