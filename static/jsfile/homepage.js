



//-----------------------------------------------------------------------------

function vehi()
{
  var user= $('#user').val();

     $.ajax({
    url: '/app/vehicleValue/',
    type: 'GET',
    dataType: 'json',
   data:{'user':user},

  })
  .done(function(data) {
console.log(data);
var stkj="";
var no_of_train = Object.keys(data).length;
var i=0
var strk=""
for( i=0;i< no_of_train;i++)
{
 if( data[i]['status'])
     {
 var html = '<div class="card vehicle" style="background-image:linear-gradient(to right,#7CFC00, #32CD32 );"  onclick=moveTo('+ data[i]['number']+')  ><p style="font-weight: bold; " >'+data[i]['number']+'</p><img style="margin-left: auto; margin-right: auto; display: block;"src="../static/img/cars1.jpg"  class="carImg center"><p>'+data[i]['address']+'</p><p>'+data[i]['update']+'</p></div>'; 
   
     }
    else{
        var html = '<div class="card vehicle"  style="background-image:linear-gradient(to right,#DC143C, #FF0000 );" onclick=moveTo('+ data[i]['number']+')   ><p style="font-weight: bold; " >'+data[i]['number']+'</p><img style="margin-left: auto; margin-right: auto; display: block;"src="../static/img/cars1.jpg"  class="carImg center"><p>'+data[i]['address']+'</p><p>'+data[i]['update']+'</p></div>'; 
    }



 stkj=stkj+html
             
   
}
    $('#vehicleadd').html(stkj);     
         



              
     

  })
  .fail(function() {
    console.log("error");
  })
  .always(function() {
    console.log("complete");
  });
}


setInterval(vehi,5000);

//----------------------------------------------------------------------------------------------------

function moveTo(k)
{
       $.ajax({
    url: '/VehicleShow/',
    type: 'GET',
    dataType: 'json',
   data:{'car':k},
           

  })
  .done(function(data) {
console.log(data);
        
            window.open('/carView/', '_blank');

  })
  .fail(function() {
    console.log("error");
  })
  .always(function() {
    console.log("complete");
  });
    
}




