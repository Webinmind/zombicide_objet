function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  } 
  return cookieValue;
}

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url) {
  // test that a given url is a same-origin URL
  // url could be relative or scheme relative or absolute
  var host = document.location.host; // host + port
  var protocol = document.location.protocol;
  var sr_origin = '//' + host;
  var origin = protocol + sr_origin;
  // Allow absolute or scheme relative URLs to same origin
  return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
      (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
      // or any other URL that isn't scheme relative or absolute i.e relative.
      !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
  }
});

function clearDropzone(modele){
  var $dropzone = $('#dropzone');
  if(modele === 'tiles'){
    $dropzone.children('.tile').remove();
  } else{
    $dropzone.find('.token').remove();
  }
}

function isNewTile(tile_id, oldTiles){
  return !(_.contains(oldTiles,tile_id));
}

function isNewToken(token_id, oldTokens){
  return !(_.contains(oldTokens,token_id));
}

function getRotationDegrees(obj) {
  var matrix = obj.css("-webkit-transform") ||
               obj.css("-moz-transform")    ||
               obj.css("-ms-transform")     ||
               obj.css("-o-transform")      ||
               obj.css("transform");
  var angle = 0;
  if(matrix !== 'none') {
    var values = matrix.split('(')[1].split(')')[0].split(',');
    var a = values[0];
    var b = values[1];
    angle = Math.round(Math.atan2(b, a) * (180/Math.PI));
  }
  return angle;
}

function _d(txt,params){
  str = '*** '+txt+' ***';
  n = function(params){
    $(params).each(function(i,v){
      return v
    })
  }
  console.log('*** '+txt+' ***', n(params))
}