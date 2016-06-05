var Mission = (function () {
    function Mission(name, numero, active, resume, objectives, rules, difficulty, players, time) {
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
    Mission.prototype.toString = function () {
        console.log(this._name);
    };
    Mission.prototype.isActive = function () {
        return this._active;
    };
    Mission.prototype.getNumero = function () {
        return this._numero;
    };
    Mission.prototype.getResume = function () {
        return this._resume;
    };
    Mission.prototype.getObjectives = function () {
        return this._objectives;
    };
    Mission.prototype.getRules = function () {
        return this._rules;
    };
    Mission.prototype.getDifficulty = function () {
        return this._difficulty;
    };
    Mission.prototype.getPlayers = function () {
        return this._players;
    };
    Mission.prototype.getTime = function () {
        return this._time;
    };
    Mission.prototype.getStorage = function () {
        console.log(localStorage.getItem(this._name));
    };
    Mission.prototype.setActive = function (active) {
        this._active = active;
    };
    Mission.prototype.setNumero = function (numero) {
        this._numero = numero;
    };
    Mission.prototype.setResume = function (resume) {
        this._resume = resume;
    };
    Mission.prototype.setObjectives = function (objectives) {
        this._objectives = objectives;
    };
    Mission.prototype.setRules = function (rules) {
        this._rules = rules;
    };
    Mission.prototype.setDifficulty = function (difficulty) {
        this._difficulty = difficulty;
    };
    Mission.prototype.setPlayers = function (players) {
        this._players = players;
    };
    Mission.prototype.setTime = function (time) {
        this._time = time;
    };
    Mission.prototype.setStorage = function () {
        localStorage.setItem(this._name, JSON.stringify(this));
    };
    return Mission;
}());
;
var Tile = (function () {
    function Tile(name, mission, top, left, angle, dropped, parent) {
        this._name = name;
        this._mission = mission;
        this._top = top;
        this._left = left;
        this._angle = angle;
        this._dropped = dropped;
        this._parent = parent;
    }
    Tile.prototype.toString = function () {
        console.log(this._name);
    };
    Tile.prototype.isDropped = function () {
        return this._dropped;
    };
    Tile.prototype.getParent = function () {
        return this._parent;
    };
    Tile.prototype.getTop = function () {
        return this._top;
    };
    Tile.prototype.getLeft = function () {
        return this._left;
    };
    Tile.prototype.getAngle = function () {
        return this._angle;
    };
    Tile.prototype.getPosition = function () {
        return { top: this._top, left: this._left, angle: this._angle };
    };
    Tile.prototype.getStorage = function () {
        console.log(localStorage.getItem(this._name));
    };
    Tile.prototype.setPosition = function (top, left, angle) {
        this._top = top;
        this._left = left;
        this._angle = angle;
    };
    Tile.prototype.setTop = function (top) {
        this._top = top;
    };
    Tile.prototype.setLeft = function (left) {
        this._left = left;
    };
    Tile.prototype.setAngle = function (angle) {
        this._angle = angle;
    };
    Tile.prototype.setDropped = function (dropped) {
        this._dropped = dropped;
    };
    Tile.prototype.setParent = function (parent) {
        this._parent = parent;
    };
    Tile.prototype.setStorage = function () {
        localStorage.setItem(this._name, JSON.stringify(this));
    };
    return Tile;
}());
;
var mission1 = new Mission('testmission', 1, true);
mission1.toString();
var tile1 = new Tile('tile 1', mission1.getNumero(), 0, 15, 0, true, 'A');
tile1.toString();
console.log(tile1.getPosition());
console.log(tile1.getTop());
console.log('****');
