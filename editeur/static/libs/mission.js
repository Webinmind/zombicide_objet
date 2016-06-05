$(function(){
  var $id    = 0;
  var $top   = 0;
  var $left  = 0;
  var $angle = 0;

  // LocalStorage
  localStorage.setItem('dropped_tiles', dropped_tiles_json);
  localStorage.setItem('dropped_doors', dropped_doors_json);
  localStorage.setItem('dropped_objectives', dropped_objectives_json);
  localStorage.setItem('dropped_spawns', dropped_spawns_json);
  localStorage.setItem('dropped_cars', dropped_cars_json);
  localStorage.setItem('dropped_noises', dropped_noises_json);
  localStorage.setItem('dropped_exits', dropped_exits_json);


  // Modal tiles actives NEW VERSION
  $('input').val('');
  $(jQuery.parseJSON(dropped_tiles_json)).each(function(i,v){
    $('#'+v.fields.name).addClass('active');
  });
  $('.btn-add-tiles').trigger('click');

  // Populate Number of Tokens
  var tokenNumberFiller = function(param){
    // Convert string to parameters
    param = param.replace(/[\[*\]*{*}*^'$*]/g,'').split(',')
    $(param).each(function(i,v){
      v=v.split(':')
      localStorage.setItem(v[0].trim(),parseInt(v[1]));
      $('#'+v[0].trim()).next('input').val(parseInt(v[1]));
    })
  };
  tokenNumberFiller(objectives_in_use);
  tokenNumberFiller(doors_in_use);
  tokenNumberFiller(cars_in_use);
  tokenNumberFiller(noises_in_use);
  tokenNumberFiller(exits_in_use);
  tokenNumberFiller(spawns_in_use);


  // Modal Tokens Activation
  doorsInUseArray      = []
  objectivesInUseArray = []
  carsInUseArray       = []
  noisesInUseArray     = []
  exitsInUseArray      = []
  spawnsInUseArray      = []

  $(jQuery.parseJSON(dropped_doors_json)).each(function(i,v){
    // doorsInUseArray.push(tokenfactory(v.fields));
    $('#token_'+v.fields.ref).addClass('active')
  });
  $(jQuery.parseJSON(dropped_objectives_json)).each(function(i,v){
    // objectivesInUseArray.push(tokenfactory(v.fields));
    $('#token_'+v.fields.ref).addClass('active')
  });
  $(jQuery.parseJSON(dropped_cars_json)).each(function(i,v){
    // carsInUseArray.push(tokenfactory(v.fields));
    $('#token_'+v.fields.ref).addClass('active')
  });
  $(jQuery.parseJSON(dropped_noises_json)).each(function(i,v){
    // noisesInUseArray.push(tokenfactory(v.fields));
    $('#token_'+v.fields.ref).addClass('active')
  });
  $(jQuery.parseJSON(dropped_exits_json)).each(function(i,v){
    // exitsInUseArray.push(tokenfactory(v.fields));
    $('#token_'+v.fields.ref).addClass('active')
  });
  $(jQuery.parseJSON(dropped_spawns_json)).each(function(i,v){
    // spawnsInUseArray.push(tokenfactory(v.fields));
    $('#token_'+v.fields.ref).addClass('active')
  });
  
  // $('.token_in_use').each(function(i,v){
  //   $('#token_'+$(v).data('id')).addClass('active');
  //   $('#door_'+$(v).data('id')).addClass('active');
  //   $('#noise_'+$(v).data('id')).addClass('active');
  //   $('#exit_'+$(v).data('id')).addClass('active');
  // });
  $('.btn-add-tokens').trigger('click');

  // Input Objects :
  //    objectsArrays
  // console.log('*** dropped_tiles_json ***',dropped_tiles_json)
  // console.log('*** dropped_doors_json ***',dropped_doors_json)
  // console.log('*** dropped_objectives_json ***',dropped_objectives_json)
  // console.log('*** dropped_spawns_json ***',dropped_spawns_json)
  // console.log('*** dropped_cars_json ***',dropped_cars_json)
  // console.log('*** dropped_noises_json ***',dropped_noises_json)
  // console.log('*** dropped_exits_json ***',dropped_exits_json)

  // Input datas :
  //    dropped_tiles_json
  //    dropped_doors_json
  //    dropped_objectives_json
  //    dropped_spawns_json
  //    dropped_cars_json
  //    dropped_noises_json
  //    dropped_exits_json

  // function setObjectsPosition(datas){
  //   var datas = jQuery.parseJSON(datas);
  //   $(datas).each(function(i,v){
  //     $('#'+v.fields.name)
  //     .css({
  //       top : v.fields.top+'px',
  //       left : v.fields.left+'px'
  //     })
  //     .children('img')
  //     .css({
  //       '-webkit-transform' : 'rotate('+v.fields.angle+'deg)'
  //     });
  //   });
  // }

  // setObjectsPosition(dropped_tiles_json)
  // Objects positionning
  // $('.objects_in_use span').each(function(i,v){
  //   $id    = $(v).data('id');
  //   $top   = $(v).data('top');
  //   $left  = $(v).data('left');
  //   $angle = $(v).data('angle');
  //   $('#'+$id).css({
  //     top : $top+'px',
  //     left : $left+'px'
  //   });
  //   $('#'+$id+' img').css({
  //     '-webkit-transform' : 'rotate('+$angle+'deg)'
  //   });
  // });

  // Mission saving
  $('.save-mission').on('click', function(event){
    var $target = $(event.target);
    var csrftoken = getCookie('csrftoken');
    $.ajax({method: 'POST',
            dataType:'json',
            url:'/savemission/',
            csrftoken:csrftoken,
            data:{'mission_id':$('.mission_number').data('id'),
                  'mission_name':$('.mission_name').val()}
                  
    })
    $('.mission-list-item-'+$('.mission_number').data('id')).text($('.mission_name').val())
  });

  // Show the hovered object
  // $('.objects_in_use span').hover(
  //   function(event){
  //     var id = $(event.target).prop('id');
  //     $('#dropzone .tile[id!="'+id+'"]').animate({'opacity':'0'});
  //     $('#dropzone .token[id!="'+id+'"]').animate({'opacity':'0'});
  //   },
  //   function(event){
  //     var id = $(event.target).prop('id');
  //     $('#dropzone .tile[id!="'+id+'"]').animate({'opacity':'1'});
  //     $('#dropzone .token[id!="'+id+'"]').animate({'opacity':'1'});
  //   }
  // );
});