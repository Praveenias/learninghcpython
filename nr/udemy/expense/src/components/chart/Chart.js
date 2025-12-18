import "./Chart.css";
import ChartBar from "./ChartBar";

const Chart = (props) => {
console.log(Math.max(1,2));
  const totalMaxValue = Math.max(...(props.datapoints.map(datap=>datap.value)))
  return (
    <div className="chart">
      {props.datapoints.map((datap) => (
        <ChartBar value={datap.value} maxValue={totalMaxValue} label={datap.label} key={datap.label}/>
      ))}
    </div>
  );
};

export default Chart;
