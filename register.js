$(document).ready(function(){
    $('#register-user').click(function(){
        // Regular Expression for Name and Email checking.
        var regexname = /^[a-zA-Z].*[\s\.]*$/g;
        var regexemail = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;

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

        var mobilenumber = $('#mobile-number').val();
        var mobno = mobilenumber.replace(/[^\d]/g, '');
        var a = (mobno.length >=7 && mobno.length <=17);

        var disclaimer = $('#disclaimer').val();

        if (fullname.length > 0 && emailaddress.length > 0){
            if (regexname.test(fullname) === false){
                alert("Please enter a valid Name");
            }
            else if (regexemail.test(emailaddress) === false){
                alert("Please enter a valid Email Address");
            }
            else if (trackArray.length === 0 || trackArray.length === 1 && trackArray.includes("on")){
                alert("Please select atleast 1 developer track of interest");
            }
            else if (language === "Select"){
                alert("Kindly select your programming language of preference");
            }
            else if (!(mobno.length >=7 && mobno.length <=17)){
                 alert("Please enter a valid mobile number or leave the text field empty");
            }
            else if ($('#disclaimer:checkbox:checked').length === 0){
                alert("You need to agree to receiving event related updates to register");
            }
            else{
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
                        mobilenumber: mobilenumber,
                        disclaimer: disclaimer
                    }),
                    success: function() {
                        window.location.href = "/registration";
                    },
                    error: function(error) {
                        console.log(error);
                    }
               })
            }
        }else{
            alert("Please Enter All Required Information");
        }
    });
});
