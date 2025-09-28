from models.producto import Producto

class ProductoController:
    def __init__(self, db):
        self.producto_model = Producto(db)

    def crear_producto(self, nombre, descripcion, precio, stock, id_proveedor):
        """Crear un nuevo producto con validación"""
        # Validaciones básicas
        if not nombre or not nombre.strip():
            return {"success": False, "message": "El nombre es obligatorio"}
        
        try:
            precio = float(precio)
            if precio < 0:
                return {"success": False, "message": "El precio debe ser mayor o igual a 0"}
        except (ValueError, TypeError):
            return {"success": False, "message": "El precio debe ser un número válido"}
        
        try:
            stock = int(stock)
            if stock < 0:
                return {"success": False, "message": "El stock debe ser mayor o igual a 0"}
        except (ValueError, TypeError):
            return {"success": False, "message": "El stock debe ser un número entero válido"}
        
        return self.producto_model.crear(nombre.strip(), descripcion, precio, stock, id_proveedor)

    def obtener_productos(self):
        """Obtener todos los productos"""
        return self.producto_model.obtener_todos()

    def obtener_producto(self, id_producto):
        """Obtener un producto por ID"""
        return self.producto_model.obtener_por_id(id_producto)

    def actualizar_producto(self, id_producto, nombre, descripcion, precio, stock, id_proveedor):
        """Actualizar un producto con validación"""
        # Validaciones básicas
        if not nombre or not nombre.strip():
            return {"success": False, "message": "El nombre es obligatorio"}
        
        try:
            precio = float(precio)
            if precio < 0:
                return {"success": False, "message": "El precio debe ser mayor o igual a 0"}
        except (ValueError, TypeError):
            return {"success": False, "message": "El precio debe ser un número válido"}
        
        try:
            stock = int(stock)
            if stock < 0:
                return {"success": False, "message": "El stock debe ser mayor o igual a 0"}
        except (ValueError, TypeError):
            return {"success": False, "message": "El stock debe ser un número entero válido"}
        
        return self.producto_model.actualizar(id_producto, nombre.strip(), descripcion, precio, stock, id_proveedor)

    def eliminar_producto(self, id_producto):
        """Eliminar un producto"""
        return self.producto_model.eliminar(id_producto)