<?php

$respuesta['estado'] = false;

try{
    require 'meta.php';

    $consulta = Meta::Consulta_Unico("SELECT * FROM fotos ORDER BY id_foto DESC LIMIT 1");

    if ($consulta['id_foto']!=''){
        $respuesta['foto'] = $consulta['foto'];
        $respuesta['estado'] = true;
    }
}catch(Exception $e){
    $respuesta['error'] = $e->getMessage();
}

echo json_encode($respuesta);