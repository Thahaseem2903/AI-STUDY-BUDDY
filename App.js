
import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import ProgressBar from "./components/ProgressBar";
import LoginForm from "./components/LoginForm";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function App() {
  const [token, setToken] = useState(null);

  const handleLogin = (jwtToken) => {
    localStorage.setItem("token", jwtToken);
    setToken(jwtToken);
  };

  return (
    <Router>
      <Switch>
        <Route path="/login">
          <LoginForm onLogin={handleLogin} />
        </Route>
        <Route path="/upload">
          <FileUpload token={token} />
        </Route>
        <Route path="/">
          <ProgressBar />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
    