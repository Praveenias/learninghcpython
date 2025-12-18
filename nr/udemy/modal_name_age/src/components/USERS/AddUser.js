import Card from "../UI/Card";
import classes from "./AddUser.module.css";
import Button from "../UI/Button";
import { useState } from "react";
import ErrorModal from "../UI/Errormodal";

const AddUser = (props) => {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [errort,setErrort] = useState();

  const addUserHandler = (e) => {
    e.preventDefault();
    if (name.trim().length === 0 || age.trim().length === 0) {
      setErrort({
        title:'Error',
        message:'Give Valid Name and Age'
      })
      return;
    }
    if (+age < 1) {
        setErrort({
            title:'Error',
            message:'Give Correct Age'
        })
        return;
    }
    props.onAddUser(name, age);
    setAge("");
    setName("");
  };

  const errorHandler = () => {
    setErrort(null);
  }
  return (
    <div>
      {errort && <ErrorModal title={errort.title} message={errort.message} onclose={errorHandler}/>}
      
      <Card className={classes.input}>
        <form onSubmit={addUserHandler}>
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            onChange={(e) => setName(e.target.value)}
            value={name}
          />
          <label htmlFor="userage">Age</label>
          <input
            type="number"
            id="userage"
            onChange={(e) => setAge(e.target.value)}
            value={age}
          />
          <Button type="submit">Add user</Button>
        </form>
      </Card>
    </div>
  );
};

export default AddUser;
