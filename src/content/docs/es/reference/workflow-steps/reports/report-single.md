---
title: Report Single
description: Genere un único informe PDF desde un paso de flujo de trabajo de PlaidCloud mediante plantillas, orígenes de datos y opciones de diseño configurables.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/report-single.md
---

## Descripción



Genera un informe PDF a partir de una plantilla RML (Report Markup Language), rellenada con datos de una o más tablas de PlaidCloud. Úselo para informes formales y con formato: facturas, estados financieros, presentaciones regulatorias, resúmenes con la imagen de marca.

La plantilla RML define el diseño (tamaño de página, fuentes, texto fijo, ubicación de las tablas); las tablas de entrada aportan los datos variables. Compárelo con [Reports Batch](/es/reference/workflow-steps/reports/reports-batch/) cuando una plantilla deba producir muchos informes (por ejemplo, uno por cliente).


## Nombres que lee la plantilla

La plantilla lee cada origen de la pestaña **Datos del informe**, y cada constante de **Constantes del informe (valores fijos)**, por su nombre. Los orígenes nuevos se llaman `new_source`, `new_source_2` y así sucesivamente, y la plantilla puede leerlos tal cual; cámbieles el nombre para indicar qué contienen.


## Qué se comprueba al guardar

Cada nombre de origen y de constante debe ser:

- **Indicado**: se rechaza un nombre en blanco.
- **Propio**: dos orígenes, dos constantes, o un origen y una constante no pueden compartir nombre, porque la plantilla solo vería uno de ellos: *Source name 'sales' is also a constant name; rename one of them.*
- **Legible por la plantilla**: letras, dígitos y guiones bajos, comenzando por una letra o un guion bajo: *Constant name 'fiscal year' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*
- **No una palabra reservada por la plantilla**: `True`, `False`, `None`, `true`, `false`, `none`, `not` y `self` se interpretan como algo distinto de sus datos: *Source name 'self' is a word the template reserves, so it can't be read as a name.*


## Ejemplos

Aún no hay ejemplos...
