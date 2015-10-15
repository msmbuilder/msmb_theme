"use strict";

// get all of the releases from versions.json, and use these to populate the
// dropdown menu of different releases
$(document).ready(function () {
    // Define base_url in versions.html, probably through a template variable
    $.getJSON(versions_json_url)
        .done(function (data) {
            $.each(data.sort(function (a, b) {
                return a.version > b.version
            }), function (i, item) {
                // TODO: select default
                $("<dd>").append(
                    $("<a>").text(item.version).attr('href', item.url)
                ).appendTo("#versionselector");
            });
        })
        .fail(function (d, textStatus, error) {
            console.error("getJSON failed, status: " + textStatus + ", error: " + error);
        });
});

console.log("Loading versions from " + versions_json_url);
