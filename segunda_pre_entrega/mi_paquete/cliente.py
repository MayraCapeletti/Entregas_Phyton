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
        print(f"{self.nombre} ha comprado {cantidad} unidades de {producto}")

    def mostrar_compras(self):
        if self.compras:
            print(f"Lista de compras de {self.nombre}:")
            for compra in self.compras:
                print(f"{compra[1]} unidades de {compra[0]}")
        else:
            print(f"{self.nombre} no ha realizado ninguna compra aún")
