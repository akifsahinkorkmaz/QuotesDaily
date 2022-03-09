import React, { ReactElement } from 'react';
import '../App.css';


interface propTypes {
  url: string,
}

interface stateTypes {
  copystatus: string,
  copystyle: any,
}

class Copy extends React.Component <propTypes, stateTypes> {
 
  constructor (props: propTypes) {
    super(props);
    this.state = {
      copystatus : "Copy",
      copystyle : {
        background : "black"
      },
    }
  }


  CopyButton () {
    var link = this.props.url
    navigator.clipboard.writeText(link);
    this.setState( {
      copystatus : "Copied",
      copystyle : {background : "green"}
    })
    setTimeout(_ => {
      this.setState( {
        copystatus : "Copy",
        copystyle : {background : "black"}
      })
    }, 10000)
  }

  
  render(): ReactElement {
    return (
     
      <div className=' relative w-min pr-20'>
        <h1 className='w-auto h-8 rounded-l-full bg-slate-50 px-3 pt-px shadow-sm'>{this.props.url}</h1>
        <button className='absolute top-0 right-0 text-white w-20 h-8 rounded-r-full shadow-sm transition' style={this.state.copystyle} onClick={this.CopyButton.bind(this)}>{this.state.copystatus}</button>
      </div>
  
    );
  }
}

export default Copy;
