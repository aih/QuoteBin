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
    $('#submit_code_form').live('click', function(e){
       e.preventDefault();
       var that = $('#entercode_form');
       var data = $(that).serialize();
       $.get(AJAX_URL, data, function(response){
            if (response.success){
                window.location = window.location + 'project/MyQuotes';
            } else {
                $(that).find('.error').html('Invalid Code');
                $.fancybox.resize();
            }
            
       });
        return false;
       
    });
    $('#submit_project_form').live('click', function(e){
       e.preventDefault();
       var that = $('#project_form');
       var data = $(that).serialize();
       $.get(AJAX_URL, data, function(response){
            if (response.success){
                $('.TabSide').replaceWith(response.html);
            } else {
                $(that).find('.error').html('Invalid project Name');
            }
            
       });
      return false; 
    });
});
