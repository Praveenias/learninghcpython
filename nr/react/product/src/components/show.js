import axios from "axios";
import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Edit from "./edit";
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';

const Display = () => {
    const navigate = useNavigate();
    const [datas,setAPIData] = useState([]);
    const [showmodal,setshow] = useState(false);
    const [editid,seteditid] = useState();
    const handleClose = () => setshow(false);
    const handleShow = () => setshow(true);
    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/cart-items/`)
            .then((response) => {
                //console.log(response.data.data)
                setAPIData(response.data.data);
            })
    }, [])

    const deleteitem = (id) => {
        axios.delete(`http://127.0.0.1:8000/cart-items/`+id)
        .then()
        console.group(datas)
        setAPIData(datas.filter((post => {
            return post.id !==id;
            }
        )));
    }

    const edititem = (id) => {
        seteditid(id)
        //navigate('/form',{state:id})
        setshow(true)
    }

    return(
        <div className="container">
            <button onClick={()=>navigate('/form')}>Add</button>
            <table className="table table-striped">
                <thead>
                    <tr >
                    <th scope="col">Product Name</th>
                    <th scope="col">Product Price</th>
                    <th scope="col">Product Qunatity</th>
                    <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                {datas.map((data) => {
                    return (
                    <tr key={data.id}>
                        <td>{data.product_name}</td>
                        <td>{data.product_price}</td>
                        <td>{data.product_quantity }</td>
                        <td>
                            <button onClick={()=>deleteitem(data.id)}>delete</button>
                            <button onClick={()=>edititem(data.id)}>Edit</button>
                        </td>
                    </tr>
                )})}
                </tbody>
            </table>
            {/* <button onClick={()=>{setshow(true)}}>Open Modal</button>
            <Modal show={showmodal} onHide={handleClose}>
                <Modal.Header closeButton>
                <Modal.Title>Modal title</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                I will not close if you click outside me. Don't even try to press
                escape key.
                </Modal.Body>
                <Modal.Footer>
                <Button variant="secondary" onClick={handleClose}>
                    Close
                </Button>
                <Button variant="primary">Understood</Button>
                </Modal.Footer>
            </Modal> */}
            <Edit1 show={showmodal} handleClose={handleClose} id={editid}/>

        </div>
        
    )
}

const Edit1 = (props) => {
    const [editdata,seteditdata] = useState([])
    let id = props.id
    console.log(id,'id');
    let url = 'http://127.0.0.1:8000/cart-items/'+id;
    console.log(url);
    useEffect(() => {
        axios.get(url)
            .then((response) => {
                console.log(response.data.data)
                seteditdata(response.data.data);
            })
    }, []) 
    const editdatas = (e) => {
        console.log(e)
    }
    const setform = () =>{
        console.log(editdata);
    }

    //console.log(props);
    return(
        <>
        <Modal show={props.show} >
                <Modal.Header closeButton>
                <Modal.Title>Edit Contact</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                <form onSubmit={setform}>
                <div className="mb-1">
                    <label className="form-label">Product Name</label>
                    <input type="text" className="form-control" value={editdata['product_name']} onChange={(e)=>editdatas(e)} required/>
                </div>
                <div className="mb-3">
                    <label className="form-label">Price</label>
                    <input type="text" className="form-control" value={editdata.product_price} onChange={(e)=>editdatas(e)} required/>
                </div>
                <div className="mb-3">
                    <label className="form-label">Quantity</label>
                    <input type="text" className="form-control" value={editdata.product_quantity} onChange={(e)=>editdatas(e)}/>
                </div>

                <button type="submit" className="btn btn-primary" >Submit</button>
            </form>
                </Modal.Body>
                
            </Modal>
        </>
    )
}

export default Display;