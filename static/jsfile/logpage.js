function login()
{
var user=$('#unam').val();
var pass=$('#pass').val();
$.ajax({
    url: 'login/',
    type: 'GET',
    dataType: 'json',
   data:{'username':user,
          'password':pass,
         },

  })
  .done(function(data) {
  if(data['status']=="success")
  {
  window.location.href = "home/";
  }
    else
  {
 $('#mss').text(data['status']);
  }
  })
  .fail(function() {
    console.log("error");
  })
  .always(function() {
    console.log("complete");
  });


       
    
    
}