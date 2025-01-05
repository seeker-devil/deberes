class ListaDeCompras:
    def __init__(self):
        self.articulos = []  # Lista para almacenar los artículos de compra

    # Método para ingresar los artículos de compra
    def ingresar_articulos(self):
        while True:
            articulo = input('Ingrese un artículo para la lista de compras (o "fin" para terminar): ')
            if articulo.lower() == 'fin':
                break
            self.articulos.append(articulo)

    # Método para mostrar la lista de compras
    def mostrar_lista(self):
        if len(self.articulos) == 0:
            print("La lista de compras está vacía.")
        else:
            print("Lista de compras para el desayuno:")
            for articulo in self.articulos:
                print(f"- {articulo}")

# Crear una instancia de la clase ListaDeCompras
lista = ListaDeCompras()

# Ingresar los artículos para el desayuno
lista.ingresar_articulos()

# Mostrar la lista de compras
lista.mostrar_lista()
