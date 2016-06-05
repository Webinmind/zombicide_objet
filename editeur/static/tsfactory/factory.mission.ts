export class Mission{
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