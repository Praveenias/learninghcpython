import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Header from "./components/Header";
import Home from "./components/Home";
import Card from "./components/Card";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <div className="App">
        <Routes>
          <Route path="/" Component={Home}/>
          <Route path="/card" Component={Card} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
