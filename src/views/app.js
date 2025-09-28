// Variables globales para almacenar datos
let clientesData = [];
let proveedoresData = [];
let productosData = [];
let ventasData = [];
let comprasData = [];

// Función para mostrar notificaciones
function showNotification(message, type = 'success') {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = `notification ${type}`;
    notification.classList.add('show');
    
    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}

// Función para mostrar/ocultar módulos
function showModule(moduleName) {
    // Ocultar todos los módulos
    const modules = document.querySelectorAll('.module');
    modules.forEach(module => module.classList.remove('active'));
    
    // Mostrar módulo seleccionado
    document.getElementById(moduleName).classList.add('active');
    
    // Actualizar navegación
    const navButtons = document.querySelectorAll('.nav-btn');
    navButtons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    
    // Cargar datos del módulo
    switch(moduleName) {
        case 'clientes':
            loadClientes();
            break;
        case 'proveedores':
            loadProveedores();
            break;
        case 'productos':
            loadProductos();
            break;
        case 'ventas':
            loadVentas();
            break;
        case 'compras':
            loadCompras();
            break;
    }
}

// FUNCIONES DE CLIENTES
function showClienteForm(cliente = null) {
    const form = document.getElementById('clienteForm');
    const title = document.getElementById('clienteFormTitle');
    const formData = document.getElementById('clienteFormData');
    
    if (cliente) {
        title.textContent = 'Editar Cliente';
        document.getElementById('clienteId').value = cliente.id_cliente;
        document.getElementById('clienteNombre').value = cliente.nombre;
        document.getElementById('clienteTelefono').value = cliente.telefono || '';
        document.getElementById('clienteEmail').value = cliente.email || '';
        document.getElementById('clienteDireccion').value = cliente.direccion || '';
    } else {
        title.textContent = 'Nuevo Cliente';
        formData.reset();
        document.getElementById('clienteId').value = '';
    }
    
    form.style.display = 'block';
}

function hideClienteForm() {
    document.getElementById('clienteForm').style.display = 'none';
}

async function loadClientes() {
    try {
        clientesData = await eel.obtener_clientes()();
        renderClientesTable();
    } catch (error) {
        showNotification('Error al cargar clientes', 'error');
    }
}

