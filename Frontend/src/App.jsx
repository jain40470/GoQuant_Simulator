import React, { useState, useEffect, useRef } from "react";
import InputPanel from "./components/InputPanel";
import OutputPanel from "./components/OutputPanel";
import "./App.css";

const App = () => {
  const [outputData, setOutputData] = useState(null);
  const [errorMsg, setErrorMsg] = useState("");
  const [loading, setLoading] = useState(false);
  const wsRef = useRef(null);

  // Clean up WebSocket on unmount
  useEffect(() => {
    return () => {
      if (wsRef.current) wsRef.current.close();
    };
  }, []);

  const handleSubmit = (inputData) => {
    setLoading(true);
    setErrorMsg("");
    // Close previous WS if any
    if (wsRef.current) {
      wsRef.current.close();
    }

    // Create new WebSocket connection
    const ws = new WebSocket("ws://localhost:8000/ws/simulate");
    wsRef.current = ws;

    ws.onopen = () => {
      // Send input data to backend
      ws.send(JSON.stringify(inputData));
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.error) {
        setErrorMsg(data.error);
      } else {
        setOutputData(data);
      }
      setLoading(false);
    };

    ws.onerror = (error) => {
      console.error("WebSocket error:", error);
      setErrorMsg("WebSocket error, please try again.");
      setLoading(false);
    };

    ws.onclose = () => {
      console.log("WebSocket closed");
      setLoading(false);
    };
  };

  return (
    <div className="flex justify-center items-center py-10 px-100">
      <div
        className="grid grid-cols-2 gap-8 w-full max-w-6xl"
        style={{ gridTemplateRows: "1fr 6fr" }}
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
            onClick={() => setErrorMsg("")}
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
  );
};

export default App;
