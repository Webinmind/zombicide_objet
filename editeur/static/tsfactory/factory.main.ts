class Mission{
  private _name      : string;
  private _numero    : number;
  private _active    : boolean;
  private _resume    : string;
  private _objectives: string;
  private _rules     : string;
  private _difficulty: string;
  private _players   : number;
  private _time      : string;
  constructor(name       : string,
              numero     : number,
              active     : boolean,
              resume?    : string,
              objectives?: string,
              rules?     : string,
              difficulty?: string,
              players?   : number,
              time?      : string){
    this._name = name;
    this._numero = numero;
    this._active = active;
    this._resume = resume;
    this._objectives = objectives;
    this._rules = rules;
    this._difficulty = difficulty;
    this._players = players;
    this._time = time;
    
  }
  toString(){
    console.log(this._name);
  }
  isActive():boolean{
    return this._active;
  }
  getNumero():number{
    return this._numero;
  }
  getResume():string{
    return this._resume;
  }
  getObjectives():string{
    return this ._objectives;
  }
  getRules():string{
    return this._rules;
  }
  getDifficulty():string{
    return this._difficulty;
  }
  getPlayers():number{
    return this._players;
  }
  getTime():string{
    return this._time;
  }
  getStorage():void{
    console.log(localStorage.getItem(this._name));
  }
  setActive(active:boolean):void{
    this._active = active;
  }
  setNumero(numero:number):void{
    this._numero = numero;
  }
  setResume(resume:string):void{
    this._resume = resume;
  }
  setObjectives(objectives:string):void{
    this._objectives = objectives;
  }
  setRules(rules:string):void {
    this._rules = rules;
  }
  setDifficulty(difficulty:string):void {
    this._difficulty = difficulty;
  }
  setPlayers(players:number):void{
    this._players = players;
  }
  setTime(time:string):void{
    this._time = time;
  }
  setStorage():void{
    localStorage.setItem(this._name, JSON.stringify(this));
  }
};

class Tile{
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

let mission1 = new Mission('testmission', 1, true);
mission1.toString();


let tile1 = new Tile('tile 1', mission1.getNumero(), 0, 15, 0, true, 'A');
tile1.toString();
console.log(tile1.getPosition());
console.log(tile1.getTop());
console.log('****');

