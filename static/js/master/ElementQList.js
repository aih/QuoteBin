$(function() {    
    $('.slide').hide();
    $('.title').live('click', function(){
        $(this).parent().siblings('.slide').toggle('slow');
    });
    $('.slide2').hide();
    $('.slider').live('click', function(){
        $(this).siblings('.slide2').toggle('slow');
    });
    $('.share_email').live('submit', function(e){
       e.preventDefault();
       var data = $(this).serialize();
       $.get(AJAX_URL, data, function(html){
       });
       $('.slide2').hide();
    });
    $('.quote_delete').live('click', function(){
        var data = $(this).attr('data-id');
        var that = this;
        $.get(AJAX_URL, {'data_id': data}, function(html){
            $(that).parent().parent().parent().remove();
        });
    });
});

