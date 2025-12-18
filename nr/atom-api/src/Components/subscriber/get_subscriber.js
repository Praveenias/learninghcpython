
import React, { useState } from "react";
import "./get_subscriber.css";
import SubscriberUser from "./subsciber_user";
import FilterSubscriber from "./filter";
import apiService from "../../services/api_service";
import Table from "../Common/table/table";
import Loader from "../Common/loader";
import SubscriberSummary from "./subscriber_summary";

const GetSubscriberList = () => {
  const [sub_list, setSubList] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [loader, setloader] = useState(false);
  const [isFIlterModelOpen,setisFIlterModelOpen] = useState(false);
  const [isSummaryModelOpen,setisSummaryModelOpen] = useState(false);
  const [selectedRowData, setSelectedRowData] = useState(null);
  const [datasuccess,setDataSuccess] = useState(false);

  const column_name = ["companyName","siteName","divisionName","primaryContact",
  "primaryEmail", "phone", "status"]


  const handleCloseModal = (data={},modaltype) => {
    console.log(data,modaltype);
    if(modaltype === 'filter'){
      let filter_keys = ["companyName", "divisionName", "siteName"]
      let params={};
      filter_keys.forEach(element => {
        if (element in data && data[element].length > 0)
          params[element] = data[element]
      });
      setisFIlterModelOpen(false);
      apiService.get('api/v1/subscribers',params).then((response) => {
        //console.log(response.data);
        setSubList(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
      
      

      //console.log(params);
    }
    if(modaltype === 'user'){
      setIsModalOpen(false);
    }

    if(modaltype === "summary"){
      setisSummaryModelOpen(false);
    }
    
    
    
  };

  const handleOpenModal = (data,modaltype) => {
    if (modaltype === 'filter') {
      setisFIlterModelOpen(true);
    }
    if(modaltype === 'user'){
      setSelectedRowData(data);
      setIsModalOpen(true);
    }
    if(modaltype === 'summary'){
     // console.log("hit");
      setSelectedRowData(data);
      setisSummaryModelOpen(true);
    } 
  };

  React.useEffect(() => {
    apiService.get('api/v1/subscribers').then((response) => {
        //console.log(response.data);
        
        setSubList(response.data);
        setDataSuccess(true)
        setloader(false);   
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  return (
    <>
      <div>
        <div className="subheading">
          <h3>IN Subscriber Details </h3>
        </div>
      </div>
      <div>
        
      </div>
      <div>
        <div className="m-4">
          <div className="d-flex m-4 align-items-center bd-highlight gap-2">
          <button className="btn btn-primary" onClick={()=>handleOpenModal({},'filter')}>Find subscriber</button>
          <button className="btn btn-primary" onClick={()=>handleCloseModal({},'filter')}>Refresh </button>
          </div>
          {datasuccess && <Table columns={column_name} data={sub_list} itemsPerPage={10} dataHandler={(data,modaltype)=>handleOpenModal(data,modaltype)} dataHandler1={(data,modaltype)=>handleOpenModal(data,modaltype)}/>}
          {loader && <Loader/>}
          
        </div>
      </div>
      {isModalOpen && <SubscriberUser onClose={(data,type)=>handleCloseModal(data,type)} rowData={selectedRowData} />}
      {isFIlterModelOpen && <FilterSubscriber onClose={(data,modaltype)=>handleCloseModal(data,modaltype)} />}
      {isSummaryModelOpen && <SubscriberSummary rowData={selectedRowData} onClose={(data,modaltype)=>handleCloseModal(data,modaltype)}/>}
    </>
  );
};

export default GetSubscriberList;
