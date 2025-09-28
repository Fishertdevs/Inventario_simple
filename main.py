import eel
import os
import sys

# Agregar el directorio src al path para importar modelos y controladores
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from models.database import Database
from controllers.cliente_controller import ClienteController
from controllers.proveedor_controller import ProveedorController
from controllers.producto_controller import ProductoController
from controllers.venta_controller import VentaController
from controllers.compra_controller import CompraController

# Inicializar Eel con la carpeta web
eel.init('src/views')

# Inicializar base de datos
db = Database()
db.create_tables()

# Inicializar controladores
cliente_controller = ClienteController(db)
proveedor_controller = ProveedorController(db)
producto_controller = ProductoController(db)
venta_controller = VentaController(db)
compra_controller = CompraController(db)

# Exponer funciones del controlador de clientes
@eel.expose
def crear_cliente(nombre, telefono, email, direccion):
    return cliente_controller.crear_cliente(nombre, telefono, email, direccion)

@eel.expose
def obtener_clientes():
    return cliente_controller.obtener_clientes()

@eel.expose
def actualizar_cliente(id_cliente, nombre, telefono, email, direccion):
    return cliente_controller.actualizar_cliente(id_cliente, nombre, telefono, email, direccion)

@eel.expose
def eliminar_cliente(id_cliente):
    return cliente_controller.eliminar_cliente(id_cliente)

# Exponer funciones del controlador de proveedores
@eel.expose
def crear_proveedor(nombre, telefono, email, direccion, empresa):
    return proveedor_controller.crear_proveedor(nombre, telefono, email, direccion, empresa)

@eel.expose
def obtener_proveedores():
    return proveedor_controller.obtener_proveedores()

@eel.expose
def actualizar_proveedor(id_proveedor, nombre, telefono, email, direccion, empresa):
    return proveedor_controller.actualizar_proveedor(id_proveedor, nombre, telefono, email, direccion, empresa)

@eel.expose
def eliminar_proveedor(id_proveedor):
    return proveedor_controller.eliminar_proveedor(id_proveedor)

# Exponer funciones del controlador de productos
@eel.expose
def crear_producto(nombre, descripcion, precio, stock, id_proveedor):
    return producto_controller.crear_producto(nombre, descripcion, precio, stock, id_proveedor)

@eel.expose
def obtener_productos():
    return producto_controller.obtener_productos()

@eel.expose
def actualizar_producto(id_producto, nombre, descripcion, precio, stock, id_proveedor):
    return producto_controller.actualizar_producto(id_producto, nombre, descripcion, precio, stock, id_proveedor)

@eel.expose
def eliminar_producto(id_producto):
    return producto_controller.eliminar_producto(id_producto)

# Exponer funciones del controlador de ventas
@eel.expose
def crear_venta(id_cliente, id_producto, cantidad, precio_unitario):
    return venta_controller.crear_venta(id_cliente, id_producto, cantidad, precio_unitario)

@eel.expose
def obtener_ventas():
    return venta_controller.obtener_ventas()

@eel.expose
def eliminar_venta(id_venta):
    return venta_controller.eliminar_venta(id_venta)

# Exponer funciones del controlador de compras
@eel.expose
def crear_compra(id_proveedor, id_producto, cantidad, precio_unitario):
    return compra_controller.crear_compra(id_proveedor, id_producto, cantidad, precio_unitario)

@eel.expose
def obtener_compras():
    return compra_controller.obtener_compras()

@eel.expose
def eliminar_compra(id_compra):
    return compra_controller.eliminar_compra(id_compra)

if __name__ == '__main__':
    # Iniciar la aplicación Eel
    try:
        print("Iniciando servidor en http://localhost:5000")
        # Configurar para abrir el navegador por defecto automáticamente
        eel.start(
            'index.html',
            mode='default',  # Abre el navegador predeterminado
            size=(1200, 800),
            port=5000,
            host='0.0.0.0',
            block=True  # Mantener el servidor corriendo
        )
    except (SystemExit, MemoryError, KeyboardInterrupt):
        print("Cerrando servidor...")
        # Cerrar la base de datos al salir
        db.close()