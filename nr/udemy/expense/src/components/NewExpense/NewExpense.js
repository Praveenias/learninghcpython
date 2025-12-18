import "./NewExpense.css";
import ExpenseForm from "./ExpenseForm";
import { useState } from "react";
const NewExpense = (props) => {
  const [showAddNew, setShow] = useState(true);
  const saveExpense = (edata) => {
    const data = { ...edata, id: Math.random().toString() };
    props.onAddExpense(data);
    // console.log(data);
  };
  const changeShowHandler = () =>{
    setShow(!showAddNew)
  }
  if (showAddNew) {
    return (
      <div className="new-expense">
        <button onClick={changeShowHandler}>Add new Expense</button>
      </div>
    );
  }
  return (
    <div className="new-expense">
      <ExpenseForm onSaveExpenseDate={saveExpense} onHideShow={changeShowHandler}/>
    </div>
  );
};

export default NewExpense;
