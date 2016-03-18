



$(function() {
    $('#geo_google').click(function() {

        $('#Precision').val('0.0');
        $.ajax({
            url: $('#geo-gm').val(),
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                response = JSON.parse(response)
                $('#Lat').val(response['lat']);
                $('#Long').val(response['lng']);
                //console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});