import sqlite3
import os
from datetime import datetime

class Database:
    def __init__(self, db_path='inventario.db'):
        self.db_path = db_path
        self.connection = None
        self.connect()

    def connect(self):
        """Conectar a la base de datos SQLite"""
        try:
            self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
            self.connection.row_factory = sqlite3.Row
            print(f"Conectado a la base de datos: {self.db_path}")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def create_tables(self):
        """Crear todas las tablas necesarias"""
        try:
            cursor = self.connection.cursor()
            
            # Tabla Clientes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    telefono TEXT,
                    email TEXT,
                    direccion TEXT,
                    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Tabla Proveedores
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS proveedores (
                    id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    telefono TEXT,
                    email TEXT,
                    direccion TEXT,
                    empresa TEXT,
                    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Tabla Productos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    precio REAL NOT NULL,
                    stock INTEGER DEFAULT 0,
                    id_proveedor INTEGER,
                    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor)
                )
            ''')
            
            # Tabla Ventas
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ventas (
                    id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER NOT NULL,
                    id_producto INTEGER NOT NULL,
                    cantidad INTEGER NOT NULL,
                    precio_unitario REAL NOT NULL,
                    total REAL NOT NULL,
                    fecha_venta DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
                    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
                )
            ''')
            
            # Tabla Compras
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS compras (
                    id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_proveedor INTEGER NOT NULL,
                    id_producto INTEGER NOT NULL,
                    cantidad INTEGER NOT NULL,
                    precio_unitario REAL NOT NULL,
                    total REAL NOT NULL,
                    fecha_compra DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor),
                    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
                )
            ''')
            
            self.connection.commit()
            print("Tablas creadas exitosamente")
            
        except sqlite3.Error as e:
            print(f"Error al crear tablas: {e}")

    def execute_query(self, query, params=None):
        """Ejecutar consulta SQL"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Error al ejecutar consulta: {e}")
            return None

    def fetch_all(self, query, params=None):
        """Obtener todos los resultados de una consulta"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener datos: {e}")
            return []

    def fetch_one(self, query, params=None):
        """Obtener un resultado de una consulta"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error al obtener dato: {e}")
            return None

    def close(self):
        """Cerrar conexión a la base de datos"""
        if self.connection:
            self.connection.close()
            print("Conexión a la base de datos cerrada")