---
title: Formato de tabla abierta Apache Hive
description: Configure una conexión a un catálogo de Apache Hive en PlaidCloud para consultas de formato de tabla abierta mediante el servicio PlaidCloud Lakehouse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/open-tables/hive.md
---

## Documentación del catálogo
[Documentación de Apache Hive](https://hive.apache.org/docs/latest/).

## Configuración

Estos campos aparecen al crear o editar esta conexión. Que sean obligatorios u opcionales depende de las opciones de autenticación que habilite.

### Identificación

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| Alias | Texto (varias líneas) | Alias o notas opcionales sobre la conexión. |
| Está activa | Interruptor | Indica si la conexión está habilitada. Deshabilítela para pausarla sin eliminarla. |
| Solo lectura de BD | Interruptor | Restringe la conexión a operaciones de solo lectura. |
| Tipo de acceso | Selección | Nivel de acceso de solo lectura, solo escritura o lectura y escritura para esta conexión. |

### Conexión

| Campo | Tipo | Descripción |
|---|---|---|
| Host de BD | Texto | Nombre de host o dirección IP del servidor de base de datos. |
| Puerto de BD | Número | Número de puerto de la conexión a la base de datos. |
| Catálogo de BD | Texto | Base de datos, catálogo o esquema al que conectarse. |

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
| Modo SSL | Selección | Modo de verificación SSL (por ejemplo, disable, require, verify-ca, verify-full). |
| Certificado de cliente SSL | Texto (varias líneas) | Certificado de cliente (PEM) para la autenticación TLS mutua. |
| Clave de cliente SSL | Texto (varias líneas) | Clave privada de cliente (PEM) para la autenticación TLS mutua. |
| Certificado raíz SSL | Texto (varias líneas) | Certificado de CA raíz (PEM) para verificar el certificado del servidor. |
| Revocación de certificados SSL | Texto (varias líneas) | Lista de revocación de certificados, si su entorno utiliza una. |

### Túnel SSH

| Campo | Tipo | Descripción |
|---|---|---|
| Usar SSH | Interruptor | Establece un túnel de la conexión a través de un host bastión SSH. |
| Host SSH | Texto | Nombre de host del bastión SSH. |
| Puerto SSH | Número | Puerto del bastión SSH (22 de forma predeterminada). |
| Usuario SSH | Texto | Nombre de usuario del bastión SSH. |
| Contraseña SSH | Contraseña | Contraseña del bastión SSH (si se usa autenticación con contraseña). |
| Usar certificado SSH | Interruptor | Se autentica en el bastión SSH con una clave privada en lugar de una contraseña. |
| Clave privada SSH | Texto (varias líneas) | Clave privada SSH (PEM) para la autenticación del bastión. |
| Clave de host SSH | Texto (varias líneas) | Clave de host SSH esperada para verificar la huella del bastión. |
