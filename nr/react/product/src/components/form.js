import axios from "axios";
import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";


const InputForm = () => {

    const [name,setname] = useState('')
    const [price,setprice] = useState()
    const [quantity,setquantity] = useState()
    const [get,isget] = useState(false);
    const navigate = useNavigate();

    const {state} = useLocation();
    if(state){
        axios.get('http://127.0.0.1:8000/cart-items/'+state)
        .then((res) =>{
            setname(res.data.data.product_name);
            setprice(res.data.data.product_price);
            setquantity(res.data.data.product_quantity)
            isget(true)
        })
    }

    const setform = (e) =>{
        e.preventDefault();
    }

    const getdata = () => {
        const dataq = {"product_name":name,"product_price":price,"product_quantity":quantity}
        if(!get){
            axios.post('http://127.0.0.1:8000/cart-items/',dataq)
            navigate('/');
        }else{
            axios.put('http://127.0.0.1:8000/cart-items/'+state,dataq)
        }
    }


    return(
        <div className="container mb-3">
            <form onSubmit={setform}>
                <div className="mb-1">
                    <label className="form-label">Product Name</label>
                    <input type="text" className="form-control" value={name} onChange={(e)=>setname(e.target.value)} required/>
                </div>
                <div className="mb-3">
                    <label className="form-label">Price</label>
                    <input type="text" className="form-control" value={price} onChange={(e)=>setprice(e.target.value)} required/>
                </div>
                <div className="mb-3">
                    <label className="form-label">Quantity</label>
                    <input type="text" className="form-control" value={quantity} onChange={(e)=>setquantity(e.target.value)}/>
                </div>

                <button type="submit" className="btn btn-primary" onClick={getdata}>Submit</button>
            </form>
        </div>
    )
}

export default InputForm;