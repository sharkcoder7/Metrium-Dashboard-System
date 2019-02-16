(function(jQuery) {
    jQuery.fn.upending = function(options) {
        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            var global = matchedObject.data("global");
            global.bind("pending.update", function(data) {
                _update(data.pendings);
            });
        };

        var _update = function(pendings) {
            var _pending = jQuery(".pending", matchedObject);

            var items = _pending.children();
            items.remove();

            for (var index = 0; index < pendings.length; index++) {
                var item = pendings[index];
                _pending.append("<li class=\"" + item.severity + "\">" + "<span class=\"pre\">" + item.pre +
                    "</span>" + "<span class=\"description\">" + item.description + "</span>" +
                    "<span class=\"author\">" + item.author + "</span>" +
                    "<span class=\"marker\"></div>" + "</li>");
            }
        };

        initialize();
        return this;
    };
})(jQuery);
