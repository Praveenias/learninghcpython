import "./table.css"
import { useNavigate,useLocation } from "react-router-dom";


const Table = () => {
    const navigate =useNavigate();
    const {state} = useLocation();
    console.log(state.table_data)
    
    return(
        <div className="tcontainer">
        <h4 id="headingT">Welcome To BloodBank</h4>
            <table class="table table-bordered ">
                <thead>
                    <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Blood Group</th>
                    <th scope="col">mobile</th>
                    <th scope="col">Location</th>
                    </tr>
                </thead>
                <tbody>
                {state.table_data.map((user)=>(
                            <tr>
                                <td>{user.name}</td>
                                <td>{user.bloodgroup}</td>
                                <td>{user.mobilenumber}</td>
                                <td>{user.location}</td>
                            </tr>
                        ))}
                </tbody>
            </table>
            <div className="form-group2">
                        <button type="button" className="log-btn2" onClick={() =>  navigate(-1)} > Back</button>
            </div>
        </div>
    )
}

export default Table;