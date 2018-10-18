$('#inicio').click(function(){
    $.ajax({
		url: 'php/camara.php',
		dataType: 'json',
		success: function(datos) {
			console.log(datos);
		}
	});
})