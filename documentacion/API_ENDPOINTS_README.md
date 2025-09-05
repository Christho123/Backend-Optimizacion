# API Endpoints (Postman-Ready)

Base URL: http://localhost:8000/api

Authentication: Most endpoints expect JWT or Session auth if enforced by the view permissions. Unless noted as `AllowAny`, send `Authorization: Bearer <token>` header.

Notes
- Pagination and filtering follow DRF conventions unless otherwise specified.
- For ViewSets registered with routers, detail endpoints use `/<resource>/{id}/`.
- Date formats are ISO-8601 unless noted.

---

## Architect Module
Base: http://localhost:8000/api/architect/

- auth
  - POST http://localhost:8000/api/architect/auth/login/
    
    Body (JSON):
    ```json
    {
      "email": "admin@gmail.com",
      "password": "admin123456"
    }
    ```
    
    Alternativas (otros usuarios):
    ```json
    { "email": "senati@gmail.com", "password": "wilber123456" }
    ```
    ```json
    { "email": "prueba2@gmail.com", "password": "clinica23456" }
    ```

  - POST http://localhost:8000/api/architect/auth/register/
    
    Body (JSON):
    ```json
    {
      "email": "new@example.com",
      "user_name": "newuser",
      "document_number": "12345678",
      "name": "Nombre",
      "paternal_lastname": "ApellidoP",
      "maternal_lastname": "ApellidoM",
      "password": "NewPass#123",
      "password_confirm": "NewPass#123"
    }
    ```
- users
  - GET http://localhost:8000/api/architect/users/
  - POST http://localhost:8000/api/architect/users/
    
    Body (JSON):
    ```json
    {
      "email": "u@example.com",
      "user_name": "userexample",
      "document_number": "87654321",
      "name": "User",
      "paternal_lastname": "Example",
      "maternal_lastname": "Demo",
      "password": "NewPass#123"
    }
    ```
- permissions
  - GET http://localhost:8000/api/architect/permissions/
- roles
  - GET http://localhost:8000/api/architect/roles/

---

## Users Profiles Module
Base: http://localhost:8000/api/profiles/

- users (current user)
  - GET http://localhost:8000/api/profiles/users/me/
  - PUT/PATCH http://localhost:8000/api/profiles/users/me/update/
  - POST http://localhost:8000/api/profiles/users/me/photo/
    
    Opción A (JSON):
    Body (JSON):
    ```json
    {
      "photo_url": "/media/users/photos/profile.jpg"
    }
    ```
    Opción B (multipart/form-data):
    Body (form-data):
    - Key: `photo_file` | Type: File | Value: seleccionar imagen
  - DELETE http://localhost:8000/api/profiles/users/me/photo/
  - GET http://localhost:8000/api/profiles/users/search/?q=test&page=1
    (Parámetros: q=texto_búsqueda, page=número_página)
  - GET http://localhost:8000/api/profiles/users/profile/

- profiles
  - GET http://localhost:8000/api/profiles/profiles/me/
  - POST http://localhost:8000/api/profiles/profiles/create/
    
    Body (JSON):
    ```json
    {
      "name": "Nuevo Usuario",
      "paternal_lastname": "ApellidoP",
      "maternal_lastname": "ApellidoM", 
      "email": "nuevo@example.com",
      "document_number": "87654324",
      "phone": "999999999",
      "sex": "M"
    }
    ```
    
    **NOTA:** Este endpoint crea un NUEVO usuario. Si quieres probarlo, cambia el email y document_number por valores únicos que no existan en la base de datos.
  - GET http://localhost:8000/api/profiles/profiles/public/{user_name}/
  - PATCH http://localhost:8000/api/profiles/profiles/settings/
  - GET http://localhost:8000/api/profiles/profiles/completion/
  - GET http://localhost:8000/api/profiles/profiles/search/?q=test&page=1
    (Parámetros: q=texto_búsqueda, page=número_página)

