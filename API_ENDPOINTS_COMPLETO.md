# 🔌 API Endpoints Completo - Backend Reflexo MTV

## 🌐 Base URL
```
http://localhost:8000/  # Desarrollo local
```

## 📋 Estándar de URLs Unificado
Todas las APIs siguen el patrón: `/api/[modulo]/[recurso]/`

---

## 🏗️ Módulo 1: Arquitectura y Autenticación (`/api/architect/`)

### Autenticación
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------| 
| **POST** | `/api/architect/auth/login/` | Login de usuario | No requerida |
| **POST** | `/api/architect/auth/register/` | Registro de usuario | No requerida |
| **GET** | `/api/architect/users/` | Listar Usuarios | Requerida |
| **POST** | `/api/architect/users/` | Crear Usuarios | Requerida |
| **GET** | `/api/architect/roles/` | Listar Roles | Requerida |
| **GET** | `/api/architect/roles/id/` | Detalle Rol Especifico | Requerida |
| **POST** | `/api/architect/roles/create/` | Crear Roles | Requerida |
| **PUT** | `/api/architect/roles/id/edit/` | Editar Rol | Requerida |
| **DELETE** | `/api/architect/roles/id/delete/` | Eliminar Rol | Requerida |


#### Ejemplos de Autenticación

**Login de Usuario:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/architect/auth/login/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "email": "prueba2@gmail.com",
    "password": "prueba2//"
  }
  ```

**Respuesta:**
```json
{
  "email": "prueba2@gmail.com",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1NzM0MTIzMywiaWF0IjoxNzU3MjU0ODMzLCJqdGkiOiI4N2Q4ZmEzN2RkNWQ0M2ZkYjk1ZDE0NDRlYzE2NTM5MCIsInVzZXJfaWQiOjIxfQ.b2ETtvK_9KyXZ24Suo0MOP_8eGSu9DTblSsTA1kngpo",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MjU1MTMzLCJpYXQiOjE3NTcyNTQ4MzMsImp0aSI6ImY5ODg5ZmFiNTk5MTRiNTc5ZWZhMGUwYTAxMmJmMzEyIiwidXNlcl9pZCI6MjF9._gGKvinZzRPAqOrXQv_a_4ibQxXz7ytSEVLAipzf8lk",
  "user_id": 21
}
```

**Registro de Usuario:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/architect/auth/register/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "document_number": "987654300",
    "user_name": "prueba3",
    "email": "prueba3@gmail.com",
    "password": "prueba3//",
    "password_confirm": "prueba3//",
    "phone": "987654300"
  }
  ```

**Respuesta Exitosa:**
```json
{
    "message": "Usuario registrado con éxito"
}
```

**Posibles Errores:**
```json
{
  "password": [
    "Esta contraseña es demasiado común. Elige una contraseña más segura."
  ]
}
```
```json
{
  "password_confirm": [
    "Las contraseñas no coinciden"
  ]
}
```
```json
{
  "email": [
    "Este campo es requerido."
  ],
  "username": [
    "Este campo es requerido."
  ]
}
```

### Usuarios
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| **GET** | `/api/architect/users/` | Listar usuarios | Requerida |
| **POST** | `/api/architect/users/` | Crear usuario | Requerida |

#### Ejemplos de Usuarios

**Listar Usuarios:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/architect/users/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Respuesta:**
```json
[
    {
        "id": 1,
        "user_name": "reflexo",
        "email": "reflexo@gmail.com",
        "phone": null,
        "is_active": true,
        "created_at": "2025-09-04T14:11:58.099045Z",
        "updated_at": "2025-09-05T18:44:50.359736Z"
    },
    {
        "id": 2,
        "user_name": "frontend",
        "email": "frontend@gmail.com",
        "phone": null,
        "is_active": true,
        "created_at": "2025-09-04T16:48:57.833522Z",
        "updated_at": "2025-09-04T16:48:57.833548Z"
    }
]
```

**Crear Usuario:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/architect/users/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "user_name": "prueba4",
    "email": "prueba4@gmail.com",
    "password": "Prueba4//",
    "first_name": "Felipe",
    "last_name": "Castillo",
    "is_staff": true,
    "is_superuser": false
  }
  ```

**Respuesta Exitosa:**
```json
{
    "id": 23,
    "user_name": "prueba4",
    "email": "prueba4@gmail.com",
    "phone": null,
    "is_active": true,
    "created_at": "2025-09-07T14:28:12.534838Z",
    "updated_at": "2025-09-07T14:28:12.534849Z"
}
```

**Posibles Errores:**
```json
{
  "email": [
    "Este campo es requerido."
  ],
  "user_name": [
    "Este campo es requerido."
  ]
}
```
```json
{
  "email": [
    "Ya existe un usuario con este email."
  ]
}
```
```json
{
  "user_name": [
    "Ya existe un usuario con este nombre de usuario."
  ]
}
```

------------------------------------------------------------------------------

**Listar Roles:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/architect/roles/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
```
Content-Type: application/json
```
- **Body (raw JSON):**
  ```json
  **vacio**
  ```

**Respuesta Exitosa:**
```json
[
    {
        "id": 1,
        "name": "prueba2",
        "guard_name": "prueba3",
        "created_at": "2025-09-13T16:52:48.732006Z",
        "updated_at": "2025-09-13T16:55:19.575166Z"
    }
]
```

------------------------------------------------------------------------------

**Crear Rol:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/architect/roles/create/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
```
Content-Type: application/json
```
- **Body (raw JSON):**
  ```json
  {
    "name": "prueba3",
    "guard_name": "prueba4"
  }
  ```

**Respuesta Exitosa:**
```json
{
    "id": 3,
    "name": "prueba3",
    "guard_name": "prueba4",
    "created_at": "2025-09-13T17:04:29.968271Z",
    "updated_at": "2025-09-13T17:04:29.968655Z"
}
```

------------------------------------------------------------------------------

**Actualizar Rol:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/architect/roles/id/edit/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
```
Content-Type: application/json
```
- **Body (raw JSON):**
  ```json
  {
    "name": "prueba5",
    "guard_name": "prueba6"
  }
  ```

**Respuesta Exitosa:**
```json
{
    "id": 3,
    "name": "prueba5",
    "guard_name": "prueba6",
    "created_at": "2025-09-13T17:04:29.968271Z",
    "updated_at": "2025-09-13T17:05:54.742110Z"
}
```

------------------------------------------------------------------------------

**Eliminar Rol:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** DELETE
- **URL:** `{{base_url}}/api/architect/roles/id/delete/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
```
Content-Type: application/json
```
- **Body (raw JSON):**
  ```json
  **vacio**
  ```

**Respuesta Exitosa:**

**204 NO CONTENT**

------------------------------------------------------------------------------

---

## 👤 Módulo 2: Perfiles de Usuarios (`/api/profiles/`)

### Gestión de Usuario
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| **GET** | `/api/profiles/users/me/` | Mi perfil de usuario | Requerida |
| **PUT** | `/api/profiles/users/me/update/` | Actualizar mi perfil | Requerida |
| **POST** | `/api/profiles/users/me/photo/` | Subir foto de perfil | Requerida |
| **GET** | `/api/profiles/users/search/` | Buscar usuarios | Requerida |
| **GET** | `/api/profiles/users/profile/` | Ver mi perfil completo | Requerida |

#### Ejemplos de Perfiles

**Obtener Mi Perfil:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/profiles/users/me/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Respuesta:**
```json
{
    "id": 1,
    "user_name": "reflexo",
    "email": "reflexo@gmail.com",
    "name": "Christhoper",
    "paternal_lastname": "Sosa",
    "maternal_lastname": "Morales",
    "phone": null,
    "document_number": "70529706",
    "profile_photo_url": null,
    "full_name": "Christhoper Sosa Morales"
}
```

**Actualizar Mi Perfil:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/profiles/users/me/update/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "name": "Eduardo",
    "paternal_lastname": "García",
    "maternal_lastname": "Castillo",
    "phone": "+51 902 887 587"
  }
  ```

**Respuesta Exitosa:**
```json
{
    "message": "Información del usuario actualizada exitosamente",
    "user": {
        "id": 1,
        "user_name": "reflexo",
        "email": "reflexo@gmail.com",
        "name": "Eduardo",
        "paternal_lastname": "García",
        "maternal_lastname": "Castillo",
        "phone": "+51 902 887 587",
        "document_number": "70529706",
        "profile_photo_url": null,
        "full_name": "Eduardo García Castillo"
    }
}
```

**Subir Foto de Perfil:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/profiles/users/me/photo/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: multipart/form-data
  ```
- **Body (form-data):**
  ```
  profile_photo: [archivo de imagen]
  ```
  - **Key:** `profile_photo`
  - **Type:** File
  - **Value:** Seleccionar archivo de imagen (JPG, PNG, etc.)

**Respuesta Exitosa:**
```json
{
  "id": 3,
  "username": "edu",
  "email": "xxangelx31@gmail.com"
}
```

**Posibles Errores:**
```json
{
  "profile_photo": [
    "Este campo es requerido."
  ]
}
```
```json
{
  "profile_photo": [
    "Sube un archivo válido. El archivo que subiste está vacío o no es una imagen válida."
  ]
}
```

**Ver Mi Perfil Completo:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/profiles/users/profile/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Respuesta:**
```json
{
    "id": 1,
    "user_name": "reflexo",
    "email": "reflexo@gmail.com",
    "name": "Eduardo",
    "paternal_lastname": "García",
    "maternal_lastname": "Castillo",
    "phone": "+51 902 887 587",
    "document_number": "70529706",
    "profile_photo_url": null,
    "full_name": "Eduardo García Castillo"
}
```

**Buscar Usuarios:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/profiles/users/search/?q=eduardo`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
  **Respuesta:**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "user_name": "reflexo",
            "email": "reflexo@gmail.com",
            "name": "Eduardo",
            "paternal_lastname": "García",
            "maternal_lastname": "Castillo",
            "phone": "+51 902 887 587",
            "document_number": "70529706",
            "profile_photo_url": null,
            "full_name": "Eduardo García Castillo"
        }
    ]
}
```

