import React, { useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import { TfiMobile } from "react-icons/tfi";
import { GiWaterDrop } from "react-icons/gi";
import { MdBloodtype } from "react-icons/md";
import { ImLocation } from "react-icons/im";
import { AiOutlineUser } from "react-icons/ai";
import { useNavigate } from "react-router-dom";
import "./donate.css"
import { Donate_data } from "../services/apiservice";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Donate = () =>{
    const u_name="sundar";
    const navigate = useNavigate();
    const [data,setdata]=useState({
        name:"",
        m_number:"",
        b_group:"",
        location:"",
    })

    const handle = (e) => {
        const newdata={...data}
        newdata[e.target.id]=e.target.value
        setdata(newdata)
        console.log(data);
    } 

    const submit1 = (e) =>{
        e.preventDefault();
        for (const key in data) {
            if(data[key] === ""){
                return alert(key+" is empty")
            }
        }
            Donate_data({
                name:data.name,
                m_num: data.m_number,
                b_group :data.b_group,
                location : data.location,
                u_name:u_name,
                }).then((res)=>{
                console.log(res.data['status']);
                if(res.data['status']=== 'failure'){
                    toast.error(res.data['msg'])
                    return
                }
                navigate('/user')
            }).catch((err)=>{
                toast.error("server error")
            })
            }
          
    
    
    return(
        <div>
             <div className="container2">
            <MdBloodtype className="logo" />
            <div className="heading">
                <h4>Blood Donation Form</h4>
                <h6>Enter the valid donor information</h6>
            </div>
            <div className="box">
                <form >
                    <div className="form-group ">
                    <AiOutlineUser className="mailicon"/>
                    <input type="text" value={data.name} onChange={(e)=> handle(e)}
                    className="form-control" placeholder="Donor name" id="name"/>
                    </div>
                    <div className="form-group log-status">
                    <TfiMobile className="mailicon"/>
                    <input type="text" className="form-control" placeholder="Mobile number" id="m_number"
                    onChange={(e) => handle(e)} value={data.m_number} />
                    </div>
                    <div className="form-group log-status">
                    <GiWaterDrop className="mailicon"/>
                    {/* <input type="text" className="form-control" placeholder="Blood group" id="b_group"
                    onChange={(e) => handle(e)} value={data.b_group} /> */}
                    <select id="b_group" className="form-control" value={data.b_group} onChange={(e)=> handle(e)}>
                        <option value=''>Select</option>
                        <option value='A+'>A+</option>
                        <option value='O+'>O+</option>
                        <option value='O-'>O-</option>
                        <option value='A-'>A-</option>
                        <option value='B+'>B+</option>
                    </select>
                    </div>
                    <div className="form-group log-status">
                    <ImLocation className="mailicon"/>
                    <input type="text" className="form-control" placeholder="Location" id="location"
                    onChange={(e) => handle(e)} value={data.location} />
                    </div>
                    <div className="form-group2">
                        <button type="submit" onClick={submit1} className="log-btn ">Donate </button>
                    </div>
                    <div className="form-group2">
                        <button type="button" className="log-btn2" onClick={() =>  navigate("/user") } > Back </button>
                    </div>
                </form>
            </div>
            </div>
        <ToastContainer/>
        </div> 
    )

}


export default Donate;