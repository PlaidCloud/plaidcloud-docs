---
title: Conector de Google BigQuery
description: Configure una conexión a Google BigQuery en PlaidCloud para ejecutar consultas analíticas e integrar datos a gran escala en los flujos de trabajo.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/google/big-query.md
---

## Documentación de la conexión
[La documentación de Google BigQuery](https://docs.cloud.google.com/bigquery/docs).

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

### Conexión de BigQuery

| Campo | Obligatorio | Descripción |
|---|---|---|
| Proyecto | Sí | El proyecto de Google Cloud que contiene el conjunto de datos. |
| Conjunto de datos | Sí | El conjunto de datos de BigQuery del que se lee y en el que se escribe. |
| Tabla | Sí | Una tabla del conjunto de datos. |

### Credenciales de autenticación

| Campo | Obligatorio | Descripción |
|---|---|---|
| Clave de la cuenta de servicio (JSON) | Sí | Pegue el archivo de clave JSON completo de una cuenta de servicio de Google que pueda leer el conjunto de datos. Concédale acceso de escritura solo si desea escribir en el conjunto de datos. La clave es de solo escritura: déjela en blanco al editar para conservar la guardada. |

La conexión se autentica únicamente con la clave de la cuenta de servicio que usted le proporcione. [Importar SQL](/es/reference/workflow-steps/import/import-sql/) lee BigQuery a través de esta conexión, y [Export External Database Tables (paso)](/es/reference/workflow-steps/export/export-external-tables/) escribe en ella mediante un trabajo de carga de BigQuery.
