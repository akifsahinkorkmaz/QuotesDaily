import React, { ReactElement, ReactNode } from 'react';
import { runInThisContext } from 'vm';
import '../App.css';

interface propTypes {
  GetImage: false | Function,
  
  Quote: string,
  Author: string,
  Day: string,
  Bg: string,
  Surl : string,
  Afont : number,
  Qfont : number,
  Printable : string, 
}

interface stateTypes {

}


class Canvas extends React.Component <propTypes, stateTypes> {

  canvas: React.RefObject<HTMLCanvasElement>;
  canvstyle: any;

  constructor (props: propTypes) {
    super(props)
    this.canvas = React.createRef();
    this.canvstyle = {};
    this.state = { };
  }

  componentDidUpdate(){
      if (this.props.GetImage != false) {
        this.props.GetImage(this.RenderImage())
      }
  }

  RenderImage() {
    const canv: any = this.canvas.current;
    let ctx: CanvasRenderingContext2D = canv.getContext("2d");
    let bgi = new Image();
    bgi.crossOrigin = "anonymous";
    bgi.src = this.props.Bg;
    
    // canvas init
    canv.width = bgi.width;
    canv.height = bgi.height;
    ctx.clearRect(0, 0, canv.width, canv.height);
    
    ctx.beginPath()
    
    // draw image
    ctx.drawImage(bgi, 0, 0)
    
    // Make texts centered / baselined
    ctx.textAlign = "center";
    ctx.textBaseline = "alphabetic";
    
    // Get Font for date and write date
    ctx.font = `32px Noto Serif`; 
    ctx.fillText(this.props.Day, 330, 280);
    
    // Get Font for author and write author
    ctx.font = `${this.props.Afont}px Noto Serif`; 
    ctx.fillText(this.props.Author, 330, 830);

    // Change text to centered / middle
    ctx.textBaseline = "middle";

    // Get Font for quote and write quote
    ctx.font = `${this.props.Qfont}px Noto Serif`; 
    ctx.fillText(this.props.Printable, 330, 550);

    // Change text to right aligned / baselined
    ctx.textAlign = "right";
    ctx.textBaseline = "alphabetic";

    // Get Font for banner and write banner
    ctx.font = `10px Noto Serif`; 
    ctx.fillText(this.props.Surl, 1000, 1000);

    ctx.closePath()

    return canv.toDataURL()
  }

  render(): ReactElement {
    return (
    
      <canvas style={this.canvstyle} ref={this.canvas}></canvas>
    );
  }
}

export default Canvas;
