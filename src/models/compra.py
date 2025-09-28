class Compra:
    def __init__(self, db):
        self.db = db

    def crear(self, id_proveedor, id_producto, cantidad, precio_unitario):
        """Crear una nueva compra"""
        total = cantidad * precio_unitario
        query = """
            INSERT INTO compras (id_proveedor, id_producto, cantidad, precio_unitario, total)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor = self.db.execute_query(query, (id_proveedor, id_producto, cantidad, precio_unitario, total))
        if cursor:
            # Actualizar stock del producto (aumentar)
            stock_query = "UPDATE productos SET stock = stock + ? WHERE id_producto = ?"
            self.db.execute_query(stock_query, (cantidad, id_producto))
            return {"success": True, "id": cursor.lastrowid, "message": "Compra registrada exitosamente"}
        return {"success": False, "message": "Error al registrar compra"}

    def obtener_todas(self):
        """Obtener todas las compras con información de proveedor y producto"""
        query = """
            SELECT c.*, pr.nombre as proveedor_nombre, pr.empresa, p.nombre as producto_nombre
            FROM compras c
            INNER JOIN proveedores pr ON c.id_proveedor = pr.id_proveedor
            INNER JOIN productos p ON c.id_producto = p.id_producto
            ORDER BY c.fecha_compra DESC
        """
        compras = self.db.fetch_all(query)
        return [dict(compra) for compra in compras]

    def obtener_por_id(self, id_compra):
        """Obtener una compra por ID"""
        query = "SELECT * FROM compras WHERE id_compra = ?"
        compra = self.db.fetch_one(query, (id_compra,))
        return dict(compra) if compra else None

    def eliminar(self, id_compra):
        """Eliminar una compra y reducir stock"""
        # Primero obtener información de la compra
        compra = self.obtener_por_id(id_compra)
        if not compra:
            return {"success": False, "message": "Compra no encontrada"}
        
        # Reducir stock
        stock_query = "UPDATE productos SET stock = stock - ? WHERE id_producto = ?"
        self.db.execute_query(stock_query, (compra['cantidad'], compra['id_producto']))
        
        # Eliminar compra
        query = "DELETE FROM compras WHERE id_compra = ?"
        cursor = self.db.execute_query(query, (id_compra,))
        if cursor:
            return {"success": True, "message": "Compra eliminada exitosamente"}
        return {"success": False, "message": "Error al eliminar compra"}