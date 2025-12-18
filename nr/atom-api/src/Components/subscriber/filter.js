import { useState } from "react";
import './common.css';

const FilterSubscriber = ({onClose}) =>{
  const [formData, setFormData] = useState({
    companyName: '',
    divisionName: '',
    siteName: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const closeModal = () => {
    onClose(formData,'filter')
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    closeModal()
  };
  return (
    <>
    <div
        className="modal fade show modal-lg"
        role="dialog"
        aria-hidden="true"
        style={{ display: "block" }}
      >
        <div className="modal-dialog" role="document">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="exampleModalLabel">
                FIlter By
              </h5>
              <button
                type="button"
                className="btn btn-secondary"
                aria-label="Close"
                onClick={()=>onClose()}
              >
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div className="modal-body">
            <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="companyName">Company Name:</label>
        <input
          type="text"
          id="companyName"
          name="companyName"
          value={formData.companyname}
          onChange={handleChange}
        />
      </div>
      <div>
        <label htmlFor="divisionName">Division Name:</label>
        <input
          type="text"
          id="divisionName"
          name="divisionName"
          value={formData.divisionname}
          onChange={handleChange}
        />
      </div>
      <div>
        <label htmlFor="siteName">Site Name</label>
        <input
          type="text"
          id="siteName"
          name="siteName"
          value={formData.sitename}
          onChange={handleChange}
        />
      </div>
      <button type="submit">Submit</button>
    </form>  
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-secondary"
                onClick={closeModal}
              >
                Close
              </button>
            </div>
          </div>
        </div>
        
      </div>
    </>
  )
}


export default FilterSubscriber;