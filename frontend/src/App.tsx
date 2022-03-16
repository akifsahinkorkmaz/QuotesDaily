import {
  Routes,
  Route,
} from "react-router-dom";
import './App.css';
import Home from './pages/Home';

function App() {
  return (
    <Routes>
      <Route path='/:shareurl'  element={<Home />}/>
      <Route path=''  element={<Home />}/>
    </Routes>
  );
}

export const apiurl: string = "http://localhost:8000/";
export const baseurl: string = "http://localhost:3000/";
export default App;

