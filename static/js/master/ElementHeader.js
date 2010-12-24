$(function(){
        $('.user_links a[href$="login"]').fancybox({
            href: '#entercode_form'
        });
        $('.user_links a[href$="get_code"]').fancybox({
            href: '#get_code_form'
        });
        $('#get_code_form').live('submit', function(e){
           e.preventDefault();
           var that = $('#get_code_form');
           var data = $(that).serialize();
           $.get(AJAX_URL, data, function(response){
                if (response.success){
                    $('#flash_messages').html('Password has been sent to your email');
                    $.fancybox.close();
                    $('#flash_messages').fadeIn("slow", function(){
                    setTimeout(function(){$("#flash_messages").fadeOut("slow");}, 2000);});
                } else {
                    $(that).find('.error').html(response.reason);
                    $.fancybox.resize();
                }
                
           });
            return false;
           
        });
    });
