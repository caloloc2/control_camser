$('#inicio').click(function(){
    $.ajax({
		url: 'php/camara.php',
		dataType: 'json',
		success: function(datos) {
            console.log(datos);
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

$('#arriba').click(function(){
    Movimientos(1); 
})

$('#abajo').click(function(){
    Movimientos(2); 
})

$('#izquierda').click(function(){
    Movimientos(3); 
})

$('#derecha').click(function(){
    Movimientos(4); 
})

function Movimientos(valor){
    $.ajax({
		url: 'php/movimientos.php',
        dataType: 'json',
        type: 'POST',
        data: {
            movimiento: valor
        },
		success: function(datos) {
            console.log(datos);
            setTimeout(function(){
                Encerar()
            }, 1000)
        },
        error: function(e){
            console.log(e.responseText);
        }
	});
}

function Encerar(){
    $.ajax({
		url: 'php/movimientos.php',
        dataType: 'json',
        type: 'POST',
        data: {
            movimiento: 0
        },
		success: function(datos) {
            console.log(datos);
        },
        error: function(e){
            console.log(e.responseText);
        }
	});
}