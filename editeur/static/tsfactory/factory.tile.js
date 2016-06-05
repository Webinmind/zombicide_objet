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
exports.Tile = Tile;
;