- password
  - POST http://localhost:8000/api/profiles/password/change/
    
    Body (JSON):
    ```json
    {
      "old_password": "oldpass",
      "new_password": "NewPass#123"
    }
    ```
  - POST http://localhost:8000/api/profiles/password/reset/
    
    Body (JSON):
    ```json
    {
      "email": "user@example.com"
    }
    ```
  - POST http://localhost:8000/api/profiles/password/reset/confirm/
    
    Body (JSON):
    ```json
    {
      "uid": "<uid>",
      "token": "<token>",
      "new_password": "NewPass#123"
    }
    ```
  - POST http://localhost:8000/api/profiles/password/strength/
    
    Body (JSON):
    ```json
    {
      "password": "Candidate#123"
    }
    ```
  - GET http://localhost:8000/api/profiles/password/history/
  - GET http://localhost:8000/api/profiles/password/policy/

- verification
  - POST http://localhost:8000/api/profiles/verification/code/
    
    Body (JSON):
    ```json
    {}
    ```
  - POST http://localhost:8000/api/profiles/verification/email/
    
    Body (JSON):
    ```json
    {
      "email": "user@example.com"
    }
    ```
  - POST http://localhost:8000/api/profiles/verification/email/confirm/
    
    Body (JSON):
    ```json
    {
      "code": "123456"
    }
    ```
  - POST http://localhost:8000/api/profiles/verification/email/change/
    
    Body (JSON):
    ```json
    {
      "new_email": "new@example.com"
    }
    ```
  - POST http://localhost:8000/api/profiles/verification/email/change/confirm/
    
    Body (JSON):
    ```json
    {
      "code": "123456"
    }
    ```
  - POST http://localhost:8000/api/profiles/verification/code/resend/
    
    Body (JSON):
    ```json
    {}
    ```
  - GET http://localhost:8000/api/profiles/verification/status/

Example (Upload profile photo - JSON)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/users/me/photo/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"photo_url":"/media/users/photos/profile.jpg"}'
```
Body (JSON):
```json
{
  "photo_url": "/media/users/photos/profile.jpg"
}
```

Example (Upload profile photo - multipart)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/users/me/photo/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: multipart/form-data' \
  -F 'photo_file=@/path/to/photo.jpg'
```

Example (Create profile)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/profiles/create/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Nuevo Usuario","paternal_lastname":"ApellidoP","maternal_lastname":"ApellidoM","email":"nuevo@example.com","document_number":"87654324","phone":"999999999","sex":"M"}'
```
Body (JSON):
```json
{
  "name": "Nuevo Usuario",
  "paternal_lastname": "ApellidoP",
  "maternal_lastname": "ApellidoM", 
  "email": "nuevo@example.com",
  "document_number": "87654324",
  "phone": "999999999",
  "sex": "M"
}
```

Example (Password reset request)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/password/reset/' \
  -H 'Content-Type: application/json' \
  -d '{"email":"user@example.com"}'
```
Body (JSON):
```json
{
  "email": "user@example.com"
}
```

Example (Verification code request)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/verification/code/' \
  -H 'Authorization: Bearer {{token}}'
```
Body (JSON):
```json
{}
```

Example (Resend verification code)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/verification/code/resend/' \
  -H 'Authorization: Bearer {{token}}'
```
Body (JSON):
```json
{}
```

Example (Email verification request)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/verification/email/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"email":"user@example.com"}'
```
Body (JSON):
```json
{
  "email": "user@example.com"
}
```

Example (Confirm email verification)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/verification/email/confirm/' \
  -H 'Content-Type: application/json' \
  -d '{"code":"123456"}'
```
Body (JSON):
```json
{
  "code": "123456"
}
```

Example (Request email change)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/verification/email/change/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"new_email":"new@example.com"}'
```
Body (JSON):
```json
{
  "new_email": "new@example.com"
}
```

Example (Confirm email change)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/verification/email/change/confirm/' \
  -H 'Content-Type: application/json' \
  -d '{"code":"123456"}'
```
Body (JSON):
```json
{
  "code": "123456"
}
```

Example (Change password)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/password/change/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"old_password":"oldpass","new_password":"NewPass#123"}'
```
Body (JSON):
```json
{
  "old_password": "oldpass",
  "new_password": "NewPass#123"
}
```

Example (Confirm password reset)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/password/reset/confirm/' \
  -H 'Content-Type: application/json' \
  -d '{"uid":"<uid>","token":"<token>","new_password":"NewPass#123"}'
```
Body (JSON):
```json
{
  "uid": "<uid>",
  "token": "<token>",
  "new_password": "NewPass#123"
}
```

