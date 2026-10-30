---
title: Conector REST de Gusto
description: Configure una conexión a la API REST de Gusto en PlaidCloud para integrar datos de nómina, beneficios y recursos humanos en sus flujos de trabajo de análisis.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/gusto.md
---

## Documentación de la API
La [referencia de la API del proveedor](https://docs.gusto.com/app-integrations/reference/get-v1-token-info) cubre los puntos de conexión de este conector.

## Configuración

Estos campos aparecen al crear o editar esta conexión. Que sean obligatorios u opcionales depende de las opciones de autenticación que habilite.

### Identificación

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| Alias | Texto (varias líneas) | Alias o notas opcionales sobre la conexión. |
| Está activa | Interruptor | Indica si la conexión está habilitada. Deshabilítela para pausarla sin eliminarla. |

### Otros

| Campo | Tipo | Descripción |
|---|---|---|
| Host | Texto | — |
| Tipo de autenticación | Selección | — |
| Habilitar la verificación de certificados SSL | Interruptor | — |
| Seguir redirecciones automáticamente | Interruptor | — |
| Seguir el método HTTP original | Interruptor | — |
| Seguir el encabezado de autorización | Interruptor | — |
| Quitar el encabezado referer en la redirección | Interruptor | — |
| Habilitar analizador HTTP estricto | Interruptor | — |
| Codificar la URL automáticamente | Interruptor | Punto de conexión de la URL. |
| Deshabilitar el almacén de cookies | Interruptor | — |
| Usar el conjunto de cifrado del servidor durante el protocolo de enlace | Interruptor | — |
| Número máximo de redirecciones | Número | — |
| Punto de conexión de prueba | Texto | — |
| Método de prueba | Selección | — |
