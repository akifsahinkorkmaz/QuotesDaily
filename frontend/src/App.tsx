import React from 'react';
import logo from './logo.svg';
import {
  Routes,
  Route,
} from "react-router-dom";
import './App.css';
import Home from './pages/Home';

function App() {
  return (
    <Routes>
      <Route path=''  element={<Home />}/>
    </Routes>
  );
}

export const apiurl: string = "http://localhost:8000/";
export default App;

