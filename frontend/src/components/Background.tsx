import React, { ReactElement } from 'react';
import '../App.css';

interface propTypes {
  url: string,
  quote: string,
}

interface stateTypes {

}


class Background extends React.Component <propTypes, stateTypes> {

  imstyle: any;

  constructor (props: propTypes) {
    super(props)
    this.imstyle = {};
    this.state = {
    };
  }

  componentDidMount(){
  
    // image styling
    if (window.innerWidth >= window.innerHeight) {
      this.imstyle = {
        width: "90vh",
        height: "90vh",
        boxShadow: "1px 1px 10px 3px black"
      }
    } else {
      this.imstyle = {
        width: "90vw",
        height: "90vw",
      }
    }
    
  }

  render(): ReactElement {
    return (
      <img style={this.imstyle} src={this.props.url} alt={this.props.quote} />
    );
  }
}

export default Background;
