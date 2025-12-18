import React, { useState } from "react";
import apiService from "../../services/api_service";
import "./common.css";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";

const SubscriberSummary = ({ rowData, onClose }) => {
  const [listdata, setListData] = useState([]);
  const [urlParams,setUrlParams] = useState({
    searchBy: "subscriber",
    subscriberId: rowData.subscriberId,
    requestType: "part_lifecycle_status",
    returnType: "summary",
  })

  const regulationOption = ["EU-RoHS","EU-REACH (SVHC List)","EU-REACH (Restricted List)","EU-REACH (Authorization List)","California Prop 65","TSCA"];
  const [requesttype, setrequestType] = useState("part_lifecycle_status");
  const [regulationtype, setrregulationType] = useState("EU-RoHS");
  

  const changedatatobar = (data) => {
    let bar_data = [];
    for (let key in data) {
      let sub_bar = {};
      sub_bar["name"] = key;
      sub_bar["count"] = data[key];
      bar_data.push(sub_bar);
    }
    setListData(bar_data);
  };

  const handleModalClose = () => {
    console.log("close");
    onClose(null, "summary");
  };


  React.useEffect(() => {
    apiService
      .get("api/v1/boms/compliance-status", urlParams)
      .then((response) => {
        changedatatobar(response.data);
        
      })
      .catch((error) => {
        console.log(error);
      });
  }, [urlParams]);

  const getlatestsummary = () =>{
    //setUrlParams({...urlParams});
    const para = {...urlParams};
    if(requesttype==="part_lifecycle_status"){
      para.requestType="part_lifecycle_status"
      delete para.regulationType
    }
    if(requesttype==="compliance"){
      para.requestType="compliance_status";
      para.regulationType=regulationtype;
    }
    console.log(para);
    apiService
      .get("api/v1/boms/compliance-status", para)
      .then((response) => {
        console.log(response.data);
        changedatatobar(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  const setrequest= (e,rtype) =>{
    e.preventDefault();
   // console.log(e.target.value);
    if (rtype === 'requesttype'){
      setrequestType(e.target.value)
      //setUrlParams({...urlParams,'requestType':e.target.value})
      //console.log(urlParams);
    }
    if (rtype === 'regulation'){
      setrregulationType(e.target.value)
    }
  }

  const BarChartComponent = () => {
    return (
      <BarChart width={800} height={300} data={listdata} barGap={5}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="count" fill="#8884d8" />
      </BarChart>
    );
  };
  return (
    <>
      <div
        className="modal fade show modal-xl"
        role="dialog"
        aria-hidden="true"
        style={{ display: "block" }}
      >
        <div className="modal-dialog" role="document">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="exampleModalLabel">
                Subscriber User
              </h5>
              <button
                type="button"
                className="btn btn-secondary"
                aria-label="Close"
                onClick={handleModalClose}
              >
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div className="modal-body">
              <div className="d-flex justify-content-around">
                <p>Subscriber Name: {rowData.companyName}</p>
                <p>Division Name: {rowData.divisionName}</p>
                <p>SIte name: {rowData.siteName}</p>
              </div>
              <div className="row">
                <div className="col">
                  <BarChartComponent />
                </div>
                <div className="col bg-light">
                  <div className="d-flex flex-column justify-content-around ">
                    <select class="custom-select" value={requesttype} onChange={(e)=>setrequest(e,'requesttype')}>
                      <option value="">Select Summary For </option>
                      <option value="part_lifecycle_status">
                        Part Life Cycle
                      </option>
                      <option value="compliance">Compliance</option>
                    </select>
                    <select className="custom-select" value={regulationtype} onChange={(e)=>setrequest(e,'regulation')}>
                      <option value="">Select Regualtion For </option>
                      {regulationOption.map((data1)=>{
                        return(
                        <option value={data1}>{data1}</option>)
                      })};
                      
                    </select>
                    <div className="p-5">
                      <button className="btn btn-primary" onClick={getlatestsummary}>Submit</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-secondary"
                onClick={handleModalClose}
              >
                Close
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default SubscriberSummary;
