var folders = {
  'season_one'      : 'static/imgs/tiles/G-Zombicide/tiles/',
  'angry_neighbors' : 'static/imgs/tiles/G-Zombicide-AN/tiles/',
  'prison_outbreak' : 'static/imgs/tiles/G-Zombicide-PO/tiles/',
  'rue_morgue'      : 'static/imgs/tiles/G-Zombicide-RM/tiles/',
  'toxic_city_mall' : 'static/imgs/tiles/G-Zombicide-TCM/tiles/',
  'silhouette_pack' : 'static/imgs/tiles/G-Zombicide-Z/tiles/'
}

var season_one_sources = {
  '1b' : folders['season_one'] + '1b.png',
  '2b' : folders['season_one'] + '2b.png',
  '3b' : folders['season_one'] + '3b.png',
  '4b' : folders['season_one'] + '4b.png',
  '5b' : folders['season_one'] + '5b.png',
  '1c' : folders['season_one'] + '1c.png',
  '2c' : folders['season_one'] + '2c.png',
  '3c' : folders['season_one'] + '3c.png',
  '4c' : folders['season_one'] + '4c.png',
  '4d' : folders['season_one'] + '4d.png',
  '4e' : folders['season_one'] + '4e.png',
  '5c' : folders['season_one'] + '5c.png',
  '5d' : folders['season_one'] + '5d.png',
  '5e' : folders['season_one'] + '5e.png',
  '5f' : folders['season_one'] + '5f.png',
  '6b' : folders['season_one'] + '6b.png',
  '6c' : folders['season_one'] + '6c.png',
  '7b' : folders['season_one'] + '7b.png'
};

season_one_thumbs_tiles = {
  '1b' : folders['season_one'] + 'thumbs/1b_thumb.png',
  '2b' : folders['season_one'] + 'thumbs/2b_thumb.png',
  '3b' : folders['season_one'] + 'thumbs/3b_thumb.png',
  '4b' : folders['season_one'] + 'thumbs/4b_thumb.png',
  '5b' : folders['season_one'] + 'thumbs/5b_thumb.png',
  '1c' : folders['season_one'] + 'thumbs/1c_thumb.png',
  '2c' : folders['season_one'] + 'thumbs/2c_thumb.png',
  '3c' : folders['season_one'] + 'thumbs/3c_thumb.png',
  '4c' : folders['season_one'] + 'thumbs/4c_thumb.png',
  '4d' : folders['season_one'] + 'thumbs/4d_thumb.png',
  '4e' : folders['season_one'] + 'thumbs/4e_thumb.png',
  '5c' : folders['season_one'] + 'thumbs/5c_thumb.png',
  '5d' : folders['season_one'] + 'thumbs/5d_thumb.png',
  '5e' : folders['season_one'] + 'thumbs/5e_thumb.png',
  '5f' : folders['season_one'] + 'thumbs/5f_thumb.png',
  '6b' : folders['season_one'] + 'thumbs/6b_thumb.png',
  '6c' : folders['season_one'] + 'thumbs/6c_thumb.png',
  '7b' : folders['season_one'] + 'thumbs/7b_thumb.png',
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

$(function(){
  $.event.props.push('dataTransfer');

  // Affichage init
  // $tiles = $('.tile');
  // $tiles.each(function(i,v){
  //   console.log('*****************',$(v).position().top)
  //   $(v).css({top:0});
  //   console.log($(v).position().top,'*****************')
  // });

  // Initialisation des objets jQueryUI
  // var $tile;
  $( ".draggable" ).draggable({
    // grid: [ 15,15 ], // Matching bootstrap margins
    revert: "invalid",
    snap:'.snappable',
    snapMode : 'both',
    snapTolerance : '5',
    handle : '.handle',
    start: function( event, ui ) {
      // console.log($(event.target))
      // $tile = $(event.target);
      // $id = $tile.prop('id');
      // console.log('*** id start ***',$tile, $id);
      // $('#img_'+$id).prop('src',season_one_sources[$id])
    },
    stop: function( event, ui ) {
      // console.log('*** ui ***',ui);
      // console.log('*** offset ***',$('#dragzone').offset().top);
      $tile = $(event.target);
      // $id = $tile.prop('id');
      // $('#img_'+$id).prop('src',season_one_thumbs_tiles[$id])
      // $tile = $(event.target);
      // var tilePosTop = $tile.position().top;
      // $tiles = $tile.nextAll();
      // $tiles.each(function(key,tile){
      //   var posTop = $(tile).position().top;
      //   console.log('*** tile ***', posTop);
      //   $(tile).offset({ top: posTop-tilePosTop-40});
      // })
    }
  });
  $( ".droppable" ).droppable({
    tolerance : "fit",
    drop: function( event, ui ) {
      // console.log('*** target ***',event.target)
      // console.log('*** tile ***',$tile)

    }
  });

  // Penser à gérer l'overlapping : 
  // déplacer la tile dans la case la plus proche
  
  // Tile rotation +=90deg
  $('.rotate').on('click', function(){
    var $tileImg = $(this).parent('li').children('img');
    var $cssRotation = getRotationDegrees($tileImg)+90;
    $tileImg.css('-webkit-transform','rotate('+$cssRotation+'deg)');
    $(this).css('-webkit-transform','rotate('+$cssRotation+'deg)');
  });

  // Tile deletion : back to initial place
  $('.delete').on('click', function(){
    console.log("*** deletion ***");
  });

  // Disable all modifications
  $('.lock').on('click',function(){
    var $tile = $(this).parent('li');
    var $id = $tile.prop('id');
    $(".lock_"+$id).toggleClass('unlocked');
    $('.handle_'+$id).toggle('invisible');
    $('.rotate_'+$id).toggle('invisible');
    $('.delete_'+$id).toggle('invisible');
    if($tile.draggable("option", "disabled")){
      $tile.draggable('enable');
    } else{
      $tile.draggable('disable');
    }
  })
});