---

## 🩺 Módulo 3: Pacientes y Diagnósticos (`/api/patients/`)

### Pacientes
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| **GET** | `/api/patients/patients/` | Listar pacientes | Requerida |
| **POST** | `/api/patients/patients/` | Crear paciente | Requerida |
| **GET** | `/api/patients/patients/1/` | Ver paciente específico | Requerida |
| **PUT** | `/api/patients/patients/{id}/` | Actualizar paciente | Requerida |
| **DELETE** | `/api/patients/patients/{id}/` | Eliminar paciente | Requerida |
| **GET** | `/api/patients/patients/search/` | Buscar pacientes | Requerida |

#### Ejemplos de Pacientes

**Listar Pacientes:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/patients/patients/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Respuesta:**
```json
[
    {
        "id": 2,
        "document_number": "70529706",
        "full_name": "Christhoper Smith Sosa Morales",
        "age": 18,
        "sex": "M",
        "phone1": null,
        "email": "cristofersosa159@gmail.com",
        "region_name": "Amazonas",
        "document_type_name": "",
        "created_at": "2025-09-07T14:34:31.685685Z"
    }
]
```

**Crear Paciente:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/patients/patients/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "document_number": "70529706",
    "paternal_lastname": "Sosa",
    "maternal_lastname": "Morales",
    "name": "Christhoper Smith",
    "birth_date": "2006-09-23",
    "sex": "M",
    "primary_phone": "902887587",
    "email": "cristofersosa159@gmail.com",
    "ocupation": "Ingeniero de Sistemas",
    "health_condition": "No tiene problemas de salud",
    "address": "Calle Nueva 123",
    "region_id": 1,
    "province_id": 1,
    "district_id": 1,
    "document_type_id": 1
  }
  ```

**Respuesta Exitosa:**
```json
{
    "id": 2,
    "document_number": "70529706",
    "paternal_lastname": "Sosa",
    "maternal_lastname": "Morales",
    "name": "Christhoper Smith",
    "personal_reference": null,
    "birth_date": "2006-09-23T00:00:00Z",
    "sex": "M",
    "phone1": null,
    "phone2": null,
    "email": "cristofersosa159@gmail.com",
    "ocupation": "Ingeniero de Sistemas",
    "health_condition": "No tiene problemas de salud",
    "address": "Calle Nueva 123",
    "region": {
        "id": 1,
        "name": "Amazonas",
        "country": 180,
        "created_at": "2025-09-04T14:18:19.089982Z",
        "updated_at": "2025-09-04T14:18:19.090014Z",
        "deleted_at": null
    },
    "province": {
        "id": 1,
        "name": "Chachapoyas",
        "region": 1,
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.160170Z",
        "updated_at": "2025-09-04T14:18:19.160189Z",
        "deleted_at": null
    },
    "district": {
        "id": 1,
        "name": "Chachapoyas",
        "province": 1,
        "province_name": "Chachapoyas",
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.849401Z",
        "updated_at": "2025-09-04T14:18:19.849435Z",
        "deleted_at": null
    },
    "document_type": {
        "id": 1,
        "name": "",
        "created_at": "2025-09-04T14:22:53.387296Z",
        "updated_at": "2025-09-04T14:22:53.387343Z",
        "deleted_at": "2025-09-05T17:52:37.224379Z"
    },
    "created_at": "2025-09-07T14:34:31.685685Z",
    "updated_at": "2025-09-07T14:34:31.685696Z",
    "deleted_at": null
}
```

**Ejemplos Adicionales de Datos Únicos:**

**Ejemplo 2:**
```json
  {
    "document_number": "11111111",
    "paternal_lastname": "Pruea2",
    "maternal_lastname": "Pruea2",
    "name": "Pruea2 Pruea2",
    "birth_date": "2000-01-01",
    "sex": "M",
    "primary_phone": "987654321",
    "email": "Pruea2@gmail.com",
    "ocupation": "Ingeniero de Sistemas",
    "health_condition": "No tiene problemas de salud",
    "address": "Calle Nueva 123",
    "region_id": 1,
    "province_id": 1,
    "district_id": 1,
    "document_type_id": 1
  }
```

**Posibles Errores de Validación:**
```json
{
  "document_number": [
    "El número de documento ya está registrado."
  ],
  "email": [
    "El correo electrónico ya está registrado."
  ]
}
```
```json
{
  "document_number": [
    "Este campo es requerido."
  ],
  "name": [
    "Este campo es requerido."
  ],
  "paternal_lastname": [
    "Este campo es requerido."
  ]
}
```
```json
{
  "birth_date": [
    "La fecha de nacimiento no puede ser en el futuro."
  ]
}
```

**Ver Paciente Específico:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/patients/patients/2/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Respuesta:**
```json
{
    "id": 2,
    "document_number": "70529706",
    "paternal_lastname": "Sosa",
    "maternal_lastname": "Morales",
    "name": "Christhoper Smith",
    "personal_reference": null,
    "birth_date": "2006-09-23T00:00:00Z",
    "sex": "M",
    "phone1": null,
    "phone2": null,
    "email": "cristofersosa159@gmail.com",
    "ocupation": "Ingeniero de Sistemas",
    "health_condition": "No tiene problemas de salud",
    "address": "Calle Nueva 123",
    "region": {
        "id": 1,
        "name": "Amazonas",
        "country": 180,
        "created_at": "2025-09-04T14:18:19.089982Z",
        "updated_at": "2025-09-04T14:18:19.090014Z",
        "deleted_at": null
    },
    "province": {
        "id": 1,
        "name": "Chachapoyas",
        "region": 1,
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.160170Z",
        "updated_at": "2025-09-04T14:18:19.160189Z",
        "deleted_at": null
    },
    "district": {
        "id": 1,
        "name": "Chachapoyas",
        "province": 1,
        "province_name": "Chachapoyas",
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.849401Z",
        "updated_at": "2025-09-04T14:18:19.849435Z",
        "deleted_at": null
    },
    "document_type": {
        "id": 1,
        "name": "",
        "created_at": "2025-09-04T14:22:53.387296Z",
        "updated_at": "2025-09-04T14:22:53.387343Z",
        "deleted_at": "2025-09-05T17:52:37.224379Z"
    },
    "created_at": "2025-09-07T14:34:31.685685Z",
    "updated_at": "2025-09-07T14:34:31.685696Z",
    "deleted_at": null
}
```

**Actualizar Paciente:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/patients/patients/1/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "document_number": "11111123",
    "paternal_lastname": "Pruea2",
    "maternal_lastname": "Pruea2",
    "name": "Pruea2 Pruea2",
    "birth_date": "2000-01-01",
    "sex": "M",
    "primary_phone": "987654321",
    "email": "Pruea2@gmail.com",
    "ocupation": "Ingeniero de Sistemas",
    "health_condition": "No tiene problemas de salud",
    "address": "Calle Nueva 123",
    "region_id": 1,
    "province_id": 1,
    "district_id": 1,
    "document_type_id": 1
  }
  ```

**Respuesta Exitosa:**
```json
{
    "id": 2,
    "document_number": "11111123",
    "paternal_lastname": "Pruea2",
    "maternal_lastname": "Pruea2",
    "name": "Pruea2 Pruea2",
    "personal_reference": null,
    "birth_date": "2000-01-01T00:00:00Z",
    "sex": "M",
    "phone1": null,
    "phone2": null,
    "email": "Pruea2@gmail.com",
    "ocupation": "Ingeniero de Sistemas",
    "health_condition": "No tiene problemas de salud",
    "address": "Calle Nueva 123",
    "region": {
        "id": 1,
        "name": "Amazonas",
        "country": 180,
        "created_at": "2025-09-04T14:18:19.089982Z",
        "updated_at": "2025-09-04T14:18:19.090014Z",
        "deleted_at": null
    },
    "province": {
        "id": 1,
        "name": "Chachapoyas",
        "region": 1,
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.160170Z",
        "updated_at": "2025-09-04T14:18:19.160189Z",
        "deleted_at": null
    },
    "district": {
        "id": 1,
        "name": "Chachapoyas",
        "province": 1,
        "province_name": "Chachapoyas",
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.849401Z",
        "updated_at": "2025-09-04T14:18:19.849435Z",
        "deleted_at": null
    },
    "document_type": {
        "id": 1,
        "name": "",
        "created_at": "2025-09-04T14:22:53.387296Z",
        "updated_at": "2025-09-04T14:22:53.387343Z",
        "deleted_at": "2025-09-05T17:52:37.224379Z"
    },
    "created_at": "2025-09-07T14:34:31.685685Z",
    "updated_at": "2025-09-07T14:34:31.685696Z",
    "deleted_at": null
}
```

**Posibles Errores de Actualización:**
```json
{
  "document_number": [
    "El número de documento ya está registrado por otro paciente."
  ]
}
```
```json
{
  "email": [
    "El correo electrónico ya está registrado por otro paciente."
  ]
}
```
```json
{
  "birth_date": [
    "La fecha de nacimiento no puede ser en el futuro."
  ]
}
```

**Buscar Pacientes:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/patients/patients/search/?q=maria`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Eliminar Paciente:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** DELETE
- **URL:** `{{base_url}}/api/patients/patients/1/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Respuesta Exitosa:**
```
Status: 204 No Content
Body: (vacío)
```

**Nota Importante sobre IDs:**
- Reemplaza `{id}` con el número real del ID del paciente
- Ejemplo: Para ver el paciente con ID 2, usa: `/api/patients/patients/2/`
- Para ver el paciente con ID 5, usa: `/api/patients/patients/5/`
- Para actualizar el paciente con ID 3, usa: `/api/patients/patients/3/`
- Para eliminar el paciente con ID 4, usa: `/api/patients/patients/4/`
- **NO uses** `/api/patients/patients/{id}/` literalmente