Example (Password strength)
```bash
curl -X POST \
  'http://localhost:8000/api/profiles/password/strength/' \
  -H 'Content-Type: application/json' \
  -d '{"password":"Candidate#123"}'
```
Body (JSON):
```json
{
  "password": "Candidate#123"
}
```

---

## Patients & Diagnoses Module
Base: http://localhost:8000/api/patients/

- diagnoses
  - GET http://localhost:8000/api/patients/diagnoses/
  - POST http://localhost:8000/api/patients/diagnoses/
    
    Body (JSON):
    ```json
    {
      "name": "Lumbalgia",
      "code": "DX001"
    }
    ```
  - GET http://localhost:8000/api/patients/diagnoses/{id}/
  - PUT http://localhost:8000/api/patients/diagnoses/{id}/
  - DELETE http://localhost:8000/api/patients/diagnoses/{id}/
  - GET http://localhost:8000/api/patients/diagnoses/search/?q={text}

- patients
  - GET http://localhost:8000/api/patients/patients/?page={n}
  - POST http://localhost:8000/api/patients/patients/
    
    Body (JSON):
    ```json
    {
      "first_name": "John",
      "last_name": "Doe",
      "document_number": "12345678"
    }
    ```
  - GET http://localhost:8000/api/patients/patients/{id}/
  - PUT http://localhost:8000/api/patients/patients/{id}/
  - DELETE http://localhost:8000/api/patients/patients/{id}/
  - GET http://localhost:8000/api/patients/patients/search/?q={text}&page={n}

- medical records
  - GET http://localhost:8000/api/patients/medical-records/
  - POST http://localhost:8000/api/patients/medical-records/
    
    Body (JSON):
    ```json
    {
      "patient": 1,
      "diagnosis": "Lumbalgia",
      "observation": "Notas"
    }
    ```
  - GET http://localhost:8000/api/patients/medical-records/{id}/
  - PUT http://localhost:8000/api/patients/medical-records/{id}/
  - DELETE http://localhost:8000/api/patients/medical-records/{id}/
  - GET http://localhost:8000/api/patients/patients/{patient_id}/medical-history/
  - GET http://localhost:8000/api/patients/diagnosis-statistics/?from=YYYY-MM-DD&to=YYYY-MM-DD

Example (Create patient)
```bash
curl -X POST \
  'http://localhost:8000/api/patients/patients/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"first_name":"John","last_name":"Doe","document_number":"12345678"}'
```
Body (JSON):
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "document_number": "12345678"
}
```

Example (Create diagnosis)
```bash
curl -X POST \
  'http://localhost:8000/api/patients/diagnoses/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Lumbalgia","code":"DX001"}'
```
Body (JSON):
```json
{
  "name": "Lumbalgia",
  "code": "DX001"
}
```

Example (Create medical record)
```bash
curl -X POST \
  'http://localhost:8000/api/patients/medical-records/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"patient":1,"diagnosis":"Lumbalgia","observation":"Notas"}'
```
Body (JSON):
```json
{
  "patient": 1,
  "diagnosis": "Lumbalgia",
  "observation": "Notas"
}
```

---

## Architect Module
Base: http://localhost:8000/api/architect/

- login
  - POST http://localhost:8000/api/architect/auth/login/

Example (Login)
```bash
curl -X POST \
  'http://localhost:8000/api/architect/auth/login/' \
  -H 'Content-Type: application/json' \
  -d '{"email":"user@example.com","password":"password"}'
```
Body (JSON):
```json
{
  "email": "user@example.com",
  "password": "password"
}
```

Example (Login as Admin)
```bash
curl -X POST \
  'http://localhost:8000/api/architect/auth/login/' \
  -H 'Content-Type: application/json' \
  -d '{"email":"admin@gmail.com","password":"admin123456"}'
