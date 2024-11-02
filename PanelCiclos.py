import networkx as nx
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (
    QApplication, QLabel, QVBoxLayout, QHBoxLayout,
    QWidget, QPushButton, QTextEdit
)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

 #llamar a main
from pv.main import *
# llamar a preguntas
from pv.preguntas import *

# Clase para el panel
class PanelDeteccionCiclos(QWidget):
    def __init__(self, grafo):
        super().__init__()

        self.grafo = grafo

        # Layout principal
        layout = QVBoxLayout()

        # Título
        title = QLabel("Detección de Ciclos en la Red Social")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Botón para detectar ciclos
        detectar_button = QPushButton("Detectar Ciclos")
        detectar_button.clicked.connect(self.detectar_ciclos)
        layout.addWidget(detectar_button)

        # Área de texto para mostrar los ciclos
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)

        # Crear un canvas de matplotlib para mostrar el grafo
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def detectar_ciclos(self):
        grafo = llenarGrafo()
        ciclos = has_cycle(grafo)
        self.result_area.clear()

        if ciclos:
            self.result_area.append("El grafo tiene los siguientes ciclos:\n")
            for ciclo in ciclos:
                self.result_area.append(" -> ".join(ciclo))
        else:
            self.result_area.append("El grafo no tiene ciclos.")

        # Graficar el grafo
        self.graficar_grafo()

    def graficar_grafo(self):
        self.figure.clear()
        g = llenarGrafo()
        G = nx.Graph()
        for id, nodo in g.listaNodos.items():
            G.add_node(nodo.nombre)

        for id, nodo in g.listaNodos.items():
            for amigo in nodo.get_friends():
                G.add_edge(nodo.nombre, amigo.nombre)

        ax = self.figure.add_subplot(111)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, ax=ax)

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication([])

    # Aquí debes proporcionar un objeto `grafo` al instanciar `PanelDeteccionCiclos`
    grafo = Grafo()
    grafo.agregar_persona(1, "Alice")
    grafo.agregar_persona(2, "Bob")
    grafo.agregar_persona(3, "Charlie")
    grafo.agregar_amistad(1, 2)
    grafo.agregar_amistad(2, 3)
    grafo.agregar_amistad(3, 1)  # Esto crea un ciclo

    window = PanelDeteccionCiclos(grafo)
    window.show()
    app.exec()
