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
    if(! USER){
        $('.side_element a[href$="MyQuotes"]').fancybox({
            href: '#entercode_form'
        });
    }
    $('.side_element a').each(function(){
        if (window.location.pathname == $(this).attr('href')){
        $(this).addClass('selected')
        }
    })
});
