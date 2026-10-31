---
title: MongoDB
description: Configure una conexión de MongoDB en PlaidCloud para leer colecciones en tablas y escribir tablas de nuevo como documentos.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/mongodb.md
---

**MongoDB** es una base de datos de documentos. Use esta conexión con [Importar MongoDB](/es/reference/workflow-steps/import/import-mongodb/) para leer una colección, o el resultado de una canalización de agregación, en una tabla, y con [Exportar MongoDB](/es/reference/workflow-steps/export/export-mongodb/) para escribir una tabla de nuevo como documentos. Para crear una, elija **MongoDB** como tipo de conexión.

## Documentación del proveedor
[La documentación de MongoDB](https://www.mongodb.com/docs/).

## Configuración

### Conexión de MongoDB

| Campo | Obligatorio | Descripción |
|---|---|---|
| Host | Sí | El nombre de host del servidor. |
| Usar una dirección SRV (mongodb+srv://, sin puerto) | No | Se conecta mediante una lista semilla de DNS, como hace MongoDB Atlas. No se usa el puerto. |
| Puerto | No | El puerto del servidor. De forma predeterminada es `27017`. |
| Base de datos predeterminada | No | La base de datos que usa un paso cuando no se indica ninguna. |

### Credenciales de autenticación

| Campo | Descripción |
|---|---|
| Usuario | El usuario con el que se conecta. |
| Contraseña | La contraseña del usuario (solo escritura). |

### Opciones

| Campo | Descripción |
|---|---|
| Opciones de conexión | Opciones de URI de MongoDB unidas con `&`, como `authSource=admin&tls=true`. Solo se aceptan las opciones que PlaidCloud permite. Déjelo en blanco al editar para conservar las opciones guardadas. |

### TLS

| Campo | Descripción |
|---|---|
| Certificado de CA (PEM) | La entidad de certificación que firmó los certificados de los servidores, cuando no es una pública. Déjelo en blanco al editar para conservar el certificado guardado. |
