import React, { useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import "./userpage.css"
import { MdBloodtype } from "react-icons/md";
import axios from "axios";
import { useNavigate,useLocation } from "react-router-dom";

const User = () =>{
    const navigate = useNavigate();
    // const {state} = useLocation();
    // let name=state.name;
    // const [data,setdata]=useState({
    //     b_group:"",
    //     location:"",
    // });

    // const handle = (e) => {
    //     const newdata={...data}
    //     newdata[e.target.id]=e.target.value
    //     setdata(newdata)
    //     console.log(data);
    // } ;



    return(
        <div className="container">
            <MdBloodtype className="logo" />
            <div className="heading">
                <h4>Welcome to your BloodBank</h4> {/*name will username return from the server*/}
            </div>
            <div className="box">
                <form>
                    <div className="form-group2">
                        <button type="button" className="log-btn2" onClick={(e) =>  navigate("/donate") } > Donate</button>
                    </div>
                    <div className="form-group2">
                        <button type="button" className="log-btn2" onClick={(e) =>  navigate("/Request") } > Request</button>
                    </div>
                    <div className="form-group2">
                        <button type="button" className="log-btn2" onClick={(e) =>  navigate("/update") } > Update Blood</button>
                    </div>
                    <div className="form-group2">
                        <button type="button" className="log-btn2" onClick={() => navigate("/delete")} > Delete Account</button>
                    </div>
                    <div className="form-group2">
                        <button type="button" className="log-btn2 logout" onClick={() =>  navigate("/") } > Log out</button>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default User;