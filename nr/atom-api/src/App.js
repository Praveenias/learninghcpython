
import { Route, Routes } from 'react-router-dom';
import './App.css';
import Header from './Components/Common/header';
import SideNavbar from './Components/Common/side_navbar';
import GetLicense from './Components/license/get_license';
import WelcomePage from './Components/welcome';
import GetSubscriberList from './Components/subscriber/get_subscriber';
import SubscriberUser from './Components/subscriber/subsciber_user';
import MComponentList from './Components/mcomponents/get_mcomp_list';
import RegualtionList from './Components/Regualtion/RegulationList';
import GetBomList from './Components/Bom/GetBomList';



function App() {
  return (
    <div className="App">
      <Header/>
      
      <SideNavbar/>
      <div className='mainclass'>
      <Routes>
        <Route path='/' element={<WelcomePage/>}/>
        <Route path='/license' element={<GetLicense/>}/>
        <Route path='/subscriberlist' element={<GetSubscriberList/>}/>
        <Route path='/subscriberuser' element={<SubscriberUser/>}/>
        <Route path='/mcomplist' element={<MComponentList/>}/>
        <Route path='/regulationlist' element={<RegualtionList/>}/>
        <Route path='/bomlist' element={<GetBomList/>}/>
      </Routes>

      </div>
      


      
    </div>
  );
}

export default App;
