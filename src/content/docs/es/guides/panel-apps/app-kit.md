---
title: El kit de aplicaciones de Panel
description: "Cree aplicaciones de Panel con el aspecto de PlaidCloud mediante el kit plaidcloud_panel: el shell App, la paleta de comandos, FilterBar, KpiCard, DataGrid, Chart, Form, los botones de ejecución, la configuración guardada, la impresión y las traducciones, en claro y oscuro."
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

Todas las aplicaciones de Panel de servidor tienen instalado el kit `plaidcloud_panel`. Le da a su aplicación el aspecto de PlaidCloud (los mismos colores, tipografía y espaciado que el resto de la plataforma, en claro y oscuro) y un conjunto de componentes listos para usar en las pantallas que la mayoría de las aplicaciones necesitan: filtros, cifras destacadas, una cuadrícula de datos grande, gráficos y formularios. Su aplicación toma automáticamente la [marca de su proyecto](/es/guides/panel-apps/branding/).

```python
import plaidcloud_panel as pcp
```

Al importar el kit, también se aplica el aspecto de PlaidCloud a los gráficos de Plotly y Matplotlib.

## Comenzar desde una plantilla

En [Panel Studio](/es/guides/panel-apps/studio/), **Nueva aplicación** > **Studio** parte de una aplicación en blanco, una tabla o vista, otra aplicación Studio o una aplicación de la [galería](/es/guides/panel-apps/gallery/), sin ningún comando que ejecutar.

Para una aplicación que mantiene en un repositorio git, el kit incluye un comando que escribe una aplicación inicial funcional. Ejecútelo desde cualquier carpeta y luego edite los nombres de la tabla y de las columnas:

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| Opción | Qué hace |
|---|---|
| `--layout dashboard` | Filtros en la barra lateral, dos cifras destacadas y un gráfico. |
| `--layout explorer` | Filtros en la barra lateral, un recuento de filas y una tabla de filas. |
| `--table` | La tabla de PlaidCloud que lee la aplicación. |
| `--filters` | Columnas, separadas por comas, por las que filtrar. La primera controla el gráfico. |
| `--measure` | La columna numérica que se va a totalizar. |
| `--dir` | Dónde escribir `app.py` y `requirements.txt`. De forma predeterminada, la carpeta actual. |

