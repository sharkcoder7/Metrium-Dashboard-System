(function(jQuery) {
    jQuery.fn.uapply = function(options) {
        // sets the jquery matched object
        var matchedObject = this;

        var pusher = jQuery(".pusher", matchedObject);
        pusher.upusher();

        var dashboard = jQuery(".dashboard", matchedObject);
        dashboard.udashboard();

        var progress = jQuery(".progress", matchedObject);
        progress.uprogress();

        var lineChart = jQuery(".line-chart", matchedObject);
        lineChart.ulinechart();

        var videoPreview = jQuery(".video-preview", matchedObject);
        videoPreview.uvideopreview();
    };
})(jQuery);
