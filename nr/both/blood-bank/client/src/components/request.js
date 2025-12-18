import React, { useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import "./login.css"
import { GiWaterDrop } from "react-icons/gi";
import { ImLocation } from "react-icons/im";
import { MdBloodtype } from "react-icons/md";
import { useNavigate } from "react-router-dom";
import { Requestblood } from "../services/apiservice";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Request = () =>{
    const navigate = useNavigate();
    const [data,setdata]=useState({
        b_group:"",
        location:""
    })

    const handle = (e) => {
        const newdata={...data}
        newdata[e.target.id]=e.target.value
        setdata(newdata,"input blood  value")
        //console.log(data,'blood group');
    } 
    
    const submit = (e) =>{
        e.preventDefault();
        for (const key in data) {
            if(data[key] === ""){
                toast.error(key+" is empty")
                return
            }
        }
        Requestblood({
            Bloodgroup :data.b_group,
            location :data.location,
          }).then((response)=>{
            console.log(response.data,"b")
            const table_data = response.data;
            if(response.data.length === 0){
                toast.error('sry, no such blood group available')
                return
            }
            navigate("/table",{state:{'table_data':table_data}})
          })
        
    } 

    return(
        <div>
            <div className="container">
                <MdBloodtype className="logo" />
                <div className="heading">
                    <h4>BloodBank Request Form</h4>
                    <h6>Enter Blood group and your Location</h6>
                </div>
                <div className="box">
                    <form >
                        <div className="form-group ">
                        <GiWaterDrop className="mailicon"/>
                        <select id="b_group" className="form-control" value={data.b_group} onChange={(e)=> handle(e)}>
                            <option value=''>Select</option>
                            <option value='A+'>A+</option>
                            <option value='O+'>O+</option>
                            <option value='O-'>O-</option>
                            <option value='A-'>A-</option>
                            <option value='B+'>B+</option>
                        </select>
                        {/* <input type="text" value={data.b_group} onChange={(e)=> handle(e)}
                        className="form-control" placeholder="Blood Group" id="b_group"/> */}
                        </div>
                        <div className="form-group log-status">
                        <ImLocation className="mailicon"/>
                        <input type="text" className="form-control" placeholder="location" id="location"
                        onChange={(e) => handle(e)} value={data.location} />
                        </div>
                        <div className="form-group2">
                            <button type="button" className="log-btn " onClick={submit}> Request</button>
                        </div>
                        <div className="form-group2">
                            <button type="button" className="log-btn2" onClick={() =>  navigate(-1) } > Back</button>
                        </div>
                    </form>
                </div>
            </div>
            <ToastContainer/>
        </div>
    )
}

export default Request;