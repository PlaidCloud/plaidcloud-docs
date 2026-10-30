---
title: Conector REST de Ramp
description: Configure una conexión a la API REST de Ramp en PlaidCloud para integrar en sus flujos de trabajo los datos de gastos y de tarjetas corporativas.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/ramp.md
---

## Documentación de la API
La [referencia de la API del proveedor](https://docs.ramp.com/developer-api/v1) cubre los puntos de conexión de este conector.

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
| ID de cliente de OAuth2 | Texto | — |
| Secreto de cliente de OAuth2 | Texto | Credencial secreta: se almacena cifrada. |
| Ámbito de Ramp | Texto | — |
