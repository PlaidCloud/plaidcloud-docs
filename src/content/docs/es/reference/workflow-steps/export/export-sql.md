---
title: Export to SQL
description: Exporte datos a bases de datos SQL externas desde un paso de flujo de trabajo de PlaidCloud para cargar resultados en sistemas de bases de datos posteriores.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Descripción



Escribe una tabla de proyecto de PlaidCloud en una cuenta de documentos como un archivo SQL con instrucciones CREATE TABLE e INSERT. Es útil cuando necesita entregar datos a un sistema que ingiere scripts SQL en lugar de CSV o Parquet.

Para cargar directamente en una base de datos remota, utilice en su lugar el paso de exportación de base de datos adecuado o [Agent Remote Import](/es/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/); son más rápidos y no requieren un archivo intermedio.

## Configuración adicional

En **Orden de las filas**, **Ordenar filas por** (`sort_columns`) ordena las filas escritas según estas columnas de origen, empezando por la primera clave, cada una con una configuración de **Columna**, **Ascendente** y **Nulos**. No es necesario que se escriba una columna clave. **Nulos** es, de forma predeterminada, primero en orden ascendente y último en orden descendente. No se usa con **Resumir** ni **Distinto**.

## Ejemplos


Todavía no hay ejemplos...
