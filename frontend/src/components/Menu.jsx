import React from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

const Menu = () => {
    const { user, logout } = useAuth()
    return (

        <ul className="nav justify-content-center">
            <li className="nav item">
                <Link to="/" className="nav-link">Home</Link>
            </li>
            {
                !!user ? (
                    <>
                        <li className="nav-item">
                            <Link to="/profile" className="nav-link">Profile</Link>
                        </li>
                        <li className="nav-item">
                            <button className="btn btn-danger btn-sm my-1" onClick={logout}>Logout</button>
                        </li>
                    </>
                ) : (
                    <>
                        <li className="nav-item">
                            <Link to="/login" className="nav-link">Login</Link>
                        </li>
                        <li className="nav-item">
                            <Link to="/register" className="nav-link">Register</Link>
                        </li>
                    </>
                )
            }
        </ul>

    )
}

export default Menu