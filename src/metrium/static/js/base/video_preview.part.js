(function(jQuery) {
    jQuery.fn.uvideopreview = function(options) {
        var matchedObject = this;
        var url = jQuery(".text-field[name=url]", matchedObject);
        var previewPanel = jQuery(".preview-panel", matchedObject);

        previewPanel.hide();

        url.bind("value_change", function() {
            var element = jQuery(this);
            var videoPreview = element.parents(".video-preview");
            var previewPanel = jQuery(".preview-panel", videoPreview);
            var videoTarget = jQuery(".video-target", previewPanel);
            var value = element.uxvalue();
            if (value) {
                previewPanel.show();
                videoTarget.html(value);
                videoTarget.uxvideo();
            } else {
                previewPanel.hide();
            }
        });

        return this;
    };
})(jQuery);
