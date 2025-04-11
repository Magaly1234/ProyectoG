<?php
// Configuración de la conexión a la base de datos
$servername = "localhost";
$username = "Magaly_PG";
$password = ""; // Asegúrate de colocar tu contraseña aquí
$database = "rehabilitacion";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $database);

// Verificar conexión
if ($conn->connect_error) {
    die(json_encode(["success" => false, "message" => "Conexión fallida: " . $conn->connect_error]));
}

// Consulta SQL para obtener los datos
$sql = "SELECT * FROM datos_sensor ORDER BY id DESC LIMIT 100"; // Últimos 100 registros
$result = $conn->query($sql);

// Verificar si hay resultados
if ($result->num_rows > 0) {
    $datos = [];
    while ($row = $result->fetch_assoc()) {
        $datos[] = $row;
    }
    echo json_encode(["success" => true, "data" => $datos]);
} else {
    echo json_encode(["success" => false, "message" => "No hay datos disponibles"]);
}

// Cerrar conexión
$conn->close();
?>
