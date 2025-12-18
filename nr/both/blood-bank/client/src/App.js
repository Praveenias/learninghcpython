import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Routes, Route} from 'react-router-dom';
import Login from "./components/login.js"
import Regsiter from "./components/register"
import Donate from './components/donate.js';
import Request from './components/request.js';
import User from './components/userpage.js';
import Table from './components/table.js';
import Update from './components/update.js';
import Delete from './components/delete.js';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route  path='/' element={<Login/>} />
        <Route path='/Register' element={<Regsiter/>} />
        <Route path='/Donate' element={<Donate/>} />
        <Route path='/request' element={<Request/>} />
        <Route path='/user' element={<User/>} />
        <Route path='/table' element={<Table/>} />
        <Route path='/update' element={<Update/>} />
        <Route path='/delete' element={<Delete/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
