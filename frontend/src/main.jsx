import React, {useState} from 'react';
import {createRoot} from 'react-dom/client';

function Experiment() {
  const [count, setCount] = useState(0);
  return <main style={{fontFamily:'Arial', maxWidth:700, margin:'40px auto', padding:20}}>
    <h2>Component state</h2>
    <p>Select the button to update React state. Reload the page to restore its initial value. Compare this with the server-rendered template exercise.</p>
    <button onClick={() => setCount(count + 1)}>Count: {count}</button>
    <p><a href="/course/templates/">Compare with the Django template laboratory</a></p>
  </main>;
}
createRoot(document.getElementById('root')).render(<Experiment />);
