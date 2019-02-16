(function(jQuery) {
    jQuery.fn.uglobalcommits = function(options) {
        var matchedObject = this;

        var initialize = function() {
            _start();
        };

        var _start = function() {
            var global = matchedObject.data("global");
            global.bind("github.commits_total", function(data) {
                _updateCommitsTotal(data.commits_total);
            });
            global.bind("github.commits_data", function(data) {
                _updateCommitsData(data.commits_data);
            });
            global.bind("github.issues_users", function(data) {
                _updateIssuesUsers(data.issues_users);
            });
            global.bind("github.commits_users", function(data) {
                _updateCommitsUsers(data.commits_users);
            });
        };

        var _updateCommitsTotal = function(commitsTotal) {
            var _commitsTotal = jQuery(".commits-total", matchedObject);
            var value = jQuery(".value", _commitsTotal);
            var subValue = jQuery(".sub-value", _commitsTotal);
            var progress = jQuery(".progress", _commitsTotal);

            var previous = commitsTotal[0];
            var current = commitsTotal[1];
            var ratio = current / previous;
            ratio = ratio > 1.0 ? 1.0 : ratio;
            ratio *= 100;
            ratio = Math.floor(ratio);
            var ratioS = String(ratio);

            value.text(current);
            subValue.text(previous);

            progress.attr("data-value", ratioS);
            progress.uprogress();
        };

        var _updateCommitsData = function(commitsData) {
            var _commitsData = jQuery(".commits-data", matchedObject);
            var lineChart = jQuery(".line-chart", _commitsData);
            var commitsDataS = String(commitsData);

            lineChart.attr("data-values", commitsDataS);
            lineChart.ulinechart();
        };

        var _updateIssuesUsers = function(issuesUsers) {
            var _issuesUsers = jQuery(".issues-users", matchedObject);
            var tableBody = jQuery("table > tbody", _issuesUsers);
            tableBody.empty();

            var size = issuesUsers.length > 5 ? 5 : issuesUsers.length;

            for (var index = 0; index < size; index++) {
                var item = issuesUsers[index];
                var open = item[0];
                var closed = item[1];
                var name = item[2];
                var row = jQuery("<tr>" + "<td>" + name + "</td>" + "<td class=\"value\">" + closed +
                    "</td>" + "<td class=\"value\">" + open + "</td>" + "</tr>");
                tableBody.append(row);
            }
        };

        var _updateCommitsUsers = function(commitsUsers) {
            var _commitsUsers = jQuery(".commits-users", matchedObject);
            var tableBody = jQuery("table > tbody", _commitsUsers);
            tableBody.empty();

            var size = commitsUsers.length > 5 ? 5 : commitsUsers.length;

            for (var index = 0; index < size; index++) {
                var item = commitsUsers[index];
                var lines = item[0];
                var commits = item[1];
                var name = item[2];
                var row = jQuery("<tr>" + "<td>" + name + "</td>" + "<td class=\"value\">" + lines +
                    "</td>" + "<td class=\"value\">" + commits + "</td>" + "</tr>");
                tableBody.append(row);
            }
        };

        initialize();
        return this;
    };
})(jQuery);
