from models.compra import Compra

class CompraController:
    def __init__(self, db):
        self.compra_model = Compra(db)
        self.db = db

    def crear_compra(self, id_proveedor, id_producto, cantidad, precio_unitario):
        """Crear una nueva compra con validación"""
        # Validar que el proveedor existe
        proveedor = self.db.fetch_one("SELECT * FROM proveedores WHERE id_proveedor = ?", (id_proveedor,))
        if not proveedor:
            return {"success": False, "message": "El proveedor seleccionado no existe"}
        
        # Validar que el producto existe
        producto = self.db.fetch_one("SELECT * FROM productos WHERE id_producto = ?", (id_producto,))
        if not producto:
            return {"success": False, "message": "El producto seleccionado no existe"}
        
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                return {"success": False, "message": "La cantidad debe ser mayor a 0"}
        except (ValueError, TypeError):
            return {"success": False, "message": "La cantidad debe ser un número entero válido"}
        
        try:
            precio_unitario = float(precio_unitario)
            if precio_unitario <= 0:
                return {"success": False, "message": "El precio unitario debe ser mayor a 0"}
        except (ValueError, TypeError):
            return {"success": False, "message": "El precio unitario debe ser un número válido"}
        
        return self.compra_model.crear(id_proveedor, id_producto, cantidad, precio_unitario)

    def obtener_compras(self):
        """Obtener todas las compras"""
        return self.compra_model.obtener_todas()

    def obtener_compra(self, id_compra):
        """Obtener una compra por ID"""
        return self.compra_model.obtener_por_id(id_compra)

    def eliminar_compra(self, id_compra):
        """Eliminar una compra"""
        return self.compra_model.eliminar(id_compra)