---
title: Dimension Sort
description: Ordena automáticamente los miembros de una dimensión en un paso de flujo de trabajo de PlaidCloud para mantener un orden coherente dentro de sus jerarquías.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-sort.md
---

## Descripción

Ordena los miembros de una dimensión bajo sus elementos principales: alfabéticamente, por valor, por propiedad o por una columna de orden personalizado. Evita la tarea tediosa de arrastrar manualmente los miembros de la jerarquía al orden correcto, algo especialmente útil después de una carga masiva o de una reestructuración importante.

Opera sobre la dimensión en el lugar; no se necesita ninguna tabla de origen ni de destino.


## Selección de dimensión
### Especificar la dimensión de forma dinámica
Si las **dimensiones** o las **rutas** se crearon de forma dinámica, pueden usarse las mismas variables para ordenarlas. Usar variables en el proceso de ordenación resulta útil porque elimina la necesidad de actualizar manualmente el paso Dimension Sort de forma periódica.



Un ejemplo que usa la variable `current_month` para ordenar de forma dinámica la dimensión Materiales:

```text
/Dimensions/{current_month}/Products/Materials
```

### Usar una dimensión específica

Use el menú desplegable para seleccionar la dimensión específica que desea ordenar.
