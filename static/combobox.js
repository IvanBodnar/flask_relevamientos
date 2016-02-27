

var list = document.getElementById('calles').value;


console.log(JSON.parse(list))

$(function() {



    $( "#calle1" ).autocomplete({
        source: JSON.parse(list)
    });
});