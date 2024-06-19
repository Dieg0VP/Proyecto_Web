function validarFormulario(){
    $('.alert').remove();
    

    var nombre=$('#nombre').val(),
        email=$('#email').val(),
        asunto=$('#asunto').val(),
        mensaje=$('#mensaje').val();

    //nombre
    if(nombre=="" ||nombre==null){
        cambiarColor("nombre");
        mostrarAlerta("campo obligatorio");
        return false;
    }else{
        var expresion =/^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(nombre)){
            cambiarColor("nombre");
            mostrarAlerta("No se permiten caracteres especiales o numeros")
            return false;
        }
    }

    //email
    if(email=="" ||email==null){
        cambiarColor("email");
        mostrarAlerta("campo obligatorio");
        return false;
    }else{
        var expresion =/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        if(!expresion.test(email)){
            cambiarColor("correo");
            mostrarAlerta("Por favor ingresar un correo válido")
            return false;
        }
    }


    //asunto
    if(asunto=="" ||asunto==null){
        cambiarColor("asunto");
        mostrarAlerta("campo obligatorio");
        return false;
    }else{
        var expresion =/^[,\\.\\a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(asunto)){
            cambiarColor("asunto");
            mostrarAlerta("No se permiten caracteres especiales")
        }
    }

    //mensaje
    if(mensaje=="" ||mensaje==null){
        cambiarColor("mensaje");
        mostrarAlerta("campo obligatorio");
        return false;
    }else{
        var expresion = /^[,\\.\\a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(mensaje)){
            cambiarColor("mensaje");
            mostrarAlerta("No se permiten caracteres especiales")
        }
    }
    $('form').submit();
    return true;
}

$('input').focus(function(){
    $('.alert').remove();
    colorDefault('nombre');
    colorDefault('email');
    colorDefault('asunto');
});

$('textarea').focus(function(){
    $('.alert').remove();
    colorDefault('mensaje');
});

function colorDefault(dato){
    $('#' + dato).css({
        border: "1px solid #999"
    });
}

function cambiarColor(dato){
    $('#' + dato).css({
        border: "1px solid #dd5144"
    });
}

function mostrarAlerta(texto){
    $('#nombre').before('<div class="alert">Error: '+ texto + '</div>');
}
