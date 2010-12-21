$(function() {
    $('.add_to_project').live('submit', function(e){
       e.preventDefault();
       var that = this;
       var data = $(this).serialize();
       $.get(AJAX_URL, data, function(response){
               
       });
       
    });
});