### Diagnósticos
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| **GET** | `/api/patients/diagnoses/` | Listar diagnósticos | Requerida |
| **POST** | `/api/patients/diagnoses/` | Crear diagnóstico | Requerida |
| **GET** | `/api/patients/diagnoses/{id}/` | Ver diagnóstico específico | Requerida |
| **PUT** | `/api/patients/diagnoses/{id}/` | Actualizar diagnóstico | Requerida |
| **DELETE** | `/api/patients/diagnoses/{id}/` | Eliminar diagnóstico | Requerida |
| **GET** | `/api/patients/diagnoses/search/` | Buscar diagnósticos | Requerida |

#### Ejemplos de Diagnósticos

**Obtener DiagnósticoS:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/patients/diagnoses/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Respuesta Exitosa:**
  ```json
  {
    "count": 2,
    "num_pages": 1,
    "current_page": 1,
    "results": [
        {
            "id": 3,
            "code": "AS122",
            "name": "Prueba1",
            "created_at": "2025-09-07T14:45:35.059687Z"
        },
        {
            "id": 2,
            "code": "AS123",
            "name": "XD",
            "created_at": "2025-09-07T14:44:30.623096Z"
        }
    ]
  }
  ```

**Crear Diagnóstico:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/patients/diagnoses/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "code": "AS122",
    "name": "Prueba1"
  }
  ```

**Respuesta Exitosa:**
```json
{
    "id": 3,
    "code": "AS122",
    "name": "Prueba1",
    "created_at": "2025-09-07T14:45:35.059687Z",
    "updated_at": "2025-09-07T14:45:35.059711Z",
    "deleted_at": null
}
```

**Ejemplos Adicionales de Diagnósticos:**

**Ejemplo 2:**
```json
{
  "code": "D002",
  "name": "Cefalea tensional"
}
```

**Ejemplo 3:**
```json
{
  "code": "D003",
  "name": "Artritis reumatoide"
}
```

**Actualizar Diagnóstico:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/patients/diagnoses/1/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "code": "AS100",
    "name": "Prueba2",
    "created_at": "2025-09-07T14:45:35.059687Z",
    "updated_at": "2025-09-07T14:49:03.283668Z",
    "deleted_at": null
  }
  ```

**Respuesta Exitosa:**
```json
{
    "id": 3,
    "code": "AS100",
    "name": "Prueba2",
    "created_at": "2025-09-07T14:45:35.059687Z",
    "updated_at": "2025-09-07T14:49:18.548643Z",
    "deleted_at": null
}
```

**Posibles Errores de Validación:**
```json
{
  "code": [
    "Este campo es requerido."
  ],
  "name": [
    "Este campo es requerido."
  ]
}
```
```json
{
  "code": [
    "Ya existe un diagnóstico con este código."
  ]
}
```
```json
{
  "code": [
    "El código solo debe contener letras y números."
  ]
}
```
```json
{
  "code": [
    "El código no debe superar los 10 caracteres."
  ]
}
```

**Buscar Diagnósticos:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/patients/diagnoses/search/?q=Prueba2`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Respuesta Exitosa:**
```json
[
    {
        "id": 3,
        "code": "AS100",
        "name": "Prueba2",
        "created_at": "2025-09-07T14:45:35.059687Z",
        "updated_at": "2025-09-07T14:49:18.548643Z",
        "deleted_at": null
    }
]
```

**Posibles Errores:**
```json
{
  "detail": "Se requiere un parámetro de búsqueda."
}
```

**Nota Importante sobre Búsqueda:**
- **Parámetro obligatorio**: `q` (query de búsqueda)
- **Ejemplos de uso**:
  - Buscar por código: `?q=D001`
  - Buscar por nombre: `?q=dolor`
  - Buscar por descripción: `?q=lumbar`
- **NO uses** `/api/patients/diagnoses/search/` sin el parámetro `q`

---

## 👨‍⚕️ Módulo 4: Terapeutas (`/api/therapists/`)

### Terapeutas
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| **GET** | `/api/therapists/therapists/` | Listar terapeutas | Requerida |
| **POST** | `/api/therapists/therapists/` | Crear terapeuta | Requerida |
| **GET** | `/api/therapists/therapists/{id}/` | Ver terapeuta específico | Requerida |
| **PUT** | `/api/therapists/therapists/{id}/` | Actualizar terapeuta | Requerida |
| **PATCH** | `/api/therapists/therapists/{id}/` | Actualizar parcialmente | Requerida |
| **DELETE** | `/api/therapists/therapists/{id}/` | Soft delete terapeuta | Requerida |
| **GET** | `/api/therapists/therapists/inactive/` | Terapeutas inactivos | Requerida |
| **POST** | `/api/therapists/therapists/{id}/restore/` | Restaurar terapeuta | Requerida |

#### Ejemplos de Terapeutas

**Listar Terapeutas:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/therapists/therapists/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
**Respuesta:**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "document_type": {
                "id": 2,
                "name": "DNI",
                "created_at": "2025-09-04T14:23:06.353132Z",
                "updated_at": "2025-09-04T14:23:06.353168Z",
                "deleted_at": null
            },
            "document_number": "87654321",
            "last_name_paternal": "Rodríguez",
            "last_name_maternal": "Martínez",
            "first_name": "Carlos",
            "birth_date": "1988-07-15T00:00:00Z",
            "gender": "M",
            "personal_reference": null,
            "is_active": true,
            "phone": "888888888",
            "email": "carlos@gmail.com",
            "region": {
                "id": 1,
                "name": "Amazonas",
                "country": 180,
                "created_at": "2025-09-04T14:18:19.089982Z",
                "updated_at": "2025-09-04T14:18:19.090014Z",
                "deleted_at": null
            },
            "province": {
                "id": 1,
                "name": "Chachapoyas",
                "region": 1,
                "region_name": "Amazonas",
                "created_at": "2025-09-04T14:18:19.160170Z",
                "updated_at": "2025-09-04T14:18:19.160189Z",
                "deleted_at": null
            },
            "district": {
                "id": 1,
                "name": "Chachapoyas",
                "province": 1,
                "province_name": "Chachapoyas",
                "region_name": "Amazonas",
                "created_at": "2025-09-04T14:18:19.849401Z",
                "updated_at": "2025-09-04T14:18:19.849435Z",
                "deleted_at": null
            },
            "address": "Calle Principal 456",
            "profile_picture": null,
            "created_at": "2025-09-04T14:25:06.253837Z",
            "updated_at": "2025-09-04T14:25:06.253853Z",
            "deleted_at": null
        }
    ]
}
```

