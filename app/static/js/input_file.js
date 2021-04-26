$(function() {
   var input__file = $('#input__file')[0]

   input__file.onchange = function() {

        if (this.files[0]) {

           $('label.file__label')[0].innerHTML = this.files[0].name;

       }

   }
})