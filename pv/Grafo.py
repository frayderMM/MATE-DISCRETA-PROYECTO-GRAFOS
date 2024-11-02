from Nodo import Nodo
import networkx as nx
import matplotlib.pyplot as plt
class Grafo:
    def __init__(self):
        self.listaNodos = {}
    
    def agregar_persona(self, id, nombre):

        if id not in self.listaNodos:
            self.listaNodos[id] = Nodo(id, nombre)  # key = id ; value = Nodo
        else:
            print("El Usuario ya existe")

    def agregar_amistad(self, id1, id2):
        if id1 in self.listaNodos and id2 in self.listaNodos:
            self.listaNodos[id1].anadirAmigos(self.listaNodos[id2]) 
            self.listaNodos[id2].anadirAmigos(self.listaNodos[id1])  

    def show(self):
        for id, nodo in self.listaNodos.items():
            print(f"NODO: {id}  Amigos : {nodo.amigos}")



    # Nueva función para graficar el grafo
    def graficar_grafo(self):
        # Crear un grafo vacío de NetworkX
        G = nx.Graph()

        # Agregar nodos al grafo
        for id, nodo in self.listaNodos.items():
            G.add_node(nodo.nombre)  # Se usa el nombre del nodo para mostrar en la gráfica

        # Agregar las relaciones (amistades) como aristas en el grafo
        for id, nodo in self.listaNodos.items():
            for amigo in nodo.get_friends():
                G.add_edge(nodo.nombre, amigo.nombre)  # Conectar nodos mediante sus nombres

        # Dibujar el grafo
        pos = nx.spring_layout(G)  # Layout para el grafo
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_color='black', font_weight='bold', edge_color='gray')

        # Mostrar la gráfica
        plt.title("Visualización del Grafo de la Red Social")
        plt.show()