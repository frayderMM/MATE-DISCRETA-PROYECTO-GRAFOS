from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout,
    QWidget, QPushButton, QStackedWidget
)
from PyQt6.QtCore import Qt

# Importar tu panel personalizado
from PanelRecomendaciones import PanelRecomendaciones
from PanelGrupos import PanelGrupos
from PanelPopular import PanelPopular
class SocialGraphApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Red Social")
        self.setGeometry(100, 100, 800, 600)

        # Contenedor principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Layout principal
        main_layout = QVBoxLayout()

        # Título
        title = QLabel("Red Social")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Fila de botones
        button_layout = QHBoxLayout()
        
        # Botones
        grupos_button = QPushButton("Grupos de amigos")
        recomendaciones_button = QPushButton("Amigos a recomendar")
        popular_button = QPushButton("Usuario más popular")
        corto_button = QPushButton("Camino corto entre dos amistades")
        ciclo_button = QPushButton("Ciclo en red social")

        # Agregar botones al layout de botones
        button_layout.addWidget(grupos_button)
        button_layout.addWidget(recomendaciones_button)
        button_layout.addWidget(popular_button)
        button_layout.addWidget(corto_button)
        button_layout.addWidget(ciclo_button)

        main_layout.addLayout(button_layout)

        # Crear un QStackedWidget para manejar los paneles
        self.paneles = QStackedWidget()
        main_layout.addWidget(self.paneles)

        # Crear paneles
        self.panel_grupos = PanelGrupos()
        self.panel_recomendaciones = PanelRecomendaciones()  # Tu panel personalizado
        self.panel_popular = PanelPopular()
        self.panel_corto = QLabel("Panel de Camino Corto")
        self.panel_ciclo = QLabel("Panel de Ciclo en Red Social")

        # Añadir paneles al QStackedWidget
        self.paneles.addWidget(self.panel_grupos)
        self.paneles.addWidget(self.panel_recomendaciones)
        self.paneles.addWidget(self.panel_popular)
        self.paneles.addWidget(self.panel_corto)
        self.paneles.addWidget(self.panel_ciclo)

        # Conectar los botones con funciones para agregar los paneles
        grupos_button.clicked.connect(self.mostrar_panel_grupos)
        recomendaciones_button.clicked.connect(self.mostrar_panel_recomendaciones)
        popular_button.clicked.connect(self.mostrar_panel_popular)
        corto_button.clicked.connect(self.mostrar_panel_corto)
        ciclo_button.clicked.connect(self.mostrar_panel_ciclo)

        main_widget.setLayout(main_layout)

    # Funciones para mostrar cada panel
    def mostrar_panel_grupos(self):
        self.paneles.setCurrentWidget(self.panel_grupos)

    def mostrar_panel_recomendaciones(self):
        self.paneles.setCurrentWidget(self.panel_recomendaciones)

    def mostrar_panel_popular(self):
        self.paneles.setCurrentWidget(self.panel_popular)

    def mostrar_panel_corto(self):
        self.paneles.setCurrentWidget(self.panel_corto)

    def mostrar_panel_ciclo(self):
        self.paneles.setCurrentWidget(self.panel_ciclo)

if __name__ == "__main__":
    app = QApplication([])
    window = SocialGraphApp()
    window.show()
    app.exec()
