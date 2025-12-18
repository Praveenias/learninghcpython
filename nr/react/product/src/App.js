
import './App.css';
import { Route, Routes } from 'react-router-dom';
import InputForm from './components/form';
import Display from './components/show';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/form' element={<InputForm/>}/>
        <Route path='/' element={<Display/>}/>
      </Routes>
    </div>
  );
}

export default App;
