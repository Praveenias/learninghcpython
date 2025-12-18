import { useState } from 'react';
import './App.css';
import Expenses from './components/ExpenseItem/Expenses';
import NewExpense from './components/NewExpense/NewExpense';


const dummy_expenses = [
  {
    id: 'e1',
    title: ' Paper',
    amount: 94.12,
    date: new Date(2022, 7, 14),
  },
  { id: 'e2', title: 'New TV', amount: 799.49, date: new Date(2021, 3, 12) },
  {
    id: 'e3',
    title: 'Car Insurance',
    amount: 294.67,
    date: new Date(2021, 2, 28),
  },
  {
    id: 'e4',
    title: 'New Desk (Wooden)',
    amount: 450,
    date: new Date(2021, 5, 12),
  },
];

function App() {

  const [expenses,setExpenses] = useState(dummy_expenses);

  const addExpenseHandler = (exp)=>{
    console.log(exp);
    setExpenses(prevExpenses =>{
      return [exp,...prevExpenses]
    })
  }
  
  return (
    <div className="App">
      <NewExpense  onAddExpense={addExpenseHandler}/>
      <Expenses data={expenses}/>
    </div>
  );
}

export default App;
