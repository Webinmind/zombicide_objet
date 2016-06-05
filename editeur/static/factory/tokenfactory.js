var Token = function(spec){
  // Private
  var defaults = {
    'name':'No Name',
    'season':'No Season',
    'type':'No Type',
    'picture':'No Picture',
    'id':'No ID',
    'color':'No Color',
    'position': {'top':0, 
                 'left':15,
                 'angle':0},
    'mission':{},
    'dropped':'Not Dropped',
    'inModal':'Not inModal'
  }
  var opts = $.extend({},defaults,spec);
  var that = {};
  
  // Getters
  that.get_name = function(){
    return opts.name;
  }
  that.get_season = function(){
    return opts.season;
  }
  that.get_type = function(){
    return opts.type;
  }
  that.get_picture = function(){
    return opts.picture;
  }
  that.get_id = function(){
    return opts.id;
  }
  that.get_color = function(){
    return opts.color;
  }
  that.get_position = function(){
    return {'top':opts.position.top, 
            'left':opts.position.left, 
            'angle':opts.position.angle};
  }
  that.get_mission = function(){
    return opts.mission;
  }
  that.is_dropped = function(){
    return opts.dropped;
  }
  that.in_modal = function(){
    return opts.inModal;
  }

  // Setters
  that.set_name = function(new_name) {
    opts.name = (typeof new_name==='string')?new_name:opts.name;
  }
  that.set_season = function(new_season) {
    opts.season = (typeof new_season==='string')?new_season:opts.season;
  }
  that.set_type = function(new_type) {
    opts.type = (typeof new_type==='string')?new_type:opts.type;
  }
  that.set_picture = function(new_picture) {
    opts.picture = (typeof new_picture==='string')?new_picture:opts.picture;
  }
  that.set_id = function(new_id) {
    opts.id = (typeof new_id==='string')?new_id:id;
  }
  that.set_color = function(new_color) {
    opts.color = (typeof new_color==='string')?new_color:opts.color;
  }
  that.set_position = function(new_position) {
    opts.position = (typeof new_position==='object')?{'top':new_position.top || opts.position.top, 
                                                      'left':new_position.left || opts.position.left,
                                                      'angle':new_position.angle || opts.position.angle}:opts.position;
  }
  that.set_mission = function(new_mission){
    opts.mission = (typeof new_mission==='object')?new_mission:opts.mission;
  }
  that.set_dropped = function(new_dropped){
    opts.dropped = (typeof new_dropped==='boolean')?new_dropped:opts.dropped;
  }
  that.set_inmodal = function(new_inmodal){
    opts.inModal = (typeof new_inmodal==='boolean')?new_inmodal:opts.inModal;
  }

  return that;
}