```
Body (JSON):
```json
{
  "email": "admin@gmail.com",
  "password": "admin123456"
}
```

Example (Login as First User)
```bash
curl -X POST \
  'http://localhost:8000/api/architect/auth/login/' \
  -H 'Content-Type: application/json' \
  -d '{"email":"senati@gmail.com","password":"wilber123456"}'
```
Body (JSON):
```json
{
  "email": "senati@gmail.com",
  "password": "wilber123456"
}
```

Example (Login as Second User)
```bash
curl -X POST \
  'http://localhost:8000/api/architect/auth/login/' \
  -H 'Content-Type: application/json' \
  -d '{"email":"prueba2@gmail.com","password":"clinica23456"}'
```
Body (JSON):
```json
{
  "email": "prueba2@gmail.com",
  "password": "clinica23456"
}
```

Pruebas en Postman (login)
- POST http://localhost:8000/api/architect/auth/login/
    
    Body (JSON):
    ```json
    {
      "email": "admin@gmail.com",
      "password": "admin123456"
    }
    ```
  
  - POST http://localhost:8000/api/architect/auth/login/
    
    Body (JSON):
    ```json
    {
      "email": "senati@gmail.com",
      "password": "wilber123456"
    }
    ```
  
  - POST http://localhost:8000/api/architect/auth/login/
    
    Body (JSON):
    ```json
    {
      "email": "prueba2@gmail.com",
      "password": "clinica23456"
    }
    ```

---

## Therapists Module
Base: http://localhost:8000/api/therapists/
Router resource: `therapists`

- standard
  - GET http://localhost:8000/api/therapists/therapists/ (filters: `active=true|false`, `region`, `province`, `district`, `search`)
  - POST http://localhost:8000/api/therapists/therapists/
    
    Body (JSON):
    ```json
    {
      "name": "Ana",
      "last_name_paternal": "Pérez"
    }
    ```
  - GET http://localhost:8000/api/therapists/therapists/{id}/
  - PUT/PATCH http://localhost:8000/api/therapists/therapists/{id}/
  - DELETE http://localhost:8000/api/therapists/therapists/{id}/ (soft delete)

- custom actions
  - GET http://localhost:8000/api/therapists/therapists/inactive/
  - POST or PATCH http://localhost:8000/api/therapists/therapists/{id}/restore/
    
    Body (JSON):
    ```json
    {}
    ```

Example (List inactive)
```bash
curl -X GET \
  'http://localhost:8000/api/therapists/therapists/inactive/' \
  -H 'Authorization: Bearer {{token}}'
```
Body (JSON):
```json
{}
```

Example (Create therapist)
```bash
curl -X POST \
  'http://localhost:8000/api/therapists/therapists/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Ana","last_name_paternal":"Pérez"}'
```
Body (JSON):
```json
{
  "name": "Ana",
  "last_name_paternal": "Pérez"
}
```

Example (Restore therapist)
```bash
curl -X POST \
  'http://localhost:8000/api/therapists/therapists/1/restore/' \
  -H 'Authorization: Bearer {{token}}'
