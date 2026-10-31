---
title: Dimension Clear
description: Borra todos los miembros de una dimensión de PlaidCloud en un paso de flujo de trabajo, conservando la estructura y la configuración de la dimensión.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-clear.md
---

## Descripción
Borra el contenido de una dimensión, incluidos su estructura, valores, alias, propiedades y jerarquías alternativas.


![Paso Dimension Clear](/images/dimension_clear.png)



## Selección de dimensión
### Especificar la dimensión de forma dinámica
Si las **dimensiones** o las **rutas** se crearon de forma dinámica, pueden usarse las mismas variables para borrarlas. Usar variables en el proceso de borrado resulta útil porque elimina la necesidad de actualizar manualmente el paso Dimension Clear de forma periódica.



Un ejemplo que usa la variable `current_month` para borrar de forma dinámica la dimensión Materiales:

```text
/Dimensions/{current_month}/Products/Materials
```

### Usar una dimensión específica

Use el menú desplegable para seleccionar la dimensión específica que desea borrar.
