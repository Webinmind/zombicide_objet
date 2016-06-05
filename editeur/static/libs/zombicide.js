// UTILISER LE LOCALSTORAGE PLUTÔT QUE L'INTERFACE !!!!

$(function(){

  var newTiles = [],
      oldTiles = [],
      newTokens = [],
      oldTokens = [],
      currentMission = $('.mission_number').data('id');
  
  /* ************** BTN-GROUPS ************** */
  $('.btn-group-tile').on('click','.btn', function(event){
    // Btn-group tweaking to behave like radio groups
    var $target = $(event.target);
    var $parent = $target.parents('button')
    var $ancestor = $target.parents('li');
    $ancestor.children('.btn').not($parent).removeClass("active");
  });
  $('.btn-group-door').on('click','.btn', function(event){
    // Btn-group tweaking to behave like radio groups
    var $target = $(event.target);
    var $parent = $target.parents('button')
    var $ancestor = $target.parents('li');
    $ancestor.children('.btn').not($parent).removeClass("active");
  });
  $('.token_number').on('click',function(e){
    e.preventDefault();
    e.stopPropagation();
  });

  // Mission saving
  $('.save-mission-pdf').on('click', function(event){
    var $target = $(event.target);
    var csrftoken = getCookie('csrftoken');
    $.ajax({method: 'POST',
            dataType:'json',
            url:'/savemission/',
            csrftoken:csrftoken,
            data:{'mission_id':$('.mission_number').data('id'),
                  'mission_name':$('.mission_name').val(),
                  'mission_difficulty':$('.mission_difficulty').val(),
                  'mission_resume':$('.mission_resume').val(),
                  'mission_objectives':$('.mission_objectives').val(),
                  'nb_of_player':$('.nb_of_player').val(),
                  'mission_time':$('.mission_time').val()}
                  
    });
    $('.mission-list-item-'+$('.mission_number').data('id')).text($('.mission_name').val())
  });

  /* ************** TILES ************** */
  // Tile Selection
  $('.btn-add-tiles').on('click',function(){
    // Tiles list UI Update
    var listTilesIds = []
    var activeTiles = $('.active').find('.tile');
    var unactiveTiles = $('button').not('.active').find('.tile');

    newTiles = [];

    // Tiles actif dans les modaux
    activeTiles.each(function(i,v){
      newTiles.push($(v).prop('id'));
    });
    
    // Tiles dans la liste
    var $tileList = $('.tile_in_use');
    $tileList.each(function(i,v){
      listTilesIds.push($(v).data('id'));
    });
    
    // Ajout des nouveaux tiles dans l'interface
    // et dans la BDD
    $(newTiles).each(function(i,v){
      var tile_id = v;

      if(!_.contains(listTilesIds,tile_id)){
        // Ajout des nouveaux tiles dans l'interface
        $("<span>",{"class":'tile_in_use '+tile_id,'html':tile_id}).appendTo($('.tiles_used'));

        // Ajout des nouveaux tiles à la BDD
        var csrftoken = getCookie('csrftoken');
        $.ajax({method: 'POST',
                dataType:'json',
                url:'/addtilesdatas/',
                csrftoken:csrftoken,
                data:{'id'     : tile_id,
                      'mission': currentMission}
        });
      }  
    });

    // Suppression de toutes les tiles non actif dans les modaux
    // Il est important de faire mieux !!!
    unactiveTiles.each(function(i,v){
      var tile_id = $(v).prop('id');
      var csrftoken = getCookie('csrftoken');
      $.ajax({method: 'POST',
              dataType:'json',
              url:'/removetilesdatas/',
              csrftoken:csrftoken,
              data:{'id'     : tile_id,
                    'mission': currentMission}
      });
    });

    clearDropzone('tiles');
    
    // Selected tiles to append to dropZone
    $(newTiles).each(function(i,id){
      var $tile = $('#'+id).children('.tile');
      var $newTile = $tile.clone(true,true).
      addClass('dropped big').
      children('img').removeClass('thumb').addClass('big').
      parent('.tile').addClass('snappable').
      draggable({
        grid: [10, 10],
        snap:'.snappable',
        snapMode : 'both',
        snapTolerance : '5',
        // handle : '.handle',
        stack  : '.tile', 
        containment: "#dropzone",
        scroll: false,
        stop:function(event, ui){
          $(this).css('z-index',1);
          var csrftoken = getCookie('csrftoken');
          var parent = $(event.target).data('parent');
          $('.tile_in_use.'+id).data({'top':$(this).position().top,
                                      'left':$(this).position().left,
                                      'angle':getRotationDegrees($(this).children('img'))});
          
          $.ajax({method: 'POST',
                  dataType:'json',
                  url:'/updatetilesdatas/',
                  csrftoken:csrftoken,
                  data:{'id':id,
                        'mission':currentMission,
                        'parent':parent,
                        'top':$(this).position().top,
                        'left':$(this).position().left,
                        'angle':getRotationDegrees($(this).children('img'))}
          })
        }
      }).
      appendTo('#dropzone');      

      // Réattribution de la position si la tile
      // est déjà sur la map avant reload
      // if(!isNewTile($newTile.prop('id'), oldTiles)){
        var datas = $('.tile_in_use.'+$newTile.prop('id')).data();
        // console.log('*** datas ***', $newTile.prop('id'), 'top:', datas.top+'px', 'left:', datas.left+'px')
        $newTile.css({
          top  : parseInt(datas.top)+'px',
          left : parseInt(datas.left)+'px'
        });
        $newTile.children('img').css({
          '-webkit-transform' : 'rotate('+datas.angle+'deg)'
        });
        $newTile.find('.fa-rotate').css('-webkit-transform','rotate('+datas.angle+'deg)');
      // }
    });
    // oldTiles = newTiles;
  });

  /* ************** PIONS ************** */

  $('.btn-add-tokens').on('click',function(){
    var listTokensIds = [];
    var nbTokens = [];
    var activeTokens = $('.active').find('.token');
    var unactiveTokens = $('button').not('.active').find('.token');

    // Tableau des Tokens en jeu
    var newTokens = [];

    // Tokens actif dans les modaux
    // Récupération des Tokens actifs
    // ainsi que leur nombre
    activeTokens.each(function(i,v){
      var cpt = 0;
      $id = $(v).prop('id');
      newTokens.push($id+'_'+cpt);
      if($(v).next('.token_number').val()){
        nbTokens[$id] = ($(v).next('.token_number').val()!='undefined')?parseInt($(v).next('.token_number').val()):1;
        for (var j=1;j<nbTokens[$id];j++){
          newTokens.push($(v).data('id')+'_'+j);
        }
        
        // Remove removed Tokens
        var tokens_to_remove = 0
        tokens_to_remove = parseInt($('span.'+$id).data('number')-nbTokens[$id]);
        // console.log('*** tokens_to_remove ***', tokens_to_remove)
        var csrftoken = getCookie('csrftoken');
        var tokenType = $('#'+$id+'_'+nbTokens[$id]).data('type');
        var tokenColor = $id.replace('close_door_','').
                                replace('open_door_','').
                                replace('objective_','').
                                replace('spawn_','').
                                replace('car_','').
                                replace('exit_','').
                                replace('noise_','');

        if(tokens_to_remove>0){
          for(var i=tokens_to_remove+1;i>0;i--){
            // console.log('*** element ***', $('#'+$id+'_'+i))
            // Remove from Tokens in use
            $('#'+$id+'_'+i).remove();
            // Remove from BDD
            $.ajax({method: 'POST',
                    dataType:'json',
                    url:'/removetokensui/',
                    csrftoken:csrftoken,
                    data:{'token_name' : $id+'_'+i,
                          'tokenType'     : tokenType,
                          'mission'  : currentMission}

            });
          }
        }
      }
    });
    

    // Tokens dans la liste
    var $tokenList = $('.token_in_use');
    $tokenList.each(function(i,v){
      listTokensIds.push($(v).prop('id'));
    });
    // console.log('*** newTokens ***', newTokens)
    // console.log('*** listTokensIds ***', listTokensIds)
    
    // Ajout des nouveaux tokens dans l'interface
    // et dans la BDD
    $(newTokens).each(function(i,v){
      var token_id = v;
      // console.log('*** token_id ***', token_id)
      if(!_.contains(listTokensIds,token_id)){
        // Ajout des nouveaux tokens à l'interface
        // console.log('*** Ajout des nouveaux tokens ***', token_id)
        var pos = token_id.lastIndexOf('_');
        var modeleid = token_id.substr(0,pos);
        var str = '<span class="token_in_use '+token_id+'" data-id="'+modeleid+'" >'+token_id+'</span>';
        $('.'+$('#'+modeleid).data('type')+'s_used').append(str);

        var tokenType = $('#'+modeleid).data('type');
        var tokenColor = modeleid.replace('close_door_','').
                                  replace('open_door_','').
                                  replace('objective_','').
                                  replace('spawn_','').
                                  replace('car_','').
                                  replace('noise_','').
                                  replace('exit_','');
        var tokenState = '';
        if(tokenType=='door'){
          var tokenState = $('#'+modeleid).data('state');
        }
        // Ajout des nouveaux tokens à la BDD
        var csrftoken = getCookie('csrftoken');
        $.ajax({method: 'POST',
                dataType:'json',
                url:'/addtokensdatas/',
                csrftoken:csrftoken,
                data:{'modeleid' : modeleid,
                      'id'       : token_id,
                      'type'     : tokenType,
                      'color'    : tokenColor,
                      'state'    : tokenState,
                      'mission'  : currentMission}
        });
      }  
    });


    // Suppression de tous les tokens non actif dans les modaux
    // Il est important de faire mieux !!!
    unactiveTokens.each(function(i,v){
      var token_id = $(v).prop('id');
      $('#'+token_id).next('input').val('')
      var dataid = $(v).data('id');
      var tokenType = $('#'+token_id).data('type');
      var tokenColor = token_id.replace('close_door_','').
                                replace('open_door_','').
                                replace('objective_','').
                                replace('spawn_','').
                                replace('car_','').
                                replace('exit_','').
                                replace('noise_','');

      var pos = tokenColor.lastIndexOf('_');
      tokenColor = tokenColor.substr(0,pos);
      $('.objects_in_use .'+token_id).remove();
      var tokenState = '';
      if($('#'+token_id).data('type')=='door'){
        var tokenState = $('#'+token_id).data('state');
      }
      var csrftoken = getCookie('csrftoken');
      $.ajax({method: 'POST',
              dataType:'json',
              url:'/removetokensdatas/',
              csrftoken:csrftoken,
              data:{'token_id' : token_id,
                    'modeleid' : dataid,
                    'type'     : tokenType,
                    'color'    : tokenColor,
                    'state'    : tokenState,
                    'mission'  : currentMission}
      });
    });
    
    clearDropzone('tokens');

    // Selected tokens to append to dropZone
    $(newTokens).each(function(i,id){
      var pos = id.lastIndexOf('_');
      original_id = id.substr(0,pos)
      var $token = $('#'+original_id);
      var $dataid = $('#'+original_id).data('id');
      var $newToken = $token.clone(true,true).
      addClass('dropped small').
      children('img').removeClass('thumb').addClass('small').
      parent('.token').addClass('snappable').
      data('type',$('#'+id).data('parent')).
      data('id',original_id).
      prop('id',id).
      draggable({
        grid: [1, 1],
        snap:'.snappable',
        snapMode : 'both',
        snapTolerance : '5',
        // handle : '.handle',
        containment: "#dropzone",
        scroll: false,
        stop:function(event, ui){
          $(this).css('z-index',1000);
          $dataid = $(this).data('id');
          var tokenType = $(this).data('type');
          var csrftoken = getCookie('csrftoken');
          var tokenColor = $dataid.replace('close_door_','').
                                   replace('open_door_','').
                                   replace('objective_','').
                                   replace('spawn_','').
                                   replace('car_','').
                                   replace('noise_','').
                                   replace('exit_','');
          var tokenState = '';
          if($('#'+id).data('type')=='door'){
            var tokenState = $('#'+id).data('state');
          }

          $('.token_in_use.'+id).data({'top':$(this).position().top,
                                      'left':$(this).position().left,
                                      'angle':getRotationDegrees($(this).children('img')),
                                      'color':tokenColor,
                                      'type':tokenType});
          
          $.ajax({method: 'POST',
                  dataType:'json',
                  url:'/updatetokensdatas/',
                  csrftoken:csrftoken,
                  data:{'modeleid':$dataid,
                        'id':$(this).prop('id'),
                        'type':tokenType,
                        'mission':currentMission,
                        'top':$(this).position().top,
                        'left':$(this).position().left,
                        'color':tokenColor,
                        'type':tokenType,
                        'angle':getRotationDegrees($(this).children('img'))}, 
          });
        }
      }).
      appendTo('#dropzone');

      // Réattribution de la position si le(s) token(s)
      // est(sont) déjà sur la map avant reload
      if(!isNewToken($newToken.prop('id'), oldTokens)){
        var datas = $('.token_in_use.'+$newToken.prop('id')).data();
        $newToken.css({
          top  : parseInt(datas.top)+'px',
          left : parseInt(datas.left)+'px'
        });
        $newToken.children('img').css({
          '-webkit-transform' : 'rotate('+datas.angle+'deg)'
        });
        $newToken.find('.fa-rotate').css('-webkit-transform','rotate('+datas.angle+'deg)');
      }
    });
    oldTokens = newTokens;
  });

  // Controls interaction
  $('.tile .rotate').on('click', function(event){
    var $target = $(event.target).parents('.tile');
    var $tileImg = $target.children('img');
    var $parent = $target.data('parent');
    var datas = {'top'    : $target.position().top,
                 'left'   : $target.position().left,
                 'angle'  : getRotationDegrees($tileImg)+90,
                 'parent' : $parent};

    $('.tile_in_use.'+$target.prop('id')).data(datas);
    
    var csrftoken = getCookie('csrftoken');
    $.ajax({method: 'POST',
            dataType:'json',
            url:'/updatetilesdatas/',
            csrftoken:csrftoken,
            data:{'id'      : $target.prop('id'),
                  'mission' : currentMission,
                  'parent'  : $parent,
                  'top'     : datas.top,
                  'left'    : datas.left, 
                  'angle'   : datas.angle}
    });
    $tileImg.css('-webkit-transform','rotate('+datas.angle+'deg)');
    $(event.target).css('-webkit-transform','rotate('+datas.angle+'deg)');
  });

  // Disable all modifications
  $('.tile .lock').on('click',function(){
    var $tile = $(event.target).parents('.tile');
    var $id = $tile.prop('id').replace('dropped_','');
    $('.lock-all').removeClass('active');
    $(".lock_"+$id).toggleClass('unlocked');
    $('.rotate_'+$id).toggle('invisible');
    if($tile.draggable("option", "disabled")){
      $tile.draggable('enable');
      $tile.removeClass('locked');
    } else{
      $tile.draggable('disable');
      $tile.addClass('locked');
    }
  });

  // Controls interaction
  $('.token .rotate').on('click', function(event){
    var $target = $(event.target).parents('.token');
    var $modeleid = $target.data('id');
    var $tokenImg = $target.children('img');
    var $id = $target.prop('id');
    var tokenType = $target.data('type');
    var tokenColor =  $modeleid.replace('close_door_','').
                                replace('open_door_','').
                                replace('objective_','').
                                replace('spawn_','').
                                replace('car_','');
    var tokenState = '';
    if($('#'+$id).data('type')=='door'){
      var tokenState = $('#'+$id).data('state');
    }

    var datas = {'top'    : $target.position().top,
                 'left'   : $target.position().left,
                 'angle'  : getRotationDegrees($tokenImg)+90,
                 'type'   : tokenType,
                 'color'  : tokenColor,
                 'state'  : tokenState,
                 'id'     : $modeleid};

    $('.token_in_use.'+$id).data(datas);
    var csrftoken = getCookie('csrftoken');
    $.ajax({method: 'POST',
            dataType:'json',
            url:'/updatetokensdatas/',
            csrftoken:csrftoken,
            data:{'id'       : $id,
                  'modeleid' : $modeleid,
                  'mission'  : currentMission,
                  'type'     : tokenType,
                  'color'    : tokenColor,
                  'top'      : datas.top,
                  'left'     : datas.left, 
                  'angle'    : datas.angle}
    });
    $tokenImg.css('-webkit-transform','rotate('+datas.angle+'deg)');
    $(event.target).css('-webkit-transform','rotate('+datas.angle+'deg)');
  });

  // Disable all modifications
  $('.token .lock').on('click',function(){
    var $token = $(event.target).parents('.token');
    var $id = $token.prop('id');
    $(".lock_"+$id).toggleClass('unlocked');
    // $('.handle_'+$id).toggle('invisible');
    $('.rotate_'+$id).toggle('invisible');
    if($token.draggable("option", "disabled")){
      $token.draggable('enable');
    } else{
      $token.draggable('disable');
    }
  });
});