```
Body (JSON):
```json
{}
```

---

## Appointments & Status Module
Base: http://localhost:8000/api/appointments/
Router resources: `appointments`, `appointment-statuses`, `tickets`

- appointments
  - GET http://localhost:8000/api/appointments/appointments/ (filters: see view; supports search, ordering, pagination)
  - POST http://localhost:8000/api/appointments/appointments/
    
    Body (JSON):
    ```json
    {
      "patient": 1,
      "therapist": 1,
      "appointment_date": "2025-01-20",
      "hour": "10:00"
    }
    ```
  - GET http://localhost:8000/api/appointments/appointments/{id}/
  - PUT/PATCH http://localhost:8000/api/appointments/appointments/{id}/
  - DELETE http://localhost:8000/api/appointments/appointments/{id}/
  - Custom actions:
    - GET http://localhost:8000/api/appointments/appointments/completed/
    - GET http://localhost:8000/api/appointments/appointments/pending/
    - GET http://localhost:8000/api/appointments/appointments/by_date_range/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
    - GET http://localhost:8000/api/appointments/appointments/check_availability/?date=YYYY-MM-DD&hour=HH:MM
    - POST http://localhost:8000/api/appointments/appointments/{id}/cancel/
      
      Body (JSON):
      ```json
      {}
      ```
    - POST http://localhost:8000/api/appointments/appointments/{id}/reschedule/
      
      Body (JSON):
      ```json
      {
        "appointment_date": "2025-01-22",
        "hour": "11:00"
      }
      ```

- appointment statuses
  - GET http://localhost:8000/api/appointments/appointment-statuses/
  - POST http://localhost:8000/api/appointments/appointment-statuses/
    
    Body (JSON):
    ```json
    {
      "name": "CONFIRMADO",
      "description": "Estado confirmado"
    }
    ```
  - GET http://localhost:8000/api/appointments/appointment-statuses/{id}/
  - PUT/PATCH http://localhost:8000/api/appointments/appointment-statuses/{id}/
  - DELETE http://localhost:8000/api/appointments/appointment-statuses/{id}/
  - Custom actions:
    - POST http://localhost:8000/api/appointments/appointment-statuses/{id}/activate/
      
      Body (JSON):
      ```json
      {}
      ```
    - POST http://localhost:8000/api/appointments/appointment-statuses/{id}/deactivate/
      
      Body (JSON):
      ```json
      {}
      ```

- tickets
  - GET http://localhost:8000/api/appointments/tickets/
  - POST http://localhost:8000/api/appointments/tickets/
    
    Body (JSON):
    ```json
    {
      "appointment": 1,
      "amount": 100.0,
      "payment_method": "cash"
    }
    ```
  - GET http://localhost:8000/api/appointments/tickets/{id}/
  - PUT/PATCH http://localhost:8000/api/appointments/tickets/{id}/
  - DELETE http://localhost:8000/api/appointments/tickets/{id}/
  - Custom actions:
    - POST http://localhost:8000/api/appointments/tickets/{id}/mark_paid/
      
      Body (JSON):
      ```json
      {}
      ```
    - POST http://localhost:8000/api/appointments/tickets/{id}/cancel/
      
      Body (JSON):
      ```json
      {}
      ```
    - GET http://localhost:8000/api/appointments/tickets/by_payment_method/?method={method}
    - GET http://localhost:8000/api/appointments/tickets/by_number/?number={ticket_no}

Example (Check availability)
```bash
curl -X GET \
  'http://localhost:8000/api/appointments/appointments/check_availability/?therapist_id=1&date=2025-01-15' \
  -H 'Authorization: Bearer {{token}}'
```
Body (JSON):
```json
{}
```

Example (Create appointment)
```bash
curl -X POST \
  'http://localhost:8000/api/appointments/appointments/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"patient":1, "therapist":1, "appointment_date":"2025-01-20", "hour":"10:00"}'
```
Body (JSON):
```json
{
  "patient": 1,
  "therapist": 1,
  "appointment_date": "2025-01-20",
  "hour": "10:00"
}
```

Example (Cancel appointment)
```bash
curl -X POST \
  'http://localhost:8000/api/appointments/appointments/1/cancel/' \
  -H 'Authorization: Bearer {{token}}'
```
Body (JSON):
```json
{}
```

Example (Reschedule appointment)
```bash
curl -X POST \
  'http://localhost:8000/api/appointments/appointments/1/reschedule/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"appointment_date":"2025-01-22","hour":"11:00"}'
```
Body (JSON):
```json
{
  "appointment_date": "2025-01-22",
  "hour": "11:00"
}
```

Example (Activate appointment status)
```bash
curl -X POST \
  'http://localhost:8000/api/appointments/appointment-statuses/1/activate/' \
  -H 'Authorization: Bearer {{token}}'
```
Body (JSON):
```json
{}
```

Example (Deactivate appointment status)
```bash
curl -X POST \
  'http://localhost:8000/api/appointments/appointment-statuses/1/deactivate/' \
  -H 'Authorization: Bearer {{token}}'
```
Body (JSON):
```json
{}
```

Example (Create appointment status)
```bash
curl -X POST \
  'http://localhost:8000/api/appointments/appointment-statuses/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"name":"CONFIRMADO","description":"Estado confirmado"}'
