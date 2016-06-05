"use strict";
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
    return Mission;
}());
exports.Mission = Mission;
;
