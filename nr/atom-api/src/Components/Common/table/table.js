import React, { useState } from "react";
import "./table.css";

const Table = ({ columns, data, itemsPerPage,dataHandler,dataHandler1 }) => {
  //console.log(data, "hit");
  const [currentPage, setCurrentPage] = useState(1);

  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = data.slice(indexOfFirstItem, indexOfLastItem);

  const totalPages = Math.ceil(data.length / itemsPerPage);
  //console.log(currentPage,indexOfFirstItem,indexOfLastItem);

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  const handlersendRowData=(data,modal_type) => {
    //console.log(data,modal_type);
    dataHandler(data,modal_type);
  }

  return (
    <div className="table-container">
      <p>Total Records Found :{data.length} </p>
      <table className="table">
        <thead>
          <tr>
            <th>Si no</th>
            {columns.map((column, index) => (
              <th key={index}>{column}</th>
            ))}
            {dataHandler && <th>Action</th>}
            {dataHandler1 && <th>Component</th>}
          </tr>
        </thead>
        <tbody>
          {currentItems.map((item, index) => (
            <tr>
              <td>{index+indexOfFirstItem+1}</td>
              {columns.map((col) => (
                <td>{item[col]}</td>
              ))}
             {dataHandler && <td>
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={() => handlersendRowData(item, "user")}
                >
                  User's
                </button>
              </td>}
              {dataHandler1 && <td>
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={() => handlersendRowData(item, "summary")}
                >
                 Summary
                </button>
              </td>}
            </tr>
          ))}
        </tbody>
      </table>
      {totalPages > 1 && (
        <div className="pagination">
          {Array.from({ length: totalPages }, (_, index) => (
            <button
              key={index}
              className={`page-link ${
                currentPage === index + 1 ? "active" : ""
              }`}
              onClick={() => handlePageChange(index + 1)}
            >
              {index + 1}
            </button>
          ))}
        </div>
      )}
    </div>
  );
};

export default Table;
