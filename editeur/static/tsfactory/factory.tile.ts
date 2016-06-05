export class Tile{
  private _name   : string;
  private _mission: number;
  private _top    : number;
  private _left   : number;
  private _angle  : number;
  private _dropped: boolean;
  private _parent : string;
  constructor(name    : string,
              mission?: number,
              top?    : number,
              left?   : number,
              angle?  : number,
              dropped?: boolean,
              parent? : string){
    this._name = name;
    this._mission = mission; 
    this._top = top; 
    this._left = left; 
    this._angle = angle; 
    this._dropped = dropped; 
    this._parent = parent; 
  }
  toString(): void{
    console.log(this._name);
  }
  isDropped():boolean{
    return this._dropped;
  }
  getParent():string{
    return this._parent;
  }
  getTop():number{
    return this._top;
  }
  getLeft():number{
    return this._left;
  }
  getAngle():number{
    return this._angle;
  }
  getPosition():any {
    return {top:this._top, left:this._left, angle:this._angle};
  }
  getStorage():void{
    console.log(localStorage.getItem(this._name));
  }
  setPosition(top:number,left:number,angle:number):void {
    this._top = top;
    this._left = left;
    this._angle = angle;
  }
  setTop(top:number):void{
    this._top = top;
  }
  setLeft(left:number):void{
    this._left = left;
  }
  setAngle(angle:number):void{
    this._angle = angle;
  }
  setDropped(dropped:boolean):void{
    this._dropped = dropped
  }
  setParent(parent:string):void{
    this._parent = parent;
  }
  setStorage():void{
    localStorage.setItem(this._name, JSON.stringify(this));
  }
};