**Crear Terapeuta:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/therapists/therapists/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "document_type_id": "1",
    "document_number": "70529706",
    "first_name": "Christhoper",
    "last_name_paternal": "Sosa",
    "last_name_maternal": "Morales",
    "birth_date": "2006-09-23",
    "gender": "M",
    "phone": "902887587",
    "email": "cristofersosa@gmail.com",
    "address": "Calle Principal 456",
    "region_id": 1,
    "province_id": 1,
    "district_id": 1
  }
  ```

  **Respuesta Exitosa:**
```json
{
    "id": 2,
    "document_type": {
        "id": 1,
        "name": "",
        "created_at": "2025-09-04T14:22:53.387296Z",
        "updated_at": "2025-09-04T14:22:53.387343Z",
        "deleted_at": "2025-09-05T17:52:37.224379Z"
    },
    "document_number": "70529706",
    "last_name_paternal": "Sosa",
    "last_name_maternal": "Morales",
    "first_name": "Christhoper",
    "birth_date": "2006-09-23T00:00:00Z",
    "gender": "M",
    "personal_reference": null,
    "is_active": true,
    "phone": "902887587",
    "email": "cristofersosa@gmail.com",
    "region": {
        "id": 1,
        "name": "Amazonas",
        "country": 180,
        "created_at": "2025-09-04T14:18:19.089982Z",
        "updated_at": "2025-09-04T14:18:19.090014Z",
        "deleted_at": null
    },
    "province": {
        "id": 1,
        "name": "Chachapoyas",
        "region": 1,
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.160170Z",
        "updated_at": "2025-09-04T14:18:19.160189Z",
        "deleted_at": null
    },
    "district": {
        "id": 1,
        "name": "Chachapoyas",
        "province": 1,
        "province_name": "Chachapoyas",
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.849401Z",
        "updated_at": "2025-09-04T14:18:19.849435Z",
        "deleted_at": null
    },
    "address": "Calle Principal 456",
    "profile_picture": null,
    "created_at": "2025-09-07T14:53:18.322073Z",
    "updated_at": "2025-09-07T14:53:18.322083Z",
    "deleted_at": null
}
```

**Buscar Terapeutas:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/therapists/therapists/?search=Christhoper`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

      **Respuesta Exitosa:**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "document_type": {
                "id": 1,
                "name": "",
                "created_at": "2025-09-04T14:22:53.387296Z",
                "updated_at": "2025-09-04T14:22:53.387343Z",
                "deleted_at": "2025-09-05T17:52:37.224379Z"
            },
            "document_number": "70529705",
            "last_name_paternal": "Sosa",
            "last_name_maternal": "Morales",
            "first_name": "Christhoper",
            "birth_date": "2006-05-05T00:00:00Z",
            "gender": "M",
            "personal_reference": null,
            "is_active": true,
            "phone": "902887587",
            "email": "cristofersosa@gmail.com",
            "region": {
                "id": 1,
                "name": "Amazonas",
                "country": 180,
                "created_at": "2025-09-04T14:18:19.089982Z",
                "updated_at": "2025-09-04T14:18:19.090014Z",
                "deleted_at": null
            },
            "province": {
                "id": 1,
                "name": "Chachapoyas",
                "region": 1,
                "region_name": "Amazonas",
                "created_at": "2025-09-04T14:18:19.160170Z",
                "updated_at": "2025-09-04T14:18:19.160189Z",
                "deleted_at": null
            },
            "district": {
                "id": 1,
                "name": "Chachapoyas",
                "province": 1,
                "province_name": "Chachapoyas",
                "region_name": "Amazonas",
                "created_at": "2025-09-04T14:18:19.849401Z",
                "updated_at": "2025-09-04T14:18:19.849435Z",
                "deleted_at": null
            },
            "address": "Calle Principal 456",
            "profile_picture": null,
            "created_at": "2025-09-04T14:25:06.253837Z",
            "updated_at": "2025-09-07T14:57:20.881730Z",
            "deleted_at": null
        },
        {
            "id": 2,
            "document_type": {
                "id": 1,
                "name": "",
                "created_at": "2025-09-04T14:22:53.387296Z",
                "updated_at": "2025-09-04T14:22:53.387343Z",
                "deleted_at": "2025-09-05T17:52:37.224379Z"
            },
            "document_number": "70529706",
            "last_name_paternal": "Sosa",
            "last_name_maternal": "Morales",
            "first_name": "Christhoper",
            "birth_date": "2006-09-23T00:00:00Z",
            "gender": "M",
            "personal_reference": null,
            "is_active": true,
            "phone": "902887587",
            "email": "cristofersosa@gmail.com",
            "region": {
                "id": 1,
                "name": "Amazonas",
                "country": 180,
                "created_at": "2025-09-04T14:18:19.089982Z",
                "updated_at": "2025-09-04T14:18:19.090014Z",
                "deleted_at": null
            },
            "province": {
                "id": 1,
                "name": "Chachapoyas",
                "region": 1,
                "region_name": "Amazonas",
                "created_at": "2025-09-04T14:18:19.160170Z",
                "updated_at": "2025-09-04T14:18:19.160189Z",
                "deleted_at": null
            },
            "district": {
                "id": 1,
                "name": "Chachapoyas",
                "province": 1,
                "province_name": "Chachapoyas",
                "region_name": "Amazonas",
                "created_at": "2025-09-04T14:18:19.849401Z",
                "updated_at": "2025-09-04T14:18:19.849435Z",
                "deleted_at": null
            },
            "address": "Calle Principal 456",
            "profile_picture": null,
            "created_at": "2025-09-07T14:53:18.322073Z",
            "updated_at": "2025-09-07T14:53:18.322083Z",
            "deleted_at": null
        }
    ]
}
```

**Filtrar por Región:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/therapists/therapists/?region=1`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

    **Respuesta Exitosa:**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "document_type": {
                "id": 2,
                "name": "DNI",
                "created_at": "2025-09-04T14:23:06.353132Z",
                "updated_at": "2025-09-04T14:23:06.353168Z",
                "deleted_at": null
            },
            "document_number": "87654321",
            "last_name_paternal": "Rodríguez",
            "last_name_maternal": "Martínez",
            "first_name": "Carlos",
            "birth_date": "1988-07-15T00:00:00Z",
            "gender": "M",
            "personal_reference": null,
            "is_active": true,
            "phone": "888888888",
            "email": "carlos@gmail.com",
            "region": {
                "id": 1,
                "name": "Amazonas",
                "country": 180,
                "created_at": "2025-09-04T14:18:19.089982Z",
                "updated_at": "2025-09-04T14:18:19.090014Z",
                "deleted_at": null
            },
            "province": {
                "id": 1,
                "name": "Chachapoyas",
                "region": 1,
                "region_name": "Amazonas",
                "created_at": "2025-09-04T14:18:19.160170Z",
                "updated_at": "2025-09-04T14:18:19.160189Z",
                "deleted_at": null
            },
            "district": {
                "id": 1,
                "name": "Chachapoyas",
                "province": 1,
                "province_name": "Chachapoyas",
                "region_name": "Amazonas",
                "created_at": "2025-09-04T14:18:19.849401Z",
                "updated_at": "2025-09-04T14:18:19.849435Z",
                "deleted_at": null
            },
            "address": "Calle Principal 456",
            "profile_picture": null,
            "created_at": "2025-09-04T14:25:06.253837Z",
            "updated_at": "2025-09-04T14:25:06.253853Z",
            "deleted_at": null
        },
        {
            "id": 2,
            "document_type": {
                "id": 1,
                "name": "",
                "created_at": "2025-09-04T14:22:53.387296Z",
                "updated_at": "2025-09-04T14:22:53.387343Z",
                "deleted_at": "2025-09-05T17:52:37.224379Z"
            },
            "document_number": "70529706",
            "last_name_paternal": "Sosa",
            "last_name_maternal": "Morales",
            "first_name": "Christhoper",
            "birth_date": "2006-09-23T00:00:00Z",
            "gender": "M",
            "personal_reference": null,
            "is_active": true,
            "phone": "902887587",
            "email": "cristofersosa@gmail.com",
            "region": {
                "id": 1,
                "name": "Amazonas",
                "country": 180,
                "created_at": "2025-09-04T14:18:19.089982Z",
                "updated_at": "2025-09-04T14:18:19.090014Z",
                "deleted_at": null
            },
            "province": {
                "id": 1,
                "name": "Chachapoyas",
                "region": 1,
                "region_name": "Amazonas",
                "created_at": "2025-09-04T14:18:19.160170Z",
                "updated_at": "2025-09-04T14:18:19.160189Z",
                "deleted_at": null
            },
            "district": {
                "id": 1,
                "name": "Chachapoyas",
                "province": 1,
                "province_name": "Chachapoyas",
                "region_name": "Amazonas",
                "created_at": "2025-09-04T14:18:19.849401Z",
                "updated_at": "2025-09-04T14:18:19.849435Z",
                "deleted_at": null
            },
            "address": "Calle Principal 456",
            "profile_picture": null,
            "created_at": "2025-09-07T14:53:18.322073Z",
            "updated_at": "2025-09-07T14:53:18.322083Z",
            "deleted_at": null
        }
    ]
}
```

**Actualizar Terapeuta:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/therapists/therapists/1/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "document_type_id": "1",
    "document_number": "70529705",
    "first_name": "Christhoper",
    "last_name_paternal": "Sosa",
    "last_name_maternal": "Morales",
    "birth_date": "2006-05-05",
    "gender": "M",
    "phone": "902887587",
    "email": "cristofersosa@gmail.com",
    "address": "Calle Principal 456",
    "region_id": 1,
    "province_id": 1,
    "district_id": 1
  }
  ```

**Respuesta Exitosa:**
```json
{
    "id": 1,
    "document_type": {
        "id": 1,
        "name": "",
        "created_at": "2025-09-04T14:22:53.387296Z",
        "updated_at": "2025-09-04T14:22:53.387343Z",
        "deleted_at": "2025-09-05T17:52:37.224379Z"
    },
    "document_number": "70529705",
    "last_name_paternal": "Sosa",
    "last_name_maternal": "Morales",
    "first_name": "Christhoper",
    "birth_date": "2006-05-05T00:00:00Z",
    "gender": "M",
    "personal_reference": null,
    "is_active": true,
    "phone": "902887587",
    "email": "cristofersosa@gmail.com",
    "region": {
        "id": 1,
        "name": "Amazonas",
        "country": 180,
        "created_at": "2025-09-04T14:18:19.089982Z",
        "updated_at": "2025-09-04T14:18:19.090014Z",
        "deleted_at": null
    },
    "province": {
        "id": 1,
        "name": "Chachapoyas",
        "region": 1,
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.160170Z",
        "updated_at": "2025-09-04T14:18:19.160189Z",
        "deleted_at": null
    },
    "district": {
        "id": 1,
        "name": "Chachapoyas",
        "province": 1,
        "province_name": "Chachapoyas",
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.849401Z",
        "updated_at": "2025-09-04T14:18:19.849435Z",
        "deleted_at": null
    },
    "address": "Calle Principal 456",
    "profile_picture": null,
    "created_at": "2025-09-04T14:25:06.253837Z",
    "updated_at": "2025-09-07T14:57:20.881730Z",
    "deleted_at": null
}
```

**Posibles Errores de Actualización:**
```json
{
  "document_number": [
    "Ya existe un terapeuta con este número de documento."
  ]
}
```json
{
  "document_tyoe_id": [
    "El tipo de documento seleccionado no existe."
  ]
}
```json
{
  "email": [
    "Ya existe un terapeuta con este email."
  ]
}
```
```json
{
  "birth_date": [
    "La fecha de nacimiento no puede ser en el futuro."
  ]
}
```

**Restaurar Terapeuta:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/therapists/therapists/1/restore/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {}
  ```

**Respuesta Exitosa:**
```json
{
    "id": 3,
    "document_type": {
        "id": 1,
        "name": "",
        "created_at": "2025-09-04T14:22:53.387296Z",
        "updated_at": "2025-09-04T14:22:53.387343Z",
        "deleted_at": "2025-09-05T17:52:37.224379Z"
    },
    "document_number": "70239706",
    "last_name_paternal": "Soaasa",
    "last_name_maternal": "Moraaales",
    "first_name": "Christhopeer",
    "birth_date": "2006-09-13T00:00:00Z",
    "gender": "M",
    "personal_reference": null,
    "is_active": true,
    "phone": "902237587",
    "email": "cristosa@gmail.com",
    "region": {
        "id": 1,
        "name": "Amazonas",
        "country": 180,
        "created_at": "2025-09-04T14:18:19.089982Z",
        "updated_at": "2025-09-04T14:18:19.090014Z",
        "deleted_at": null
    },
    "province": {
        "id": 1,
        "name": "Chachapoyas",
        "region": 1,
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.160170Z",
        "updated_at": "2025-09-04T14:18:19.160189Z",
        "deleted_at": null
    },
    "district": {
        "id": 1,
        "name": "Chachapoyas",
        "province": 1,
        "province_name": "Chachapoyas",
        "region_name": "Amazonas",
        "created_at": "2025-09-04T14:18:19.849401Z",
        "updated_at": "2025-09-04T14:18:19.849435Z",
        "deleted_at": null
    },
    "address": "Calle Principal 456",
    "profile_picture": null,
    "created_at": "2025-09-07T16:28:00.727649Z",
    "updated_at": "2025-09-07T17:05:17.725649Z",
    "deleted_at": null
}
```

**Posibles Errores:**

```json
{
  "detail": "Terapeuta no encontrado."
}
```

**Nota Importante sobre Restauración:**
- **Solo funciona** con terapeutas que han sido eliminados (soft delete)
- **No requiere datos** en el body, solo el ID en la URL
- **Cambia `is_active`** de `false` a `true`
- **Mantiene** todos los datos originales del terapeuta

## 📅 Módulo 5: Citas y Estados (`/api/appointments/`)

### Estados de Citas
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| **GET** | `/api/appointments/appointment-statuses/` | Listar estados | Requerida |
| **POST** | `/api/appointments/appointment-statuses/` | Crear estado | Requerida |
| **GET** | `/api/appointments/appointment-statuses/{id}/` | Ver estado específico | Requerida |
| **PUT** | `/api/appointments/appointment-statuses/{id}/` | Actualizar estado | Requerida |
| **DELETE** | `/api/appointments/appointment-statuses/{id}/` | Eliminar estado | Requerida |

#### Ejemplos de Estados de Citas

**Listar Estados de Citas:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/appointments/appointment-statuses/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Respuesta:**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "name": "En espera",
            "description": "En espera",
            "created_at": "2025-09-04T19:42:06.608348Z",
            "updated_at": "2025-09-04T19:42:06.608375Z",
            "deleted_at": null
        },
        {
            "id": 1,
            "name": "En Proceso",
            "description": "Cita en proceso de atención",
            "created_at": "2025-09-04T15:14:20.142404Z",
            "updated_at": "2025-09-04T15:14:20.142436Z",
            "deleted_at": null
        }
    ]
}
```

