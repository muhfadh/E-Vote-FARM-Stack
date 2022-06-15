import './App.css';
import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
    return ( 
    <div className="App">
        Hello World!
        <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{"width": "400px", "backgroundColor": "white", "marginTop": "15px"}}>
        <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">E-Vote</h1>
        </div>
    </div>
    );
}

export default App;