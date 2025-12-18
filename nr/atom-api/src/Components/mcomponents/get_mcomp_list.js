import React, { useState } from "react";
import apiService from "../../services/api_service";
import Table from "../Common/table/table";

const MComponentList = () => {

  const [mccompList,setCompList] = useState([]);
  const [successdata,setSuccessData] = useState(false);
  const columnName = ["manufacturerName","manufacturerPartnumber","manufacturerDescription","partLifecycleStatus","leadTime","stockPosition"]
  
  React.useEffect(() => {
    apiService.get('api/v1/components',{manufacturerPartnumber:"74ALVC164245DLRG4"}).then((response) => {
        console.log(response.data);
        setCompList(response.data);
        setSuccessData(true)
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  return(
    <>
    <div>
        <div className="subheading pb-3">
          <h3>Master Component Details </h3>
        </div>
        <div className="m-4">
        { successdata && <Table columns={columnName} data={mccompList} itemsPerPage={10} />}
        </div>
        
        
    </div>
    </>
  )
}


export default MComponentList;