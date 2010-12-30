$(function(){
        $('.user_links a[href$="login"]').fancybox({
            href: '#entercode_form',
            onStart: function(){
                $('form#entercode_form')[0].reset();
                $('form#entercode_form').find('input[name="code"]').val('Enter Password');
                $('form#entercode_form').find('input[name="code"]').addClass('help_input');
                }
        });
        $('.user_links a[href$="get_code"]').fancybox({
            href: '#get_code_form',
            onStart: function(){
                $('form#get_code_form')[0].reset();
                $('form#get_code_form').find('input[name="email"]').val('Enter Email');
                $('form#get_code_form').find('input[name="email"]').addClass('help_input');
                }
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
                    setTimeout(function(){$("#flash_messages").fadeOut("slow");}, 7000);});
                } else {
                    $(that).find('.error').html(response.reason);
                    $.fancybox.resize();
                }
                
           });
            return false;
           
        });
    });
