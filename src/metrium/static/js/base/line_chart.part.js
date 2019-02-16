(function(jQuery) {
    jQuery.fn.ulinechart = function(options) {
        var PADDING_TOP = 32;
        var PADDING_LEFT = 5;
        var PADDING_RIGHT = 5;

        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            if (matchedObject.length === 0) {
                return;
            }

            var index = 0;
            var value = null;

            var width = matchedObject.width();
            var height = matchedObject.height();

            width && matchedObject.attr("width", width);
            height && matchedObject.attr("height", height);

            var widthS = matchedObject.attr("width");
            var heightS = matchedObject.attr("height");

            width = parseInt(widthS);
            height = parseInt(heightS);

            var values = matchedObject.attr("data-values") || "";
            values = values.split(",");

            for (index = 0; index < values.length; index++) {
                value = values[index];
                values[index] = parseFloat(value);
            }

            var maxValue = 0;

            for (index = 0; index < values.length; index++) {
                value = values[index];
                maxValue = value > maxValue ? value : maxValue;
            }

            var _draw = function(canvas) {
                var context = canvas.getContext("2d");
                context.setTransform(1, 0, 0, 1, 0, 0);
                context.clearRect(0, 0, width, height);

                var widthChart = width - PADDING_LEFT - PADDING_RIGHT;
                var heightChart = height - PADDING_TOP;
                var stepWidth = widthChart / (values.length - 1);
                var xPosition = PADDING_LEFT;

                for (var index = 0; index < values.length; index++) {
                    var value = values[index];
                    var yPosition = height - (value * heightChart / maxValue);

                    if (index !== 0) {
                        context.beginPath();
                        context.strokeStyle = "#ffffff";
                        context.moveTo(xPositionP, yPositionP);
                        context.lineTo(xPosition, yPosition);
                        context.lineWidth = 4;
                        context.stroke();

                        context.beginPath();
                        context.fillStyle = "rgba(255, 255, 255, 0.2)";
                        context.moveTo(xPositionP, yPositionP);
                        context.lineTo(xPosition, yPosition);
                        context.lineTo(xPosition, height);
                        context.lineTo(xPositionP, height);
                        context.closePath();
                        context.fill();
                    }

                    if (index !== 0 && index !== values.length - 1) {
                        context.beginPath();
                        context.strokeStyle = "rgba(255, 255, 255, 0.3)";
                        context.lineWidth = 2;
                        context.dashedLine(xPosition, yPosition, xPosition,
                            height, [6, 4]);
                        context.stroke();
                    }

                    context.beginPath();
                    context.fillStyle = "#ffffff";
                    context.arc(xPosition, yPosition, 5, 0, 2 * Math.PI, false);
                    context.fill();

                    var xPositionP = xPosition;
                    var yPositionP = yPosition;

                    xPosition += stepWidth;
                }
            };

            matchedObject.each(function(index, element) {
                var _element = jQuery(this);
                var canvas = _element[0];
                _draw(canvas);
            });
        };

        initialize();
        return this;
    };
})(jQuery);
