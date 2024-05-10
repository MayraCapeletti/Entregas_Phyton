class Cliente():
    def __init__(self, nombre, apellido, edad, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.compras = []

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\nEmail: {self.email}"

    def comprar(self, producto, cantidad):
        self.compras.append((producto, cantidad))
        print(f"\n{self.nombre} ha comprado {cantidad} unidades de {producto}")
        print(f"Se le enviará su factura al siguiente correo {self.email}")

    def mostrar_compras(self):
        if self.compras:
            print(f"\nLista de compras de {self.nombre}:")
            for compra in self.compras:
                print(f"{compra[1]} unidades de {compra[0]}")
        else:
            print(f"{self.nombre} no ha realizado ninguna compra aún")

    def menu_cliente(self):
        while True:
            print("\nOpciones: ")
            print("1. Obtener información del cliente")
            print("2. Comprar")
            print("3. Mostrar compra")
            print("4. Salir")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                print()
                print(self.obtener_informacion())
            elif opcion == "2":
                producto = input("Ingrese el producto que desea comprar: ")
                cantidad = int(
                    input("Ingrese la cantidad que desea comprar: "))
                self.comprar(producto, cantidad)
            elif opcion == "3":
                self.mostrar_compras()
            elif opcion == "4":
                print("Hasta la próxima.")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")
