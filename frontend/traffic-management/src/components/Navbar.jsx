import { Link, useNavigate } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  const navigate = useNavigate();
  const isLoggedIn = localStorage.getItem("isAdminLoggedIn");

  const logout = () => {
    localStorage.removeItem("isAdminLoggedIn");
    navigate("/");
  };

  return (
    <nav className="navbar">
      <div className="nav-logo">🚦 AI Traffic</div>
      <ul className="nav-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/about">About</Link></li>

        {isLoggedIn ? (
          <>
            <li><Link to="/admin">Admin</Link></li>
            <li onClick={logout} style={{ cursor: "pointer" }}>Logout</li>
          </>
        ) : (
          <li><Link to="/login">Admin</Link></li>
        )}
      </ul>
    </nav>
  );
}

export default Navbar;