**Crear Nuevo Estado:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/appointments/appointment-statuses/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "name": "Completada",
    "description": "La cita fue atendida"
  }
  ```

  **Respuesta Exitosa**
    ```json
  {
    "id": 5,
    "name": "Completada",
    "description": "La cita fue atendida",
    "created_at": "2025-09-07T15:03:43.955258Z",
    "updated_at": "2025-09-07T15:03:43.955284Z",
    "deleted_at": null
  }
  ```

**Actualizar Estado de Cita:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/appointments/appointment-statuses/1/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "name": "Completadaa",
    "description": "La cita fue atendida exitosamente"
  }
  ```

**Respuesta Exitosa:**
```json
{
    "id": 1,
    "name": "Completadaa",
    "description": "La cita fue atendida exitosamente",
    "created_at": "2025-09-04T15:14:20.142404Z",
    "updated_at": "2025-09-07T15:06:03.357937Z",
    "deleted_at": null
}
```

**Posibles Errores de Actualización:**
```json
{
  "name": [
    "Este campo es requerido."
  ]
}
```
```json
{
  "name": [
    "Ya existe un estado con este nombre."
  ]
}
```
```json
{
  "description": [
    "La descripción no puede estar vacía."
  ]
}
```

### Citas
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| **GET** | `/api/appointments/appointments/` | Listar citas | Requerida |
| **POST** | `/api/appointments/appointments/` | Crear cita | Requerida |
| **GET** | `/api/appointments/appointments/{id}/` | Ver cita específica | Requerida |
| **PUT** | `/api/appointments/appointments/{id}/` | Actualizar cita | Requerida |
| **DELETE** | `/api/appointments/appointments/{id}/` | Eliminar cita | Requerida |
| **GET** | `/api/appointments/appointments/completed/` | Citas completadas | Requerida |
| **GET** | `/api/appointments/appointments/pending/` | Citas pendientes | Requerida |
| **GET** | `/api/appointments/appointments/by_date_range/` | Citas por rango de fechas | Requerida |

#### Ejemplos de Citas

**Crear Cita:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/appointments/appointments/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
  "history": 3,
  "patient": 3,
  "therapist": 1,
  "appointment_date": "2025-09-10",
  "hour": "14:38:00",
  "appointment_type": 2,
  "room": 1,
  "social_benefit": true
  }

  ```

**Respuesta Exitosa:**
```json
{
    "id": 1,
    "history": 3,
    "patient": 3,
    "patient_name": "Pruea3 Pruea3 Pruea3 Pruea3",
    "therapist": 1,
    "therapist_name": "Christhoper Sosa Morales",
    "appointment_date": "2025-09-10T00:00:00Z",
    "hour": "14:38:00",
    "ailments": null,
    "diagnosis": null,
    "surgeries": null,
    "reflexology_diagnostics": null,
    "medications": null,
    "observation": null,
    "initial_date": null,
    "final_date": null,
    "appointment_type": "2",
    "room": 1,
    "social_benefit": true,
    "payment_detail": null,
    "payment": null,
    "payment_type": null,
    "payment_type_name": null,
    "payment_status": null,
    "payment_status_name": null,
    "ticket_number": null,
    "appointment_status": "PENDIENTE",
    "is_completed": false,
    "is_pending": true,
    "created_at": "2025-09-07T15:52:01.780503Z",
    "updated_at": "2025-09-07T15:52:01.780515Z",
    "deleted_at": null
}
```

**Posibles Errores de Validación:**
```json
{
  "patient": [
    "This field is required."
  ],
  "therapist": [
    "This field is required."
  ]
}
```

**❌ NO existe un estado con ID: 1**
```json
{
  "appointment_date": [
    "La fecha de la cita no puede ser en el pasado."
  ]
}
```
```json
{
  "appointment_hour": [
    "La hora de la cita no es válida."
  ]
}
```
```json
{
  "patient": [
    "El paciente seleccionado no existe."
  ]
}
```
```json
{
  "therapist": [
    "El terapeuta seleccionado no existe."
  ]
}
```

**Actualizar Cita Específica:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/appointments/appointments/1/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
  "appointment_date": "2025-09-10",
  "hour": "14:38:00",
  "appointment_type": 2,
  "room": 2,
  "social_benefit": true
  }

  ```

**Respuesta Exitosa:**
```json
{
    "message": "Cita actualizada exitosamente",
    "appointment": {
        "id": 1,
        "history": 3,
        "patient": 3,
        "patient_name": "Pruea3 Pruea3 Pruea3 Pruea3",
        "therapist": 1,
        "therapist_name": "Christhoper Sosa Morales",
        "appointment_date": "2025-09-10",
        "hour": "14:38:00",
        "ailments": null,
        "diagnosis": null,
        "surgeries": null,
        "reflexology_diagnostics": null,
        "medications": null,
        "observation": null,
        "initial_date": null,
        "final_date": null,
        "appointment_type": "2",
        "room": 2,
        "social_benefit": true,
        "payment_detail": null,
        "payment": null,
        "payment_type": null,
        "payment_type_name": null,
        "payment_status": null,
        "payment_status_name": null,
        "ticket_number": "TKT-001",
        "appointment_status": "PENDIENTE",
        "created_at": "2025-09-07T15:52:01.780503Z",
        "updated_at": "2025-09-07T15:55:49.788400Z",
        "deleted_at": null
    }
}
```

**Posibles Errores de Actualización:**
```json
{
  "patient": [
    "El paciente seleccionado no existe."
  ]
}
```
```json
{
  "therapist": [
    "El terapeuta seleccionado no existe."
  ]
}
```
```json
{
  "appointment_status": [
    "Invalid pk \"1\" - object does not exist."
  ]
}
```
```json
{
  "appointment_date": [
    "La fecha de la cita no puede ser en el pasado."
  ]
}
```

**Filtrar Citas por Fecha:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/appointments/appointments/?appointment_date=2025-09-10`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Obtener Citas Completadas:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/appointments/appointments/completed/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Citas por Rango de Fechas:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/appointments/appointments/by_date_range/?start_date=2025-08-20&end_date=2025-09-10`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Respuesta Exitosa:**
```json
{
    "count": 1,
    "results": [
        {
            "id": 1,
            "history": 3,
            "patient": 3,
            "patient_name": "Pruea3 Pruea3 Pruea3 Pruea3",
            "therapist": 1,
            "therapist_name": "Christhoper Sosa Morales",
            "appointment_date": "2025-09-10T00:00:00Z",
            "hour": "14:38:00",
            "ailments": null,
            "diagnosis": null,
            "surgeries": null,
            "reflexology_diagnostics": null,
            "medications": null,
            "observation": null,
            "initial_date": null,
            "final_date": null,
            "appointment_type": "2",
            "room": 2,
            "social_benefit": true,
            "payment_detail": null,
            "payment": null,
            "payment_type": null,
            "payment_type_name": null,
            "payment_status": null,
            "payment_status_name": null,
            "ticket_number": "TKT-001",
            "appointment_status": "PENDIENTE",
            "is_completed": false,
            "is_pending": true,
            "created_at": "2025-09-07T15:52:01.780503Z",
            "updated_at": "2025-09-07T15:55:49.788400Z",
            "deleted_at": null
        }
    ]
}
```

**Posibles Errores:**
```json
{
  "error": "Se requieren start_date y end_date"
}
```
```json
{
  "error": "El formato de fecha debe ser YYYY-MM-DD"
}
```
```json
{
  "error": "start_date no puede ser mayor que end_date"
}
```

**Nota Importante sobre Rango de Fechas:**
- **Parámetros obligatorios**: `start_date` y `end_date` en la URL
- **Formato de fecha**: YYYY-MM-DD (ejemplo: 2025-08-20)
- **Ejemplos de uso**:
  - Rango de una semana: `?start_date=2025-08-20&end_date=2025-08-27`
  - Rango de un mes: `?start_date=2025-08-01&end_date=2025-08-31`
  - Rango de un día: `?start_date=2025-08-25&end_date=2025-08-25`
- **NO uses** `/api/appointments/appointments/by_date_range/` sin los parámetros

