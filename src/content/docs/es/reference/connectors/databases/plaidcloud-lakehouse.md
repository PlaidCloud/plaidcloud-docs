---
title: PlaidCloud Lakehouse
description: Configure la conexión de base de datos de PlaidCloud Lakehouse para consultas y análisis de alto rendimiento sobre los datos de su lakehouse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/plaidcloud-lakehouse.md
---

**PlaidCloud Lakehouse** es el almacén de datos analítico integrado en cada espacio de trabajo de PlaidCloud. Este conector se usa principalmente para leer del lakehouse de un espacio de trabajo en otro, o para compartir datos entre inquilinos en implementaciones multiinquilino. Dentro de un mismo espacio de trabajo, las tablas del proyecto son accesibles directamente sin necesidad de este conector.

## Documentación del proveedor
Para usar PlaidCloud Lakehouse integrado se necesita muy poca configuración. Consulte la [documentación del servicio](https://docs.plaidcloud.com/docs/plaidcloud/analyze/dw/getting-started/).

## Configuración

Estos campos aparecen al crear o editar esta conexión. Que sean obligatorios u opcionales depende de las opciones de autenticación que habilite.

### Identificación

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| Alias | Texto (varias líneas) | Alias opcional o notas sobre la conexión. |
| Activa | Interruptor | Indica si la conexión está habilitada. Deshabilítela para pausarla sin eliminarla. |
| BD de solo lectura | Interruptor | Restringe la conexión a operaciones de solo lectura. |
| Tipo de acceso | Selección | Nivel de acceso de esta conexión: solo lectura, solo escritura o lectura y escritura. |

### Conexión

| Campo | Tipo | Descripción |
|---|---|---|
| Puerto de BD | Número | Número de puerto de la conexión a la base de datos. |
| Catálogo de BD | Texto | Base de datos, catálogo o esquema al que se conecta. |

### Autenticación

| Campo | Tipo | Descripción |
|---|---|---|
| Usuario de BD | Texto | Nombre de usuario para la autenticación en la base de datos. |
| Usar SSO | Interruptor | Autentica mediante inicio de sesión único en lugar de usuario y contraseña. |
| Contraseña de BD | Contraseña | Contraseña para la autenticación en la base de datos. |

### SSL / TLS

| Campo | Tipo | Descripción |
|---|---|---|
| Usar SSL | Interruptor | Cifra la conexión con SSL/TLS. |
| Modo SSL | Selección | Modo de verificación de SSL (p. ej., disable, require, verify-ca, verify-full). |
| Certificado de cliente SSL | Texto (varias líneas) | Certificado de cliente (PEM) para la autenticación TLS mutua. |
| Clave de cliente SSL | Texto (varias líneas) | Clave privada de cliente (PEM) para la autenticación TLS mutua. |
| Certificado raíz SSL | Texto (varias líneas) | Certificado de CA raíz (PEM) para verificar el certificado del servidor. |
| Revocación de certificados SSL | Texto (varias líneas) | Lista de revocación de certificados, si su entorno usa una. |

### Túnel SSH

| Campo | Tipo | Descripción |
|---|---|---|
| Usar SSH | Interruptor | Canaliza la conexión a través de un bastión SSH. |
| Host SSH | Texto | Nombre de host del bastión SSH. |
| Puerto SSH | Número | Puerto del bastión SSH (predeterminado: 22). |
| Usuario SSH | Texto | Nombre de usuario del bastión SSH. |
| Contraseña SSH | Contraseña | Contraseña del bastión SSH (si se usa autenticación con contraseña). |
| Usar certificado SSH | Interruptor | Autentica en el bastión SSH con una clave privada en lugar de una contraseña. |
| Clave privada SSH | Texto (varias líneas) | Clave privada SSH (PEM) para la autenticación en el bastión. |
| Clave de host SSH | Texto (varias líneas) | Clave de host SSH esperada para verificar la huella digital del bastión. |

### Otros

| Campo | Tipo | Descripción |
|---|---|---|
| Servidor | Texto | — |
| Lakehouse | Número | — |
