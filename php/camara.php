<?php

$respuesta['estado'] = false;

try{
    $ruta = '../estado.txt';
    $estado = '';
    // Primero lee el valor del archivo
    $file = fopen($ruta, "r");
    while(!feof($file)) {
        $estado = fgets($file);
    }
    fclose($file);

    // cambia el estado del valor obtenido
    $nuevo_estado = abs(intval($estado)-1);

    $file = fopen($ruta, "w");
    fwrite($file, $nuevo_estado);
    fclose($file);

    $respuesta['estado'] = true;

}catch(Exception $e){
    $respuesta['error'] = $e->getMessage();
}

echo json_encode($respuesta);


