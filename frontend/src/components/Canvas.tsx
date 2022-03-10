import React, { ReactElement} from 'react';
import '../App.css';

interface propTypes {
  SetImage: Function,
  
  Author: string,
  Day: string,
  Bg: string,
  Surl : string,
  Afont : number,
  Qfont : number,
  Printable : string, 
}

interface stateTypes {}


class Canvas extends React.Component <propTypes, stateTypes> {

  canvas: React.RefObject<HTMLCanvasElement>;

  constructor (props: propTypes) {
    super(props)
    this.canvas = React.createRef();
  }


  componentDidMount(){
    
    let ImageManipulator = async () => {
      let bgi: HTMLImageElement = new Image();
      bgi.crossOrigin = "anonymous";
      bgi.src = this.props.Bg;
      let imagepromise: Promise<void> = new Promise((resolve, reject) => {
        bgi.onload = () => {
            resolve();
        }
      });
      await imagepromise
      this.canvas.current.width = bgi.width;
      this.canvas.current.height = bgi.height;
      let ctx = this.canvas.current.getContext("2d");
      
      ctx.beginPath()
      
      // draw image
      ctx.drawImage(bgi, 0, 0)
      
      // Make texts centered / baselined
      ctx.textAlign = "center";
      ctx.textBaseline = "alphabetic";
      
      // Get Font for date and write date
      ctx.font = `600 33px "Noto Serif", serif`; 
      ctx.fillText(this.props.Day, 330, 280);
      
      // Get Font for author and write author
      ctx.font = `600 ${this.props.Afont + 1}px "Noto Serif", serif`; 
      ctx.fillText(this.props.Author, 330, 830);
  
      // Change text to centered / middle
      ctx.textBaseline = "middle";
  
      // Get Font for quote and write quote
      ctx.font = `600 ${this.props.Qfont + 1}px "Noto Serif", serif`;
      var qy =  550;
      var print = this.props.Printable.split(/\r\n|\r|\n/)
      qy = qy - (print.length / 2) * (this.props.Qfont+1) * 1.1 
      for (let i = 0; i < print.length; i++ ) {
        ctx.fillText(print[i], 330, qy);
        qy = qy + (this.props.Qfont+1) * 1.2
      }
      
  
      // Change text to right aligned / baselined
      ctx.textAlign = "right";
      ctx.textBaseline = "alphabetic";
  
      // Get Font for banner and write banner
      ctx.font = `600 17px "Noto Serif", serif`; 
      ctx.fillText(this.props.Surl, 1000, 1020);
      ctx.closePath()
  
  
      var data = this.canvas.current.toDataURL()
      this.props.SetImage(data);
    }
    
    ImageManipulator = ImageManipulator.bind(this);
    ImageManipulator()
  }


  render(): ReactElement {
    return (
      <canvas style={{width: "50vh", height: "50vh" , border: "2px solid red"}} ref={this.canvas}></canvas>
    );
  }
}

export default Canvas;
