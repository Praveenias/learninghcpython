import { Link } from "react-router-dom";
import "./side_navbar.css";
import { useState } from "react";



const SideNavbar = () => {
  const [activeDropdown, setActiveDropdown] = useState(null);

  const toggleDropdown = (dropdownId) => {
    setActiveDropdown((prevDropdown) =>
      prevDropdown === dropdownId ? null : dropdownId
    );
  };

  return (
    <>
      {/* <div className="sidebar">
      <Link to="subscriberlist">Subscribers</Link>
      <Link to="/license">Licenses</Link>
      <Link to="#">Products</Link>
      <Link to="#">Manufacturers</Link>
      <Link to="#">Components</Link>
      <Link to="#">Regulation</Link>

    </div> */}

      <div className="sidenav">
        
        <div className="dropdown"  onClick={() => toggleDropdown('subscriber')}>
        <a href="#" role="button">Subscriber</a>
          <div className={`dropdown-content ${activeDropdown === 'subscriber' ? 'show' : ''}`}>
          <Link to="subscriberlist">Subscribers List</Link>
          <Link to="#">Sub Component</Link>
          </div>
        </div>
        <div className="dropdown"  onClick={() => toggleDropdown('component')}>
          <a href="#">Component</a>
          <div className={`dropdown-content ${activeDropdown === 'component' ? 'show' : ''}`}>
          <Link to="mcomplist">Component List</Link>
          
          </div>
        </div>
        <div className="dropdown"  onClick={() => toggleDropdown('regulation')}>
          <a href="#">Regualtion</a>
          <div className={`dropdown-content ${activeDropdown === 'regulation' ? 'show' : ''}`}>
          <Link to="regulationlist">Regulation List</Link>
          </div>
        </div>
        <div className="dropdown"  onClick={() => toggleDropdown('bom')}>
          <a href="#">Bom</a>
          <div className={`dropdown-content ${activeDropdown === 'bom' ? 'show' : ''}`}>
          <Link to="bomlist">Bom List</Link>
          </div>
        </div>
        <div className="dropdown"  onClick={() => toggleDropdown('license')}>
        <a href="#">License</a>
          <div className={`dropdown-content ${activeDropdown === 'license' ? 'show' : ''}`}>
          <Link to="bomlist">License List</Link>
          </div>
        </div>
        <div className="dropdown"  onClick={() => toggleDropdown('substance')}>
        <a href="#">Substance</a>
          <div className={`dropdown-content ${activeDropdown === 'substance' ? 'show' : ''}`}>
          <Link to="bomlist"> Substance List</Link>
          </div>
        </div>

       
      </div>
    </>
  );
};

export default SideNavbar;
