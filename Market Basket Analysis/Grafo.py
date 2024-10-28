from Nodo import Nodo
import networkx as nx
import matplotlib.pyplot as plt
from Producto import Producto

class Grafo:
    def __init__(self):
        self.listaNodos = {}

    def agregar_nodo(self, producto):
        if producto.product_id not in self.listaNodos:
            self.listaNodos[producto.product_id] = Nodo(producto)
        else:
            print("El nodo ya existe.")

    def agregar_arista(self, producto1, producto2):
        id1, id2 = producto1.product_id, producto2.product_id
        if id1 in self.listaNodos and id2 in self.listaNodos:
            self.listaNodos[id1].anadirAmigos(self.listaNodos[id2])
            self.listaNodos[id2].anadirAmigos(self.listaNodos[id1])
        else:
            print("Uno o ambos nodos no existen en el grafo.")

    def show(self):
        for id, nodo in self.listaNodos.items():
            print(f"Nodo {id}: {nodo.producto.name}, Amigos: {[amigo.producto.name for amigo in nodo.get_friends()]}")

    def graficar_grafo(self):

        G = nx.Graph()
        for id, nodo in self.listaNodos.items():
            G.add_node(nodo.producto.name)
        for id, nodo in self.listaNodos.items():
            for amigo in nodo.get_friends():
                G.add_edge(nodo.producto.name, amigo.producto.name)
        pos = nx.spring_layout(G)  # Layout para el grafo
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_color='black', font_weight='bold', edge_color='gray')
        plt.title("Visualización del Grafo de Co-ocurrencia de Productos")
        plt.show()
