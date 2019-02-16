(function(jQuery) {
    jQuery.fn.umessages = function(options) {
        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            var global = matchedObject.data("global");
            global.bind("messages.update", function(data) {
                _update(data.messages);
            });
        };

        var _update = function(messages) {
            var _messages = jQuery(".messages", matchedObject);

            var items = _messages.children();
            items.remove();

            for (var index = 0; index < messages.length; index++) {
                var message = messages[index];

                var result = _messages.append("<div class=\"side\">" + "<h3>" + message.title + "</h3>" +
                    "<ul></ul>" + "</div>");
                _items = jQuery("> :last ul", result);

                for (var _index = 0; _index < message.items.length; _index++) {
                    var item = message.items[_index];
                    _items.append("<li>" + item.message + "</li>");
                }
            }

            matchedObject.trigger("sound", ["info"]);
        };

        initialize();
        return this;
    };
})(jQuery);
