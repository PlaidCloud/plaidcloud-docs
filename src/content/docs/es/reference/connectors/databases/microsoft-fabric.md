---
title: Microsoft Fabric
description: Configure una conexión a Microsoft Fabric en PlaidCloud para integrar capacidades de análisis, almacenamiento de datos y lakehouse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/microsoft-fabric.md
---

**Microsoft Fabric** combina Power BI, Synapse y Data Factory en una plataforma de análisis unificada. Use este conector para acceder a los almacenes y lakehouses de Fabric como orígenes relacionales desde los flujos de trabajo de PlaidCloud. La autenticación se realiza mediante un punto de conexión compatible con SQL Server y las credenciales de su inquilino de Microsoft.

## Documentación del proveedor
[La documentación de Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/).

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
| Host de BD | Texto | Nombre de host o dirección IP del servidor de base de datos. |
| Puerto de BD | Número | Número de puerto de la conexión a la base de datos. |
| Catálogo de BD | Texto | Base de datos, catálogo o esquema al que se conecta. |

### Autenticación

| Campo | Tipo | Descripción |
|---|---|---|
| Usuario de BD | Texto | Nombre de usuario para la autenticación en la base de datos. |
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
| Confiar en certificados | Interruptor | — |
| Tipo de controlador | Selección | — |
| Autenticación de usuario | Interruptor | — |
