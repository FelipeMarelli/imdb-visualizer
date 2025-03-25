import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

export const API_BASE_URL = "http://127.0.0.1:8000";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <App/>
  </React.StrictMode>
);