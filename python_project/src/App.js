import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [ip, setIp] = useState('');
  const [ports, setPorts] = useState('');

  const handleIpChange = (event) => {
    setIp(event.target.value);
  };

  const handlePortsChange = (event) => {
    setPorts(event.target.value);
  };

  const handleScan = () => {
    const portList = ports.split(',').map(port => parseInt(port, 10));

    axios.get(`http://localhost:8000/?ip=${ip}&port=${ports}`, )
        .then(response => {
          console.log('Scan result:', response.data);
        })
        .catch(error => {
          console.error('Error:', error);
        });
  };

  return (
      <div style={{ padding: '20px' }}>
        <h1>Network Scanner</h1>
        <label htmlFor="ip">Enter IP: </label>
        <input type="text" id="ip" name="ip" value={ip} onChange={handleIpChange} /><br />

        <label htmlFor="ports">Enter Ports (comma-separated): </label>
        <input type="text" id="ports" name="ports" value={ports} onChange={handlePortsChange} /><br />

        <button onClick={handleScan}>Scan</button>
      </div>
  );
}

export default App;
