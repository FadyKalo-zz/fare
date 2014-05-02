$(document).ready(function () {
    var rec_id;
    rec_id = $('#recipe').attr("data-recid");

    $('#like').click(function () {
        $.ajax({
            type: "GET",
            url: "like/" + rec_id+"/",
            data: {'test':'test'},
            dataType: "text",
            success: function (response) {
//                console.log(response);
                alert('You liked this');
            },
            error: function (rs, e) {
                alert(rs.responseText);
            },
            always: function (rs, e) {
                alert(rs.responseText);
            }
        });
    })
});