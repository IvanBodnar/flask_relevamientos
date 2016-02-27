
$(function() {
    var tags = [
        "uno",
        "dos",
        "tres",
        "tristes",
        "tigres"
    ];
    $( "#calle1" ).autocomplete({
        source: tags
    });
});