### Tickets
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| **GET** | `/api/appointments/tickets/` | Listar tickets | Requerida |
| **GET** | `/api/appointments/tickets/{id}/` | Ver ticket específico | Requerida |
| **PUT** | `/api/appointments/tickets/{id}/` | Actualizar ticket | Requerida |
| **DELETE** | `/api/appointments/tickets/{id}/` | Eliminar ticket | Requerida |
| **GET** | `/api/appointments/tickets/paid/` | Tickets pagados | Requerida |
| **GET** | `/api/appointments/tickets/pending/` | Tickets pendientes | Requerida |
| **GET** | `/api/appointments/tickets/cancelled/` | Tickets cancelados | Requerida |
| **POST** | `/api/appointments/tickets/{id}/mark_as_paid/` | Marcar como pagado | Requerida |
| **POST** | `/api/appointments/tickets/{id}/mark_as_cancelled/` | Marcar como cancelado | Requerida |

#### Ejemplos de Tickets

**📋 Ejemplo Completo - Crear Cita y Ticket:**

**Paso 1: Crear Cita**
- **Base URL:** `http://178.156.204.38/`
```json
POST {{base_url}}/api/appointments/appointments/
  {
  "history": 3,
  "patient": 3,
  "therapist": 1,
  "appointment_date": "2025-09-10",
  "hour": "14:38:00",
  "appointment_type": 2,
  "room": 1,
  "social_benefit": true
  }
```

**Respuesta de Cita Creada:**
```json
{
    "id": 1,
    "history": 3,
    "patient": 3,
    "patient_name": "Pruea3 Pruea3 Pruea3 Pruea3",
    "therapist": 1,
    "therapist_name": "Christhoper Sosa Morales",
    "appointment_date": "2025-09-10T00:00:00Z",
    "hour": "14:38:00",
    "ailments": null,
    "diagnosis": null,
    "surgeries": null,
    "reflexology_diagnostics": null,
    "medications": null,
    "observation": null,
    "initial_date": null,
    "final_date": null,
    "appointment_type": "2",
    "room": 1,
    "social_benefit": true,
    "payment_detail": null,
    "payment": null,
    "payment_type": null,
    "payment_type_name": null,
    "payment_status": null,
    "payment_status_name": null,
    "ticket_number": null,
    "appointment_status": "PENDIENTE",
    "is_completed": false,
    "is_pending": true,
    "created_at": "2025-09-07T15:52:01.780503Z",
    "updated_at": "2025-09-07T15:52:01.780515Z",
    "deleted_at": null
}
```

**NOTA IMPORTANTE:**
- **Al crear una cita, se crea automaticamente su ticket**

**Posibles Errores de Validación:**
```json
{
  "appointment": [
    "This field is required."
  ]
}
```
```json
{
  "ticket_number": [
    "Este campo es requerido."
  ],
  "amount": [
    "Este campo es requerido."
  ]
}
```
```json
{
  "appointment": [
    "Invalid pk \"999\" - object does not exist."
  ]
}
```
```json
{
  "ticket_number": [
    "Ya existe un ticket con este número."
  ]
}
```
```json
{
  "amount": [
    "El monto debe ser mayor a 0."
  ]
}
```
```json
{
  "payment_method": [
    "Método de pago no válido."
  ]
}
```
```json
{
  "status": [
    "Estado no válido. Opciones: pending, paid, cancelled"
  ]
}
```

**Nota Importante sobre Tickets:**
- **`appointment`**: ID de la cita (no `appointment_id`)
- **`ticket_number`**: Número único del ticket
- **`amount`**: Monto en decimal (ejemplo: 150.00)
- **`payment_method`**: Método de pago (Efectivo, Tarjeta, Transferencia, etc.)
- **`status`**: Estado del ticket (pending, paid, cancelled)
- **`description`**: Descripción opcional del servicio

**⚠️ IMPORTANTE - Crear Cita Primero:**
**DEBES crear una cita primero**. Los IDs disponibles son:
- **Pacientes**: ID 3
- **Terapeutas**: ID 1
- **Estados de cita**: **DEFAULT**

**Pasos para crear un ticket:**
1. **Crear cita**: POST `/api/appointments/appointments/` con datos válidos y automaticamentee se crea su ticket

**Marcar Ticket como Pagado:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/appointments/tickets/1/mark_as_paid/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {}
  ```

**Respuesta Exitosa:**
```json
{
    "message": "Ticket marcado como pagado exitosamente",
    "ticket": {
        "id": 1,
        "appointment": 1,
        "appointment_details": "Cita 1 - 2025-09-10 00:00:00+00:00 14:38:00",
        "ticket_number": "TKT-001",
        "payment_date": "2025-09-07T15:52:01.785981Z",
        "amount": "0.00",
        "payment_method": "efectivo",
        "description": "Ticket generado automáticamente para cita #1",
        "status": "paid",
        "is_paid": true,
        "is_pending": false,
        "created_at": "2025-09-07T15:52:01.786036Z",
        "updated_at": "2025-09-07T16:05:22.856706Z",
        "deleted_at": null
    }
}
```

**Posibles Errores:**
```json
{
  "detail": "No Ticket matches the given query."
}
```
```json
{
  "detail": "El ticket ya está pagado."
}
```
```json
{
  "detail": "No se puede marcar como pagado un ticket cancelado."
}
```

**Nota Importante sobre Marcar como Pagado:**
- **Solo funciona** con tickets que están en estado `pending`
- **No requiere datos** en el body, solo el ID en la URL
- **Cambia `status`** de `pending` a `paid`
- **Actualiza `payment_date`** automáticamente con la fecha y hora actual
- **Mantiene** todos los demás datos del ticket

**⚠️ IMPORTANTE - Crear Ticket Primero:**
Antes de marcar un ticket como pagado, **DEBES crear una cita primero**. Los pasos son:
1. **Crear cita**: POST `/api/appointments/appointments/` con datos válidos
2. **Marcar como pagado**: POST `/api/appointments/tickets/{id}/mark_as_paid/` usando el ID del ticket creado

**Actualizar Ticket Específico:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/appointments/tickets/1/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "amount": 180.00,
    "status": "paid"
  }
  ```

**Respuesta Exitosa:**
```json
{
    "message": "Ticket actualizado exitosamente",
    "ticket": {
        "id": 1,
        "appointment": 1,
        "appointment_details": "Cita 1 - 2025-09-10 00:00:00+00:00 14:38:00",
        "ticket_number": "TKT-001",
        "payment_date": "2025-09-07T15:52:01.785981Z",
        "amount": "180.00",
        "payment_method": "efectivo",
        "description": "Ticket generado automáticamente para cita #1",
        "status": "paid",
        "is_paid": true,
        "is_pending": false,
        "created_at": "2025-09-07T15:52:01.786036Z",
        "updated_at": "2025-09-07T16:07:50.757060Z",
        "deleted_at": null
    }
}
```

**Posibles Errores de Actualización:**
```json
{
  "appointment": [
    "Invalid pk \"999\" - object does not exist."
  ]
}
```
```json
{
  "ticket_number": [
    "Ya existe un ticket con este número."
  ]
}
```
```json
{
  "amount": [
    "El monto debe ser mayor a 0."
  ]
}
```
```json
{
  "payment_method": [
    "Método de pago no válido."
  ]
}
```
```json
{
  "status": [
    "Estado no válido. Opciones: pending, paid, cancelled"
  ]
}
```

**Nota Importante sobre Actualización de Tickets:**
- **`amount`**: Monto en decimal (debe ser mayor a 0)
- **`payment_method`**: Método de pago válido
- **`status`**: Estado válido (pending, paid, cancelled)

**Filtrar Tickets por Estado:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/appointments/tickets/?status=paid`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

---

## ⚙️ Módulo 6: Historiales y Configuraciones (`/api/configurations/`)

### Historiales
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| **GET** | `/api/configurations/histories/` | Listar historiales | Requerida |
| **POST** | `/api/configurations/histories/create/` | Crear historial | Requerida |
| **POST** | `/api/configurations/histories/{id}/delete/` | Eliminar historial | Requerida |
| **GET** | `/api/configurations/document_types/` | Listar Tipos de Documentos | Requerida |
| **POST** | `/api/configurations/document_types/create/` | Crear Tipo de Documento | Requerida |
| **DELETE** | `/api/configurations/document_types/id/delete/` | Eliminar Tipo de Documento | Requerida |
| **GET** | `/api/configurations/payment_types/` | Listar Tipos de Pagos | Requerida |
| **POST** | `/api/configurations/payment_types/create/` | Crear Tipo de Pago | Requerida |
| **PUT** | `/api/configurations/payment_types/id/edit/` | Actualizar Tipo de Pago | Requerida |
| **DELETE** | `/api/configurations/payment_types/id/delete/` | Eliminar Tipo de Pago | Requerida |
| **GET** | `/api/configurations/predetermined_prices/` | Listar Precios Predeterminados | Requerida |
| **POST** | `/api/configurations/predetermined_prices/create/` | Crear Precio Predeterminado | Requerida |
| **PUT** | `/api/configurations/predetermined_prices/id/edit/` | Actualizar Precio Predeterminado | Requerida |
| **DELETE** | `/api/configurations/predetermined_prices/id/delete/` | Eliminar Precio Predeterminado | Requerida |


#### Ejemplos de Historiales

**Crear Historial:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/configurations/histories/create/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "patient": 3,
    "patient_name": "Pruea3 Pruea3 Pruea3"
  }
  ```

**Respuesta Exitosa:**
```json
  {
    "id": 3,
    "patient": 3,
    "patient_name": "Pruea3 Pruea3 Pruea3"
  }
```

**Posibles Errores de Validación:**
```json
{
  "error": "Campos obligatorios faltantes"
}
```
```json
{
  "error": "JSON inválido"
}
```

------------------------------------------------------------------------------

