import React, { ReactElement } from 'react';
import '../App.css';
import Canvas from '../components/Canvas';
import Copy from '../components/Copy';
import Background from '../components/Background';
import {apiurl} from '../App';


interface propTypes {
  shared?: string,
}

interface stateTypes {
  Quote: string,
  Author: string,
  Day: string,
  Surl: string,
  Bg: string,
  Font: number,
  Imurl?: string,
}

class Home extends React.Component <propTypes, stateTypes> {
  quotestyle: any;
  copystyle: any;
  copystatus: string
  constructor (props: propTypes) {
    super(props);
    this.quotestyle = {};
    this.copystyle = {
      background : "black"
    };
    this.copystatus = "Copy";
    this.state = {
      Quote: "",
      Author: "",
      Day: "",
      Surl: "",
      Bg: (apiurl + "static/1.jpg"),
      Font: 12,
      Imurl: "",
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
    localurl = localurl + "ssim/" + this.state.Surl.split("/").pop() 
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
          Imurl: result.downloadlink
    })); 

    var l: number = this.state.Quote.length
    var f: number = 0;
    if (l < 120) {f = 2.5}
    else if (120 <= l && l < 180) {f = 2}
    else if (180 <= l && l < 280) {f = 1.6}
    else if (280 <= l && l < 400) {f = 1.4}
    
    if (window.innerWidth >= window.innerHeight) {
      this.quotestyle = f ? {fontSize : f+"vh"}: {fontSize : "2vh"};
    } else {
      this.quotestyle = f ? {fontSize : f+"vw"}: {fontSize : "2vw"};
    }
  }

  
  render(): ReactElement {
    return (
    
      
      <main className='w-screen h-screen bg-slate-200'>
        <div className='absolute text-center top-2/4 left-2/4 -translate-x-2/4 -translate-y-2/4'>
          <h1 className='absolute top-[25%] left-[32%] -translate-x-2/4 -translate-y-2/4' >{this.state.Day}</h1>
          <h1 style={this.quotestyle} className={'absolute top-[50%] left-[32%] w-[58%] whitespace-normal break-words -translate-x-2/4 -translate-y-2/4 '} >{this.state.Quote}</h1>
          <h1 className='absolute top-[75%] left-[32%] -translate-x-2/4 -translate-y-2/4' >{this.state.Author}</h1>
          <Background url={this.state.Bg} quote={this.state.Quote} />
        </div>
        
        <div className='absolute bottom-8 right-4 space-y-4'>
          <a className='block text-white text-center mw-36 h-8 rounded-full bg-green-400 px-3 pt-px shadow-sm' href={this.state.Imurl} >Download from servers</a>
          <Copy url={this.state.Surl}></Copy>
        </div>
        
        <div className='hidden'>
          <Canvas Quote={this.state.Quote} Author={this.state.Author} Day={this.state.Day} Bg={this.state.Bg}/>
        </div>
      </main>
    
    );
  }
}

export default Home;
