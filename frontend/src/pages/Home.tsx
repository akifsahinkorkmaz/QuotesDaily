import React, { ReactComponentElement, ReactElement } from 'react';
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
  FontRules: object,
  Bg: string,
  AFont: number,
  QFont: number,
  Printable: string,
  Imurl?: string,
  Canvurl?: string | boolean,
}

class Home extends React.Component <propTypes, stateTypes> {
  quotestyle: any;
  constructor (props: propTypes) {
    super(props);
    this.quotestyle = {};
    this.state = {
      Quote: "",
      Author: "",
      Day: "",
      Surl: "",
      FontRules: {},
      Bg: (apiurl + "static/1.jpg"),
      QFont: 16,
      AFont: 20,
      Printable: "",
      Imurl: "",
      Canvurl: false,
    }
  }

  componentDidMount(){
    var localurl: string = apiurl 
    fetch(localurl, {
          method: 'GET', mode: 'cors', cache: 'no-cache', 
          headers: {'Content-Type': 'application/json'}
    }).then((res) => res.json())
    .then(result => this.setState({
        Quote: result.quote,
        Author: result.author,
        Day: result.day, 
        Surl: apiurl + result.shareurl,
        AFont : result.afont,
        QFont : result.qfont,
        Printable : result.printable,
        Bg: result.Bg ? apiurl + "static/" + result.Bg : this.state.Bg,
    })).then(
      _=>{
        localurl = apiurl +  "ssim/" + this.state.Surl.split("/").pop() 
        fetch(localurl, {
          method: 'GET', mode: 'cors', cache: 'no-cache', 
          headers: {'Content-Type': 'application/json'}
        }).then((res) => res.json())
        .then(result => this.setState({
          Imurl : apiurl + result.downloadlink  
        }))
        .then(_ =>{
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
        })
      }
    );
  
  }

  GetImage() {
    var that = this;
    return that.setState
  }

  GenerateImage() {
    this.setState({Canvurl : true})
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
          <button className='w-full h-8' onClick={this.GenerateImage.bind(this)}> 
            <p className={this.state.Canvurl ? "hidden" : "block text-white text-center h-8 rounded-full bg-orange-400 px-3 pt-px shadow-sm"}>Generate image locally</p>
            <a className={!this.state.Canvurl ? "hidden" : "block text-white text-center  h-8 rounded-full bg-green-400 px-3 pt-px shadow-sm"} href={typeof(this.state.Canvurl) == 'string' ? this.state.Canvurl : "/"}> Get image </a> 
          </button>
          <a className='block w-full text-white text-center h-8 rounded-full bg-green-400 px-3 pt-px shadow-sm' href={this.state.Imurl ? this.state.Imurl : apiurl + "static/download/" + this.state.Surl.split("/").pop() + ".png"  } >Download from servers</a>
          <Copy url={this.state.Surl}></Copy>
        </div>
        
        <div className='hidden'>
          <Canvas GetImage={!this.state.Canvurl ? false : this.GetImage.bind(this)} Quote={this.state.Quote} Author={this.state.Author} Day={this.state.Day} Surl={this.state.Surl} Afont={this.state.AFont} Qfont={this.state.QFont} Printable={this.state.Printable} Bg={this.state.Bg}/>
        </div>
    
      </main>
    
    );
  }
}

export default Home;
