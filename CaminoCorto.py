import networkx as nx
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (
    QApplication, QLabel, QVBoxLayout, QHBoxLayout,
    QWidget, QComboBox, QPushButton, QTextEdit
)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from collections import deque

# Llamar a main
from pv.main import *
# Llamar a preguntas
from pv.preguntas import *

class PanelCaminoCorto(QWidget):
    def __init__(self, grafo):
        super().__init__()

        self.grafo = grafo  # Grafo que se usará en la función

        # Layout principal
        layout = QVBoxLayout()

        # Título
        title = QLabel("Camino Corto entre Dos Amistades")
        layout.addWidget(title)

        # Selección de personas
        selection_layout = QHBoxLayout()
        self.combo_person1 = QComboBox()
        self.combo_person2 = QComboBox()

        # Llenar los ComboBoxes con los nombres de las personas en el grafo
        for person_id, person in self.grafo.listaNodos.items():
            self.combo_person1.addItem(person.nombre, person_id)
            self.combo_person2.addItem(person.nombre, person_id)

        selection_layout.addWidget(QLabel("Persona 1:"))
        selection_layout.addWidget(self.combo_person1)
        selection_layout.addWidget(QLabel("Persona 2:"))
        selection_layout.addWidget(self.combo_person2)
        layout.addLayout(selection_layout)

        # Botón para calcular el camino corto
        calcular_button = QPushButton("Calcular Camino Corto")
        calcular_button.clicked.connect(self.mostrar_camino_corto)
        layout.addWidget(calcular_button)

        # Área de texto para mostrar el camino
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)

        # Crear un canvas de matplotlib para mostrar el grafo
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Botón para regresar
        regresar_button = QPushButton("Regresar")
        regresar_button.clicked.connect(self.limpiar_grafo)
        layout.addWidget(regresar_button)

        self.setLayout(layout)

    def mostrar_camino_corto(self):
        # Obtener las IDs de las personas seleccionadas
        person1_id = self.combo_person1.currentData()
        person2_id = self.combo_person2.currentData()

        # Calcular el camino más corto usando la función shortest_path
        camino = shortest_path(self.grafo, person1_id, person2_id)

        # Mostrar el resultado
        if camino:
            self.result_area.setText(" -> ".join(camino))
            self.graficar_camino(camino)
        else:
            self.result_area.setText("No hay un camino disponible entre estas dos personas.")
            self.limpiar_grafo()

    def graficar_camino(self, camino):
        # Limpiar la figura anterior
        self.figure.clear()

        # Crear un nuevo grafo usando networkx
        G = nx.Graph()

        # Añadir nodos al grafo solo si están en el camino o conectados al camino
        for nodo in self.grafo.listaNodos.values():
            if nodo.nombre in camino:
                G.add_node(nodo.nombre)

        # Añadir aristas (conexiones de amigos) solo para nodos en el camino
        for nodo in self.grafo.listaNodos.values():
            if nodo.nombre in camino:
                for amigo in nodo.amigos:
                    if amigo.nombre in camino:
                        G.add_edge(nodo.nombre, amigo.nombre)

        # Dibujar el grafo del subgrupo
        ax = self.figure.add_subplot(111)
        ax.clear()  # Limpiar el contenido previo del gráfico
        pos = nx.spring_layout(G)  # Disposición del grafo
        nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=10, ax=ax)

        # Resaltar el camino encontrado
        camino_edges = [(camino[i], camino[i + 1]) for i in range(len(camino) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=camino_edges, width=2, edge_color="red", ax=ax)

        # Refrescar el canvas para mostrar el grafo actualizado
        self.canvas.draw()

    def limpiar_grafo(self):
        # Limpiar la figura anterior y el área de texto
        self.figure.clear()
        self.canvas.draw()
        self.result_area.clear()

if __name__ == "__main__":
    app = QApplication([])

    # Aquí debes proporcionar un objeto `grafo` al instanciar `PanelCaminoCorto`
    # Asegúrate de que `grafo` esté definido antes de ejecutar el código
    grafo = llenarGrafo()  # Reemplaza esto con la creación de tu grafo
    window = PanelCaminoCorto(grafo)
    window.show()
    app.exec()
