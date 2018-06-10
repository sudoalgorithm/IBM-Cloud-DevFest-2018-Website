$(document).ready(function(){
    $('#register-user').click(function(){
        var fullname = $('#full-name').val();
        var emailaddress = $("#email-address").val();
        var trackArray = [];
        $(':checkbox:checked').each(function(i){
            trackArray[i] = $(this).val();
        });
        var language = $('#language :selected').text();
        if (language === "Other"){
            language = $('#other').val(); 
        }
        var disclaimer = $('#disclaimer').val();
                if (fullname.length > 0 && emailaddress.length > 0){
            if (trackArray.length == 0){
                alert("Please select atleast 1 developer track of interest");
            }

            if (language === "Select"){
                alert("Kindly select your programming language of preference");
            }

            if ($('#disclaimer:checkbox:checked').length == 0){
                alert("You need to agree to receiving event related updates to register");
            }
            $.ajax({
                method: "POST",
                url: "/api/register",
                contentType: "application/json",
                cache: false,
                data: JSON.stringify({
                    fullname: fullname,
                    emailaddress: emailaddress,
                    trackArray: trackArray,
                    language: language,
                    disclaimer: disclaimer
                }),
                success: function() {
                    window.location.href = "/registration";
                },
                error: function(error) {
                    console.log(error);
                }

            })
        }else{
            alert("Please Enter All Required Information");
        }
    });
});
