function fancyAlert(msg) {
    jQuery.fancybox({
        'modal' : true,
        'content' : "<div style=\"margin:1px;width:240px;\">"+msg+"<div style=\"text-align:right;margin-top:10px;\"><input style=\"margin:3px;padding:0px;\" type=\"button\" onclick=\"jQuery.fancybox.close();\" value=\"Ok\"></div></div>"
    });
}
 
function fancyConfirm(msg,callback) {
    var ret;
    jQuery.fancybox({
        modal : true,
        content : "<div style=\"margin:1px;width:240px;\">"+msg+"<div style=\"text-align:right;margin-top:10px;\"><input id=\"fancyConfirm_cancel\" style=\"margin:3px;padding:0px;\" type=\"button\" value=\"Cancel\"><input id=\"fancyConfirm_ok\" style=\"margin:3px;padding:0px;\" type=\"button\" value=\"Ok\"></div></div>",
        onComplete : function() {
            jQuery("#fancyConfirm_cancel").click(function() {
                ret = false; 
                jQuery.fancybox.close();
            })
            jQuery("#fancyConfirm_ok").click(function() {
                ret = true; 
                jQuery.fancybox.close();
            })
        },
        onClosed : function() {
            callback.call(this,ret);
        }
    });
}
 
function fancyConfirm_text() {
    fancyConfirm("Ceci est un test", function(ret) {
        alert(ret)
    })
}