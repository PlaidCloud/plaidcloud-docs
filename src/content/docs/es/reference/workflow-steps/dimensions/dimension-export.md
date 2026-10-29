---
title: Dimension Export
description: Exporta los datos de una dimensión de PlaidCloud en un paso de flujo de trabajo para guardar estructuras jerárquicas como archivos o transferirlas a otros sistemas.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-export.md
---

## Descripción

Aplana una dimensión en una tabla tabular de PlaidCloud: una fila por miembro, con columnas para el elemento principal, el nivel, el valor, los alias y las propiedades. Úsela cuando necesite consultar o combinar la estructura de la dimensión, o enviarla a sistemas posteriores que no pueden leer directamente el formato jerárquico de PlaidCloud.

Uso habitual: exporte la dimensión como una tabla y luego escríbala en un sistema externo (una herramienta de BI, una base de datos de informes, una entrega de archivos) mediante un paso de exportación normal.

## Exportación de todas las jerarquías

Elija **Todas las jerarquías** para llevar todas las jerarquías a una sola tabla. El resultado incluye una columna `hierarchy` que indica a qué jerarquía pertenece cada fila, y las filas se ordenan con la jerarquía principal primero, seguida de las alternativas en orden alfabético.
