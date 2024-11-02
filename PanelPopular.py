from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout,
    QHBoxLayout, QWidget, QGroupBox, QPushButton, QLineEdit, QComboBox
)
from PyQt6.QtCore import Qt

 
#llamar a main
from pv.main import *
# llamar a preguntas
from pv.preguntas import *


class PanelPopular(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Usuario Más Popular")
        self.setGeometry(100, 100, 800, 400)

        # Contenedor principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Layout principal
        main_layout = QVBoxLayout()

        # Título del panel
        title = QLabel("Usuario más popular")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Sección de filtrado y búsqueda
        filter_layout = QHBoxLayout()
        filter_label = QLabel("Filtrar por:")
        filter_combobox = QComboBox()
        filter_combobox.addItems(["Nombre", "Seguidores", "Actividad"])  # Opciones de filtro
        search_input = QLineEdit()
        search_input.setPlaceholderText("Buscar...")

        filter_layout.addWidget(filter_label)
        filter_layout.addWidget(filter_combobox)
        filter_layout.addWidget(search_input)
        main_layout.addLayout(filter_layout)

        # Sección del usuario más popular
        popular_user_box = QGroupBox("Detalles del usuario más popular : ")
        popular_user_layout = QVBoxLayout()


        grafo = llenarGrafo()
        nombre, numAmigos, amigos = most_popular_friend(grafo)

        # Información del usuario más popular (puedes actualizar estos valores dinámicamente)
        
        popular_user_name = QLabel(f"Usuario mas popular: {nombre}")
        popular_user_layout.addWidget(popular_user_name)
        popular_user_followers = QLabel(f"Numero de amigos: {numAmigos}")
        popular_user_layout.addWidget(popular_user_followers)
        for i in amigos:
            popular_user_layout.addWidget(QLabel(f"amigos: {i.nombre}"))
        
        popular_user_box.setLayout(popular_user_layout)
        main_layout.addWidget(popular_user_box)

        # Botón "Regresar"
        back_button = QPushButton("Regresar")
        main_layout.addWidget(back_button)

        main_widget.setLayout(main_layout)
    

if __name__ == "__main__":
    app = QApplication([])
    window = PanelPopular()
    window.show()
    app.exec()
