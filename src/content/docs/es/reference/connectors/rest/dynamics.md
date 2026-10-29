---
title: Conector REST de Microsoft Dynamics 365
description: Configure una conexión a la API REST de Microsoft Dynamics en PlaidCloud para integrar datos de ERP y CRM en sus flujos de trabajo de análisis.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics.md
---

## Documentación de la API
La [referencia de la API del proveedor](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) cubre los puntos de conexión de este conector.

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

### Otros

| Campo | Tipo | Descripción |
|---|---|---|
| Inquilino de Dynamics | Texto | — |
| ID de cliente de OAuth2 | Texto | — |
| Secreto de cliente de OAuth2 | Texto | Credencial secreta: se almacena cifrada. |
| CRM de Dynamics | Texto | — |