function renderClientesTable() {
    const tbody = document.querySelector('#clientesTable tbody');
    tbody.innerHTML = '';
    
    clientesData.forEach(cliente => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${cliente.id_cliente}</td>
            <td>${cliente.nombre}</td>
            <td>${cliente.telefono || ''}</td>
            <td>${cliente.email || ''}</td>
            <td>${cliente.direccion || ''}</td>
            <td>
                <button class="btn btn-warning btn-sm" onclick="editCliente(${cliente.id_cliente})">Editar</button>
                <button class="btn btn-danger btn-sm" onclick="deleteCliente(${cliente.id_cliente})">Eliminar</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

function editCliente(id) {
    const cliente = clientesData.find(c => c.id_cliente === id);
    if (cliente) {
        showClienteForm(cliente);
    }
}

function deleteCliente(id) {
    showConfirmModal('¿Está seguro de eliminar este cliente?', () => confirmDeleteCliente(id));
}

async function confirmDeleteCliente(id) {
    try {
        const result = await eel.eliminar_cliente(id)();
        if (result.success) {
            showNotification(result.message);
            loadClientes();
        } else {
            showNotification(result.message, 'error');
        }
    } catch (error) {
        showNotification('Error al eliminar cliente', 'error');
    }
    hideConfirmModal();
}

// FUNCIONES DE PROVEEDORES
function showProveedorForm(proveedor = null) {
    const form = document.getElementById('proveedorForm');
    const title = document.getElementById('proveedorFormTitle');
    const formData = document.getElementById('proveedorFormData');
    
    if (proveedor) {
        title.textContent = 'Editar Proveedor';
        document.getElementById('proveedorId').value = proveedor.id_proveedor;
        document.getElementById('proveedorNombre').value = proveedor.nombre;
        document.getElementById('proveedorEmpresa').value = proveedor.empresa || '';
        document.getElementById('proveedorTelefono').value = proveedor.telefono || '';
        document.getElementById('proveedorEmail').value = proveedor.email || '';
        document.getElementById('proveedorDireccion').value = proveedor.direccion || '';
    } else {
        title.textContent = 'Nuevo Proveedor';
        formData.reset();
        document.getElementById('proveedorId').value = '';
    }
    
    form.style.display = 'block';
}

function hideProveedorForm() {
    document.getElementById('proveedorForm').style.display = 'none';
}

async function loadProveedores() {
    try {
        proveedoresData = await eel.obtener_proveedores()();
        renderProveedoresTable();
        updateProveedorSelects();
    } catch (error) {
        showNotification('Error al cargar proveedores', 'error');
    }
}

function renderProveedoresTable() {
    const tbody = document.querySelector('#proveedoresTable tbody');
    tbody.innerHTML = '';
    
    proveedoresData.forEach(proveedor => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${proveedor.id_proveedor}</td>
            <td>${proveedor.nombre}</td>
            <td>${proveedor.empresa || ''}</td>
            <td>${proveedor.telefono || ''}</td>
            <td>${proveedor.email || ''}</td>
            <td>${proveedor.direccion || ''}</td>
            <td>
                <button class="btn btn-warning btn-sm" onclick="editProveedor(${proveedor.id_proveedor})">Editar</button>
                <button class="btn btn-danger btn-sm" onclick="deleteProveedor(${proveedor.id_proveedor})">Eliminar</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

function editProveedor(id) {
    const proveedor = proveedoresData.find(p => p.id_proveedor === id);
    if (proveedor) {
        showProveedorForm(proveedor);
    }
}

function deleteProveedor(id) {
    showConfirmModal('¿Está seguro de eliminar este proveedor?', () => confirmDeleteProveedor(id));
}

async function confirmDeleteProveedor(id) {
    try {
        const result = await eel.eliminar_proveedor(id)();
        if (result.success) {
            showNotification(result.message);
            loadProveedores();
        } else {
            showNotification(result.message, 'error');
        }
    } catch (error) {
        showNotification('Error al eliminar proveedor', 'error');
    }
    hideConfirmModal();
}

function updateProveedorSelects() {
    const selects = ['productoProveedor', 'compraProveedor'];
    
    selects.forEach(selectId => {
        const select = document.getElementById(selectId);
        if (select) {
            const currentValue = select.value;
            select.innerHTML = '<option value="">Seleccionar proveedor</option>';
            
            proveedoresData.forEach(proveedor => {
                const option = document.createElement('option');
                option.value = proveedor.id_proveedor;
                option.textContent = `${proveedor.nombre} - ${proveedor.empresa || 'Sin empresa'}`;
                select.appendChild(option);
            });
            
            if (currentValue) {
                select.value = currentValue;
            }
        }
    });
}

// FUNCIONES DE PRODUCTOS
function showProductoForm(producto = null) {
    loadProveedores(); // Cargar proveedores para el select
    
    const form = document.getElementById('productoForm');
    const title = document.getElementById('productoFormTitle');
    const formData = document.getElementById('productoFormData');
    
    if (producto) {
        title.textContent = 'Editar Producto';
        document.getElementById('productoId').value = producto.id_producto;
        document.getElementById('productoNombre').value = producto.nombre;
        document.getElementById('productoDescripcion').value = producto.descripcion || '';
        document.getElementById('productoPrecio').value = producto.precio;
        document.getElementById('productoStock').value = producto.stock;
        document.getElementById('productoProveedor').value = producto.id_proveedor || '';
    } else {
        title.textContent = 'Nuevo Producto';
        formData.reset();
        document.getElementById('productoId').value = '';
    }
    
    form.style.display = 'block';
}

function hideProductoForm() {
    document.getElementById('productoForm').style.display = 'none';
}

async function loadProductos() {
    try {
        productosData = await eel.obtener_productos()();
        renderProductosTable();
        updateProductoSelects();
    } catch (error) {
        showNotification('Error al cargar productos', 'error');
    }
}

function renderProductosTable() {
    const tbody = document.querySelector('#productosTable tbody');
    tbody.innerHTML = '';
    
    productosData.forEach(producto => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${producto.id_producto}</td>
            <td>${producto.nombre}</td>
            <td>${producto.descripcion || ''}</td>
            <td>$${parseFloat(producto.precio).toFixed(2)}</td>
            <td>${producto.stock}</td>
            <td>${producto.proveedor_nombre || 'Sin proveedor'}</td>
            <td>
                <button class="btn btn-warning btn-sm" onclick="editProducto(${producto.id_producto})">Editar</button>
                <button class="btn btn-danger btn-sm" onclick="deleteProducto(${producto.id_producto})">Eliminar</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

function editProducto(id) {
    const producto = productosData.find(p => p.id_producto === id);
    if (producto) {
        showProductoForm(producto);
    }
}

function deleteProducto(id) {
    showConfirmModal('¿Está seguro de eliminar este producto?', () => confirmDeleteProducto(id));
}

async function confirmDeleteProducto(id) {
    try {
        const result = await eel.eliminar_producto(id)();
        if (result.success) {
            showNotification(result.message);
            loadProductos();
        } else {
            showNotification(result.message, 'error');
        }
    } catch (error) {
        showNotification('Error al eliminar producto', 'error');
    }
    hideConfirmModal();
}

function updateProductoSelects() {
    const selects = ['ventaProducto', 'compraProducto'];
    
    selects.forEach(selectId => {
        const select = document.getElementById(selectId);
        if (select) {
            const currentValue = select.value;
            select.innerHTML = '<option value="">Seleccionar producto</option>';
            
            productosData.forEach(producto => {
                const option = document.createElement('option');
                option.value = producto.id_producto;
                option.textContent = `${producto.nombre} - Stock: ${producto.stock}`;
                option.dataset.precio = producto.precio;
                option.dataset.stock = producto.stock;
                select.appendChild(option);
            });
            
            if (currentValue) {
                select.value = currentValue;
            }
        }
    });
}

// FUNCIONES DE VENTAS
function showVentaForm() {
    loadClientes(); // Cargar clientes para el select
    loadProductos(); // Cargar productos para el select
    
    const form = document.getElementById('ventaForm');
    const formData = document.getElementById('ventaFormData');
    
    formData.reset();
    document.getElementById('ventaProductInfo').style.display = 'none';
    form.style.display = 'block';
}

function hideVentaForm() {
    document.getElementById('ventaForm').style.display = 'none';
}

function updateVentaProductInfo() {
    const select = document.getElementById('ventaProducto');
    const selectedOption = select.options[select.selectedIndex];
    const info = document.getElementById('ventaProductInfo');
    
    if (selectedOption && selectedOption.value) {
        const stock = selectedOption.dataset.stock;
        const precio = selectedOption.dataset.precio;
        
        document.getElementById('ventaProductStock').textContent = stock;
        document.getElementById('ventaProductPrecio').textContent = parseFloat(precio).toFixed(2);
        document.getElementById('ventaPrecioUnitario').value = precio;
        
        info.style.display = 'block';
        calculateVentaTotal();
    } else {
        info.style.display = 'none';
    }
}

function calculateVentaTotal() {
    const cantidad = parseFloat(document.getElementById('ventaCantidad').value) || 0;
    const precioUnitario = parseFloat(document.getElementById('ventaPrecioUnitario').value) || 0;
    const total = cantidad * precioUnitario;
    
    document.getElementById('ventaTotal').value = '$' + total.toFixed(2);
}

async function loadVentas() {
    try {
        ventasData = await eel.obtener_ventas()();
        renderVentasTable();
    } catch (error) {
        showNotification('Error al cargar ventas', 'error');
    }
}

function renderVentasTable() {
    const tbody = document.querySelector('#ventasTable tbody');
    tbody.innerHTML = '';
    
    ventasData.forEach(venta => {
        const row = document.createElement('tr');
        const fecha = new Date(venta.fecha_venta).toLocaleDateString();
        row.innerHTML = `
            <td>${venta.id_venta}</td>
            <td>${venta.cliente_nombre}</td>
            <td>${venta.producto_nombre}</td>
            <td>${venta.cantidad}</td>
            <td>$${parseFloat(venta.precio_unitario).toFixed(2)}</td>
            <td>$${parseFloat(venta.total).toFixed(2)}</td>
            <td>${fecha}</td>
            <td>
                <button class="btn btn-danger btn-sm" onclick="deleteVenta(${venta.id_venta})">Eliminar</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

function deleteVenta(id) {
    showConfirmModal('¿Está seguro de eliminar esta venta?', () => confirmDeleteVenta(id));
}

async function confirmDeleteVenta(id) {
    try {
        const result = await eel.eliminar_venta(id)();
        if (result.success) {
            showNotification(result.message);
            loadVentas();
            loadProductos(); // Actualizar stock de productos
        } else {
            showNotification(result.message, 'error');
        }
    } catch (error) {
        showNotification('Error al eliminar venta', 'error');
    }
    hideConfirmModal();
}

function updateClienteSelects() {
    const select = document.getElementById('ventaCliente');
    if (select) {
        const currentValue = select.value;
        select.innerHTML = '<option value="">Seleccionar cliente</option>';
        
        clientesData.forEach(cliente => {
            const option = document.createElement('option');
            option.value = cliente.id_cliente;
            option.textContent = cliente.nombre;
            select.appendChild(option);
        });
        
        if (currentValue) {
            select.value = currentValue;
        }
    }
}

// FUNCIONES DE COMPRAS
function showCompraForm() {
    loadProveedores(); // Cargar proveedores para el select
    loadProductos(); // Cargar productos para el select
    
    const form = document.getElementById('compraForm');
    const formData = document.getElementById('compraFormData');
    
    formData.reset();
    document.getElementById('compraProductInfo').style.display = 'none';
    form.style.display = 'block';
}

function hideCompraForm() {
    document.getElementById('compraForm').style.display = 'none';
}

function updateCompraProductInfo() {
    const select = document.getElementById('compraProducto');
    const selectedOption = select.options[select.selectedIndex];
    const info = document.getElementById('compraProductInfo');
    
    if (selectedOption && selectedOption.value) {
        const stock = selectedOption.dataset.stock;
        
        document.getElementById('compraProductStock').textContent = stock;
        info.style.display = 'block';
    } else {
        info.style.display = 'none';
    }
}

function calculateCompraTotal() {
    const cantidad = parseFloat(document.getElementById('compraCantidad').value) || 0;
    const precioUnitario = parseFloat(document.getElementById('compraPrecioUnitario').value) || 0;
    const total = cantidad * precioUnitario;
    
    document.getElementById('compraTotal').value = '$' + total.toFixed(2);
}

async function loadCompras() {
    try {
        comprasData = await eel.obtener_compras()();
        renderComprasTable();
    } catch (error) {
        showNotification('Error al cargar compras', 'error');
    }
}

function renderComprasTable() {
    const tbody = document.querySelector('#comprasTable tbody');
    tbody.innerHTML = '';
    
    comprasData.forEach(compra => {
        const row = document.createElement('tr');
        const fecha = new Date(compra.fecha_compra).toLocaleDateString();
        row.innerHTML = `
            <td>${compra.id_compra}</td>
            <td>${compra.proveedor_nombre} - ${compra.empresa || ''}</td>
            <td>${compra.producto_nombre}</td>
            <td>${compra.cantidad}</td>
            <td>$${parseFloat(compra.precio_unitario).toFixed(2)}</td>
            <td>$${parseFloat(compra.total).toFixed(2)}</td>
            <td>${fecha}</td>
            <td>
                <button class="btn btn-danger btn-sm" onclick="deleteCompra(${compra.id_compra})">Eliminar</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

function deleteCompra(id) {
    showConfirmModal('¿Está seguro de eliminar esta compra?', () => confirmDeleteCompra(id));
}

async function confirmDeleteCompra(id) {
    try {
        const result = await eel.eliminar_compra(id)();
        if (result.success) {
            showNotification(result.message);
            loadCompras();
            loadProductos(); // Actualizar stock de productos
        } else {
            showNotification(result.message, 'error');
        }
    } catch (error) {
        showNotification('Error al eliminar compra', 'error');
    }
    hideConfirmModal();
}

// FUNCIONES DEL MODAL DE CONFIRMACIÓN
function showConfirmModal(message, callback) {
    document.getElementById('confirmMessage').textContent = message;
    document.getElementById('confirmModal').style.display = 'block';
    document.getElementById('confirmBtn').onclick = callback;
}

function hideConfirmModal() {
    document.getElementById('confirmModal').style.display = 'none';
}

// EVENT LISTENERS
document.addEventListener('DOMContentLoaded', function() {
    // Cargar datos iniciales
    loadClientes();
    
    // Formulario de clientes
    document.getElementById('clienteFormData').addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const id = document.getElementById('clienteId').value;
        const nombre = document.getElementById('clienteNombre').value;
        const telefono = document.getElementById('clienteTelefono').value;
        const email = document.getElementById('clienteEmail').value;
        const direccion = document.getElementById('clienteDireccion').value;
        
        try {
            let result;
            if (id) {
                result = await eel.actualizar_cliente(parseInt(id), nombre, telefono, email, direccion)();
            } else {
                result = await eel.crear_cliente(nombre, telefono, email, direccion)();
            }
            
            if (result.success) {
                showNotification(result.message);
                hideClienteForm();
                loadClientes();
            } else {
                showNotification(result.message, 'error');
            }
        } catch (error) {
            showNotification('Error al guardar cliente', 'error');
        }
    });
    
    // Formulario de proveedores
    document.getElementById('proveedorFormData').addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const id = document.getElementById('proveedorId').value;
        const nombre = document.getElementById('proveedorNombre').value;
        const empresa = document.getElementById('proveedorEmpresa').value;
        const telefono = document.getElementById('proveedorTelefono').value;
        const email = document.getElementById('proveedorEmail').value;
        const direccion = document.getElementById('proveedorDireccion').value;
        
        try {
            let result;
            if (id) {
                result = await eel.actualizar_proveedor(parseInt(id), nombre, telefono, email, direccion, empresa)();
            } else {
                result = await eel.crear_proveedor(nombre, telefono, email, direccion, empresa)();
            }
            
            if (result.success) {
                showNotification(result.message);
                hideProveedorForm();
                loadProveedores();
            } else {
                showNotification(result.message, 'error');
            }
        } catch (error) {
            showNotification('Error al guardar proveedor', 'error');
        }
    });
    
    // Formulario de productos
    document.getElementById('productoFormData').addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const id = document.getElementById('productoId').value;
        const nombre = document.getElementById('productoNombre').value;
        const descripcion = document.getElementById('productoDescripcion').value;
        const precio = parseFloat(document.getElementById('productoPrecio').value);
        const stock = parseInt(document.getElementById('productoStock').value);
        const id_proveedor = document.getElementById('productoProveedor').value || null;
        
        try {
            let result;
            if (id) {
                result = await eel.actualizar_producto(parseInt(id), nombre, descripcion, precio, stock, id_proveedor)();
            } else {
                result = await eel.crear_producto(nombre, descripcion, precio, stock, id_proveedor)();
            }
            
            if (result.success) {
                showNotification(result.message);
                hideProductoForm();
                loadProductos();
            } else {
                showNotification(result.message, 'error');
            }
        } catch (error) {
            showNotification('Error al guardar producto', 'error');
        }
    });
    
    // Formulario de ventas
    document.getElementById('ventaFormData').addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const id_cliente = parseInt(document.getElementById('ventaCliente').value);
        const id_producto = parseInt(document.getElementById('ventaProducto').value);
        const cantidad = parseInt(document.getElementById('ventaCantidad').value);
        const precio_unitario = parseFloat(document.getElementById('ventaPrecioUnitario').value);
        
        try {
            const result = await eel.crear_venta(id_cliente, id_producto, cantidad, precio_unitario)();
            
            if (result.success) {
                showNotification(result.message);
                hideVentaForm();
                loadVentas();
                loadProductos(); // Actualizar stock de productos
            } else {
                showNotification(result.message, 'error');
            }
        } catch (error) {
            showNotification('Error al registrar venta', 'error');
        }
    });
    
    // Formulario de compras
    document.getElementById('compraFormData').addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const id_proveedor = parseInt(document.getElementById('compraProveedor').value);
        const id_producto = parseInt(document.getElementById('compraProducto').value);
        const cantidad = parseInt(document.getElementById('compraCantidad').value);
        const precio_unitario = parseFloat(document.getElementById('compraPrecioUnitario').value);
        
        try {
            const result = await eel.crear_compra(id_proveedor, id_producto, cantidad, precio_unitario)();
            
            if (result.success) {
                showNotification(result.message);
                hideCompraForm();
                loadCompras();
                loadProductos(); // Actualizar stock de productos
            } else {
                showNotification(result.message, 'error');
            }
        } catch (error) {
            showNotification('Error al registrar compra', 'error');
        }
    });
    
    // Cerrar modal al hacer clic fuera
    document.getElementById('confirmModal').addEventListener('click', function(e) {
        if (e.target === this) {
            hideConfirmModal();
        }
    });
});