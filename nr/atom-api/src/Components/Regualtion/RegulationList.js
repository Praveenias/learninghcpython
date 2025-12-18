

import React, { useState } from "react";
import apiService from "../../services/api_service";
import Table from "../Common/table/table";



const RegualtionList = () =>{
  const [regulationList,setRegualtionList] = useState([]);
  const [successdata,setSuccessData] = useState(false);

  const columnName = ["regulationType","regulationName","directiveName","startDate"];

  React.useEffect(()=>{
    apiService.get('api/v1/regulations').then((res)=>{
      console.log(res.data);
      setRegualtionList(res.data)
      setSuccessData(true);
    }).catch((err)=>{
      console.log(err);
    });
  },[]);

  return (
    <>
    <div>
        <div className="subheading">
          <h3>Regulation Details </h3>
        </div>
    </div>
    <div className="m-4">
      {successdata && <Table columns={columnName} data={regulationList} itemsPerPage={10} />}
    </div>
    </>
  )
}


export default RegualtionList