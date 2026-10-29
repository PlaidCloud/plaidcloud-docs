---
title: La API de datos para aplicaciones Panel
description: "Lea tablas de PlaidCloud desde una aplicación Panel con panel_data: filtre, pagine, cuente y agregue en el servidor, como el visualizador con sesión iniciada, con la seguridad a nivel de fila aplicada."
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/data-api.md
---

`plaidcloud.utilities.panel_data` es la forma en que una aplicación Panel de servidor lee una tabla sin cargar la tabla completa en la aplicación. Usted describe lo que desea (las filas que cumplen ciertos filtros, una página de ellas, un recuento, un total agrupado) y la base de datos de PlaidCloud hace el trabajo. A la aplicación solo vuelve el resultado.

Cada solicitud se ejecuta como la persona que está viendo la aplicación, por lo que sus permisos de proyecto y la [seguridad a nivel de fila](/es/guides/panel-apps/accessing-data/) se aplican a todo lo que devuelve.

```python
from plaidcloud.utilities.panel_data import table

sales = table("sales")
```

`table(name)` abre una tabla del proyecto de la aplicación, que es el proyecto al que la aplicación fue [asignada](/es/guides/panel-apps/branding/#asignar-una-aplicación-a-un-proyecto) cuando se publicó. Para leer una tabla de un proyecto distinto, páselo: `table("sales", project="Finance")`. El proyecto puede ser un id, un nombre o una ruta.

Un identificador de tabla nunca cambia. `filter` devuelve un identificador nuevo, por lo que puede conservar el que no tiene filtros y derivar varias vistas a partir de él.

## Filter

```python
emea = sales.filter(region="EMEA", year=[2025, 2026])
```

Cada argumento de palabra clave es el nombre de una columna. Un valor único coincide con las filas iguales a él. Una lista, tupla o conjunto coincide con las filas iguales a cualquiera de sus miembros. Varios argumentos se combinan con AND, y llamar de nuevo a `filter` sobre el resultado agrega más condiciones.

Un valor `None`, una cadena vacía o una lista vacía deja esa columna sin filtrar. Eso es lo que permite que un widget de filtro en blanco deje los datos intactos: `sales.filter(**widget_values)` funciona sin comprobar antes si hay valores en blanco.

Nombrar una columna que no existe genera un error que indica la tabla y la columna.

## Page

```python
rows = emea.page(1, 200, sort=["-amount"], key="id")
```

`page(n, size, sort, key)` devuelve la página `n` (contando desde 1) de `size` filas como un dataframe de pandas.

- `sort` es una lista de nombres de columna. Anteponga `-` a un nombre para el orden descendente: `["region", "-amount"]`.
- `key` es la columna única, o la lista de columnas únicas, de la tabla. Páselo siempre.

### Paginación estable

La paginación toma un segmento de una lista ordenada de filas. Cada solicitud es una consulta independiente. Si dos filas empatan en las columnas de ordenación, la base de datos puede devolverlas en un orden distinto en la siguiente solicitud, de modo que una fila puede aparecer en dos segmentos o en ninguno. `key` cierra esa brecha: PlaidCloud la agrega después de sus columnas de ordenación, de modo que el orden siempre es completo y cada fila queda en exactamente un segmento.

Sin `key`, la paginación recurre a ordenar por todas las columnas. Eso es lento en una tabla ancha, y sigue siendo inestable si dos filas son idénticas. Pase una clave única siempre que pagine y, por la misma razón, pásela a [`DataGrid`](/es/guides/panel-apps/app-kit/#datagrid).

## Count

```python
total_rows = emea.count()
```

Devuelve el número de filas que cumplen los filtros, como un número entero.

## Aggregate

```python
by_region = sales.aggregate(by=["region"], total=("amount", "sum"), orders=("id", "count"))
grand_total = emea.aggregate(total=("amount", "sum"))
```

`aggregate(by=(), limit=1000, **measures)` devuelve un dataframe con una fila por grupo, ordenado por las columnas de `by`. Cada medida es `name=(column, function)`, donde la función es `sum`, `count`, `avg`, `min` o `max`. Se requiere al menos una medida.

Sin `by`, obtiene una sola fila de totales sobre las filas filtradas. `limit` limita el número de grupos devueltos.

Las columnas decimales pueden llegar como cadenas. Conviértalas con `float(...)` o `astype(float)` antes de graficarlas o darles formato.

## Poner todo junto

```python
import panel as pn
import plaidcloud_panel as pcp
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

orders = table("orders")
bar = pcp.FilterBar(orders, "status")

pcp.App(
    "Orders",
    sidebar=[bar],
    main=[
        pcp.KpiCard("Open value", bar.table, "amount"),
        pn.bind(lambda t: pcp.DataGrid(t, key="order_id"), bar.table),
    ],
).servable()
```

`FilterBar`, `KpiCard` y `DataGrid` aceptan todos estos identificadores de tabla, por lo que la mayoría de las aplicaciones nunca llaman directamente a `page`, `count` o `aggregate`. Úselos cuando cree sus propias vistas. Consulte [El kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/).

## Relacionado

- [Lectura de datos y usuario con sesión iniciada](/es/guides/panel-apps/accessing-data/): conectarse como el visualizador y cuándo usar `PlaidConnection` directamente.
