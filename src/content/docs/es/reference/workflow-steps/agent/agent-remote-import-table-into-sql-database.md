---
title: Agent Remote Import Table into SQL Database
description: Importe datos de tablas de PlaidCloud a bases de datos SQL remotas mediante un agente de PlaidLink para cargar datos de forma segura detrás de cortafuegos.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database.md
---

## Descripción



Envía una tabla de proyecto de PlaidCloud a una base de datos a la que solo se puede acceder mediante un agente de PlaidLink. El agente recibe los datos de PlaidCloud y realiza la carga localmente, lo que resulta útil para mantener sincronizada una base de datos operativa local con el análisis de PlaidCloud.

Uso habitual: PlaidCloud genera un pronóstico o un resultado de asignación actualizado y el agente lo carga en el ERP, el data mart o la base de datos de informes operativos locales.


## Cómo llegan los datos al agente

Un agente de PlaidLink de la versión 1.2.33 o posterior recibe las filas de la tabla como un único archivo Parquet. Los números, las fechas, las marcas de tiempo y los valores verdadero/falso llegan con sus propios tipos. Las demás columnas, como las de hora, intervalo y JSON, llegan como texto. Un valor de texto vacío llega vacío (NULL), como siempre.

Un agente anterior recibe las filas como un archivo comprimido en zip delimitado por tabuladores, como antes. [Actualice el agente](/es/reference/cli/plaidlink/upgrade/) para recibir Parquet.

## Ejemplos

Todavía no hay ejemplos...
