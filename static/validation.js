
// On #altura.focus turn off altura if #calle2 has some value

$('#altura').focus(function() {

   if( $('#calle2').val() ) {
        $('#altura').val('');
        $('#altura').prop('readonly', true);
   }
   else{
        $('#altura').prop('readonly', false);
   }


});