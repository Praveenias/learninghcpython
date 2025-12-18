import { useEffect, useState } from 'react';
import './App.css';
import Addcontact from './components/addcontact';
import ContactList from './components/contactlist';
import Header from './components/header';
import Toaster from './components/toast';
function App() {
  const LOCAL_STORAGE_KEY = 'contacts'
  const [contacts,setcontacts] = useState([]);
  const [toast,settoast] = useState(false);
  const toastTrigger = document.getElementById('liveToastBtn')
  const toastLiveExample = document.getElementById('liveToast')
  if (toastTrigger) {
    toastTrigger.addEventListener('click', () => {
      const toast = new bootstrap.Toast(toastLiveExample)

      toast.show()
  })
}
  
  const addContactHandler = (contact) => {
    setcontacts([...contacts,contact])
  }
  useEffect(()=>{
    const getcont = JSON.parse( localStorage.getItem(LOCAL_STORAGE_KEY));
    if(getcont){
      setcontacts(getcont);
    }
  },[]);

  useEffect(()=>{
    localStorage.setItem(LOCAL_STORAGE_KEY,JSON.stringify(contacts))
  },[contacts])


  return (
    <div className='ui container'>
      <Header/>
      <Addcontact addContactHandler={addContactHandler}/>
      <ContactList contacts={contacts}/>
      <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
          <img src="..." class="rounded me-2" alt="..."/>
          <strong class="me-auto">Bootstrap</strong>
          <small class="text-muted">11 mins ago</small>
          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
      <div class="toast-body">
        Hello, world! This is a toast message.
      </div>
    </div>
    </div>
    
  );
}

export default App;
