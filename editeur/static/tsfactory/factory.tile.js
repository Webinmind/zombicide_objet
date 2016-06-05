// import { Mission } from './factory.mission';
"use strict";
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
        // console.log(this._name);
        console.log(JSON.stringify(this));
    };
    Tile.prototype.getPosition = function () {
        return { top: this._top, left: this._left, angle: this._angle };
    };
    Tile.prototype.setPosition = function (top, left, angle) {
        this._top = top;
        this._left = left;
        this._angle = angle;
    };
    Tile.prototype.getStorage = function () {
        console.log(localStorage.getItem(this._name));
    };
    Tile.prototype.setStorage = function () {
        localStorage.setItem(this._name, JSON.stringify(this));
    };
    return Tile;
}());
exports.Tile = Tile;
;