```
Body (JSON):
```json
{
  "name": "CONFIRMADO",
  "description": "Estado confirmado"
}
```

Example (Create ticket)
```bash
curl -X POST \
  'http://localhost:8000/api/appointments/tickets/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"appointment":1, "amount":100.0, "payment_method":"cash"}'
```
Body (JSON):
```json
{
  "appointment": 1,
  "amount": 100.0,
  "payment_method": "cash"
}
```

Example (Mark ticket as paid)
```bash
curl -X POST \
  'http://localhost:8000/api/appointments/tickets/1/mark_paid/' \
  -H 'Authorization: Bearer {{token}}'
```
Body (JSON):
```json
{}
```

Example (Cancel ticket)
```bash
curl -X POST \
  'http://localhost:8000/api/appointments/tickets/1/cancel/' \
  -H 'Authorization: Bearer {{token}}'
```
Body (JSON):
```json
{}
```

---

## Histories & Configurations Module
Base: http://localhost:8000/api/configurations/

- histories
  - GET http://localhost:8000/api/configurations/histories/
  - POST http://localhost:8000/api/configurations/histories/create/
    
    Body (JSON):
    ```json
    {
      "patient": 1,
      "is_active": true
    }
    ```
  - POST http://localhost:8000/api/configurations/histories/{id}/delete/
    
    Body (JSON):
    ```json
    {}
    ```

- document types
  - GET http://localhost:8000/api/configurations/document_types/
  - POST http://localhost:8000/api/configurations/document_types/create/
    
    Body (JSON):
    ```json
    {
      "name": "Factura"
    }
    ```
  - DELETE http://localhost:8000/api/configurations/document_types/{id}/delete/

- payment types
  - GET http://localhost:8000/api/configurations/payment_types/
  - POST http://localhost:8000/api/configurations/payment_types/create/
    
    Body (JSON):
    ```json
    {
      "name": "Efectivo"
    }
    ```
  - DELETE http://localhost:8000/api/configurations/payment_types/{id}/delete/
  - PUT http://localhost:8000/api/configurations/payment_types/{id}/edit/

Example (Create document type)
```bash
curl -X POST \
  'http://localhost:8000/api/configurations/document_types/create/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Factura"}'
```
Body (JSON):
```json
{
  "name": "Factura"
}
```

Example (Create payment type)
```bash
curl -X POST \
  'http://localhost:8000/api/configurations/payment_types/create/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Efectivo"}'
```
Body (JSON):
```json
{
  "name": "Efectivo"
}
```

Example (Create history)
```bash
curl -X POST \
  'http://localhost:8000/api/configurations/histories/create/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"patient":1, "is_active":true}'
```
Body (JSON):
```json
{
  "patient": 1,
  "is_active": true
}
```

Example (Delete history)
```bash
curl -X POST \
  'http://localhost:8000/api/configurations/histories/1/delete/' \
  -H 'Authorization: Bearer {{token}}'
