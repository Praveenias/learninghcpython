

import React, { useState } from "react";
import apiService from "../../services/api_service";
import Table from "../Common/table/table";



const GetBomList = () =>{
  const [bomList,setBomList] = useState([]);
  const [successdata,setSuccessData] = useState(false);

  const columnName = ["bomName","description","revision","status","productName","modelName","location","companyName",
  "siteName","divisionName"];



  React.useEffect(()=>{
    apiService.get('api/v1/boms').then((res)=>{
      console.log(res.data);
      setBomList(res.data)
      setSuccessData(true);
    }).catch((err)=>{
      console.log(err);
    });
  },[]);

  return (
    <>
    <div>
        <div className="subheading">
          <h3>Bom Details </h3>
        </div>
    </div>
    <div className="m-4">
      {successdata && <Table columns={columnName} data={bomList} itemsPerPage={10} />}
    </div>
    </>
  )
}


export default GetBomList