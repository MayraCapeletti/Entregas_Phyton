from mi_paquete.usuarios import registrar_usuario, mostrar_datos, login_usuario
from mi_paquete.cliente import Cliente


# Crear un objeto Cliente
cliente1 = Cliente("Juan", "Perez", 30, "juan@example.com")

# Imprimir el objeto usando el método __str__
print(cliente1)

# Obtener información detallada del cliente
print(f"Información del cliente:\n{cliente1.obtener_informacion()}")

# El cliente realiza una compra
cliente1.comprar("Camisa", 2)
cliente1.comprar("Pantalón", 1)

# Mostrar las compras del cliente
cliente1.mostrar_compras()
