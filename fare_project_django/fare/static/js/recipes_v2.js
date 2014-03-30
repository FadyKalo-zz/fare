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
    var carousel = $("#carousel-" + type).find('.carousel-inner');
    console.log(content);
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
                $('<div>',{class:"col-xs-6"}).append(
                    $('<div>',{class:"rating"}).append(

                    )
                )
            ).append($('<div>',{class:"col-xs-6"}).append( $('<div>',{class:"btn-group btn-group-xs pull-right"}
                ).append(
                    $('<a>',{class:"btn btn-primary",href :'#' }).append(
                        $('<span>',{class:'fui-time'}))
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
//        $('<li>').attr('data-slide-to',i).attr('data-target', '#carousel-' + type).appendTo(listIndicators);
        ++i;
    });
}

$(document).ready(function () {
    $('div.carousel').each(function(index, element){
        var type = $(element).attr('data-meal-type');
        get_content(type);
     }).carousel({interval:false});


//    $('#quote-carousel').carousel({interval:false});
});
//
//
//<div class="item active">
//                    <div class="row pad-top-20">
//                        <div class="col-xs-4 text-center recipe_pix">
//                            <img class="img-circle" src="http://wp-desk.com/lovinflat/images/persons/person_1.png">
//                        </div>
//                        <div class="col-xs-8 item-info">
//                            <p>Recipe Name</p>
//                            <span class="label label-warning">Soups</span>
//                            <span class="label label-warning">Main Dishes</span>
//                            <span class="label label-warning">Italian</span>
//                        </div>
//                    </div>
//                    <div class="row">
//                        <div class="col-xs-6">
//                            <div class="rating">
//                                <span class="glyphicon glyphicon-star-empty"></span>
//                                <span class="glyphicon glyphicon-star-empty"></span>
//                                <span class="glyphicon glyphicon-star-empty"></span>
//                                <span class="glyphicon glyphicon-star-empty"></span>
//                                <span class="glyphicon glyphicon-star-empty"></span>
//                            </div>
//                        </div>
//                        <div class="col-xs-6">
//                            <div class="btn-group btn-group-xs pull-right">
//                                <a class="btn btn-primary" href="#"><span class="fui-time"></span></a>
//                                <a class="btn btn-primary" href="#"><span class="fui-check"></span></a>
//                                <a class="btn btn-primary" href="#"><span class="fui-heart"></span></a>
//                                <a class="btn btn-primary" href="#"><span class="fui-eye"></span></a>
//                            </div>
//                        </div>
//                    </div>
//                </div>