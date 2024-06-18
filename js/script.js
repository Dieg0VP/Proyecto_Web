$(document).ready(function(){
  $("#benviar").click(function(){
    var email = $("#email").val();
    var password = $("#password").val();

    if(email = ""){
      $("#mensaje1").fadeIn();
      return false;
    }else{
      $("#mensaje1").fadeOut();
      if(password = ""){
        $("#mensaje2").fadeIn();
        return false;
      }else{
        $("#mensaje1").fadeOut();
      }
    }
  });
});
