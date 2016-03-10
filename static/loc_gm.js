
$(function() {
    $('#geo_google').click(function() {
        var lat = $('#lat').val();
        var long = $('#long').val();
        var altura = $('#altura').val();
        $.ajax({
            url: '/geo_gm',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                response = JSON.parse(response)
                $('#Lat').val(response[0]);
                $('#Long').val(response[1]);
                //console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});