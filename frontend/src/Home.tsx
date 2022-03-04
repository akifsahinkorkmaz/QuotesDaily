import React, { ReactElement } from 'react';
import './App.css';
import {apiurl} from './App';


interface propTypes {
  shared?: string,
}

interface stateTypes {
  Quote: string,
  Author: string,
  Day: string,
  Surl: string,
  Bg: string,
}

class App extends React.Component <propTypes, stateTypes> {
  constructor (props: propTypes) {
    super(props)
    this.state = {
      Quote: "",
      Author: "",
      Day: "",
      Surl: "",
      Bg: (apiurl + "static/1.jpg"),

    }
  }

  componentDidMount(){
    var localurl: string = apiurl + ""
    fetch(localurl, {
          method: 'GET', 
          mode: 'cors', 
          cache: 'no-cache', 
          headers: {
            'Content-Type': 'application/json'
          }
    })
      .then((res) => res.json())
      .then(result => this.setState({
        Quote: result.quote,
        Author: result.author,
        Day: result.day, 
        Surl: apiurl + result.shareurl,
        Bg: result.Bg ? apiurl + "static/" + result.Bg : this.state.Bg,
      })); 
  }

  render(): ReactElement {
    return (
    
      <main>
        <h1>Quote of {this.state.Day}</h1>
        <hr />
        <h1>{this.state.Quote}</h1>
        <h1>by : {this.state.Author}</h1>
        <hr />
        <h1>Share url : {this.state.Surl}</h1>
        <img src={this.state.Bg} alt="Quote Background" />
      </main>
    
    );
  }
}

export default App;
