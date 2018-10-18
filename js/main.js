$('#inicio').click(function(){
    $.ajax({
		url: 'php/camara.php',
		dataType: 'json',
		success: function(datos) {
			if (datos['estado']){
                if (datos['nuevo_estado']=='0'){
                    $('#inicio').html("Iniciar C&aacute;mara");
                }else{
                    $('#inicio').html("Detener C&aacute;mara");
                }
            }else{
                allert('No se pudo tener acceso a la camara.');
            }
        },
        error: function(e){
            console.log(e.responseText);
        }
	});
})