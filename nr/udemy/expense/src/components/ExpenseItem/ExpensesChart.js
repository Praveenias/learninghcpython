import Chart from "../chart/Chart";


const ExpensesChart = (props) =>{
    const chartDataPoint = [
        {label:'Jan',value:0},
        {label:'Feb',value:0},
        {label:'Mar',value:0},
        {label:'Api',value:0},
        {label:'May',value:0},
        {label:'Jun',value:0},
        {label:'Jul',value:0},
        {label:'Aug',value:0},
        {label:'Sep',value:0},
        {label:'Oct',value:0},
        {label:'Nov',value:0},
        {label:'Dec',value:0},
    ]

    for(const ex of props.expenses){
        const expenseMonth = ex.date.getMonth();
        chartDataPoint[expenseMonth].value += ex.amount;
    }
    return(
        <Chart datapoints={chartDataPoint}/>
    )
}

export default ExpensesChart;