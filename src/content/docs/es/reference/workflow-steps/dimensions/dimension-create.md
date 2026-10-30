---
title: Dimension Create
description: Cree una nueva dimensión jerárquica en un paso de flujo de trabajo de PlaidCloud para organizar y estructurar su sistema de clasificación de datos.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-create.md
---

## Descripción
Crea una dimensión para su uso y carga.


![Dimension Create](/images/dimension_create.png)

## Dimensión que crear
### Nombre
Puede usar un nombre específico para la dimensión que se creará o incluir variables para asignarle un nombre dinámico.


Las variables resultan útiles cuando las dimensiones se actualizan de forma periódica y se desea conservar la vista histórica.

Un ejemplo que usa la variable `current_month` para asignar un nombre dinámico a la dimensión:

```text
dimension_name_{current_month}
```
### Ruta
Las rutas le permiten crear estructuras de carpetas en las que se almacenan las dimensiones. También puede usar variables aquí para que la estructura de carpetas sea dinámica.
Un ejemplo que usa la variable `current_month` para asignar un nombre dinámico a una carpeta:

```text
/Dimensions/{current_month}/Product/
```

### Nota
El campo Nota se usa como un lugar para almacenar comentarios o notas.
