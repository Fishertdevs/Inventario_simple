from models.proveedor import Proveedor

class ProveedorController:
    def __init__(self, db):
        self.proveedor_model = Proveedor(db)

    def crear_proveedor(self, nombre, telefono, email, direccion, empresa):
        """Crear un nuevo proveedor con validación"""
        # Validaciones básicas
        if not nombre or not nombre.strip():
            return {"success": False, "message": "El nombre es obligatorio"}
        
        if email and "@" not in email:
            return {"success": False, "message": "El email no tiene formato válido"}
        
        return self.proveedor_model.crear(nombre.strip(), telefono, email, direccion, empresa)

    def obtener_proveedores(self):
        """Obtener todos los proveedores"""
        return self.proveedor_model.obtener_todos()

    def obtener_proveedor(self, id_proveedor):
        """Obtener un proveedor por ID"""
        return self.proveedor_model.obtener_por_id(id_proveedor)

    def actualizar_proveedor(self, id_proveedor, nombre, telefono, email, direccion, empresa):
        """Actualizar un proveedor con validación"""
        # Validaciones básicas
        if not nombre or not nombre.strip():
            return {"success": False, "message": "El nombre es obligatorio"}
        
        if email and "@" not in email:
            return {"success": False, "message": "El email no tiene formato válido"}
        
        return self.proveedor_model.actualizar(id_proveedor, nombre.strip(), telefono, email, direccion, empresa)

    def eliminar_proveedor(self, id_proveedor):
        """Eliminar un proveedor"""
        return self.proveedor_model.eliminar(id_proveedor)