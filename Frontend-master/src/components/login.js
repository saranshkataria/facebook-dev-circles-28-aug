import React, { Component, PropTypes } from 'react';
import "./../login.css";

export default class Login extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="wrapper">
        <div className="container">
            <h1>Welcome</h1>

            <form className="form" action="">
                <button type="submit" id="login-button">FB LOGIN</button>
            </form>
        </div>
      </div>
    );
  }
}
