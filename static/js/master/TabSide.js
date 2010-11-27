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
    $('.help_input').live('click', function(){
       $(this).removeClass('help_input').val(' ');
       
    });
    $('#entercode_form').live('submit', function(e){
       e.preventDefault();
       var that = this;
       var data = $(this).serialize();
       $.get(AJAX_URL, data, function(response){
            if (response.success){
                window.location = window.location;
            } else {
                $(that).find('.error').html('Invalid Code');
                $.fancybox.resize();
            }
            
       });
       
    });
    $('#bundle_form').live('submit', function(e){
       e.preventDefault();
       var that = this;
       var data = $(this).serialize();
       $.get(AJAX_URL, data, function(response){
            if (response.success){
                $('.TabSide').replaceWith(response.html);
            } else {
                $(that).find('.error').html('Invalid Bundle Name');
            }
            
       });
       
    });
});