El comando se detiene sin escribir nada si `app.py` ya existe. Confirme los dos archivos en su repositorio y [publíquelo como una aplicación de servidor](/es/guides/panel-apps/creating/#creación-de-una-aplicación-de-servidor).

## Una aplicación de ejemplo

Esta aplicación filtra una tabla de ventas por región y año, muestra dos cifras destacadas, un gráfico y una cuadrícula con paginación de las filas coincidentes. La cuadrícula muestra los importes con separadores de miles y los márgenes como porcentajes. Todas las piezas siguen los filtros.

```python
import panel as pn
import plaidcloud_panel as pcp
from bokeh.plotting import figure
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

sales = table("sales")
bar = pcp.FilterBar(sales, "region", "year")


def by_region(t):
    df = t.aggregate(by=["region"], total=("amount", "sum"))
    regions = df["region"].astype(str).tolist()
    fig = figure(x_range=regions, height=320, toolbar_location=None)
    fig.vbar(x=regions, top=df["total"].astype(float).tolist(), width=0.8, color=pcp.series()[0])
    return fig


def grid(t):
    return pcp.DataGrid(t, key="id", totals={"amount": "sum"}, formats={"amount": "0,0", "margin": "0.0%"})


pcp.App(
    "Sales",
    sidebar=[bar],
    main=[
        pn.Row(
            pcp.KpiCard("Total amount", bar.table, "amount"),
            pcp.KpiCard("Orders", bar.table),
        ),
        pcp.Chart(pn.bind(by_region, bar.table), title="Amount by region"),
        pcp.Section("Orders", pn.bind(grid, bar.table)),
    ],
).servable()
```

El patrón es el mismo en todas las aplicaciones del kit: cree un `FilterBar` sobre una tabla y luego vincule cada vista a `bar.table`. Una vista que no está vinculada a `bar.table` (ni a un widget) nunca se actualiza cuando cambian los filtros.

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` crea el shell de la aplicación: un encabezado con el título, el logotipo del proyecto y el usuario que ha iniciado sesión, una barra lateral y un área principal. Llame a `.servable()` sobre el resultado.

- **Navegación**: pase `nav=[("Overview", overview_page), ("Detail", detail_page)]` para obtener un menú de páginas en la parte superior de la barra lateral. Cada página es un objeto de Panel o una función que devuelve uno. Las funciones se ejecutan cuando se selecciona la página.
- **Tema**: la aplicación se abre en el tema claro. Pase `theme="dark"` para abrirla en el tema oscuro, o agregue `?theme=dark` a la URL. Con `theme_toggle=True` (el valor predeterminado), el encabezado incluye un interruptor claro/oscuro.
- **Marca**: la aplicación lee los colores de marca y el logotipo de su proyecto cuando se inicia una sesión. Un proyecto sin marca recibe los valores predeterminados de PlaidCloud.
- **Paleta de comandos**: pulse Ctrl-K (Cmd-K en Mac) para buscar y ejecutar comandos. Cada página de `nav` aparece en la lista como **Ir a** el nombre de la página, y `commands={"Refresh data": refresh}` agrega sus propias entradas, cada una con una etiqueta y una función que no recibe argumentos. Elija una entrada y la aplicación la ejecuta.
- **Recorrido de primera ejecución**: `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` muestra una breve introducción paso a paso, cada paso con un encabezado y una línea de texto. Aparece en la parte superior de la página hasta que la termina o la omite, y no se le vuelve a mostrar.
- **Cualquier otra cosa**: los demás argumentos de palabra clave se pasan a `FastListTemplate` de Panel.

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` crea un cuadro de selección múltiple con búsqueda por cada columna que nombre, con los valores distintos de esa columna (hasta 1,000, con un aviso cuando la lista se corta). Un cuadro muestra **Todos** cuando no se ha elegido nada. Pase sus propios widgets por nombre de columna para cualquier otro caso.

- `bar.table` es la tabla reducida por las selecciones actuales. Un widget en blanco no reduce los datos.
- Las selecciones se guardan en la URL de la página (`?region=EU`), por lo que una vista filtrada se puede compartir como un enlace.

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` muestra una cifra destacada. `fn` es `sum`, `count`, `avg`, `min` o `max`, calculado por el servidor sobre toda la tabla. Sin `column`, muestra el recuento de filas. Pase `bar.table` como origen para que la cifra siga los filtros.

Pase `drill_to=grid`, un `DataGrid`, para agregar un botón **View rows** debajo de la cifra. Al elegirlo, la cuadrícula apunta a la tabla de la propia tarjeta, de modo que la cuadrícula enumera las filas que hay detrás de la cifra.

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` es una vista de tabla para datos de cualquier tamaño. Al navegador solo se envía la página actual; la paginación, la ordenación, los totales y la exportación se ejecutan en el servidor.

- **Paginación**: 200, 500 o 1,000 filas por página, con botones Previous y Next y un contador de filas.
- **Ordenación**: haga clic en el encabezado de una columna. La ordenación se aplica a toda la tabla, no solo a la página visible.
- **Totales**: `totals` asigna a una columna `sum`, `count`, `avg`, `min` o `max`. El servidor calcula cada uno sobre todas las filas coincidentes y fija el resultado como la última fila de la cuadrícula.
- **Exportación**: los botones **CSV** y **XLSX** descargan todas las filas coincidentes con la ordenación actual, hasta `export_cap` filas (100,000 de forma predeterminada). Cuando la tabla es mayor, un aviso le indica que reduzca los filtros. Las celdas de texto que empiezan por `=`, `+`, `-` o `@` llevan un apóstrofo como prefijo para que una hoja de cálculo las lea como texto.
- **Formatos numéricos**: `formats={"margin": "0.0%", "amount": "0,0"}` establece un formato de visualización por columna, mediante cadenas de formato de [numbro](https://numbrojs.com/format.html). Un formato `%` multiplica por 100. La fila Total usa el mismo formato. Las columnas de punto flotante sin formato muestran hasta dos decimales con separadores de miles. **Copiar**, **CSV** y **XLSX** conservan los valores sin procesar.
- **Clave**: `key` es la columna, o la lista de columnas, que identifica de forma única una fila. Páselo siempre. Consulte [Paginación estable](/es/guides/panel-apps/data-api/#paginación-estable).

- **Agrupar por**: `group_by=["region"]` muestra una fila por grupo, con las medidas de `totals` y un recuento `rows`, todo calculado por el servidor, y una fila **Total** sobre todas las filas coincidentes. Pase `groupable=["region", "year"]` para agregar un selector **Agrupar por** con el que los usuarios que visualizan eligen las columnas. Una cuadrícula muestra hasta 1,000 grupos e indica cuándo ha cortado la lista. Las filas de grupo no tienen enlaces **Abrir**.
- **Formato condicional**: `rules` colorea las celdas según el valor. Cada regla nombra una `column`, una `op` (`>`, `>=`, `<`, `<=`, `==`, `!=` o `between`), un `value` (`[low, high]` para `between`) y un `token` (`success`, `warning`, `error` o `info`), por ejemplo `{"column": "margin", "op": "<", "value": 0, "token": "error"}`. La fila Total nunca se colorea.
- **Copiar**: el botón **Copiar** coloca en el portapapeles la página actual, con las columnas visibles y la fila Total, como texto separado por tabuladores que se puede pegar en Excel.
- **Abrir en PlaidCloud**: cuando el origen es una tabla de PlaidCloud, un enlace **Open in PlaidCloud** abre esa tabla.
- **Diseño de columnas guardado**: `layout_key="orders"` agrega los selectores **Columnas** y **Pinned** para elegir y ordenar columnas y fijar algunas de ellas. La elección de cada persona se guarda con ese nombre y se restaura la próxima vez que abre la aplicación.
- **Enlaces de fila**: `row_link` es una función que recibe una fila, como diccionario, y devuelve una dirección web, o `None` si no hay enlace. La cuadrícula agrega una columna **Abrir** con un enlace en cada fila que lo tiene. Solo se enlazan las direcciones `http` y `https` y las rutas del mismo sitio.
- **Actualización**: `grid.refresh()` vuelve a consultar el mismo origen y conserva la página, la ordenación y la agrupación. Llámelo después de que una [ejecución](#botones-de-ejecución-y-actualidad) termine de escribir la tabla.

`source` es el nombre de una tabla o una tabla de la [Data API](/es/guides/panel-apps/data-api/). Para volver a filtrar una cuadrícula, establezca `grid.source` con una tabla filtrada, o cree una cuadrícula nueva a partir de `bar.table`, como hace el ejemplo.

La cuadrícula está sujeta a la seguridad a nivel de fila del usuario que visualiza: lee a través de su propia conexión.

## Chart

`pcp.Chart(obj, title=None, height=320)` coloca un gráfico en una tarjeta con título. `obj` puede ser una figura de Bokeh, un gráfico de hvPlot o HoloViews, una figura de Plotly, una figura de Matplotlib o un `pn.bind(...)` que devuelva cualquiera de ellos. Los ejes numéricos de las figuras de Bokeh muestran separadores de miles, de modo que 800000 se lee 800,000.

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")` dispone los widgets de entrada como un único formulario con un botón de envío. `form.values()` devuelve `{widget.name: widget.value}` para cada widget con nombre, y `on_submit` recibe ese diccionario cuando se hace clic en el botón.

## Section, Card, Tabs y Loading

| Componente | Para qué se usa |
|---|---|
| `pcp.Section(title, *objects)` | Un grupo con título directamente sobre el fondo de la página. |
| `pcp.Card(title, *objects)` | Un grupo con título sobre una superficie elevada. |
| `pcp.Tabs(Overview=obj, Detail=obj)` | Pestañas que cargan el contenido de una pestaña cuando se selecciona. La pestaña activa toma el color de la marca. |
| `pcp.Loading(height=200)` | Un marcador de posición con efecto de brillo que se muestra mientras se cargan los datos. |

## StatusBanner

`pcp.StatusBanner(message, kind="info")` muestra un aviso en línea. `kind` es `error`, `warning`, `success` o `info`.

## Botones de ejecución y actualidad

`pcp.run_workflow_button(workflow_id, label=None)` agrega un botón que ejecuta un flujo de trabajo de PlaidCloud como la persona que abrió la aplicación, y muestra **En ejecución…**, luego **Hecho** o **Error**. Un fallo nombra los pasos que fallaron, hasta cinco. El flujo de trabajo pertenece al proyecto de la aplicación, a menos que pase `project_id`.

`pcp.RunButton(label, start, status)` hace lo mismo para cualquier trabajo. `start` lo inicia y devuelve un id de ejecución; `status(run_id)` devuelve `"running"`, `"succeeded"` o `"failed"`, o `("failed", reason)` para mostrar un motivo. Ambas son funciones normales, como llamadas a una API REST. El valor `runs` del botón aumenta en uno cada vez que una ejecución se completa correctamente, de modo que una vista que deba actualizarse después se vincula a él:

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` muestra cuándo se escribió por última vez una tabla, como **Updated 5 min ago**. La antigüedad avanza mientras la página permanece abierta. Pase `stale_after=datetime.timedelta(hours=24)` para marcar con una advertencia los datos más antiguos, y llame a `.refresh()` después de una ejecución. Una tabla cuya fecha no se puede determinar muestra **Last update unknown**; eso nunca es un error. `pcp.Freshness(fetch)` hace lo mismo para cualquier origen, donde `fetch` devuelve cuándo cambiaron los datos por última vez.

## Configuración guardada

`pcp.user_state` recuerda las elecciones de cada persona entre visitas, de modo que una aplicación se abre tal como la dejó.

- `pcp.user_state.persist(widget, "region")` restaura el valor guardado en el widget y lo guarda en cada cambio. Un valor guardado que el widget ya no ofrece se ignora.
- La página elegida en `nav` se guarda automáticamente.
- Una clave que empieza por `filters.`, como `pcp.user_state.persist(widget, "filters.region")`, guarda la elección de un filtro. PlaidCloud la recorta según el acceso a filas actual de la persona cada vez que se lee, de modo que un filtro guardado nunca recupera valores que ya no puede ver.
- `pcp.user_state.get(key, default)` y `pcp.user_state.set(key, value)` guardan cualquier otro valor pequeño.

La configuración guardada pertenece a una persona en una aplicación, hasta 8 KB. La configuración nunca se comparte entre personas. Si no se puede acceder a PlaidCloud cuando se guarda un ajuste, la aplicación lo conserva hasta que termine la sesión.

## Impresión y guardado como PDF

`pcp.PrintButton()` abre el cuadro de diálogo de impresión del navegador, donde el destino puede ser **Guardar como PDF**. La página se imprime con la barra lateral y los controles ocultos y con la marca de su proyecto aplicada. Cada `DataGrid` imprime toda su página actual, hasta 1,000 filas, con su fila Total al final. Una aplicación oscura se imprime con la paleta clara.

## Idiomas

El texto propio del kit, como los botones, los avisos, la paleta de comandos, el recorrido, los mensajes de ejecución y actualidad y el pie de la cuadrícula, aparece en inglés, alemán o francés. El idioma es `?lang=de` o `?lang=fr` en la dirección de la página; si no, el idioma del navegador. Los números usan los separadores del idioma. Sus datos, los nombres de columna y las etiquetas que usted escriba nunca se traducen.

## Presupuestos de rendimiento

Una carga de página cuyo primer renderizado tarda más de 3,000 ms, o que ejecuta una consulta de más de 2,000 ms, escribe una advertencia en el registro de la aplicación que nombra lo que se excedió. Las mismas cifras aparecen en la pestaña **Análisis** de [Panel Studio](/es/guides/panel-apps/studio/#análisis). Para establecer límites distintos para una aplicación, defina estas variables de entorno:

| Variable | Valor predeterminado | Establece |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | Milisegundos hasta el primer renderizado. |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | Milisegundos para una consulta. |

Un valor que no sea un número entero se ignora y se aplica el valor predeterminado.

## Colores para sus propios gráficos

`pcp.series()` devuelve la paleta de gráficos de PlaidCloud como una lista de colores, en orden. Utilícela para que los gráficos que usted mismo dibuja coincidan con los componentes propios del kit, como hace el ejemplo con el gráfico de barras.

## Pasos siguientes

- [La Data API](/es/guides/panel-apps/data-api/): filtre, pagine, cuente y agregue tablas de PlaidCloud desde su aplicación.
- [Alertas y resúmenes](/es/guides/panel-apps/alerts-and-digests/): envíe alertas de KPI y resúmenes programados desde una aplicación.
- [Marca del proyecto](/es/guides/panel-apps/branding/): defina sus colores y su logotipo una sola vez para todas las aplicaciones de un proyecto.
