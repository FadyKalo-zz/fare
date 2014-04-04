function get_content(type, diet) {
    $.get('/dietapp/recipe/' + type+"?diet="+diet, function () {
    }).done(function (data) {
            load_carousel(data, type);
    })
    .fail(function () {
        console.log("error");
    });
}

function load_carousel(content, type) {
    var carousel = $("#carousel-" + type).find('.carousel-inner');
    var i = 1;
    $.each(content, function (k, v) {
        $('<div>', {class: 'item'})
        .append(
                $('<div>',{class:'row pad-top-20'}).append(
                    $('<div>',{class:"col-xs-4 text-center recipe_pix"}).append(
                        $('<img/>', {class: 'img-circle', src: v[0][0]})
                    )
                ).append(
                        $('<div>',{class:"col-xs-8 item-info"}).append($('<div>', {}).html(k))

                    )
        )
        .append($('<div>',{class:"row"}).append(
            $('<div>',{class:"col-xs-3 col-xs-offset-1"}).append(
                $('<div>',{class:"rating"})
            )
            ).append($('<div>',{class:"col-xs-7"}).append( $('<div>',{class:"btn-group btn-group-sm"}
                ).append(
                    $('<a>',{class:"btn btn-primary",href :'#' }).append(
                        $('<span>',{class:'fui-time'}).html(' '+v[2]/60 + 'min'))
                ).append(
                    $('<a>',{class:"btn btn-primary",href :'#' }).append(
                        $('<span>',{class:'fui-check'}))
                ).append(
                    $('<a>',{class:"btn btn-primary",href :'#' }).append(
                        $('<span>',{class:'fui-heart'}))
                ).append(
                    $('<a>',{class:"btn btn-primary",href :'../recipe/?recipe_id='+v[1] }).append(
                        $('<span>',{class:'fui-eye'}))
                )

                )
            )
        ).appendTo(carousel);

        var rating = carousel.find('.item').last().find('.rating');
        var rank = $('<span>', {class: 'glyphicon'});
        $(rating).append($('<span>', {class: "pull-right"}).html('x ' + Math.round(v[3]))).append(rank.addClass('glyphicon-star'));
        ++i;
    });
}

$(document).ready(function () {
    $('div.carousel').each(function(index, element){
        var type = $(element).attr('data-meal-type');
        var diet = $(element).attr('data-diet');
        get_content(type, diet);
     }).carousel({interval:false});
});