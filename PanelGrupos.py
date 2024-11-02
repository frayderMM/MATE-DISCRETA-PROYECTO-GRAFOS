from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout,
    QHBoxLayout, QWidget, QGroupBox, QPushButton, QScrollArea
)
from PyQt6.QtCore import Qt

 #llamar a main
from pv.main import *
# llamar a preguntas
from pv.preguntas import *

class PanelGrupos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grupo de Amigos en la Red Social")
        self.setGeometry(100, 100, 800, 600)

        # Contenedor principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Layout principal
        main_layout = QVBoxLayout()

        # Título
        title = QLabel("GRUPO DE AMIGOS EN LA RED SOCIAL")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Sección de número de grupos
        num_groups_layout = QHBoxLayout()
        num_groups_label = QLabel("Número de grupos:")
        self.num_groups_input = QLineEdit()
        self.num_groups_input.setFixedWidth(50)
        self.num_groups_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        generate_button = QPushButton("Generar Grupos")
        self.generate_groups
        generate_button.clicked.connect(self.generate_groups)
        
        num_groups_layout.addWidget(num_groups_label)
        num_groups_layout.addWidget(self.num_groups_input)
        num_groups_layout.addWidget(generate_button)
        main_layout.addLayout(num_groups_layout)

        # Sección de grupos de amigos
        self.groups_container = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_widget.setLayout(self.groups_container)
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)

        # Botones "Regresar" y "Mostrar Grafo"
        buttons_layout = QHBoxLayout()
        back_button = QPushButton("Regresar")
        show_graph_button = QPushButton("Mostrar Grafo")
        buttons_layout.addWidget(back_button)
        buttons_layout.addWidget(show_graph_button)
        main_layout.addLayout(buttons_layout)

        main_widget.setLayout(main_layout)

    def generate_groups(self):
        # Limpiar el contenedor de grupos antes de generar nuevos
        for i in reversed(range(self.groups_container.count())):
            item = self.groups_container.itemAt(i)
            if item and item.widget():
                item.widget().deleteLater()

        # Llenar el grafo y encontrar los grupos de amigos
        grafo = llenarGrafo()
        numeroGrupos, grupos = find_friend_groups_bfs(grafo)

        # Añadir el número de grupos encontrados
        numero_grupos_label = QLabel(f"Numero de grupos encontrados en la red social son: {numeroGrupos}")
        self.groups_container.addWidget(numero_grupos_label)

        # Crear y agregar los grupos al contenedor
        num = 0
        for grupo in grupos:
            num += 1
            group_box = QGroupBox(f"Grupo {num}:")
            group_layout = QVBoxLayout()
            
            # Añadir cada miembro del grupo al layout
            for miembro in grupo:
                group_layout.addWidget(QLabel(f"miembro : {miembro.nombre}"))
            
            group_box.setLayout(group_layout)
            self.groups_container.addWidget(group_box)



        


if __name__ == "__main__":
    app = QApplication([])
    window = PanelGrupos()
    window.show()
    app.exec()
