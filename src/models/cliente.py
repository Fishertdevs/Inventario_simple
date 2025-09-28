class Cliente:
    def __init__(self, db):
        self.db = db

    def crear(self, nombre, telefono, email, direccion):
        """Crear un nuevo cliente"""
        query = """
            INSERT INTO clientes (nombre, telefono, email, direccion)
            VALUES (?, ?, ?, ?)
        """
        cursor = self.db.execute_query(query, (nombre, telefono, email, direccion))
        if cursor:
            return {"success": True, "id": cursor.lastrowid, "message": "Cliente creado exitosamente"}
        return {"success": False, "message": "Error al crear cliente"}

    def obtener_todos(self):
        """Obtener todos los clientes"""
        query = "SELECT * FROM clientes ORDER BY nombre"
        clientes = self.db.fetch_all(query)
        return [dict(cliente) for cliente in clientes]

    def obtener_por_id(self, id_cliente):
        """Obtener un cliente por ID"""
        query = "SELECT * FROM clientes WHERE id_cliente = ?"
        cliente = self.db.fetch_one(query, (id_cliente,))
        return dict(cliente) if cliente else None

    def actualizar(self, id_cliente, nombre, telefono, email, direccion):
        """Actualizar un cliente existente"""
        query = """
            UPDATE clientes 
            SET nombre = ?, telefono = ?, email = ?, direccion = ?
            WHERE id_cliente = ?
        """
        cursor = self.db.execute_query(query, (nombre, telefono, email, direccion, id_cliente))
        if cursor:
            return {"success": True, "message": "Cliente actualizado exitosamente"}
        return {"success": False, "message": "Error al actualizar cliente"}

    def eliminar(self, id_cliente):
        """Eliminar un cliente"""
        query = "DELETE FROM clientes WHERE id_cliente = ?"
        cursor = self.db.execute_query(query, (id_cliente,))
        if cursor:
            return {"success": True, "message": "Cliente eliminado exitosamente"}
        return {"success": False, "message": "Error al eliminar cliente"}