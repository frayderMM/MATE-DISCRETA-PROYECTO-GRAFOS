class Producto:
    def __init__(self, product_id, name, unit_price):
        self.product_id = product_id
        self.name = name
        self.unit_price = unit_price

    

    def info(self):
        """Devuelve una descripción básica del producto."""
        return (f"ID: {self.product_id}\n"
                f"Nombre: {self.name}\n"
                f"Precio Unitario: ${self.unit_price:.2f}")