---
title: Dimension Delete
description: Elimina una dimensión de PlaidCloud en un paso de flujo de trabajo para quitar estructuras de datos jerárquicas que ya no se necesitan.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-delete.md
---

## Descripción
Elimina una dimensión junto con toda su estructura, valores, propiedades, alias y jerarquías alternativas.


![Paso Dimension Clear](/images/dimension_clear.png)



## Selección de dimensión
### Especificar la dimensión de forma dinámica
Si las **dimensiones** o las **rutas** se crearon de forma dinámica, pueden usarse las mismas variables para eliminarlas. Usar variables en el proceso de eliminación resulta útil porque elimina la necesidad de actualizar manualmente el paso Dimension Delete de forma periódica.



Un ejemplo que usa la variable `current_month` para eliminar de forma dinámica la dimensión Materiales:

```text
/Dimensions/{current_month}/Products/Materials
```

### Usar una dimensión específica

Use el menú desplegable para seleccionar la dimensión específica que desea eliminar.

### Dimensiones que coinciden con la búsqueda

Con **Dimensiones que coinciden con la búsqueda**, el paso no se guardará con un **Texto de búsqueda** vacío mientras la **Ruta de búsqueda** sea el nivel superior del proyecto (`/`), porque eliminaría todas las dimensiones del proyecto. Introduzca el texto que debe coincidir o elija una carpeta.
