


## CLASE Nodo --> Persona 
class Nodo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.amigos = []

    def anadirAmigos(self, nodo):
        if nodo not in self.amigos:
            self.amigos.append(nodo)

    # Método para obtener los amigos de este nodo
    def get_friends(self):
        return self.amigos
    
    def __repr__(self):
        return f"Nodo({self.id}, {self.nombre})"

    