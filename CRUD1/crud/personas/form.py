<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Persona</title>
</head>
<body>
    <h1>Editar Persona</h1>
    <form method="post">
        {% csrf_token %}
        <label for="documento">Documento:</label><br>
        <input type="text" id="documento" name="documento" value="{{ persona.numero_de_documento }}"><br>
        
        <label for="nombre">Nombre:</label><br>
        <input type="text" id="nombre" name="nombre" value="{{ persona.nombre }}"><br>
        
        <label for="apellidos">Apellidos:</label><br>
        <input type="text" id="apellidos" name="apellidos" value="{{ persona.apellidos }}"><br>
        
        <label for="fecha_nacimiento">Fecha de Nacimiento:</label><br>
        <input type="text" id="fecha_nacimiento" name="fecha_nacimiento" value="{{ persona.fecha_nacimiento }}"><br>
        
        <label for="ciudad">Ciudad:</label><br>
        <input type="text" id="ciudad" name="ciudad" value="{{ persona.ciudad }}"><br>
        
        <label for="correo">Correo:</label><br>
        <input type="email" id="correo" name="correo" value="{{ persona.correo }}"><br>
        
        <label for="telefono">Teléfono:</label><br>
        <input type="text" id="telefono" name="telefono" value="{{ persona.telefono }}"><br>
        
        <label for="ocupacion">Ocupación:</label><br>
        <input type="text" id="ocupacion" name="ocupacion" value="{{ persona.ocupacion }}"><br>
        
        <input type="submit" value="Guardar cambios">
    </form>
</body>
</html>
