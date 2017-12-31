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
         	$("label[for='id_description']:eq(0)").remove();
         	$(".desc:eq(0)").remove();
         	$('input[type=file]:eq(0)').remove();
         	$('#upload1').remove();

			$('#clockdiv').css('display','block');
				var date = new Date();
				var countDownDate = date.getTime() + (7 * 24 * 60 * 60 * 1000) - ((date.getHours()*60*60*1000)+(date.getMinutes()*60*1000)+(date.getSeconds()*1000));
				//alert(countDownDate);
				var nowt = new Date().getTime();
				var distance = countDownDate - nowt;
				var deadline = new Date(Date.parse(new Date()) + distance);
				initializeClock('clockdiv', deadline);
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


function upload1(event) {
event.preventDefault();
var data = new FormData($('#upload_form1').get(0));
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
         	$('#success_message1').html(data['message']);
         	$(".desc:eq(0)").remove();
         	$("label[for='id_description']:eq(0)").remove();
         	$('input[type=file]:eq(0)').remove();
         	$('#upload1').remove();
			$('#upload2').remove();
         }
     	 else
     	 $('#success_message').html("Error Uploading Image");
    }
});
return false;
}

$(function() {
    $('#upload_form1').submit(upload1);
});


			$('.imgupload').change(function () {
			     if (this.files && this.files[0]) {
			     	//alert("a");
			                var reader = new FileReader();

			                reader.onload = function (e) {
			                	if($('.imgupload:eq(1)').length>0)
			                		$('#img_id').attr('src', e.target.result);
			                	else
			                    $('#img_id1').attr('src', e.target.result);
			                }

			                reader.readAsDataURL(this.files[0]);
			            }
			});


function fileupload(event) {
event.preventDefault();
var data = new FormData($('#upload_files').get(0));

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
         	$('#success_files').html(data['message']);
         }
     	 else
     	 $('#success_files').html("Error Uploading Contact");
    }
});
return false;
}

$(function() {
    $('#upload_files').submit(fileupload);
});




$("label[for=id_document]").hide();

});