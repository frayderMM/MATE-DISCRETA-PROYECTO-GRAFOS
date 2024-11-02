from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout,
    QHBoxLayout, QWidget, QGroupBox, QPushButton, QListWidget, QScrollArea
)
from PyQt6.QtCore import Qt

# Llamar a main
from pv.main import *
# Llamar a preguntas
from pv.preguntas import *

class PanelRecomendaciones(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Amigos a Recomendar")
        self.setGeometry(100, 100, 800, 400)

        # Contenedor principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Layout principal
        main_layout = QVBoxLayout()

        # Título del panel de recomendaciones
        user_name = "usuario"  # Puedes cambiar esto dinámicamente según el usuario
        title = QLabel(f"Amigos a recomendar a {user_name}")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Crear un área de scroll para las recomendaciones
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        # Widget y layout que contendrán las recomendaciones
        recommendations_widget = QWidget()
        self.recommendations_container = QVBoxLayout(recommendations_widget)

        # Llenar el grafo y obtener las recomendaciones
        grafo = llenarGrafo()
        recomendaciones = recommend_friends(grafo)

        # Crear y agregar las recomendaciones al contenedor
        for i, value in grafo.listaNodos.items():
            # Crear un cuadro de grupo para cada persona
            recommendations_box = QGroupBox(f"Recomendaciones para {value.nombre}")
            recommendations_layout = QVBoxLayout()

            # Añadir cada amigo recomendado al layout
            for j in recomendaciones[i]:
                recommendations_layout.addWidget(QLabel(f"Amigo recomendado: {j.nombre}"))

            recommendations_box.setLayout(recommendations_layout)
            self.recommendations_container.addWidget(recommendations_box)

        # Configurar el área de scroll
        scroll_area.setWidget(recommendations_widget)
        main_layout.addWidget(scroll_area)

        # Botón "Regresar"
        back_button = QPushButton("Regresar")
        main_layout.addWidget(back_button)

        main_widget.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication([])
    window = SocialGraphApp()
    window.show()
    app.exec()
