# 📋 INSTRUCCIONES PARA IMPORTAR EN POSTMAN

## 🚀 **PASO A PASO PARA IMPORTAR LA COLECCIÓN**

### **1. Importar la Colección**
1. Abre **Postman**
2. Haz clic en **"Import"** (botón en la esquina superior izquierda)
3. Selecciona **"Upload Files"**
4. Busca y selecciona el archivo: `Backend-Optimizacion-Postman-Collection.json`
5. Haz clic en **"Import"**

### **2. Configurar Variables de Entorno**
1. En Postman, ve a **"Environments"** (esquina superior izquierda)
2. Crea un nuevo environment llamado **"Backend-Optimizacion"**
3. Agrega estas variables:

```
base_url: http://localhost:8000
access_token: (se llena automáticamente)
access_token_clinica_a: (se llena automáticamente)
access_token_clinica_b: (se llena automáticamente)
access_token_admin: (se llena automáticamente)
```

### **3. Seleccionar el Environment**
1. En la esquina superior derecha, selecciona **"Backend-Optimizacion"** como environment activo

## 🎯 **NUEVOS ENDPOINTS AGREGADOS**

### **👤 Gestión de Usuarios**
- ✅ **DELETE** `users/me/delete/` - Eliminar usuario (soft delete)

### **📋 Historiales**
- ✅ **PUT/PATCH** `histories/<id>/update/` - Actualizar historial

### **⚙️ Configuraciones (NUEVA SECCIÓN)**
- ✅ **GET** `document_types/` - Listar tipos de documento
- ✅ **POST** `document_types/create/` - Crear tipo de documento
- ✅ **PATCH** `document_types/<id>/edit/` - Actualizar tipo de documento
- ✅ **DELETE** `document_types/<id>/delete/` - Eliminar tipo de documento

- ✅ **GET** `payment_types/` - Listar tipos de pago
- ✅ **POST** `payment_types/create/` - Crear tipo de pago
- ✅ **PATCH** `payment_types/<id>/edit/` - Actualizar tipo de pago
- ✅ **DELETE** `payment_types/<id>/delete/` - Eliminar tipo de pago

- ✅ **GET** `predetermined_prices/` - Listar precios predeterminados
- ✅ **POST** `predetermined_prices/create/` - Crear precio predeterminado
- ✅ **PUT/PATCH** `predetermined_prices/<id>/update/` - Actualizar precio
- ✅ **DELETE** `predetermined_prices/<id>/delete/` - Eliminar precio

## 🧪 **CÓMO PROBAR EL MULTI-TENANCY**

### **Paso 1: Login con diferentes usuarios**
1. Ejecuta **"Login Clínica A"** → Se guarda `access_token_clinica_a`
2. Ejecuta **"Login Clínica B"** → Se guarda `access_token_clinica_b`
3. Ejecuta **"Login Admin Principal"** → Se guarda `access_token_admin`

### **Paso 2: Probar filtrado**
1. Ejecuta **"Pacientes - Clínica A"** → Solo verás pacientes de Clínica A
2. Ejecuta **"Pacientes - Clínica B"** → Solo verás pacientes de Clínica B
3. Ejecuta **"Pacientes - Admin (ve todo)"** → Verás pacientes de ambas clínicas

## 📝 **NOTAS IMPORTANTES**

1. **Cambia las contraseñas**: En los endpoints de login, cambia `"tu_password"` por las contraseñas reales
2. **Verifica la URL**: Si tu servidor corre en otro puerto, cambia `base_url` en las variables de entorno
3. **Tokens automáticos**: Los tokens se guardan automáticamente, no necesitas copiarlos manualmente
4. **Multi-tenancy**: Usa los endpoints de la sección "🧪 Pruebas Multi-Tenancy" para verificar que el filtrado funciona

## 🎉 **¡LISTO!**

Ya tienes todos los endpoints para probar tu API en Postman, incluyendo los nuevos métodos DELETE, PUT y PATCH que agregamos.
