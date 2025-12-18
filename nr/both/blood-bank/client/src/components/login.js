import React, { useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import "./login.css"
import { CgProfile } from "react-icons/cg";
import { Si1Password } from "react-icons/si";
import { MdBloodtype } from "react-icons/md";
import { useNavigate } from "react-router-dom";
import { Loginpost } from "../services/apiservice";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Login = () =>{
    const navigate = useNavigate();
    const [data,setdata]=useState({
        name:"",
        password:""
    })

    const handle = (e) => {
        const newdata={...data}
        newdata[e.target.id]=e.target.value
        setdata(newdata)
    } 
    
    const submit = (e) =>{
        Loginpost({
            name:data.name,
            password:data.password,
        }).then((response) =>{
            console.log(response.data)
            if (response.data['status'] === "failure") {
                toast.error(response.data['msg']);
                return
            };
            let temp = response.data
            navigate('/user',{state:{'name':temp}});
        }).catch((err)=>{
            toast.error("Server Error, Contact Admin");
        })
    } 

    return(
        <>
        <div className="container">
            <MdBloodtype className="logo" />
            <div className="heading">
                <h4>Welcome To BloodBank</h4>
                <h6>Enter your credentials to access your account</h6>
            </div>
            <div className="box">
                <form >
                    <div className="form-group ">
                    <CgProfile className="mailicon"/>
                    <input type="text" value={data.name} onChange={(e)=> handle(e)}
                    className="form-control" placeholder="Username" id="name"/>
                    </div>
                    <div className="form-group log-status">
                    <Si1Password className="mailicon"/>
                    <input type="password" className="form-control" placeholder="Enter your password" id="password"
                    onChange={(e) => handle(e)} value={data.password} />
                    </div>
                    <div className="form-group2">
                        <button type="button" onClick={submit}  className="log-btn "> Log in</button>
                    </div>
                    <div className="form-group2">
                        <button type="button" className="log-btn2" onClick={() =>  navigate("/Register") } > Register</button>
                    </div>
                </form>
            </div>
            
        </div>
        <ToastContainer />
        </>
        
    )
}

export default Login;