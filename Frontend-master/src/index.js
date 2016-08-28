import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';
import Login from './components/login';
import Events from './components/events';
import Navbar from './components/navbar';

ReactDOM.render(
  <App>
    <Login />
  </App>,
  document.getElementById('root')
);
