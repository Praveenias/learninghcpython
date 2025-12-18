import React, { useState } from "react";
import axios from "axios";
import Loader from "../Common/loader";
// import '../Common/modal.css';

const SubscriberUser = ({ rowData, onClose }) => {
  const [dataFromAPI, setDataFromAPI] = useState([]);
  const [loading, setloading] = useState(true);

  //console.log(url_params);
  React.useEffect(() => {
    let url_params = {
      subscriberId: rowData.subscriberId,
    };
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/api/v1/subscribers/users",
          { params: url_params }
        );
        if (Array.isArray(response.data.data)) {
          
          setTimeout(() => {
            setloading(false);
            setDataFromAPI(response.data.data);
          }, 1000);
        } else {
          console.error("API response is not an array:", response.data);
        }
        // setDataFromAPI(response.data);
        // console.log(response.data);
      } catch (error) {
        console.error("Error fetching data from API:", error);
      }
    };

    fetchData();
  }, [rowData]);

  const handleModalClose = () => {
    onClose({},'user');
  };
  return (
    <>
      <div
        className="modal fade show modal-lg"
        role="dialog"
        aria-hidden="true"
        tabIndex="-1"
        style={{ display: "block" }}
      >
        <div className="modal-dialog" role="document">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="exampleModalLabel">
                Subscriber User
              </h5>
              <button
                type="button"
                className="btn btn-secondary"
                aria-label="Close"
                onClick={handleModalClose}
              >
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div className="modal-body">
              <div className="d-flex justify-content-around">
                <p>Subscriber Name: {rowData.companyName}</p>
                <p>Division Name: {rowData.divisionName}</p>
                <p>SIte name: {rowData.siteName}</p>
              </div>
              <table className="table table-striped ">
                <thead>
                  <tr className="bg-primary">
                    <th scope="col"> Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Role</th>
                    <th scope="col">Status</th>
                  </tr>
                </thead>
                <tbody>
                  {dataFromAPI.map((data) => {
                    return (
                      <tr key={data.name}>
                        <td>{data.name}</td>
                        <td>{data.email}</td>
                        <td>{data.role}</td>
                        <td>{data.status}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
              {loading && <Loader/>}
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-secondary"
                onClick={handleModalClose}
              >
                Close
              </button>
            </div>
          </div>
        </div>
        
      </div>
    </>
  );
};

export default SubscriberUser;
