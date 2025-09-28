from models.venta import Venta

class VentaController:
    def __init__(self, db):
        self.venta_model = Venta(db)
        self.db = db

    def crear_venta(self, id_cliente, id_producto, cantidad, precio_unitario):
        """Crear una nueva venta con validación"""
        # Validar que el cliente existe
        cliente = self.db.fetch_one("SELECT * FROM clientes WHERE id_cliente = ?", (id_cliente,))
        if not cliente:
            return {"success": False, "message": "El cliente seleccionado no existe"}
        
        # Validar que el producto existe y tiene suficiente stock
        producto = self.db.fetch_one("SELECT * FROM productos WHERE id_producto = ?", (id_producto,))
        if not producto:
            return {"success": False, "message": "El producto seleccionado no existe"}
        
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                return {"success": False, "message": "La cantidad debe ser mayor a 0"}
        except (ValueError, TypeError):
            return {"success": False, "message": "La cantidad debe ser un número entero válido"}
        
        if producto['stock'] < cantidad:
            return {"success": False, "message": f"Stock insuficiente. Stock disponible: {producto['stock']}"}
        
        try:
            precio_unitario = float(precio_unitario)
            if precio_unitario <= 0:
                return {"success": False, "message": "El precio unitario debe ser mayor a 0"}
        except (ValueError, TypeError):
            return {"success": False, "message": "El precio unitario debe ser un número válido"}
        
        return self.venta_model.crear(id_cliente, id_producto, cantidad, precio_unitario)

    def obtener_ventas(self):
        """Obtener todas las ventas"""
        return self.venta_model.obtener_todas()

    def obtener_venta(self, id_venta):
        """Obtener una venta por ID"""
        return self.venta_model.obtener_por_id(id_venta)

    def eliminar_venta(self, id_venta):
        """Eliminar una venta"""
        return self.venta_model.eliminar(id_venta)