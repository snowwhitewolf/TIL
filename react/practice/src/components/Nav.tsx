import { Link } from "react-router-dom";

export default function Nav() {
  return (
    <>
      <ul className="navList">
        <li>
          <p>ssdf</p>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/signup">Signup</Link>
        </li>
      </ul>
    </>
  )
}