jQuery(document).ready(function() {
    var _body = jQuery("body");
    _body.bind("applied", function(event, base) {
        base.uapply();
    });
});
