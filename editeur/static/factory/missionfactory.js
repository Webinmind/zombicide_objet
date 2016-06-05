var Mission = function(spec){
  // Private
  var defaults = {
    'name':'No Name',
    'number':'666',
    'active':1,
    'summary':'No Summary',
    'objectives':'No Objectives',
    'rules':'No specialrules',
    'difficulty':'easy',
    'nb_players':4,
    'mission_time':'60mn',
  }
  var opts = $.extend({},defaults,spec);
  var that = {};

  // Getters
  that.get_name = function() {
    return opts.name;
  }
  that.get_number = function(){
    return opts.number;
  };
  that.get_active = function(){
    return opts.active;
  };
  that.get_summary = function(){
    return opts.summary;
  };
  that.get_objectives = function(){
    return opts.objectives;
  };
  that.get_rules = function(){
    return opts.rules;
  };
  that.get_difficulty = function(){
    return opts.difficulty;
  };
  that.get_nb_players = function(){
    return opts.nb_players;
  };
  that.get_mission_time = function(){
    return opts.mission_time;
  };

  // Setters
  that.set_name = function(new_name) {
    opts.name = (typeof new_name==='string')?new_name:opts.name;
  }
  that.set_number = function(new_number){
    opts.number=(typeof new_number==='number' || typeof parseInt(new_number)==='number')?parseInt(new_number):opts.number;
  };
  that.set_active = function(new_active){
    opts.active=(typeof new_active==='number' || typeof parseInt(new_active)==='number')?parseInt(new_active):opts.active;
  };
  that.set_summary = function(new_summary){
    opts.summary=(typeof new_summary==='string')?new_summary:opts.summary;
  };
  that.set_objectives = function(new_objectives){
    opts.objectives=(typeof new_objectives==='string')?new_objectives:opts.objectives;
  };
  that.set_rules = function(new_rules){
    opts.rules=(typeof new_rules==='string')?new_rules:opts.rules;
  };
  that.set_difficulty = function(new_difficulty){
    opts.difficulty=(typeof new_difficulty==='string')?new_difficulty:opts.difficulty;
  };
  that.set_nb_players = function(new_nb_players){
    opts.nb_players=(typeof new_nb_players==='number' || typeof parseInt(new_nb_players))?parseInt(new_nb_players):opts.nb_players;
  };
  that.set_mission_time = function(new_mission_time){
    opts.mission_time=(typeof new_mission_time==='string')?new_mission_time:opts.mission_time;
  }

  return that;
}