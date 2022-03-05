import React, { ReactElement } from 'react';
import '../App.css';

interface propTypes {
  Quote: string,
  Author: string,
  Day: string,
  Bg: string,
}

interface stateTypes {
  Quote: string,
  Author: string,
  Day: string,
  Bg: string,
  // Surl: string,
}


class Canvas extends React.Component <propTypes, stateTypes> {

  canv: React.RefObject<HTMLCanvasElement>;
  canvstyle: any;

  constructor (props: propTypes) {
    super(props)
    this.canv = React.createRef();
    this.canvstyle = {};
    this.state = {
      Quote: props.Quote,
      Author: props.Author,
      Day: props.Day,
      Bg: props.Bg,
    };
  }

  componentDidMount(){
    const canv: any = this.canv.current;
    let ctx: CanvasRenderingContext2D = canv.getContext("2d")
    let bgi = new Image()
    bgi.src = this.state.Bg

    // canvas styling
    canv.width = bgi.width
    canv.height = bgi.height
    if (window.innerWidth >= window.innerHeight) {
      this.canvstyle = {
        width: "90vh",
        height: "90vh",
        boxShadow: "1px 1px 10px 3px black"
      }
    } else {
      this.canvstyle = {
        width: "90vw",
        height: "90vw",
      }
    }
    
    ctx.drawImage(bgi, 0, 0)

    
    
  }

  render(): ReactElement {
    return (
    
      <canvas style={this.canvstyle} ref={this.canv}></canvas>
    );
  }
}

export default Canvas;
