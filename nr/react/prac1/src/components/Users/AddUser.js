import React from "react";
import classes from './AddUse.Module.css'

const AddUser = props => {
  const addUserHandler = (event) =>{
    event.preventDefaukt();
  };

  return (
    <form onSubmit={addUserHandler}>
      <label htmlFor="username">Username</label>
      <input id="username" type="text"/>
      <label htmlFor="age">Age</label>
      <input id="age" type="number"/>
      <button type="submit">Adduser</button>
    </form>
  )
};

export default AddUser