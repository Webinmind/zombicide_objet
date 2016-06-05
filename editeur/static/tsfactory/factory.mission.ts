export class Mission{
  _name: string;
  _numero: number;
  _active: boolean;
  _resume: string;
  _objectives: string;
  _rules: string;
  _difficulty: string;
  _players: number;
  _time: string;
  constructor(name: string,
              numero: number,
              active: boolean,
              resume: string,
              objectives: string,
              rules: string,
              difficulty: string,
              players: number,
              time: string){
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
};