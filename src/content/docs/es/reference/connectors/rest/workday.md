---
title: Conector REST de Workday
description: Configure una conexión de API REST de Workday en PlaidCloud para integrar datos de RR. HH., finanzas y planificación en sus flujos de trabajo.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday.md
---

## Documentación de la API
La [referencia de la API del proveedor](https://community.workday.com/sites/default/files/file-hosting/restapi/) cubre los puntos de conexión de este conector.

## Configuración

Estos campos aparecen al crear o editar esta conexión. Que sean obligatorios u opcionales depende de las opciones de autenticación que habilite.

### Identificación

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| Alias | Texto (varias líneas) | Alias o notas opcionales sobre la conexión. |
| Is active | Alternar | Indica si la conexión está habilitada. Desactívela para pausarla sin eliminarla. |
| Db read only | Alternar | Restringe la conexión a operaciones de solo lectura. |
| Access type | Selección | Nivel de acceso de esta conexión: solo lectura, solo escritura o lectura y escritura. |

### Otros

| Campo | Tipo | Descripción |
|---|---|---|
| Oauth2 client id | Texto | — |
| Oauth2 client secret | Texto | Credencial secreta: se almacena cifrada. |
| Workday url | Texto | Punto de conexión de URL. |
| Oauth2 refresh token | Texto | — |