**Eliminar Historial:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/configurations/histories/2/delete/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {}
  ```

**Respuesta Exitosa:**
```json
{
  "status": "deleted"
}
```

**Posibles Errores:**
```json
{
  "error": "No encontrado"
}
```

**Nota Importante sobre Eliminación:**
- **Método POST**: Aunque es una eliminación, usa POST, no DELETE
- **Soft Delete**: Marca el historial como eliminado (`deleted_at = now()`) pero no lo borra físicamente
- **Body vacío**: No requiere datos en el body, solo el ID en la URL
- **Reutilización**: Después de eliminar, puedes crear un nuevo historial con la misma combinación de documento

---

## 📊 Ejemplos de Respuestas

### Estado de Cita
```json
{
  "id": 3,
  "name": "Completada",
  "description": "Cita completada exitosamente",
  "is_active": true,
  "created_at": "2025-08-21T20:22:27.178462Z",
  "updated_at": "2025-08-21T20:22:27.178462Z"
}
```

### Lista Paginada
```json
{
  "count": 4,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 3,
      "name": "Completada",
      "description": "Cita completada",
      "is_active": true
    }
  ]
}
```

### Error de Autenticación
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### Error de Validación
```json
{
  "name": [
    "Este campo es requerido."
  ],
  "email": [
    "Ingrese una dirección de correo válida."
  ]
}
```

------------------------------------------------------------------------------

**Listar Tipos de Documentos:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/configurations/document_types/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  *vacio*
  ```

**Respuesta Exitosa:**
```json
  {
    "document_types": [
        {
            "id": 2,
            "name": "DNI"
        },
        {
            "id": 20,
            "name": "Prueba4"
        }
    ]
  }
```

------------------------------------------------------------------------------

**Crear Tipo de Documento:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/configurations/document_types/create/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "name": "Prueba4"
  }
  ```

**Respuesta Exitosa:**
```json
  {
    "id": 20,
    "name": "Prueba4"
  }
```

------------------------------------------------------------------------------

**Eliminar Tipo de Documento:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** DELETE
- **URL:** `{{base_url}}/api/configurations/document_types/20/delete/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  **vacio**
  ```

**Respuesta Exitosa:**
```json
  {
    "status": "deleted",
    "id": 20
  }
```

------------------------------------------------------------------------------

**Listar Tipos de Pagos:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/configurations/payment_types/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  **vacio**
  ```

**Respuesta Exitosa:**
```json
  {
    "payment_types": [
        {
            "id": 2,
            "name": "Efectivo"
        },
        {
            "id": 5,
            "name": "Tarjeta"
        }
    ]
  }
```

------------------------------------------------------------------------------

**Crear Tipo de Pago:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/configurations/payment_types/create/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "name": "coimitaaaa"
  }
  ```

**Respuesta Exitosa:**
```json
  {
    "id": 8,
    "name": "coimitaaaa"
  }
```

------------------------------------------------------------------------------

**Editar Tipo de Pago:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/configurations/payment_types/8/edit/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "name": "coimitaaa12"
  }
  ```

**Respuesta Exitosa:**
```json
  {
    "id": 8,
    "name": "coimitaaa12"
  }
```

------------------------------------------------------------------------------

**Eliminar Tipo de Pago:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** DELETE
- **URL:** `{{base_url}}/api/configurations/payment_types/8/delete/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  **vacio**
  ```

**Respuesta Exitosa:**
```json
  {
    "status": "deleted",
    "id": 8
  }
```
------------------------------------------------------------------------------

**Listar Precios predeterminados:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** GET
- **URL:** `{{base_url}}/api/configurations/predetermined_prices/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  **vacio**
  ```

**Respuesta Exitosa:**
```json
  {
    "predetermined_prices": [
        {
            "id": 1,
            "name": "Cupon sin costo",
            "price": "50.00"
        }
    ]
  }
```

------------------------------------------------------------------------------

**Crear Precio predeterminado:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/configurations/predetermined_prices/create/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "name": "coimitaaa",
    "price": 100.00
  }
  ```

**Respuesta Exitosa:**
```json
  {
    "id": 2,
    "name": "coimitaaa",
    "price": 100.00
  }
```

------------------------------------------------------------------------------

**Editar Precio predeterminado:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/configurations/predetermined_prices/2/edit/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  {
    "name": "coimitaaaaaaaaa1222",
    "price": 150.00
  }
  ```

**Respuesta Exitosa:**
```json
  {
    "id": 2,
    "name": "coimitaaaaaaaaa1222",
    "price": "150.0"
  }
```

------------------------------------------------------------------------------

**Editar Precio predeterminado:**
- **Base URL:** `http://178.156.204.38/`
- **Método:** DETELE
- **URL:** `{{base_url}}/api/configurations/predetermined_prices/2/detele/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON):**
  ```json
  **vacio**
  ```

**Respuesta Exitosa:**
```json
  {
    "status": "deleted"
  }
```

------------------------------------------------------------------------------

---
## ⚙️ Módulo 8: Empresa y reportes (`/api/company/`)
### Empresa
|   Método   | Endpoint | Descripción | Autenticación |
|------------|----------|-------------|---------------|
| **GET**    |  `/api/company/company/` | Listar Empresa | Requerida |
| **POST**   |  `/api/company/company/` | Crear Empresa  | Requerida |
| **GET**    | `/api/company/company/{id}/` | Ver empresa específica | Requerida |
| **POST**   | `/api/company/company/{id}/upload_logo/` | Subir Logo | Requerida |
| **DELETE** | `/api/company/company/{id}` | Eliminar Empresa | Requerida |
| **DELETE** | `/api/company/company/{id}/delete_logo/` | Eliminar Logo | Requerida |
| **GET**    | `/api/company/company/{id}/show_logo/` | Mostrar Logo | Requerida |
| **PUT**    | `/api/company/company/{id}/` | Actualizar Nombre y Logo | Requerida |

### Ejemplo de Empresa
**Crear Empresa**
- **Base URL:** `http://178.156.204.38/`
- **Método**:POST
- **URL**: `{{base_url}}/api/company/company/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
-**Headers:**
-**Body (raw):**
```json
{
    "company_name": "prueba12"
}
```

**Respuesta Exitosa:**
```json
{
    "id": 4,
    "company_name": "prueba12",
    "company_logo": null,
    "logo_url": null,
    "has_logo": false,
    "created_at": "2025-09-07T16:14:33.374603Z",
    "updated_at": "2025-09-07T16:14:33.374631Z"
}
```

**Posibles Errores al crear el nombre de la empresa:**
```json
{
    "company_name": [
        "Company Data with this company name already exists."
    ]
}
```

**Nota Importante sobre crear  la empresa**
Al crear una empresa no se tiene que poner el mismo nombre , la idea esa solo usar la unica empresa creada y editarla aunque
se pueda crear más.

------------------------------------------------------------------------------

**Subir Logo**
- **Base URL:** `http://178.156.204.38/`
- **Método:** POST
- **URL:** `{{base_url}}/api/company/company/{id}/upload_logo/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/json
  ```
- **Body (Form-data):**
  |        Key         |       Value        | 
  |--------------------|--------------------|
  | logo       [file]  |  *escoger imagen*  | 
  |-----------------------------------------|

  ```json
  {
    "message": "Logo subido correctamente"
  }
  ```

**Posibles Errores al subir el logo:**

```json
{
    "logo": [
        "Solo se permiten imágenes JPG o PNG."
    ]
}
```

```json
{
    "logo": [
        "El logo no puede superar los 2 MB."
    ]
}
```

```json
{
    "error": "La empresa ya tiene un logo. Use PUT para actualizar."
}
```
**Nota Importante sobre crear  la empresa**
-*Colocar en la parte de key "logo" y seleccionar file, por defecto está text*
-*No subir una imagen de mas de 2mb*
-*Solo se puede subir un logo si la empresa no cuenta con ella, para actualizar se usa put*

-------------------------------------------------------------------------------------------

**Eliminar Empresa**
- **Base URL:** `http://178.156.204.38/`
- **Método**:DELETE
- **URL**: `{{base_url}}/api/company/company/3/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
-**Headers:**
-**Body (raw):**

**Respuesta Exitosa:**
```json
{
    "status": "success",
    "message": "Empresa \"xd\" eliminada correctamente"
}
```
**Posibles Errores al Elimnar empresa**

```json
{
    "status": "error",
    "message": "Empresa no encontrada"
}
```
**Nota Importante sobre eliminar empresa**
-*Colocar el id correcto de la empresa creada*

**Eliminar Logo**
- **Base URL:** `http://178.156.204.38/`
- **Método**:DELETE
- **URL**: `{{base_url}}/api/company/company/{id}/delete_logo`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
-**Headers:**
-**Body (raw):**

**Respuesta Exitosa:**
```json
{
    "message": "Logo eliminado correctamente"
}
```
**Posibles Errores Logo**

```json
{
    "detail": "No CompanyData matches the given query."
}
```
**Nota Importante sobre eliminar empresa**
-*Colocar el id correcto de la empresa creada*

--------------------------------------------------------------

**Actualizar Empresa**
*SOLO ACTUALIZAR EL NOMBRE*
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/company/company/4/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
-**Body (raw):** 

```json
{
    "company_name": "pruebba123"
}
```

**Respuesta Exitosa:**
```json
{
    "id": 4,
    "company_name": "pruebba123",
    "company_logo": null,
    "logo_url": null,
    "has_logo": false,
    "created_at": "2025-09-07T16:14:33.374603Z",
    "updated_at": "2025-09-07T16:18:32.312245Z"
}
```
**ACTUALIZAR NOMBRE Y LOGO**
- **Base URL:** `http://178.156.204.38/`
- **Método:** PUT
- **URL:** `{{base_url}}/api/company/company/{id}/`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
- **Body (Form-data):**
  |        Key           |       Value        | 
  |----------------------|--------------------|
  | company_name  [text] |       reflexo      | 
  |----------------------|--------------------|
  | company_logo  [file] |  *escoger imagen*  |
  |----------------------|--------------------|

