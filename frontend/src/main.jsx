import React, {useState} from 'react';
import {createRoot} from 'react-dom/client';

function Experiment() {
  const [count, setCount] = useState(0);
  return <main style={{fontFamily:'Arial', maxWidth:700, margin:'40px auto', padding:20}}>
    <h1>JSX component served with Django</h1>
    <p>Vite compiles this source into JavaScript. Copy dist into Django static assets and embed the built module as documented in the README.</p>
    <button onClick={() => setCount(count + 1)}>Count: {count}</button>
    <p><a href="http://127.0.0.1:8000/course/templates/">Compare with the Django template laboratory</a></p>
  </main>;
}
createRoot(document.getElementById('root')).render(<Experiment />);
