import React from 'react'
import { Link, withRouter } from 'react-router-dom'
// import ReactDOM from 'react-dom'
// import axios from 'axios'
import logo from '../assets/chic-logo.jpg'

class NavBar extends React.Component {
  constructor() {
    super()

    this.state = {

    }
  }

  render() {
    return(
      <nav className="navbar container">
        <div className="navbar-brand">
          <Link className="navbar-item" to="/">
            <img className="logo" src={logo} />
            <p>Chic</p>
          </Link>
        </div>
        <div className="navbar-menu" aria-label="menu" aria-expanded="false">
          <div className="navbar-end">
            <Link className="navbar-item create" to="/meals/new">
              <i className="fas fa-utensils"></i>
            </Link>
          </div>
        </div>
      </nav>
    )
  }
}

export default withRouter(NavBar)
