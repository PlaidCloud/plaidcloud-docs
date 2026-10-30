---
title: Solución de problemas de asignaciones
description: Solucione problemas de asignaciones de PlaidCloud, incluidos errores comunes, problemas de configuración y técnicas para depurar resultados.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/troubleshooting-allocations.md
---

## Por qué no se puede guardar un paso de asignación

PlaidCloud comprueba la asignación de columnas de un paso de asignación al guardarlo. Una asignación que no se puede ejecutar se rechaza en ese momento, con una notificación **No se puede guardar** que enumera lo que debe corregir, y el formulario cambia a la pestaña que contiene el problema. Antes, un paso así se guardaba sin quejas y luego detenía el flujo de trabajo a mitad de una ejecución, a menudo minutos después y con un mensaje que nombraba un recuento en lugar de un campo.

No se comprueba nada hasta que haya elegido tanto la **Tabla de valores que asignar** como la **Tabla de datos de inductores**. La asignación de columnas se construye a partir de esas dos tablas, así que mientras no estén definidas ambas, el paso solo solicita las tablas.

### Mapa de origen de la asignación

**"No columns specified for allocation."**
Establezca el **Rol** de al menos una columna en **Valor que asignar**. Esa columna contiene los valores que se reparten entre los destinos.

**"Only numeric columns can be allocated, but ... is not numeric."**
Una columna marcada como **Valor que asignar** tiene un **Tipo** no numérico. Cambie el tipo a uno numérico: Numeric, Currency, Integer, Entero grande, Entero pequeño, Entero diminuto, Float, Double, Decimal, Serial o Serial grande.

**"Rename the `alloc_status` target column."**
Una asignación escribe su propia columna `alloc_status` en la tabla de resultados, así que una columna de destino con ese nombre entra en conflicto con ella. Cambie el nombre de la suya.

### Mapa de datos de inductores

**"No driver split value column found."**
Establezca el **Rol** de una columna de inductor en **Valor de división**. Esa columna contiene las ponderaciones o los porcentajes por los que divide la asignación.

**"The driver value column ... must be numeric."**
Cambie el **Tipo** de la columna **Valor de división** a uno numérico.

**"No driver relation columns specified."**
Establezca el **Rol** de al menos una columna de inductor en **Relación de origen (denominador)**. Esto es lo que relaciona las filas de inductor con las filas de origen.

**"No allocation target columns are indicated."**
Establezca el **Rol** de al menos una columna de inductor en **Destino de la asignación (numerador)**. Estas se convierten en los destinos de la asignación y aparecen en la tabla de resultados.

**"Driver relation columns do not exist in the source data."**
Una columna marcada como **Relación de origen (denominador)** no tiene en el **Mapa de origen de la asignación** una columna con el mismo nombre. Cambie su nombre para que coincida o agregue la columna al mapa de origen.

**"Allocation value column ... is also used as a numerator or denominator column."**
El mismo nombre de columna es a la vez un **Valor que asignar** en el mapa de origen y una **Relación de origen (denominador)** o un **Destino de la asignación (numerador)** en el mapa de inductores. Cambie el nombre de uno de ellos para que el valor que se asigna sea distinto de las columnas que describen adónde va.

### Solo para dividir mediante dimensión

**"Please select a hierarchy to use for the allocation dimension."**
Elija una **Jerarquía de la dimensión de asignación** en la pestaña **Configuración de la tabla de datos**. Consulte [Configurar una asignación](/es/guides/allocations/setup/configure-an-allocation/).

## Costo varado


El costo varado es....



## Sobreasignación de costo


La sobreasignación de costo es cuando se obtiene más costo de salida...



## Asignación incorrecta de costo


La asignación incorrecta de costos ocurre cuando...