```
Body (JSON):
```json
{}
```

---

## Locations Module (Ubi Geo)
Base: http://localhost:8000/api/locations/
Router resources: `regions`, `provinces`, `districts`

- regions
  - GET http://localhost:8000/api/locations/regions/
  - GET http://localhost:8000/api/locations/regions/{id}/

- provinces
  - GET http://localhost:8000/api/locations/provinces/?region={region_id}
  - GET http://localhost:8000/api/locations/provinces/{id}/

- districts
  - GET http://localhost:8000/api/locations/districts/?province={province_id}
  - GET http://localhost:8000/api/locations/districts/{id}/

Example (List provinces by region)
```bash
curl -X GET 'http://localhost:8000/api/locations/provinces/?region=1'
```
Body (JSON):
```json
{}
```

---

## Company Reports Module
Base: http://localhost:8000/api/company/
Router resources: `statistics`, `company`

- statistics
  - GET http://localhost:8000/api/company/statistics/ (from router viewset wrapper)
  - GET http://localhost:8000/api/company/reports/statistics/?from=YYYY-MM-DD&to=YYYY-MM-DD (metrics APIView)

- company
  - GET http://localhost:8000/api/company/company/
  - POST http://localhost:8000/api/company/company/
    
    Body (JSON):
    ```json
    {
      "name": "Mi Empresa",
      "ruc": "12345678901"
    }
    ```
  - GET http://localhost:8000/api/company/company/{id}/
  - PUT/PATCH http://localhost:8000/api/company/company/{id}/
  - DELETE http://localhost:8000/api/company/company/{id}/
  - Custom actions (file/logo)
    - POST http://localhost:8000/api/company/company/{id}/upload_logo/ (multipart/form-data)
      
      Body (JSON):
      ```json
      {}
      ```
    - PATCH http://localhost:8000/api/company/company/{id}/update_logo/ (multipart/form-data)
    - DELETE http://localhost:8000/api/company/company/{id}/delete_logo/
    - POST http://localhost:8000/api/company/company/{id}/store_data/
      
      Body (JSON):
      ```json
      {
        "address": "Av. Siempre Viva 123"
      }
      ```
    - GET http://localhost:8000/api/company/company/{id}/show_company/

- reports (JSON)
  - GET http://localhost:8000/api/company/reports/appointments-per-therapist/?from=YYYY-MM-DD&to=YYYY-MM-DD&therapist_id={id}
  - GET http://localhost:8000/api/company/reports/patients-by-therapist/?from=YYYY-MM-DD&to=YYYY-MM-DD&therapist_id={id}
  - GET http://localhost:8000/api/company/reports/daily-cash/?date=YYYY-MM-DD
  - GET http://localhost:8000/api/company/reports/improved-daily-cash/?date=YYYY-MM-DD
  - GET http://localhost:8000/api/company/reports/daily-paid-tickets/?date=YYYY-MM-DD
  - GET http://localhost:8000/api/company/reports/appointments-between-dates/?from=YYYY-MM-DD&to=YYYY-MM-DD

- exports (files)
  - GET http://localhost:8000/api/company/exports/pdf/citas-terapeuta/?from=YYYY-MM-DD&to=YYYY-MM-DD&therapist_id={id}
  - GET http://localhost:8000/api/company/exports/pdf/pacientes-terapeuta/?from=YYYY-MM-DD&to=YYYY-MM-DD&therapist_id={id}
  - GET http://localhost:8000/api/company/exports/pdf/resumen-caja/?date=YYYY-MM-DD
  - GET http://localhost:8000/api/company/exports/pdf/caja-chica-mejorada/?date=YYYY-MM-DD
  - GET http://localhost:8000/api/company/exports/pdf/tickets-pagados/?date=YYYY-MM-DD
  - GET http://localhost:8000/api/company/exports/excel/citas-rango/?from=YYYY-MM-DD&to=YYYY-MM-DD
  - GET http://localhost:8000/api/company/exports/excel/caja-chica-mejorada/?date=YYYY-MM-DD
  - GET http://localhost:8000/api/company/exports/excel/tickets-pagados/?date=YYYY-MM-DD

Example (Company logo upload)
```bash
curl -X POST \
  'http://localhost:8000/api/company/company/1/upload_logo/' \
  -H 'Authorization: Bearer {{token}}' \
  -F 'logo=@/path/logo.png'
```
Body (JSON):
```json
{}
```

Example (Create company)
```bash
curl -X POST \
  'http://localhost:8000/api/company/company/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Mi Empresa","ruc":"12345678901"}'
```
Body (JSON):
```json
{
  "name": "Mi Empresa",
  "ruc": "12345678901"
}
```

Example (Store company data)
```bash
curl -X POST \
  'http://localhost:8000/api/company/company/1/store_data/' \
  -H 'Authorization: Bearer {{token}}' \
  -H 'Content-Type: application/json' \
  -d '{"address":"Av. Siempre Viva 123"}'
```
Body (JSON):
```json
{
  "address": "Av. Siempre Viva 123"
}
```

---

## Global Headers and Auth
- Authorization: `Bearer {{token}}`
- Content-Type: `application/json` (unless multipart/form-data)

## Environment Variables for Postman
- `BASE_URL`: `http://localhost:8000` (examples already use absolute URLs)
- `token`: JWT access token

## Change Log
- v1.0 Initial extraction from `urls.py` and views across modules.

