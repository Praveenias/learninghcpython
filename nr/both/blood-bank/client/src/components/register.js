import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from "react";
import './register.css'
import { CgProfile } from "react-icons/cg";
import { Si1Password } from "react-icons/si";
import { MdBloodtype } from "react-icons/md";
import { AiFillMail } from "react-icons/ai";
import { useNavigate } from "react-router-dom";
import { RegisterUser } from '../services/apiservice';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Register = () =>{
    const navigate = useNavigate();
    const [data,setdata]=useState({
        name:"",
        email:"",
        password:"",
        password2:""
    })

    const handle = (e) => {
        //console.log(e.target);
        const newdata={...data}
        newdata[e.target.id]=e.target.value
        setdata(newdata)
    } 
    
const submit1 = (e) =>{
    RegisterUser({
        name:data.name,
        email:data.email,
        password:data.password,
       }).then((Response)=>{
        console.log(Response.data)
        if (Response.data['status'] === "success"){
            toast.success('Registered Successfully')
            navigate('/')
        }
        else return (
            alert('Fill all Fields Correctly')
        );
       })
       
    }

    return(
        <div>
            <div className="container2">
                <MdBloodtype className="logo" />
                <div className="heading">
                    <h4>Welcome To BloodBank</h4>
                    <h6>Create your credentials to access your account</h6>
                </div>
                <div className="box">
                    <form>
                        <div className="form-group ">
                        <CgProfile className="mailicon"/>
                        <input type="text" value={data.name} onChange={(e)=> handle(e)}
                        className="form-control" placeholder="Username" id="name"/>
                        </div>
                        <div className="form-group log-status">
                        <AiFillMail className="mailicon"/>
                        <input type="email" className="form-control" placeholder="Enter your Email" id="email"
                        onChange={(e) => handle(e)} value={data.email} />
                        </div>
                        <div className="form-group log-status">
                        <Si1Password className="mailicon"/>
                        <input type="password" className="form-control" placeholder="Enter your password" id="password"
                        onChange={(e) => handle(e)} value={data.password} />
                        </div>
                    
                        
                        <div className="form-group2">
                            <button type="button" onClick={()=>submit1()} className="log-btn ">Register </button>
                        </div>
                        <div className="form-group2">
                            <button type="button" className="log-btn2" onClick={() =>  navigate("/") } > Log in</button>
                        </div>
                    </form>
                </div>
            </div>
            <ToastContainer/>
        </div>
    )
}
export default Register;