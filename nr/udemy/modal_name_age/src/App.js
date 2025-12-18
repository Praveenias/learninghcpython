import React, { useState } from 'react';
import AddUser from './components/USERS/AddUser';
import UserList from './components/USERS/UserList';



function App() {

  const [list,setList] = useState([]);

  const addUserHandler = (uname,uage)=>{
    setList((prev)=>{
      return [...prev,{name:uname,age:uage,id:Math.random().toString()}]
    })
  }
  return (
    <div>
      <AddUser  onAddUser={addUserHandler}/>
      <UserList listdata={list}/>
    </div>
  );
}

export default App;