**Respuesta Exitosa:**
```json
{
    "id": 1,
    "company_name": "reflexo",
    "company_logo": "reflexo.jpg",
    "logo_url": "http://127.0.0.1:8000/media/logos/oskar-smethurst-B1GtwanCbiw-unsplash_1.jpg",
    "has_logo": true,
    "created_at": "2025-08-24T16:24:25.239714Z",
    "updated_at": "2025-08-24T17:01:41.761879Z"
}
```
**Advertencias**
```json
{
    "warning": "El logo no se actualizó: Formato no permitido. Solo se aceptan: jpg, jpeg, png",
    "id": 1,
    "company_name": "reflexo",
    "company_logo": "reflexo.jpg",
    "logo_url": "http://127.0.0.1:8000/media/logos/oskar-smethurst-B1GtwanCbiw-unsplash_1.jpg",
    "has_logo": true,
    "created_at": "2025-08-24T16:24:25.239714Z",
    "updated_at": "2025-08-24T17:15:02.281286Z"
}
```

```json
{
    "warning": "El logo no se actualizó: El logo excede el tamaño máximo permitido de 2097152 bytes.",
    "id": 1,
    "company_name": "reflexo",
    "company_logo": "reflexo.jpg",
    "logo_url": "http://127.0.0.1:8000/media/logos/oskar-smethurst-B1GtwanCbiw-unsplash_1.jpg",
    "has_logo": true,
    "created_at": "2025-08-24T16:24:25.239714Z",
    "updated_at": "2025-08-24T17:16:38.328992Z"
}
```
**Nota Importante Actualizar Empresa**
-*Hay dos maneras de actualizar una por "raw" solo actualiza el nombre y la otra manera "Form-data" permite ambos el nombre y el logo*
-*La imagen se actualiza solo si es un formtato de imagen permitido o si no pasa los 2mb de lo contrario te da una advertencia y se queda la imagen que ya tenia antes*
-**si pones PATCH en vez de PUT realiza lo mismo**

### Reportes
### Cuando generen la cita pongan payment, payment_type, ,payment_type_name para que se muestre bien los reports:
| Método     | Endpoint                                                                                     | Descripción               | Autenticación |
|--------    |----------------------------------------------------------------------------------------------|-------------              |---------------|
| **GET**    | `/api/company/reports/appointments-per-therapist/?date=2025-08-25`                           | Reporte por terapeuta     | Requerida     |
| **GET**    | `/api/company/reports/daily-cash/?date=2025-08-25`                                           | Caja diaria               | Requerida     |
| **GET**    | `/api/company/reports/patients-by-therapist/?date=2025-08-25`                                | Pacientes por terapeuta   | Requerida     |
| **GET**    | `/api/company/reports/appointments-between-dates/?start_date=2025-08-25&end_date=2025-08-28` | Citas entre fechas        | Requerida     |
| **GET**    | `/api/company/exports/excel/citas-rango/?start_date=2025-08-25&end_date=2025-08-28`          | Generar reporte en excel  | Requerida     |


### Ejemplos de reporte de citas por terapeuta
**Mostrar: "Reporte de cita por terapeuta":**
- **Base URL:** `http://178.156.204.38/`
- **Método: GET** 
- **URL:** `{{base_url}}/api/company/reports/appointments-per-therapist/?date=2025-09-10`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/JSON
  ```
**Respuesta Exitosa:**
```json
{
    "date": "2025-09-10",
    "therapists_appointments": [
        {
            "id": 1,
            "name": "Christhoper Sosa Morales",
            "last_name_paternal": "Sosa",
            "last_name_maternal": "Morales",
            "appointments_count": 1,
            "percentage": 100.0
        }
    ],
    "total_appointments_count": 1
}
```
**Nota Importante sobre Citas por terapeuta:**
- **No hay cita creada**: Se debe crear antes una cita para mostrar un reporte.


### Ejemplos de Reporte diario de caja
**Mostrar: "Reporte de diario de caja":**
- **Base URL:** `http://178.156.204.38/`
- **Método: GET** 
- **URL:** `{{base_url}}/api/company/reports/daily-cash/?date=2025-08-25`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/JSON
  ```
**Respuesta Exitosa:**
```json
[
    {
        "id_cita": 2,
        "payment": "50.00",
        "payment_type": 2,
        "payment_type_name": "Efectivo"
    },
    {
        "id_cita": 1,
        "payment": "100.00",
        "payment_type": 1,
        "payment_type_name": "Yape"
    }
]
```
**Nota Importante sobre Reporte diario de caja:**
- **`payment_type`**: Se debe crear antes generar un reporte diario de caja.

### Ejemplos de Reporte de pacientes por Terapeuta
**Mostrar: "Reporte de paciente por Terapeuta":**
- **Base URL:** `http://178.156.204.38/`
- **Método: GET** 
- **URL:** `{{base_url}}/api/company/reports/patients-by-therapist/?date=2025-09-10`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`
- **Headers:**
  ```
  Content-Type: application/JSON
  ```
**Respuesta Exitosa:**
```json
[
    {
        "therapist_id": "1",
        "therapist": "Sosa Morales Christhoper",
        "patients": [
            {
                "patient_id": 3,
                "patient": "Pruea3 Pruea3 Pruea3 Pruea3",
                "appointments": 1
            }
        ]
    }
]
```
**Nota Importante sobre Reporte de pacientes por Terapeuta:**
- **`therapist`**: Debe estar agregado a una cita.
- **`patient`**: Debe estar agregado a una cita y relacionado con un terapeuta.


### Ejemplos de Reporte de Citas en un rango de fechas
**Mostrar: "Reporte citas entre fechas":**
- **Base URL:** `http://178.156.204.38/`
- **Método: GET** 
- **URL:** `{{base_url}}/api/company/reports/appointments-between-dates/?start_date=2025-08-25&end_date=2025-08-28`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Respuesta Exitosa:**

```json
[
    {
        "appointment_id": 1,
        "patient_id": 3,
        "document_number_patient": "11111333",
        "patient": "Pruea3 Pruea3 Pruea3 Pruea3",
        "phone1_patient": null,
        "appointment_date": "2025-09-10",
        "hour": "14:38"
    }
]
```

**Nota Importante sobre Reporte de pacientes por Terapeuta:**
- **Debe contener lo necesario**: De haber un paciente, una fecha exacta de la cita y también una hora de la cita .
--------------------------------------------------------------

**Mostrar: "Reporte citas entre fechas (EXCEL)":**
- **Base URL:** `http://178.156.204.38/`
- **Método: GET** 
- **URL:** `{{base_url}}http://178.156.204.38/api/company/exports/excel/citas-rango/?start_date=2025-08-25&end_date=2025-09-10`
- **Auth:** 
- **Headers:**

**Probarlo en un navegador**
**Respuesta Exitosa:**
*se genera un excel*

ID Paciente	DNI/Documento	Paciente	      Teléfono	      Fecha	   Hora
1	11111111	García Hernández Ana Sofía	+51 444 444 444	2025-08-25	14:30
1	11111111	García Hernández Ana Sofía	+51 444 444 444	2025-08-25	14:30
1	11111111	García Hernández Ana Sofía	+51 444 444 444	2025-08-25	14:30
1	11111111	García Hernández Ana Sofía	+51 444 444 444	2025-08-25	14:30
1	11111111	García Hernández Ana Sofía	+51 444 444 444	2025-08-25	14:30

**Nota Importante**
-**Usar el endpoint en un navegador ya que si se pone en el postman no se ve de una manera adecuado**


------------------------------------------------------------------------------------------------------------------------

### Estadísticas
| Método     | Endpoint                                                               | Descripción                    | Autenticación |
|--------    |----------------------------------------------------------------------- |--------------------------------|---------------|
| **GET**    | `/api/company/reports/statistics/?start=2025-08-25&end=2025-08-28`     | Mostrar estadísticas de datos  | Requerida     |


### Ejemplos de Estadísticas
**Mostrar: "Estadísticas de datos":**
- **Base URL:** `http://178.156.204.38/`
- **Método: GET** 
- **URL:** `{{base_url}}/api/company/reports/statistics/?start=2025-08-25&end=2025-08-28`
- **Auth:** Basic Auth
  - Username: `reflexo@gmail.com`
  - Password: `Reflexo159//`

**Respuesta Exitosa:**
```json
{
    "terapeutas": [
        {
            "id": 1,
            "terapeuta": "Rodríguez Martínez, Carlos",
            "sesiones": 2,
            "ingresos": 150,
            "raiting": 5
        }
    ],
    "tipos_pago": {
        "Efectivo": 1,
        "Yape": 1
    },
    "metricas": {
        "ttlpacientes": 2,
        "ttlsesiones": 2,
        "ttlganancias": 150
    },
    "ingresos": {
        "Lunes": 150
    },
    "sesiones": {
        "Lunes": 2
    },
    "tipos_pacientes": {
        "c": 0,
        "cc": 0
    }
}
 ```
**Nota Importante sobre Reporte de pacientes por Terapeuta:**
- **Debe existir lo necesario**: Se debe haber ingresado datos como ingresos, citas, cant. de tipo de pacientes, terapeutas, etc.

--------------------------------------------------------------------------------------------

## 🔍 Filtros y Búsquedas

### Filtros Comunes
- `is_active=true/false` - Filtrar por estado activo
- `search=texto` - Búsqueda por texto
- `ordering=field` - Ordenar por campo

### Ejemplos de Filtros
```
GET /api/appointments/appointment-statuses/?is_active=true
GET /api/therapists/therapists/?search=ana
GET /api/patients/patients/?ordering=-created_at
GET /api/appointments/appointments/?appointment_date=2025-08-25
GET /api/therapists/therapists/?region=1&active=true
```

### Combinación de Filtros
```
GET /api/therapists/therapists/?region=1&active=true&search=ana
```

---

## 📝 Notas Importantes

1. **Autenticación**: La mayoría de endpoints requieren autenticación
2. **Paginación**: Los endpoints de listado incluyen paginación automática
3. **Soft Delete**: Algunos recursos usan eliminación lógica
4. **Filtros**: Se pueden combinar múltiples filtros
5. **Búsqueda**: La búsqueda es case-insensitive
6. **Fechas**: Usar formato ISO 8601 (YYYY-MM-DD)
7. **Horas**: Usar formato 24h (HH:MM:SS)