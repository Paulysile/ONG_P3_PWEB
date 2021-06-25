fn_ocultarEtiquetas();



function fn_ocultarEtiquetas() {

    $('#lbl_nombre').hide();
    $('#lbl_contrasena').hide();
    $('#lbl_correcto').hide();
    $('#lbl_nombrecorto').hide();
    $('#lbl_espacio').hide();
    $('#lbl_contrasena_numero').hide();

}

function fn_nombreVacio() {

    var nombre = $('#txt_nombre').val();
    var validadorNombre = false;

    if (nombre == "") {

        $('#lbl_nombre').show();

        $('#txt_nombre').addClass('is-invalid');

        validadorNombre = false;

    }
    else if (nombre.length < 8) {
        $('#lbl_nombrecorto').show();
        $('#lbl_nombre').hide();
        $('#lbl_espacio').hide();
        $('#txt_nombre').addClass('is-invalid');
        validadorNombre = false;
    }
    else if (nombre.indexOf(' ') >= 0) {

        $('#lbl_espacio').show();
        $('#lbl_nombre').hide();
        $('#lbl_nombrecorto').hide();
        $('#txt_nombre').addClass('is-invalid');
        validadorNombre = false;
    }
    else {

        $('#lbl_nombre').hide();
        $('#lbl_nombrecorto').hide();
        $('#lbl_espacio').hide();

        $('#txt_nombre').removeClass('is-invalid');

        $('#txt_nombre').addClass('is-valid');
        validadorNombre = true;

    }
    function fn_contrasena() {
        var contrasena = $('#txt_contrasena').val();
        var numero = /(.*\d){2}/g;
        var letra = /(.*[a-zA-Z]){2}/g;
        validadorContrasena = false;

        if (contrasena.match(numero) && contrasena.match(letra)) {
            console.log('ENTRE AL IF')
            $('#lbl_contrasena_numero').hide();
            $('#txt_contrasena').removeClass('is-invalid');
            $('#txt_contrasena').addClass('is-valid');
            validadorContrasena = true
        }
        else {
            console.log('ENTRE AL ELSE')
            $('#lbl_contrasena_numero').show();
            $('#txt_contrasena').addClass('is-invalid');
            validadorContrasena = false;
        }
        console.log(validadorNombre, validadorContrasena)
    } fn_contrasena();

    function fn_loginCorrecto() {

        if (validadorNombre == true && validadorContrasena == true) {
            window.location.href = "/login-exitoso"
        }
    } fn_loginCorrecto();
}

