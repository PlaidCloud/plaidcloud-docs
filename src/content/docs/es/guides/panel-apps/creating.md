---
title: Crear una aplicación Panel
description: Cree una aplicación Panel en Panel Studio, a partir de una aplicación en blanco, una tabla, una vista o la galería, o publique una aplicación de servidor desde git o una aplicación WASM estática para necesidades a medida.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Comience con Panel Studio. No requiere repositorio ni configuración: usted crea la aplicación en PlaidCloud, la previsualiza y la publica cuando esté lista. Elija un tiempo de ejecución a medida solo cuando Studio no se ajuste a sus necesidades.

## Crear una aplicación de Studio

Abra **Mis aplicaciones Panel**. **Nueva aplicación Studio** es el primer botón de la barra de herramientas. También puede elegir **Nueva aplicación Studio** en el cuadro **Aplicaciones de Panel** de la pestaña **Inicio** de un proyecto, o [comenzar desde una tabla](#comenzar-desde-una-tabla).

1. Elija **Nueva aplicación Studio**.
2. Escriba un **Nombre**. El **Slug de URL** se completa a partir de él.
3. Elija el **Proyecto** al que pertenece la aplicación. Necesita acceso de edición al proyecto.
4. En **Comenzar desde**, elija dónde empieza la aplicación:

   | Comenzar desde | Qué obtiene |
   |---|---|
   | **Aplicación en blanco** | Una aplicación mínima con un `app.py` y un `requirements.txt`. |
   | **Desde una tabla** | Una aplicación creada sobre la tabla que elija. |
   | **Desde una vista** | Lo mismo, creada sobre una vista del proyecto. |
   | **Desde otra aplicación Studio** | Una copia de una de sus aplicaciones de Studio. |
   | **Desde la galería** | Una copia de una aplicación que su espacio de trabajo [incluyó en la galería](#comenzar-desde-la-galería). |

5. Elija **Crear**. Studio abre la nueva aplicación. Si parte de una tabla o una vista, el prompt de Weave para crear la primera página está listo para enviarse.

Consulte [Panel Studio](/es/guides/panel-apps/studio/) para editar, previsualizar y publicar la aplicación.

### Comenzar desde una tabla

También puede empezar en la pestaña **Tablas** de un proyecto. Seleccione una tabla o una vista y luego elija **Crear aplicación Panel** en el menú **Nuevo** o en el menú contextual. Se abre el cuadro de diálogo **Nueva aplicación Studio** con el proyecto y la tabla ya elegidos. El comando está disponible cuando usted tiene acceso de edición al proyecto y el proyecto no es de solo lectura.

### Comenzar desde la galería

Elija **Galería** en la barra de herramientas de **Mis aplicaciones Panel** para explorar las aplicaciones que su espacio de trabajo ha incluido y luego **Crear aplicación a partir de esto…** para crear su propia copia. O bien elija **Desde la galería** en el cuadro de diálogo **Nueva aplicación Studio**. Consulte [La galería de aplicaciones](/es/guides/panel-apps/gallery/), que incluye cómo incluir su propia aplicación.

## Otros tiempos de ejecución

Las aplicaciones de Studio cubren la mayoría de los paneles de control y herramientas. Para una necesidad a medida, publique con uno de los otros [tiempos de ejecución](/es/guides/panel-apps/) desde la barra de herramientas de **Mis aplicaciones Panel**:

- **Agregar aplicación WASM**: publique una aplicación estática que se ejecuta en el navegador a partir de un archivo.
- **Nueva aplicación de servidor**: compile y ejecute una aplicación desde un repositorio de git que usted administra, por ejemplo para reutilizar código existente o su propio proceso de compilación.
- **Nueva aplicación Dash**: publique una aplicación de Plotly Dash. Consulte [Aplicaciones de Dash](/es/guides/dash-apps/).

## Crear una aplicación de servidor

Una aplicación de servidor se compila desde un repositorio de git y se sirve en `https://<your-tenant-host>/serve/<slug>/`. Usted indica a PlaidCloud una rama de un repositorio; este compila el código en un contenedor, ejecuta `panel serve` sobre él y lo vuelve a compilar automáticamente cada vez que usted envía cambios a esa rama.

### Preparar el repositorio de la aplicación

Su repositorio necesita dos cosas: un **punto de entrada** (un archivo de Python que crea una aplicación Panel y la marca como `.servable()`) y, opcionalmente, un archivo **`requirements.txt`** con los paquetes adicionales, ya sea en la raíz del repositorio o junto a su punto de entrada.

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Hola, mundo

Cree `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

Eso es una aplicación completa. La llamada a `.servable()` es lo que PlaidCloud sirve: todo lo que desee mostrar debe marcarse como servable (directamente, o por estar dentro de un diseño servable).

#### Un ejemplo algo más completo

Las aplicaciones Panel son interactivas. Esta agrega un control deslizante que actualiza una tabla en tiempo real:

```python
import pandas as pd
import panel as pn

pn.extension()

multiplier = pn.widgets.IntSlider(name="Multiplier", start=1, end=10, value=3)

@pn.depends(multiplier)
def times_table(m):
    df = pd.DataFrame({"n": range(1, 6)})
    df["result"] = df["n"] * m
    return pn.pane.DataFrame(df, index=False)

pn.Column(
    "# Times Table",
    multiplier,
    times_table,
).servable()
```

#### Agregar dependencias

Este segundo ejemplo importa `pandas`, que no forma parte de la imagen base, así que agregue un `requirements.txt` (en la raíz del repositorio o junto a su punto de entrada):

```text
pandas
```

PlaidCloud las instala con `pip` al compilar la imagen. Las bibliotecas de visualización habituales (`plotly`, `holoviews`, `hvplot`) tampoco están en la imagen base, así que enumere aquí las que importe su aplicación.

> **Lo que la plataforma ofrece y espera.** Tenga en cuenta estos supuestos al escribir su aplicación:
>
> - **`panel` y `bokeh` están preinstalados** en la imagen base de la plataforma. No los incluya en `requirements.txt` y evite fijar una versión anterior de Panel: la reconexión de actualización en vivo depende de una versión reciente.
> - **Las bibliotecas cliente de PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) están preinstaladas.** Importe `plaidcloud.rpc` o `plaidcloud.utilities` directamente; no las incluya en `requirements.txt`.
> - **`requirements.txt` puede estar en la raíz del repositorio o junto a su punto de entrada.** En un repositorio compartido (monorepo), mantenga las dependencias de cada aplicación en su propia carpeta. Si existe un archivo en la raíz, también se instala: coloque allí las dependencias compartidas y junto a la aplicación las específicas de ella.
> - **La aplicación se ejecuta como un usuario sin privilegios de root en un sistema de archivos de solo lectura.** Solo se puede escribir en `/tmp`, así que escriba allí cualquier archivo temporal (la mayoría de las bibliotecas ya respetan `$TMPDIR`).
> - **No fije el puerto, el prefijo de URL ni el host en el código.** PlaidCloud los asigna y los inyecta en el momento de la implementación; basta con llamar a `.servable()`.

Para obtener el aspecto de PlaidCloud y filtros, cuadrículas y gráficos ya hechos, cree su aplicación con [el kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/).

### Definir el tema: claro, oscuro o con interruptor

De forma predeterminada, las aplicaciones de servidor se muestran con el diseño moderno **Fast** de PlaidCloud, un aspecto limpio de estilo Fluent aplicado en toda la plataforma. En el cuadro de diálogo de publicación, **Diseño** controla esa capa de la plataforma:

- **FAST**: el valor predeterminado de PlaidCloud. Úselo para aplicaciones nuevas y para aplicaciones creadas con plantillas Fast.
- **Predeterminado**: el estilo predeterminado de Panel. Úselo cuando el CSS o los elementos visuales de una aplicación existente fallen con FAST.

Lo que usted controla en el código de su aplicación es el **tema**: claro, oscuro o un interruptor que el usuario puede cambiar.

El tema es una propiedad de la **plantilla** que usted sirve. Las plantillas Fast (`FastListTemplate`, de una sola columna, y `FastGridTemplate`, una cuadrícula adaptable) admiten dos parámetros para ello:

- **`theme`**: `"default"` para claro o `"dark"`. Al establecerlo, la aplicación queda fijada a ese tema, aunque un usuario agregue `?theme=dark` a la URL.
- **`theme_toggle`**: `True` muestra un interruptor claro/oscuro en el encabezado; `False` lo oculta. El valor predeterminado es `True`. Ocultar el interruptor no fija el tema por sí solo: fíjelo con `theme` (más arriba); establezca `theme_toggle=False` una vez hecho, para que los usuarios no vean un interruptor que no cambia nada.

Elija el patrón que mejor se ajuste a su aplicación.

**Solo claro**: lo mejor para informes densos y tablas financieras, que suelen tener un estilo manual para un fondo claro:

```python
import panel as pn

pn.extension("tabulator")

pn.template.FastListTemplate(
    title="Sales Dashboard",
    theme="default",      # light
    theme_toggle=False,   # hide the switch
    main=[...],
).servable()
```

**Solo oscuro:**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**Dejar que el usuario elija**: por defecto es claro, con un interruptor en el encabezado. Omita `theme` para que siga el interruptor:

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Si permite el modo oscuro, haga que sus tablas lo admitan.** Un `Tabulator` fijado a un tema de tabla claro (`theme="bootstrap"`), o un CSS personalizado con colores claros codificados como `background: #fff`, se muestra como un bloque blanco ilegible en una página oscura. Use un tema de tabla que siga el de la aplicación, `pn.widgets.Tabulator(..., theme="fast")`, y evite los colores claros codificados. Si un informe tiene un estilo manual muy orientado al modo claro, fíjelo en claro (el primer patrón anterior).

Una aplicación simple sin plantilla (`pn.Column(...).servable()`) sigue el valor predeterminado de Panel y no se ve afectada por estos parámetros; recurra a una plantilla cuando desee un control explícito.

Su repositorio debe ser accesible mediante una **conexión de git** en PlaidCloud. Si su código está en [PlaidCloud Git](/es/guides/git/), cree una conexión administrada **PlaidCloud Git** en **Tools > Connections**: no requiere URL de servidor ni credenciales. Para ver todo el recorrido desde un repositorio vacío hasta una aplicación servida, consulte [Implementar una aplicación Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/).

### Publicar la aplicación

1. Haga clic en **Nueva aplicación de servidor** para abrir el cuadro de diálogo **Publicar aplicación Panel de servidor**. Su configuración se agrupa en secciones.
2. En **Configuración del directorio**:
   - **Nombre de la aplicación**: el nombre visible que se muestra en la lista.
   - **Slug de URL**: es a la vez la URL de la aplicación y su nombre interno, por lo que debe ser una etiqueta DNS válida: letras minúsculas, dígitos y guiones, que empiece por una letra y tenga 40 caracteres o menos (por ejemplo, `sales-dashboard`). El cuadro de diálogo lo comprueba antes de publicar.
   - **Nota**: una descripción opcional.
   - **Proyecto**: el proyecto al que pertenece la aplicación. Aporta la [marca](/es/guides/panel-apps/branding/) de la aplicación y es el proyecto predeterminado de sus tablas. No puede cambiarlo aquí después de publicar; use [Asignar](/es/guides/panel-apps/branding/#para-aplicaciones-existentes).
3. En **Conexión de Git y observador de publicación**:
   - **Conexión de Git**: la conexión que contiene el repositorio de su aplicación.
   - **Rama**: la rama desde la que se compila. Los envíos a esta rama vuelven a compilar y a implementar la aplicación automáticamente.
   - **Punto de entrada**: el archivo `.py` que Panel debe servir (su `app.py`).
4. En **Tiempo de ejecución**:
   - **CPU** y **Memoria** que debe solicitar el contenedor de la aplicación.

     > Con menos recursos (menos CPU y memoria), la aplicación se programa e inicia en frío más rápido.

   - **Diseño**: elija **FAST** para el diseño moderno de PlaidCloud, o **Predeterminado** si el CSS de la aplicación espera el estilo predeterminado de Panel.
   - **Inactividad (minutos)**: cuánto tiempo permanece activa la aplicación sin tráfico antes de reducirse a cero. El valor predeterminado es de 5 minutos.
   - **Permitir acceso público**: márquelo para permitir el acceso sin autenticación; de lo contrario, los usuarios deben iniciar sesión en su tenant.
5. En **Avanzado (servicio incrustado)**: opcional. De forma predeterminada, la aplicación se sirve solo desde su tenant de PlaidCloud. Para incrustarla en otro sitio, haga clic en **Agregar dominio** e introduzca cada dominio autorizado a cargarla, uno por fila: solo el host, sin esquema ni ruta (por ejemplo, `example.com` o `app.example.com:8443`). Deje la lista vacía a menos que vaya a incrustar la aplicación en otro lugar.
6. Haga clic en **Publicar**.

Después de publicar, la aplicación se **compila**: su **Estado** aparece en la lista y se actualiza automáticamente. Consulte [Usar una aplicación Panel](/es/guides/panel-apps/using/) para saber qué significan los estados, cómo abrir la aplicación cuando esté lista y cómo iniciar una recompilación sin cancelar la publicación.

> La URL de la aplicación solo funciona cuando su estado de compilación es **Lista**, y la primera solicitud tras un período de inactividad la reactiva (unos 15 segundos).

### Avanzado: reproducir PlaidCloud en local

Los usuarios técnicos pueden compilar y probar la aplicación con las mismas entradas que usa PlaidCloud. Es la comprobación local más cercana antes de publicar o de hacer clic en **Recompilar**.

PlaidCloud compila desde la rama de git seleccionada con este Dockerfile generado. Use el mismo contenido en local como `Dockerfile.plaidcloud-panel`:

```dockerfile
FROM us-docker.pkg.dev/plaidcloud-build/panel-base/platform-panel-base:0.5.1
USER root
COPY . /app
RUN if [ -f /app/requirements.txt ]; then pip install --no-cache-dir -r /app/requirements.txt; fi
# If your entry point is in a subfolder, PlaidCloud also installs that folder's requirements.txt,
# after the root one (so a per-app pin wins). Replace <app-folder> with your entry point's folder,
# or drop this line if your app is at the repository root.
RUN if [ -f "/app/<app-folder>/requirements.txt" ]; then pip install --no-cache-dir -r "/app/<app-folder>/requirements.txt"; fi
USER 10001
```

Para reproducir la compilación del servidor:

1. Obtenga la misma rama que selecciona en **Rama**.
2. Ejecute la compilación desde la raíz del repositorio, para que `COPY . /app` coincida con PlaidCloud.
3. Coloque las dependencias opcionales en un `requirements.txt`, en la raíz del repositorio o junto a su punto de entrada. Se instalan ambos, el de la carpeta de la aplicación en último lugar (para que prevalezca una fijación específica de la aplicación).
4. Use la misma ruta del punto de entrada que selecciona en **Punto de entrada**.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

La imagen implementada no reemplaza el punto de entrada de la imagen base. Ejecuta `panel serve` a partir de variables de entorno inyectadas por PlaidCloud. Pruebe la imagen compilada con el mismo contrato de ejecución:

```sh
docker run --rm \
  --cpus 0.5 \
  --memory 512m \
  -p 5006:5006 \
  -e APP_PATH=/app/app.py \
  -e PANEL_PREFIX=/serve/local \
  -e PANEL_PORT=5006 \
  -e PANEL_ORIGIN=localhost:5006 \
  -e PANEL_KEEP_ALIVE_MS=25000 \
  -e PLAID_PANEL_DESIGN=fast \
  local-panel-app:plaidcloud
```

Abra `http://localhost:5006/serve/local/`.

Haga coincidir la configuración del cuadro de diálogo de publicación al probar:

- **Punto de entrada** corresponde a `APP_PATH=/app/<entry-point>`.
- **CPU** y **Memoria** corresponden a los límites `--cpus` y `--memory` de Docker.
- **Diseño: FAST** corresponde a `PLAID_PANEL_DESIGN=fast`.
- **Diseño: Predeterminado** significa omitir `PLAID_PANEL_DESIGN`.
- **Inactividad (minutos)** corresponde a la ventana de reducción de escala de la implementación. Docker local no la aplica, pero la aplicación sigue usando la misma configuración de mantenimiento de conexión de websocket y de limpieza de sesiones de Panel.
- Los dominios de **servicio incrustado** corresponden a `PANEL_ORIGIN`; use una lista separada por espacios si necesita probar más de un host.

Si no necesita un contenedor, igualmente puede probar la capa de servicio desde un entorno local de Python. Instale el mismo `requirements.txt`, defina las variables de entorno de la plataforma y luego ejecute `panel serve` con los mismos indicadores que usa la imagen implementada.

```sh
export APP_PATH=app.py
export PANEL_PREFIX=/serve/local
export PANEL_PORT=5006
export PANEL_ORIGIN=localhost:5006
export PANEL_KEEP_ALIVE_MS=25000
export PLAID_PANEL_DESIGN=fast

panel serve "$APP_PATH" \
  --address 0.0.0.0 \
  --port "$PANEL_PORT" \
  --prefix "$PANEL_PREFIX" \
  --allow-websocket-origin "$PANEL_ORIGIN" \
  --num-procs 1 \
  --keep-alive "$PANEL_KEEP_ALIVE_MS" \
  --unused-session-lifetime 15000 \
  --index "$(basename "$APP_PATH" .py)"
```

Abra `http://localhost:5006/serve/local/`.

Use `PLAID_PANEL_DESIGN=fast` para reproducir el aspecto predeterminado de la implementación. Para probar la opción de diseño **Predeterminado** del cuadro de diálogo de publicación, deje `PLAID_PANEL_DESIGN` sin definir y ejecute el mismo comando. Conserve `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive` y `--unused-session-lifetime`; forman parte del contrato de ejecución de la implementación.

## Crear una aplicación WASM

Una aplicación WASM se ejecuta en el navegador a partir de un archivo HTML ya compilado.

1. Haga clic en **Agregar aplicación WASM** para abrir el cuadro de diálogo **Publicar aplicación Panel sin servidor**.
2. Escriba un **Nombre de la aplicación** y una **Versión**.
3. Elija la **Ubicación HTML de la aplicación**: el archivo HTML en una cuenta de documentos.
4. Escriba un **Slug de URL de la aplicación** y una **Nota** opcional.
5. Haga clic en **Publicar**. Una aplicación WASM no tiene paso de compilación y se sirve de inmediato.
