

var list = $('#calles').val();

//console.log(JSON.parse(list))

$(function() {
    $( "#calle1" ).autocomplete({
        source: JSON.parse(list),
        minLength: 3
    });
});

$(function() {
    $( "#calle2" ).autocomplete({
        source: JSON.parse(list),
        minLength: 3
    });
});





