// src/components/Navigation/Navigation.jsx

import { NavLink, useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";
import { useState, useEffect } from "react";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal/LoginFormModal";
import logo from '../../assets/TryThisLogo.png';

function Navigation() {
  const sessionUser = useSelector((state) => state.session.user);
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredExperiences, setFilteredExperiences] = useState([]);
  const [experiences, setExperiences] = useState([]);
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
      return;
    }

    const price = parseFloat(term);
    if (!isNaN(price)) {
      fetch(`/api/experiences?minPrice=${price}&maxPrice=${price}`)
        .then(res => res.json())
        .then(data => setFilteredExperiences(data.experiences || []));
      return;
    }

    const matches = experiences.filter((exp) => {
      const title = exp.title?.toLowerCase() || "";
      const category = exp.category?.toLowerCase() || "";
      return title.includes(term) || category.includes(term);
    });

    setFilteredExperiences(matches.slice(0, 3));
  }, [searchTerm, experiences]);

  const handleSelect = (exp) => {
    navigate(`/experiences/${exp.id}`);
    setSearchTerm("");
  };

  return (
    <nav className="nav-bar">
      <NavLink to="/" className="nav-logo">
        <img src={logo} alt="TryThis logo" className="nav-logo-img" />
      </NavLink>

      <div className="nav-center">
        <ul className="nav-links">
          <li><NavLink to="/">Home</NavLink></li>
          <li><NavLink to="/explore">Explore Experiences</NavLink></li>

          {sessionUser && (
            <>
              <li><NavLink to="/create">New Experience</NavLink></li>
              <li><NavLink to="/my-experiences">My Experiences</NavLink></li>
            </>
          )}
        </ul>

        <div className="search-container">
          <input
            type="text"
            className="search-input"
            placeholder="Search by name, category, or price"
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
      </div>

      <div className="nav-right">
        {!sessionUser && (
          <div className="nav-auth">
            <OpenModalButton buttonText="Log In" modalComponent={<LoginFormModal />} />
            <NavLink to="/signup">Sign Up</NavLink>
          </div>
        )}
        <div className="nav-profile">
          <ProfileButton />
        </div>
      </div>
    </nav>
  );
}

export default Navigation;
