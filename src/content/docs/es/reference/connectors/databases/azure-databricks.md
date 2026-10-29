---
title: Azure Databricks
description: Configure una conexión de Azure Databricks en PlaidCloud para integrar en los flujos de trabajo análisis basados en Spark y datos de lakehouse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/azure-databricks.md
---

**Azure Databricks** combina Apache Spark, Delta Lake y un entorno de notebooks administrado en Microsoft Azure. Use este conector para leer y escribir tablas en un espacio de trabajo de Databricks desde los flujos de trabajo de PlaidCloud. La autenticación usa un token de acceso personal o una entidad de servicio; la URL del espacio de trabajo y la ruta HTTP identifican el almacén SQL de destino.

## Documentación del proveedor
[Documentación de Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/).

## Configuración

Estos campos aparecen al crear o editar esta conexión. Que sean obligatorios u opcionales depende de las opciones de autenticación que habilite.

### Identificación

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| Alias | Texto (varias líneas) | Alias o notas opcionales sobre la conexión. |
| Está activa | Interruptor | Indica si la conexión está habilitada. Deshabilítela para pausarla sin eliminarla. |
| Base de datos de solo lectura | Interruptor | Restringe la conexión a operaciones de solo lectura. |
| Tipo de acceso | Selección | Nivel de acceso de esta conexión: solo lectura, solo escritura o lectura y escritura. |

### Conexión

| Campo | Tipo | Descripción |
|---|---|---|
| Host de la base de datos | Texto | Nombre de host o dirección IP del servidor de la base de datos. |
| Catálogo de la base de datos | Texto | Base de datos, catálogo o esquema al que conectarse. |
| Esquema de la base de datos | Texto | Nombre del esquema dentro de la base de datos. |

### Autenticación

| Campo | Tipo | Descripción |
|---|---|---|
| Usuario de la base de datos | Texto | Nombre de usuario para la autenticación en la base de datos. |
| Usar SSO | Interruptor | Autenticarse mediante inicio de sesión único en lugar de usuario y contraseña. |
| Contraseña de la base de datos | Contraseña | Contraseña para la autenticación en la base de datos. |

### SSL / TLS

| Campo | Tipo | Descripción |
|---|---|---|
| Usar SSL | Interruptor | Cifra la conexión con SSL/TLS. |
| Modo SSL | Selección | Modo de verificación SSL (por ejemplo, disable, require, verify-ca, verify-full). |
| Certificado de cliente SSL | Texto (varias líneas) | Certificado de cliente (PEM) para la autenticación TLS mutua. |
| Clave de cliente SSL | Texto (varias líneas) | Clave privada de cliente (PEM) para la autenticación TLS mutua. |
| Certificado raíz SSL | Texto (varias líneas) | Certificado de CA raíz (PEM) para verificar el certificado del servidor. |
| Revocación de certificados SSL | Texto (varias líneas) | Lista de revocación de certificados, si su entorno usa una. |

### Túnel SSH

| Campo | Tipo | Descripción |
|---|---|---|
| Usar SSH | Interruptor | Canaliza la conexión a través de un host bastión SSH. |
| Host SSH | Texto | Nombre de host del bastión SSH. |
| Puerto SSH | Número | Puerto del bastión SSH (el valor predeterminado es 22). |
| Usuario SSH | Texto | Nombre de usuario del bastión SSH. |
| Contraseña SSH | Contraseña | Contraseña del bastión SSH (si se usa autenticación por contraseña). |
| Usar certificado SSH | Interruptor | Se autentica en el bastión SSH con una clave privada en lugar de una contraseña. |
| Clave privada SSH | Texto (varias líneas) | Clave privada SSH (PEM) para la autenticación en el bastión. |
| Clave de host SSH | Texto (varias líneas) | Clave de host SSH esperada para verificar la huella del bastión. |

### Otros

| Campo | Tipo | Descripción |
|---|---|---|
| Ruta HTTP | Texto | — |
