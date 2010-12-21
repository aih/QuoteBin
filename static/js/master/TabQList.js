$(function() {
    //if(USER){
        /*$('.side_element a').live('click', function(){
            var that = this;
            $.get(
                  $(that).attr('href'),
                  {},
                  function(html){
                    $('div[data-id="masterQListTab"]').html(html);
                    $('.slide').hide();
                    $('.slide2').hide();
                    }
                  );
            return false;
        });*/
    //} else {
    //$('.help_input').val($('.help_input').val());
    $('.project_delete').live('click', function(){
       var data = $(this).attr('data-id');
       if(!data){
        return;
       }
       $.get(AJAX_URL, {'data_id': data}, function(reponse){
            window.location="/";
       });
       
    });
    
});
