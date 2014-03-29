function get_content(type) {
    $.get('/dietapp/recipe/' + type, function () {
    }).done(function (data) {
            load_carousel(data, type);
        })
        .fail(function () {
            console.log("error");
        })
        .always(function () {
//            console.log("finished");
        });
}

function load_carousel(content, type) {
    var carousel = $("#carousel-" + type).find('.carousel-inner'); console.log(carousel);
    var listIndicators = $("#carousel-" + type + " ol.carousel-indicators");
    var i = 1;
    $.each(content, function (k, v) {
        $('<div>', {class: 'item'})
        .append(
            $('<img/>', {class: 'img-responsive', src: v[0]})
        )
        .append(
            $('<div>', {class: 'carousel-caption img-overlay-label'})
                .append($('<span>', {class: 'text'}).html(k))
        ).appendTo(carousel);
        $('<li>').attr('data-slide-to',i).attr('data-target', '#carousel-' + type).appendTo(listIndicators);
        ++i;
    });
}

$(document).ready(function () {
    $('div.carousel').each(function(index, element){
        var type = $(element).attr('data-meal-type');
        get_content(type);
     }).carousel({interval:false});
});