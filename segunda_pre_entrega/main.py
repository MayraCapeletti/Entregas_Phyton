from mi_paquete.usuarios import registrar_usuario, mostrar_datos, login_usuario
from mi_paquete.cliente import Cliente


# Crear un objeto Cliente
cliente1 = Cliente("Juan", "Perez", 30, "juan@example.com")

# Imprimir el objeto usando el método __str__
print(cliente1)


cliente1.menu_cliente()
