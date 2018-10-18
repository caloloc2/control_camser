<?php

$respuesta['estado'] = false;

try{
    $ruta = '../movimientos.txt';
    $movimiento = $_POST['movimiento'];
    
    $file = fopen($ruta, "w");
    fwrite($file, $movimiento);
    fclose($file);

    $respuesta['estado'] = true;

}catch(Exception $e){
    $respuesta['error'] = $e->getMessage();
}

echo json_encode($respuesta);


