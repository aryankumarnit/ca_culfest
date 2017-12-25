$(document).ready(function(){

$('#myform').submit(function(e){
    $.post('', $(this).serialize(), function(data){
    	//console.log(data);
       $('#success_div').html(data['message']);
       // of course you can do something more fancy with your respone
    });
    e.preventDefault();
});

function upload(event) {
event.preventDefault();
var data = new FormData($('#upload_form').get(0));

$.ajax({
    url: $(this).attr('action'),
    type: $(this).attr('method'),
    data: data,
    cache: false,
    processData: false,
    contentType: false,
    success: function(data) {
    	 if(data['result']=="success")
         {
         	$('#success_message').html(data['message']);
         	$('input[type=file]').val('');
         	 $('#img_id').attr('src', '');
         }
     	 else
     	 $('#success_message').html("Error Uploading Image");
    }
});
return false;
}

$(function() {
    $('#upload_form').submit(upload);
});

$('input[type=file]').change(function () {
     if (this.files && this.files[0]) {
     	//alert("a");
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#img_id').attr('src', e.target.result);
                }

                reader.readAsDataURL(this.files[0]);
            }
});


$("label[for=id_document]").hide();

});