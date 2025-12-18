import { Link } from "react-router-dom";
import "./styles.css";

const Header = () => {
  return(
    <div>
      <span className="head">REact COntext API Tutorial</span>
      <ul className="nav">
        <li className="prod">
    <Link to={'/'}>Home</Link>
        </li>
        <li className="prod">
        <Link to={'/card'}>Card</Link>
        </li>

      </ul>
    </div>
  )
}

export default Header;