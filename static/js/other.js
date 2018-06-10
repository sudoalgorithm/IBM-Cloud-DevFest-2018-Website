$(document).ready(function() {  
	$('#other').hide();  
	$('#language').change(function(){   
	if($('#language').val() === 'Other')   
	   {   
	   $('#other').show();    
	   }   
	else 
	   {   
	   $('#other').hide();      
	   }   
	});   
});   