(function(jQuery) {
    jQuery.fn.ulog = function(options) {
        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            var global = matchedObject.data("global");
            global.bind("log.message", function(data) {
                _new(data.contents);
            });
        };

        var _new = function(contents) {
            var date = new Date(contents.timestamp * 1000);
            var hours = date.getHours();
            var minutes = date.getMinutes();
            var timeLine = _toString(hours) + ":" + _toString(minutes);

            var context = jQuery(".context", matchedObject);
            var news = jQuery(".news", context);
            if (news.length === 0) {
                return;
            }

            var item = "<div class=\"news-item\">" + "<div class=\"title\">" + "<span class=\"time\">" +
                timeLine + "</span>" + "<span class=\"message\">" + contents.owner + "</span>" +
                "<span class=\"marker " + contents.type + "\"></span>" + "</div>" +
                "<div class=\"message\">" + contents.message + "</div>" + "</div>";
            news.prepend(item);

            var newsElement = news[0];

            matchedObject.trigger("message", [contents.type, contents.owner,
                contents.message
            ]);

            while (true) {
                var overflows = newsElement.scrollHeight > newsElement.clientHeight;
                if (!overflows) {
                    break;
                }

                var lastChild = jQuery("> :last-child", news);
                lastChild.remove();
            }
        };

        var _toString = function(value, length) {
            length = length || 2;
            value = String(value);

            for (var index = value.length; index < length; index++) {
                value = "0" + value;
            }
            return value;
        };

        initialize();
        return this;
    };
})(jQuery);
