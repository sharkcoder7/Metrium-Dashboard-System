(function(jQuery) {
    jQuery.fn.udashboard = function(options) {
        var MESSAGE_TIMEOUT = 15000;
        var BOARD_TIMEOUT = 30000;
        var LINE_HEIGHT = 49;

        var matchedObject = this;
        var pusher = jQuery(".pusher", matchedObject);
        var status = jQuery(".status", matchedObject);
        var _window = jQuery(window);

        pusher = pusher.data("pusher");
        if (!pusher) {
            return this;
        }

        var initialize = function() {
            _start();
            _layout();
            _boards();
            _general();
            _modules();

        };

        var _start = function() {
            var connection = pusher.connection;
            var global = pusher.subscribe("global");
            matchedObject.data("global", global);
            var video = jQuery(".video", matchedObject);
            var sections = jQuery("ul.sections > li", matchedObject);

            matchedObject.bind("message",
                function(event, type, owner, message) {
                    _showMessage(type, owner, message);
                    _playSound("/static/sounds/" + type + ".mp3");
                });

            matchedObject.bind("sound",
                function(event, type, owner) {
                    _playSound("/static/sounds/" + type + ".mp3");
                });

            _window.keydown(function(event) {
                var keyValue = event.keyCode ? event.keyCode : event.charCode ? event.charCode :
                    event.which;

                switch (keyValue) {
                    case 37:
                        _previous();
                        break;

                    case 39:
                        _next();
                        break;
                }
            });

            connection.bind("connecting", function() {});

            connection.bind("connected", function() {
                _hideError();
            });

            connection.bind("unavailable", function() {
                _showError();
            });

            connection.bind("disconnected", function() {
                _showError();
            });

            connection.bind("error", function(error) {
                _showError();
            });

            global.bind("video.open", function(data) {
                var url = data.url;
                url && _showVideo(url);
            });

            video.bind("ended", function() {
                var element = jQuery(this);
                var overlay = jQuery(".overlay:first");

                overlay.triggerHandler("hide", [250]);
                element.fadeOut(250);
            });

            sections.click(function() {
                var element = jQuery(this);
                var index = element.index();
                _showBoard(index);
            });
        };

        var _layout = function() {
            var _html = jQuery("html");
            _html.css("overflow-y", "auto");
        };

        var _general = function() {
            jQuery.ajax({
                url: "/state",
                beforeSend: function() {
                    _hide();
                },
                success: function(data) {
                    _onState(data);
                    _show();
                },
                error: function() {
                    _show();
                }
            });
        };

        var _boards = function() {
            var boards = jQuery(".boards > .board", matchedObject);
            boards.hide();

            var first = jQuery(boards[0]);
            first.show();

            matchedObject.data("index", 0);
            if (boards.length <= 1) {
                return;
            }

            setInterval(function() {
                _next();
            }, BOARD_TIMEOUT);
        };

        var _next = function() {
            var boards = jQuery(".boards > .board", matchedObject);
            var index = matchedObject.data("index");
            index = index + 1 >= boards.length ? 0 : index + 1;
            _showBoard(index);
        };

        var _previous = function() {
            var boards = jQuery(".boards > .board", matchedObject);
            var index = matchedObject.data("index");
            index = index - 1 >= 0 ? index - 1 : boards.length - 1;
            _showBoard(index);
        };

        var _hide = function() {
            matchedObject.css("visibility", "hidden");
        };

        var _show = function() {
            matchedObject.css("visibility", "visible");
        };

        var _onState = function(state) {
            var global = matchedObject.data("global");
            for (var module in state) {
                var events = state[module];

                for (var name in events) {
                    var event = events[name];
                    for (var index = event.length - 1; index >= 0; index--) {
                        var _event = event[index];
                        global.emit(name, _event);
                    }
                }
            }
        };

        var _modules = function() {
            matchedObject.udate();
            matchedObject.ulog();
            matchedObject.uglobalsales();
            matchedObject.umessages();
            matchedObject.upending();
            matchedObject.uglobalcommits();
        };

        var _showBoard = function(index) {
            var boards = jQuery(".boards > .board:visible", matchedObject);
            var sections = jQuery("ul.sections > li.active", matchedObject);

            boards.fadeOut(350, function() {
                var board = jQuery(".boards > .board:nth-child(" + (index + 1) + ")", matchedObject);
                var section = jQuery("ul.sections > li:nth-child(" + (index + 1) + ")",
                    matchedObject);

                sections.removeClass("active");
                section.addClass("active");
                board.fadeIn(350);

                matchedObject.data("index", index);
            });
        };

        var _showVideo = function(link) {
            var isVisible = matchedObject.css("visibility") === "visible";
            if (!isVisible) {
                return;
            }

            var overlay = jQuery(".overlay:first");
            var video = jQuery(".video", matchedObject);

            video.html(link);
            video.uxvideo();

            overlay.triggerHandler("show", [350]);
            video.fadeIn(350);
            video.uxcenter(0, 0, false, false, false, true);
        };

        var _showMessage = function(type, author, contents) {
            var isVisible = matchedObject.css("visibility") === "visible";
            if (!isVisible) {
                return;
            }

            var timeoutP = matchedObject.data("timeout");
            var intervalP = matchedObject.data("interval");
            if (timeoutP) {
                clearTimeout(timeoutP);
            }
            if (intervalP) {
                clearInterval(intervalP);
            }

            var _message = jQuery("> .message", matchedObject);
            var _author = jQuery("> .author", _message);
            var _contents = jQuery("> .contents", _message);

            _message.show();
            _message.scrollTop(0);
            _message.hide();

            _author.html(author);
            _contents.html(contents);

            _message.removeClass("info");
            _message.removeClass("success");
            _message.removeClass("warning");
            _message.removeClass("error");

            _message.addClass(type);
            _message.fadeIn(200);

            var paddingVertical = _message.outerHeight() - _message.height();
            var lines = ((_message[0].scrollHeight - paddingVertical) / LINE_HEIGHT);
            var timing = MESSAGE_TIMEOUT / lines;

            var interval = setInterval(function() {
                _message.animate({
                    scrollTop: "+=" + LINE_HEIGHT + "px"
                }, 300);
            }, timing);

            var timeout = setTimeout(function() {
                clearInterval(interval);
                _message.fadeOut(150);
            }, MESSAGE_TIMEOUT);

            matchedObject.data("timeout", timeout);
            matchedObject.data("interval", interval);
        };

        var _playSound = function(path) {
            var isVisible = matchedObject.css("visibility") === "visible";
            if (!isVisible) {
                return;
            }

            var sound = jQuery(".sound", matchedObject);
            var soundElement = sound[0];
            sound.attr("src", path);
            soundElement.play();
        };

        var _showError = function() {
            var overlay = jQuery(".overlay:first");
            var errorPanel = jQuery(".error-panel");
            overlay.triggerHandler("show", [350]);
            errorPanel.fadeIn(350);
            errorPanel.uxcenter(0, 0, false, false, false, true);
        };

        var _hideError = function() {
            var overlay = jQuery(".overlay:first");
            var errorPanel = jQuery(".error-panel");
            overlay.triggerHandler("hide", [200]);
            errorPanel.fadeOut(200);
        };

        initialize();
        return this;
    };
})(jQuery);

(function(jQuery) {
    jQuery.fn.udate = function(options) {

        var TIMEOUT = 10000;

        var DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Starturday"
        ];

        var DAYS_PT = ["Domingo", "Segunda-feira", "Terça-Feira",
            "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"
        ];

        var MONTHS = ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November",
            "December"
        ];

        var MONTHS_PT = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio",
            "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro",
            "Dezembro"
        ];

        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            _update();
            setInterval(function() {
                _update();
            }, TIMEOUT);
        };

        var _update = function() {
            var date = jQuery(".date", matchedObject);
            var weekDay = jQuery(".week-day", date);
            var day = jQuery(".day", date);
            var time = jQuery(".time", date);

            var _date = new Date();
            var dayIndex = _date.getDay();
            var dayString = DAYS_PT[dayIndex];

            var dayMonth = _date.getDate();
            var dayMonthS = _toString(dayMonth);
            var month = _date.getMonth();
            var monthS = MONTHS_PT[month];
            var dayLine = dayMonthS + " " + monthS;

            var hours = _date.getHours();
            var minutes = _date.getMinutes();
            var timeLine = _toString(hours) + ":" + _toString(minutes);

            weekDay.html(dayString);
            day.html(dayLine);
            time.html(timeLine);
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
