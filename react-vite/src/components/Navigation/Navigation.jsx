// src/components/Navigation/Navigation.jsx

import { NavLink, useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";
import { useState, useEffect } from "react";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  const sessionUser = useSelector((state) => state.session.user);
  const [searchTerm, setSearchTerm] = useState("");
  const [experiences, setExperiences] = useState([]);
  const [filteredExperiences, setFilteredExperiences] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchExperiences = async () => {
      const res = await fetch("/api/experiences");
      if (res.ok) {
        const data = await res.json();
        setExperiences(data.experiences || []);
      }
    };
    fetchExperiences();
  }, []);

  useEffect(() => {
    const term = searchTerm.trim().toLowerCase();
    if (!term) {
      setFilteredExperiences([]);
    } else {
      const matches = experiences.filter((exp) => {
        const title = exp.title?.toLowerCase() || "";
        const location = exp.location?.toLowerCase() || "";
        return title.includes(term) || location.includes(term);
      });
      setFilteredExperiences(matches.slice(0, 3));
    }
  }, [searchTerm, experiences]);

  const handleSelect = (exp) => {
    navigate(`/experiences/${exp.id}`);
    setSearchTerm("");
  };

  return (
    <nav className="nav-bar">
      {/* ✅ Left: Logo */}
      <NavLink to="/" className="nav-logo">
        TryThis!
      </NavLink>

      {/* ✅ Center: Nav Links */}
      <ul className="nav-links">
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
        {sessionUser && (
          <li>
            <NavLink to="/create">New Experience</NavLink>
          </li>
        )}
        {!sessionUser && (
          <>
            <li>
              <NavLink to="/login">Log In</NavLink>
            </li>
            <li>
              <NavLink to="/signup">Sign Up</NavLink>
            </li>
          </>
        )}
      </ul>

      {/* ✅ Right: Search + Profile */}
      <div className="nav-profile">
        <div className="search-container">
          <input
            type="text"
            className="search-input"
            placeholder="Search experiences..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          {filteredExperiences.length > 0 && (
            <ul className="search-dropdown">
              {filteredExperiences.map((exp) => (
                <li
                  key={exp.id}
                  className="dropdown-item"
                  onClick={() => handleSelect(exp)}
                >
                  <span className="dropdown-title">{exp.title}</span>
                  <span className="dropdown-location"> – {exp.location}</span>
                </li>
              ))}
            </ul>
          )}
        </div>
        <ProfileButton />
      </div>
    </nav>
  );
}

export default Navigation;
