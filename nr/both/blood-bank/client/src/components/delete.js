import React, { useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import "./login.css"
import { GiWaterDrop } from "react-icons/gi";
import { ImLocation } from "react-icons/im";
import { MdBloodtype } from "react-icons/md";
import { useNavigate } from "react-router-dom";
import { Delete_blood } from "../services/apiservice";

const Delete = () =>{
    const navigate = useNavigate();
    const [data,setdata]=useState({
        // name:"",
        m_num:""
    })

    const handle = (e) => {
        const newdata={...data}
        newdata[e.target.id]=e.target.value
        setdata(newdata,"input your details")
        console.log(data,'blood group');
    } 
    
    const submit = (e) =>{
        e.preventDefault();
        for (const key in data) {
            if(data[key] === ""){
                return alert(key+" is empty")
            }
        }
        console.log(data,'hit');
        const number=data.m_num
        Delete_blood(number).then((response)=>{
            if(response.data['status'] == 'failure'){
                alert(response.data['msg'])
                return
            }
            console.log(response.data)
          })
        
    } 

    return(
        <div className="container">
            <MdBloodtype className="logo" />
            <div className="heading">
                <h4>BloodBank Delete Form</h4>
                <h6>Enter name and your mobilenumber</h6>
            </div>
            <div className="box">
                <form >
                    {/* <div className="form-group ">
                    <GiWaterDrop className="mailicon"/>
                    <input type="text" value={data.name} onChange={(e)=> handle(e)}
                    className="form-control" placeholder="name" id="name"/> 
                    </div> */}
                    <div className="form-group log-status">
                    <ImLocation className="mailicon"/>
                    <input type="text" className="form-control" placeholder="mobile number" id="m_num"
                    onChange={(e) => handle(e)} value={data.m_num} />
                    </div>
                    <div className="form-group2">
                        <button type="button" className="log-btn " onClick={submit}> Delete </button>
                    </div>
                    <div className="form-group2">
                        <button type="button" className="log-btn2" onClick={() =>  navigate(-1) } > Back</button>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Delete;