(function(jQuery) {
    jQuery.fn.upusher = function(options) {
        var matchedObject = this;
        matchedObject.each(function() {
            var element = jQuery(this);
            var key = element.attr("data-key");
            var cluster = element.attr("data-cluster");
            if (!key) {
                return;
            }

            var pusher = new Pusher(key, {
                cluster: cluster || null
            });
            element.data("pusher", pusher);
        });
        return this;
    };
})(jQuery);
