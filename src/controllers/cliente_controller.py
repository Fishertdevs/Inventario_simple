from models.cliente import Cliente

class ClienteController:
    def __init__(self, db):
        self.cliente_model = Cliente(db)

    def crear_cliente(self, nombre, telefono, email, direccion):
        """Crear un nuevo cliente con validación"""
        # Validaciones básicas
        if not nombre or not nombre.strip():
            return {"success": False, "message": "El nombre es obligatorio"}
        
        if email and "@" not in email:
            return {"success": False, "message": "El email no tiene formato válido"}
        
        return self.cliente_model.crear(nombre.strip(), telefono, email, direccion)

    def obtener_clientes(self):
        """Obtener todos los clientes"""
        return self.cliente_model.obtener_todos()

    def obtener_cliente(self, id_cliente):
        """Obtener un cliente por ID"""
        return self.cliente_model.obtener_por_id(id_cliente)

    def actualizar_cliente(self, id_cliente, nombre, telefono, email, direccion):
        """Actualizar un cliente con validación"""
        # Validaciones básicas
        if not nombre or not nombre.strip():
            return {"success": False, "message": "El nombre es obligatorio"}
        
        if email and "@" not in email:
            return {"success": False, "message": "El email no tiene formato válido"}
        
        return self.cliente_model.actualizar(id_cliente, nombre.strip(), telefono, email, direccion)

    def eliminar_cliente(self, id_cliente):
        """Eliminar un cliente"""
        return self.cliente_model.eliminar(id_cliente)