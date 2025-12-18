import { useState } from "react";
import "./ExpenseFrom.css";

const ExpenseForm = (props) => {

  const [userInput,setUserInput] = useState({
    'title':'',
    'amount':'',
    'date':new Date()
  })
  const titleChangeHandler = (e) =>{
    setUserInput((prevState)=>{
        return{...prevState,title:e.target.value}
    })
  }
  const dateChangeHandler = (e) =>{
    setUserInput((prevState)=>{
        return{...prevState,date:e.target.value}
    })
  }
  const amountChangeHandler = (e) =>{
    setUserInput((prevState)=>{
        return{...prevState,amount:e.target.value}
    })
  }

  const submitHandler = (e)=>{
    e.preventDefault();
    props.onSaveExpenseDate(userInput);
    props.onHideShow()
    setUserInput(prev=>{
      return{prev}
    })
  }
  return (
    <form onSubmit={submitHandler}>
      <div className="new-expense__controls">
        <div className="new-expense__control">
          <label>Title</label>
          <input type="text" onChange={titleChangeHandler} value={userInput.title}/>
        </div>
        <div className="new-expense__control">
          <label>Amount</label>
          <input type="number" onChange={amountChangeHandler} value={userInput.amount}/>
        </div>
        <div className="new-expense__control">
          <label>Date</label>
          <input type="date" min='2019-01-01' max='2023-12-31' onChange={dateChangeHandler} value={ new Date(userInput.date)}/>
        </div>
      </div>
      <div className="new-expense__actions">
        <button onClick={()=>props.onHideShow()}>Cancel</button>
        <button type="submit">Submit</button>
        
      </div>
    </form>
  );
};

export default ExpenseForm;
