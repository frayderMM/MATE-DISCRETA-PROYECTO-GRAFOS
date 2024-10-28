from Producto import Producto
class Nodo:
    def __init__(self, producto):
        self.id = producto.product_id   
        self.producto = producto
        self.amigos = []

    def anadirAmigos(self, nodo):
        if nodo not in self.amigos:
            self.amigos.append(nodo)

    # Método para obtener los amigos de este nodo
    def get_friends(self):
        return self.amigos
    
    def info(self):
        self.producto.info()





