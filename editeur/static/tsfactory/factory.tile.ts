// import { Mission } from './factory.mission';

export class Tile{
  _name:    string;
  _mission: number;
  _top:     number;
  _left:    number;
  _angle:   number;
  _dropped: boolean;
  _parent:  string;
  constructor(name:     string,
              mission?: number,
              top?:     number,
              left?:    number,
              angle?:   number,
              dropped?: boolean,
              parent?:  string){
    this._name = name;
    this._mission = mission; 
    this._top = top; 
    this._left = left; 
    this._angle = angle; 
    this._dropped = dropped; 
    this._parent = parent; 
  }
  toString(): void{
    // console.log(this._name);
    console.log(JSON.stringify(this));
  }
  getPosition():any {
    return {top:this._top, left:this._left, angle:this._angle};
  }
  setPosition(top:number,left:number,angle:number):void {
    this._top = top;
    this._left = left;
    this._angle = angle;
  }
  getStorage():void{
    console.log(localStorage.getItem(this._name));
  }
  setStorage():void{
    localStorage.setItem(this._name, JSON.stringify(this));
  }
};