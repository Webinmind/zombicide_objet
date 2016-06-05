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
exports.Mission = Mission;
;
