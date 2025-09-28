class Producto:
    def __init__(self, db):
        self.db = db

    def crear(self, nombre, descripcion, precio, stock, id_proveedor):
        """Crear un nuevo producto"""
        query = """
            INSERT INTO productos (nombre, descripcion, precio, stock, id_proveedor)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor = self.db.execute_query(query, (nombre, descripcion, precio, stock, id_proveedor))
        if cursor:
            return {"success": True, "id": cursor.lastrowid, "message": "Producto creado exitosamente"}
        return {"success": False, "message": "Error al crear producto"}

    def obtener_todos(self):
        """Obtener todos los productos con información del proveedor"""
        query = """
            SELECT p.*, pr.nombre as proveedor_nombre, pr.empresa
            FROM productos p
            LEFT JOIN proveedores pr ON p.id_proveedor = pr.id_proveedor
            ORDER BY p.nombre
        """
        productos = self.db.fetch_all(query)
        return [dict(producto) for producto in productos]

    def obtener_por_id(self, id_producto):
        """Obtener un producto por ID"""
        query = "SELECT * FROM productos WHERE id_producto = ?"
        producto = self.db.fetch_one(query, (id_producto,))
        return dict(producto) if producto else None

    def actualizar(self, id_producto, nombre, descripcion, precio, stock, id_proveedor):
        """Actualizar un producto existente"""
        query = """
            UPDATE productos 
            SET nombre = ?, descripcion = ?, precio = ?, stock = ?, id_proveedor = ?
            WHERE id_producto = ?
        """
        cursor = self.db.execute_query(query, (nombre, descripcion, precio, stock, id_proveedor, id_producto))
        if cursor:
            return {"success": True, "message": "Producto actualizado exitosamente"}
        return {"success": False, "message": "Error al actualizar producto"}

    def eliminar(self, id_producto):
        """Eliminar un producto"""
        query = "DELETE FROM productos WHERE id_producto = ?"
        cursor = self.db.execute_query(query, (id_producto,))
        if cursor:
            return {"success": True, "message": "Producto eliminado exitosamente"}
        return {"success": False, "message": "Error al eliminar producto"}

    def actualizar_stock(self, id_producto, cantidad, operacion="sumar"):
        """Actualizar stock de un producto"""
        if operacion == "sumar":
            query = "UPDATE productos SET stock = stock + ? WHERE id_producto = ?"
        else:
            query = "UPDATE productos SET stock = stock - ? WHERE id_producto = ?"
        
        cursor = self.db.execute_query(query, (cantidad, id_producto))
        return cursor is not None