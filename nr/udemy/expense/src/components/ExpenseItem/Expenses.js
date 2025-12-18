import { useState } from "react";
import ExpenseFilter from "./ExpenseFilter";
import ExpenseItem from "./ExpenseItem";
import "./Expenses.css";
import ExpensesChart from "./ExpensesChart";

function Expenses(props) {
  const expenses = props.data;
  const [year, setYear] = useState("2022");
  const filteredYear = (ye) => {
    setYear(ye);
  };

  const filteredYearExpenses = expenses.filter(exp=>{
    return exp.date.getFullYear().toString() === year;
  })
  return (
    <div className="expenses">
      <ExpenseFilter selected={year} onChangeFilter={filteredYear} />
      <ExpensesChart expenses={filteredYearExpenses}/>
      {filteredYearExpenses.length === 0 && <p>No Expense Found</p>}
      {filteredYearExpenses.length >0 && filteredYearExpenses.map((expense) => (
        <ExpenseItem data={expense} key={expense.id} />
      ))}
    </div>
  );
}

export default Expenses;
