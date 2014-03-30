function get_content(type, diet) {
    $.get('/dietapp/recipe/' + type+"?diet="+diet, function () {
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
    var carousel = $("#carousel-" + type).find('.carousel-inner');
//    var listIndicators = $("#carousel-" + type + " ol.carousel-indicators");
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
        .append( $('<div>',{class:"row"}).append(
                $('<div>',{class:"col-xs-5"}).append(
                    $('<div>',{class:"rating"}).append(

                    )
                )
            ).append($('<div>',{class:"col-xs-7"}).append( $('<div>',{class:"btn-group btn-group-xs pull-right"}
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
                    $('<a>',{class:"btn btn-primary",href :'#' }).append(
                        $('<span>',{class:'fui-eye'}))
                )

                )
            )
        ).appendTo(carousel);

        var rating = carousel.find('.item').last().find('.rating'); console.log(rating);
        for(j=1;j<6;j++){
            var rank = $('<span>', {class: 'glyphicon'});
            if (j <= v[3]) {
                $(rating).append(rank.addClass('glyphicon-star'));
            } else {
                $(rating).append(rank.addClass('glyphicon-star-empty'));
            }
        }
        var arr = v[4].cuisine;
        if(typeof arr != 'undefined'){
            var info = carousel.find('.item').last().find('.item-info'); console.log(info);
            for(j=0;j<arr.length;j++){
                var label = $('<span>', {class: 'label'});
                    $(info).append(label.html(arr[j]));
            }
        }

        ++i;
    });
}

$(document).ready(function () {
    $('div.carousel').each(function(index, element){
        var type = $(element).attr('data-meal-type');
        var diet = $(element).attr('data-diet');
        get_content(type, diet);
     }).carousel({interval:false});


//    $('#quote-carousel').carousel({interval:false});
});