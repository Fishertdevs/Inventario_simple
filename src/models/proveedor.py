class Proveedor:
    def __init__(self, db):
        self.db = db

    def crear(self, nombre, telefono, email, direccion, empresa):
        """Crear un nuevo proveedor"""
        query = """
            INSERT INTO proveedores (nombre, telefono, email, direccion, empresa)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor = self.db.execute_query(query, (nombre, telefono, email, direccion, empresa))
        if cursor:
            return {"success": True, "id": cursor.lastrowid, "message": "Proveedor creado exitosamente"}
        return {"success": False, "message": "Error al crear proveedor"}

    def obtener_todos(self):
        """Obtener todos los proveedores"""
        query = "SELECT * FROM proveedores ORDER BY nombre"
        proveedores = self.db.fetch_all(query)
        return [dict(proveedor) for proveedor in proveedores]

    def obtener_por_id(self, id_proveedor):
        """Obtener un proveedor por ID"""
        query = "SELECT * FROM proveedores WHERE id_proveedor = ?"
        proveedor = self.db.fetch_one(query, (id_proveedor,))
        return dict(proveedor) if proveedor else None

    def actualizar(self, id_proveedor, nombre, telefono, email, direccion, empresa):
        """Actualizar un proveedor existente"""
        query = """
            UPDATE proveedores 
            SET nombre = ?, telefono = ?, email = ?, direccion = ?, empresa = ?
            WHERE id_proveedor = ?
        """
        cursor = self.db.execute_query(query, (nombre, telefono, email, direccion, empresa, id_proveedor))
        if cursor:
            return {"success": True, "message": "Proveedor actualizado exitosamente"}
        return {"success": False, "message": "Error al actualizar proveedor"}

    def eliminar(self, id_proveedor):
        """Eliminar un proveedor"""
        query = "DELETE FROM proveedores WHERE id_proveedor = ?"
        cursor = self.db.execute_query(query, (id_proveedor,))
        if cursor:
            return {"success": True, "message": "Proveedor eliminado exitosamente"}
        return {"success": False, "message": "Error al eliminar proveedor"}