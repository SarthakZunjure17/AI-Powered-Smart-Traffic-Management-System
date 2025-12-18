import { Link, useNavigate } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  const navigate = useNavigate();
  const isAuth = localStorage.getItem("isAuthenticated");

  const handleLogout = () => {
    localStorage.removeItem("isAuthenticated");
    navigate("/login");
  };

  return (
    <nav className="navbar">
      <div className="nav-logo">🚦 AI Traffic</div>

      {isAuth === "true" && (
        <ul className="nav-links">
          <li><Link to="/home">Home</Link></li>
          <li><Link to="/admin">Admin</Link></li>
          <li><Link to="/about">About</Link></li>
          <li onClick={handleLogout} className="logout">Logout</li>
        </ul>
      )}
    </nav>
  );
}

export default Navbar;
