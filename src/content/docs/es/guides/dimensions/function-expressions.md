---
title: Funciones de dimensión para expresiones y agregaciones
description: Use expresiones de función en las dimensiones de PlaidCloud para definir valores calculados, lógica condicional y propiedades dinámicas de los miembros.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/function-expressions.md
---

## Funciones para usar en las expresiones de jerarquía de dimensión

En la pantalla Jerarquía de la dimensión es posible agregar “Agregaciones” y “Expresiones”. A continuación se incluye una descripción de cada una.

## Agregaciones
Una agregación se usa para mostrar un valor agregado de una tabla (que puede ser “Sum”, “Count”, “Min” o “Max”).
La siguiente imagen muestra una agregación configurada para obtener valores de una tabla de “Valores de partida” de modo que se puedan mostrar valores para cada “Período” de la jerarquía.

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_1_agg.png)

Las agregaciones se pueden filtrar para que solo se muestren los elementos que coinciden con el filtro. En la siguiente imagen hemos configurado la agregación para mostrar valores de un elemento seleccionado de la dimensión “Cuenta”.

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_2_agg.png)

Si estos filtros se dejan en blanco, los datos se pueden filtrar mediante la barra de filtros de dimensión de la parte superior de la pantalla, como se ve en la siguiente imagen:

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_3_agg.png)

## Expresiones

Con las expresiones es posible mostrar valores que se calculan a partir de los valores de las agregaciones mostradas para la dimensión.
Las expresiones se construyen con fórmulas matemáticas, que pueden contener muchos tipos de operadores y algunas funciones especiales. Consulte la [lista de operadores](https://mathjs.org/docs/expressions/syntax.html). Las funciones disponibles se describen a continuación.


## Funciones
### Column(`<column_name>`)
Obtiene un valor de una columna con nombre para la fila o el nodo actual.

A continuación vemos un ejemplo de una expresión definida para mostrar el resultado de multiplicar el Valor de partida por 2.

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_4_func_column.png)


![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_5_func_column.png)

### Childcount()

Devuelve el número de elementos hijo de la fila o el nodo actual. Si la fila o el nodo actual es un elemento hoja, devuelve 0.

En el siguiente ejemplo se usa para devolver el valor promedio de los nodos hijo de un nodo padre.

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_6_func_childcount.png)

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_7_func_childcount.png)

### Leafcount()
Devuelve el número de elementos hoja que hay en el árbol para la fila o el nodo actual. Si la fila o el nodo actual es un elemento hoja, devuelve 1.

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_8_func_leafcount.png)

### Descendantcount()
Devuelve el número total de elementos que hay en el árbol para la fila o el nodo actual. Si la fila o el nodo actual es un elemento hoja, devuelve 0.

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_9_func_desccount.png)


### Siblingcount()
Devuelve el número de elementos del mismo nivel de la fila o el nodo actual. El valor devuelto incluye el nodo actual.

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_10_func_siblingcount.png)


### Nodevalue("`<node_name>`","`<column_name>`")
Devuelve el valor de una columna con nombre para un nodo con nombre.
Este es un ejemplo que se usa para mostrar el porcentaje del total de “LIV” correspondiente a cada fila o nodo.

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_11_func_nodevalue.png)

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_12_func_nodevalue.png)


### Parentvalue("<column_name")
Devuelve el valor de una columna dada para el elemento padre del nodo actual.
Este ejemplo muestra el porcentaje del valor de un nodo padre que usa un nodo hijo.

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_13_func_parentvalue.png)

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_14_func_parentvalue.png)

### Columntextcompare("<column_name", "`<text>`")

Devuelve un resultado numérico que indica si el texto de una columna con nombre es mayor, menor o igual que un valor proporcionado.

Si el texto de la columna es igual al texto proporcionado, esta función devuelve 0.

Si el texto de la columna es menor que el texto proporcionado, esta función devuelve -1.

Si el texto de la columna es mayor que el texto proporcionado, esta función devuelve 0.


El siguiente ejemplo compara el nombre del período con “Jun”.


![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_15_func_textcompare.png)

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_16_func_textcompare.png)


## Expresiones condicionales
Los ejemplos anteriores son bastante sencillos. Si se usan condicionales dentro de las expresiones, es posible crear expresiones más complejas.
Dentro de las expresiones, los condicionales tienen la siguiente forma:
`<condition>` ? `<value_if_true>` : `<value_if_false>`
por ejemplo, '12 > 6 ? 1000: 0'

Al combinar expresiones que contienen tanto condicionales como funciones, podemos crear expresiones más complejas, como este ejemplo en el que se suman 100 000 a un Valor de partida si el mes es “Jun”.

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_17_cond.png)

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_18_cond.png)


## Otro ejemplo: asignación sencilla

Este ejemplo muestra el importe del Valor de partida de un elemento padre que se consume mediante el Valor de inductor de recursos de un nodo hoja.

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_19_alloc.png)

![Carga de dimensión](/images/dimensions/expressions/dimension_expressions_20_alloc.png)

## Limitaciones:
Actualmente no es posible crear expresiones basadas en valores de otras expresiones. Las expresiones solo se pueden crear con valores de agregaciones.
