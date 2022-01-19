import { BrowserRouter as Router, Route } from "react-router-dom";

import Home from "./routes/Home"
import SignupForm from "./routes/signupForm";
import Nav from "./components/Nav";

function App() {
  return (
    <Router>
      <Nav></Nav>
      <Route path="/" element={Home}/>
      <Route path="/signup" element={SignupForm}/>
    </Router>
  );
}

export default App;
