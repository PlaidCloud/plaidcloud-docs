---
title: Amazon Redshift
description: Configure una conexión de base de datos de Amazon Redshift en PlaidCloud para consultar, importar y exportar datos con su almacén de datos Redshift.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/amazon-redshift.md
---

**Amazon Redshift** es el almacén de datos administrado en la nube de AWS, diseñado para cargas de trabajo analíticas sobre grandes conjuntos de datos. Use este conector para leer y escribir tablas de Redshift desde flujos de trabajo de PlaidCloud. El conector utiliza el protocolo de red de PostgreSQL; la autenticación usa credenciales estándar de base de datos o credenciales temporales respaldadas por IAM.

## Documentación del proveedor
Consulte la [documentación de Amazon Redshift](https://docs.aws.amazon.com/redshift/) para ver guías y material de referencia.

## Configuración

Estos campos aparecen al crear o editar esta conexión. Que sean obligatorios u opcionales depende de las opciones de autenticación que habilite.

### Identificación

| Campo | Tipo | Descripción |
|---|---|---|
| Name | Texto | Nombre para mostrar de esta conexión. |
| Alias | Texto (varias líneas) | Alias o notas opcionales sobre la conexión. |
| Is active | Interruptor | Indica si la conexión está habilitada. Desactívela para pausarla sin eliminarla. |
| Db read only | Interruptor | Restringe la conexión a operaciones de solo lectura. |
| Access type | Selección | Nivel de acceso de esta conexión: solo lectura, solo escritura o lectura y escritura. |

### Conexión

| Campo | Tipo | Descripción |
|---|---|---|
| Db host | Texto | Nombre de host o dirección IP del servidor de base de datos. |
| Db port | Número | Número de puerto de la conexión a la base de datos. |
| Db catalog | Texto | Base de datos, catálogo o esquema al que se conecta. |

### Autenticación

| Campo | Tipo | Descripción |
|---|---|---|
| Db user | Texto | Nombre de usuario para la autenticación en la base de datos. |
| Use sso | Interruptor | Autentica mediante inicio de sesión único en lugar de usuario y contraseña. |
| Db password | Contraseña | Contraseña para la autenticación en la base de datos. |

### SSL / TLS

| Campo | Tipo | Descripción |
|---|---|---|
| Use ssl | Interruptor | Cifra la conexión con SSL/TLS. |
| Ssl mode | Selección | Modo de verificación SSL (por ejemplo, disable, require, verify-ca, verify-full). |
| Ssl auth client cert | Texto (varias líneas) | Certificado de cliente (PEM) para la autenticación TLS mutua. |
| Ssl auth client key | Texto (varias líneas) | Clave privada de cliente (PEM) para la autenticación TLS mutua. |
| Ssl auth root cert | Texto (varias líneas) | Certificado de CA raíz (PEM) para verificar el certificado del servidor. |
| Ssl auth cert revoke | Texto (varias líneas) | Lista de revocación de certificados, si su entorno usa una. |

### Túnel SSH

| Campo | Tipo | Descripción |
|---|---|---|
| Use ssh | Interruptor | Canaliza la conexión a través de un host bastión SSH. |
| Ssh host | Texto | Nombre de host del bastión SSH. |
| Ssh port | Número | Puerto del bastión SSH (22 de forma predeterminada). |
| Ssh user | Texto | Nombre de usuario del bastión SSH. |
| Ssh password | Contraseña | Contraseña del bastión SSH (si se usa autenticación por contraseña). |
| Use ssh cert | Interruptor | Autentica en el bastión SSH con una clave privada en lugar de una contraseña. |
| Ssh private key | Texto (varias líneas) | Clave privada SSH (PEM) para la autenticación en el bastión. |
| Ssh host key | Texto (varias líneas) | Clave de host SSH esperada para verificar la huella digital del bastión. |
