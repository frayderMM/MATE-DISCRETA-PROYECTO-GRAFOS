import mysql.connector

from mysql.connector import Error

class DbBean:
    def __init__(self):
        self.db_url = "localhost"
        self.database = "ClinicaR"
        self.user = "root"
        self.password = "123456789"
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.db_url,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Conectado exitosamente al servidor")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

    def resultado_sql(self, sql):
        cursor = None
        result = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(sql)
            result = cursor.fetchall()
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            if cursor:
                cursor.close()
        return result

    def ejecuta_sql(self, sql):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
        except Error as e:
            print(f"Error al ejecutar la operación SQL: {e}")
            self.connection.rollback()
        finally:
            if cursor:
                cursor.close()
