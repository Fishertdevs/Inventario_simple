class Venta:
    def __init__(self, db):
        self.db = db

    def crear(self, id_cliente, id_producto, cantidad, precio_unitario):
        """Crear una nueva venta"""
        total = cantidad * precio_unitario
        query = """
            INSERT INTO ventas (id_cliente, id_producto, cantidad, precio_unitario, total)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor = self.db.execute_query(query, (id_cliente, id_producto, cantidad, precio_unitario, total))
        if cursor:
            # Actualizar stock del producto (reducir)
            stock_query = "UPDATE productos SET stock = stock - ? WHERE id_producto = ?"
            self.db.execute_query(stock_query, (cantidad, id_producto))
            return {"success": True, "id": cursor.lastrowid, "message": "Venta registrada exitosamente"}
        return {"success": False, "message": "Error al registrar venta"}

    def obtener_todas(self):
        """Obtener todas las ventas con información de cliente y producto"""
        query = """
            SELECT v.*, c.nombre as cliente_nombre, p.nombre as producto_nombre
            FROM ventas v
            INNER JOIN clientes c ON v.id_cliente = c.id_cliente
            INNER JOIN productos p ON v.id_producto = p.id_producto
            ORDER BY v.fecha_venta DESC
        """
        ventas = self.db.fetch_all(query)
        return [dict(venta) for venta in ventas]

    def obtener_por_id(self, id_venta):
        """Obtener una venta por ID"""
        query = "SELECT * FROM ventas WHERE id_venta = ?"
        venta = self.db.fetch_one(query, (id_venta,))
        return dict(venta) if venta else None

    def eliminar(self, id_venta):
        """Eliminar una venta y restaurar stock"""
        # Primero obtener información de la venta
        venta = self.obtener_por_id(id_venta)
        if not venta:
            return {"success": False, "message": "Venta no encontrada"}
        
        # Restaurar stock
        stock_query = "UPDATE productos SET stock = stock + ? WHERE id_producto = ?"
        self.db.execute_query(stock_query, (venta['cantidad'], venta['id_producto']))
        
        # Eliminar venta
        query = "DELETE FROM ventas WHERE id_venta = ?"
        cursor = self.db.execute_query(query, (id_venta,))
        if cursor:
            return {"success": True, "message": "Venta eliminada exitosamente"}
        return {"success": False, "message": "Error al eliminar venta"}