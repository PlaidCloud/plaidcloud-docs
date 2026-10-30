---
title: Formato de números y otros tipos de datos
description: Dé formato a los números en los paneles de control de PlaidCloud, incluidos moneda, porcentajes, posiciones decimales y patrones personalizados de visualización numérica.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dashboards/formatting-numbers.md
---

## Formato de números y otros tipos de datos

Hay 2 maneras de dar formato a los números en PlaidCloud. Una consiste en transformar directamente los valores de las tablas; la otra (más habitual) es darles formato al mostrarlos, de modo que los valores no pierdan precisión en la tabla y el usuario pueda verlos de una forma más limpia y apropiada.

Cuando muestro un valor en un panel de control, ¿cómo le doy el formato que quiero?
La forma principal de mostrar un valor es mediante un objeto de gráfico en un panel de control. Los gráficos pueden ser tablas, números grandes, gráficos de barras, etc. Cada objeto de gráfico puede tener un lugar o un medio ligeramente distinto para mostrar los valores. Por ejemplo, en las tablas se puede cambiar el formato de cada columna, y en un número grande se puede cambiar el formato del número.

Para cambiar el formato, edite el gráfico y busque el campo `D3 FORMAT` o `NUMBER FORMAT`. Para un gráfico de número grande, haga clic en la pestaña `CUSTOMIZE` y verá `NUMBER FORMAT`. Para una tabla, haga clic en la pestaña `CUSTOMIZE`, seleccione una columna numérica (se muestra con #) en `CUSTOMIZE COLUMN` y verá el campo `D3 FORMAT`.

El valor predeterminado es `Adaptive formatting`. Este ajusta el formato según los valores. Pero si desea fijar un formato (por ejemplo, $12.23 o 12,345,678), seleccione el formato que desee en la lista desplegable o escriba manualmente otro valor (si el campo lo permite).

## Formato D3: qué es

El formato D3 es una forma estructurada y formalizada de mostrar los resultados de datos en un formato determinado. Por ejemplo, en ciertas situaciones puede querer mostrar un valor grande como 3B (3 mil millones), con formato `.3s` en D3, o como 3,001,238,383, con formato `,d`. Otro ejemplo habitual es decidir si los valores en dólares se representan con 2 decimales de precisión o se redondean al dólar más cercano: $,d o $,.2f para mostrar el signo de dólar, las comas, 2 decimales de precisión y notación de punto fijo.
Para profundizar en D3, consulte el siguiente sitio: [GitHub D3](https://github.com/d3/d3-format)


## Formato D3 general

La estructura general de D3 es la siguiente:

`[​[fill]align][sign][symbol][0][width][,][.precision][~][type]`

El carácter de relleno (fill) puede ser cualquier carácter (como un punto, una x o cualquier otro). Si hay un carácter de relleno, a continuación va un carácter `align`, que debe ser uno de los siguientes:

`>` - Alineado a la derecha dentro del espacio disponible. (Comportamiento predeterminado).
`<` - Alineado a la izquierda dentro del espacio disponible.
`^` - Centrado dentro del espacio disponible.
`=` - como >, pero con cualquier signo y símbolo a la izquierda de todo el relleno.

El `sign` puede ser:
`-` - en blanco para cero o positivo y un signo menos para negativo. (Comportamiento predeterminado).
`+` - un signo más para cero o positivo y un signo menos para negativo.
`(` - nada para cero o positivo y paréntesis para negativo.
(espacio) - un espacio para cero o positivo y un signo menos para negativo.

El `symbol` puede ser:
`$` - aplicar el símbolo de moneda.

La opción `zero` (0) habilita el relleno con ceros; esto establece implícitamente el relleno en 0 y la alineación en =.

El `width` define el ancho mínimo del campo; si no se especifica, el ancho lo determina el contenido. Por ejemplo, si indica 8, el ancho del campo será de 8 caracteres.

La opción `comma` (,) habilita el uso de comas como separadores (por ejemplo, para los millares).

Según el tipo, el `precision` puede indicar el número de dígitos que siguen al punto decimal (tipos f y %) o el número de dígitos significativos (tipos ​, g, r, s y p). Si no se especifica la precisión, el valor predeterminado es 6 para todos los tipos excepto (ninguno), cuyo valor predeterminado es 12.

La opción `tilde` ~ elimina los ceros finales no significativos en todos los tipos de formato. Se usa con mayor frecuencia junto con los tipos r, s y %.

`types`
|Tipo |   Descripción                                                                               |
|-----|---------------------------------------------------------------------------------------------|
|f    |notación de punto fijo. **(común)**
|d    |notación decimal, redondeada a entero. **(común)**
|%    |multiplica por 100 y luego aplica notación decimal con un signo de porcentaje. **(común)**
|g    |notación decimal o exponencial, redondeada a dígitos significativos.
|r    |notación decimal, redondeada a dígitos significativos.
|s    |notación decimal con un prefijo del SI, redondeada a dígitos significativos.
|p    |multiplica por 100, redondea a dígitos significativos y luego aplica notación decimal con un signo de porcentaje.

## Ejemplos
|Expresión|Entrada|Salida|Notas|
|----------|-----|------|-----|
|,d|12345.67|12,346|redondea el valor al entero más cercano y agrega comas
|,.2f|12345.678|12,345.68|Agrega comas y 2 decimales, y redondea al centésimo más cercano
|$,.2f|12345.67|$12,345.67|Agrega un símbolo $, tiene comas y 2 dígitos después del decimal
|$,d|12345.67|$12,346|
|.&lt;10,|151925|151,925...|tiene puntos a la izquierda del valor, 10 caracteres de ancho y comas
|0>10|12345|0000012345|rellena el valor con ceros a la izquierda, con 10 caracteres de ancho. Funciona bien para fijar el ancho de un valor de código 
|,.2%|13.215|1,321.50%|tiene comas, 2 dígitos a la derecha del decimal, convierte a porcentaje y muestra un símbolo %
|x^+$16,.2f|123456|xx+$123,456.00xx| rellena con "x", centrado, con un símbolo +/-, un símbolo $, 16 caracteres de ancho, comas y 2 decimales
