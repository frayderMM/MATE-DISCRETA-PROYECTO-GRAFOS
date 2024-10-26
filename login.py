from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QGridLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize, Qt
import os
import sys
from UZ.DbBean import DbBean
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Login")
        self.setStyleSheet("background-color: #87CEEB;")  # Color celeste de fondo

        # Definir img_dir como un atributo de clase
        self.img_dir = os.path.join(os.path.dirname(__file__), "Images")

        # Imagen de fondo
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(os.path.join(self.img_dir, "fondo.jpg")))
        self.background_label.setScaledContents(True)

        # Crear un contenedor para los campos y el botón
        container = QWidget(self)
        container.setFixedSize(300, 250)
        container.setStyleSheet("background-color: rgba(255, 255, 255, 0.8); border-radius: 10px;")
        
        # Campo de nombre de usuario
        self.username_input = QLineEdit(container)
        self.username_input.setPlaceholderText("Nombre de usuario")
        self.username_input.setStyleSheet("background-color: white; color: black; padding: 10px; border-radius: 5px;")

        # Campo de contraseña
        self.password_input = QLineEdit(container)
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("background-color: white; color: black; padding: 10px; border-radius: 5px;")

        # Botón de mostrar/ocultar contraseña
        self.show_password_button = QPushButton(container)
        try:
            self.show_password_button.setIcon(QIcon(os.path.join(self.img_dir, "eye2.png")))  # Icono inicial
        except Exception as e:
            print(f"Error al cargar el icono: {e}")
            sys.exit(1)

        self.show_password_button.setIconSize(QSize(24, 24))
        self.show_password_button.setCheckable(True)
        self.show_password_button.setStyleSheet("background-color: white; padding: 5px; border-radius: 5px;")
        self.show_password_button.clicked.connect(self.toggle_password_visibility)

        # Botón de ingreso
        self.login_button = QPushButton("Ingresar", container)
        self.login_button.setStyleSheet("background-color: #007BFF; color: white; padding: 10px; border-radius: 5px;")
        self.login_button.setFixedSize(100, 38)
        self.login_button.clicked.connect(self.verificar)

        # Layout para los campos de entrada
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.username_input)
        
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_input)
        password_layout.addWidget(self.show_password_button)
        input_layout.addLayout(password_layout)

        # Layout principal del contenedor
        container_layout = QVBoxLayout(container)
        container_layout.addLayout(input_layout)
        container_layout.addWidget(self.login_button)
        container_layout.setAlignment(self.login_button, Qt.AlignmentFlag.AlignCenter)
        container.setLayout(container_layout)

        # Layout principal para centrar el contenedor
        main_layout = QGridLayout(self)
        main_layout.addWidget(self.background_label, 0, 0, 1, 1)
        main_layout.addWidget(container, 0, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(main_layout)
        self.background_label.lower()

    def verificar(self):
        
        con = DbBean()
        
        us = self.username_input.text()
        pw = self.password_input.text()
        
        sql = "SELECT u.usuario FROM usuarios AS u INNER JOIN empleados AS e ON e.id_empleados = u.id_empleados WHERE u.usuario = '" + us +"' AND u.contrasena = '"+ pw+"'"
        print(sql)
        try:
            # Ejecutar la consulta con parámetros
            result = con.resultado_sql(sql)
            
            print(result)
            if result:
                QMessageBox.warning(self, "Error", "Inicio de seccion correctos")
                # Cierra la ventana de login
                
                # Llama a la función que muestra la ventana principal
                
                self.panel = MainWindow()  # Crear una instancia del panel
                self.panel.showMaximized()
                self.close()
                
                
            else:
                QMessageBox.warning(self, "Error", "Datos incorrectos. Por favor, verifique su usuario y contraseña.")
        except Exception as e:
            print(f"Error al conectar con usuario y empleado: {e}")
            QMessageBox.critical(self, "Error", f"Se produjo un error: {e}")
        finally:
            try:
                con.disconnect()
            except Exception as e:
                print(f"Error al cerrar la conexión: {e}")
        
    def toggle_password_visibility(self):
        try:
            if self.show_password_button.isChecked():
                self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
                self.show_password_button.setIcon(QIcon(os.path.join(self.img_dir, "eye.png")))
            else:
                self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
                self.show_password_button.setIcon(QIcon(os.path.join(self.img_dir, "eye2.png")))
        except Exception as e:
            print(f"Error al cambiar la visibilidad de la contraseña: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.showMaximized()
    sys.exit(app.exec())

