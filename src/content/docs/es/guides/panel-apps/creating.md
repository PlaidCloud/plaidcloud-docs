---
title: Creación de una aplicación de Panel
description: Cree una aplicación de Panel en Panel Studio, a partir de una aplicación en blanco, una tabla, una vista o la galería, o publique una aplicación de servidor desde git o una aplicación WASM estática para necesidades a medida.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Comience con Panel Studio. No necesita repositorio ni configuración: usted crea la aplicación en PlaidCloud, la previsualiza y la publica cuando esté listo. Elija un tiempo de ejecución a medida solo cuando Studio no se ajuste a sus necesidades.

## Creación de una aplicación Studio

Abra **Aplicaciones** y abra el menú **Nueva aplicación**. Bajo el encabezado **Aplicación Panel**, **Studio** escribe y publica la aplicación en el editor de PlaidCloud con el diseño estándar y conserva el código por usted. También puede elegir **Nueva aplicación Studio** en la fila **Aplicaciones Studio** de la tarjeta **Aplicaciones y marca** de la pestaña **Inicio** de un proyecto, o [comenzar desde una tabla](#comenzar-desde-una-tabla).

1. Elija **Nueva aplicación** > **Studio**.
2. Introduzca un **Nombre**. El **Slug de la URL** se completa a partir de él.
3. Elija el **Proyecto** propietario de la aplicación. Necesita acceso de edición al proyecto.
4. En **Comenzar desde**, elija dónde empieza la aplicación:

   | Comenzar desde | Qué obtiene |
   |---|---|
   | **Aplicación en blanco** | Una aplicación mínima con un `app.py` y un `requirements.txt`. |
   | **Desde una tabla** | Una aplicación creada sobre la tabla que elija. |
   | **Desde una vista** | Lo mismo, creada sobre una vista del proyecto. |
   | **Desde otra aplicación Studio** | Una copia de una de sus aplicaciones Studio. |
   | **Desde la galería** | Una copia de una aplicación que su espacio de trabajo [incluyó en la galería](#comenzar-desde-la-galería). |

5. Elija **Crear**. Studio abre la aplicación nueva. Para una tabla o una vista, el mensaje de Weave para crear la primera página está listo para enviarse.

Consulte [Panel Studio](/es/guides/panel-apps/studio/) para editar, previsualizar y publicar la aplicación.

### Comenzar desde una tabla

También puede empezar en la pestaña **Tablas** de un proyecto. Seleccione una tabla o vista y luego elija **Crear aplicación Panel** en el menú **Nuevo** o en el menú contextual. Se abre el cuadro de diálogo **Nueva aplicación Studio** con el proyecto y la tabla ya elegidos. El comando está disponible cuando tiene acceso de edición al proyecto y el proyecto no es de solo lectura.

### Comenzar desde la galería

Elija **Nueva aplicación** > **Desde la galería…** para explorar las aplicaciones que su espacio de trabajo ha incluido y luego **Crear aplicación a partir de esto…** para hacer su propia copia. O elija **Desde la galería** en el cuadro de diálogo **Nueva aplicación Studio**. Consulte [La galería de aplicaciones](/es/guides/panel-apps/gallery/), incluido cómo incluir su propia aplicación.

## Otros tiempos de ejecución

Las aplicaciones Studio cubren la mayoría de los paneles de control y herramientas. Para una necesidad a medida, publique con uno de los otros [tiempos de ejecución](/es/guides/panel-apps/) desde el menú **Nueva aplicación**:

- **Solo navegador**: su propio repositorio; la aplicación se ejecuta en el navegador de quien la visualiza.
- **Basada en servidor**: su propio repositorio; la aplicación se ejecuta en un servidor de PlaidCloud, por ejemplo para reutilizar código existente o su propio proceso de compilación.
- **Aplicación de Dash**: publique una aplicación de Plotly Dash. Consulte [Aplicaciones de Dash](/es/guides/dash-apps/).

## Creación de una aplicación de servidor

Una aplicación de servidor se crea a partir de un repositorio git y se sirve en `https://<your-tenant-host>/serve/<slug>/`. Usted apunta PlaidCloud a una rama de un repositorio; este compila el código en un contenedor, ejecuta `panel serve` sobre él y vuelve a compilar automáticamente cada vez que usted envía cambios a esa rama.

### Preparación del repositorio de su aplicación

Su repositorio necesita dos cosas: un **punto de entrada**, un archivo de Python que crea una aplicación de Panel y la marca con `.servable()`, y, opcionalmente, un **`requirements.txt`** que enumere los paquetes adicionales, ya sea en la raíz del repositorio o junto a su punto de entrada.

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Hello World

Cree `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

Eso es una aplicación completa. La llamada `.servable()` es lo que PlaidCloud sirve: todo lo que desee mostrar debe marcarse como servible (directamente o por estar dentro de un diseño servible).

#### Un ejemplo algo más completo

Las aplicaciones de Panel son interactivas. Esta agrega un control deslizante que actualiza una tabla en vivo:

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

Este segundo ejemplo importa `pandas`, que no forma parte de la imagen base, por lo que debe agregar un `requirements.txt` (en la raíz del repositorio o junto a su punto de entrada):

```text
pandas
```

PlaidCloud las instala con `pip` cuando compila la imagen. Las bibliotecas de visualización habituales (`plotly`, `holoviews`, `hvplot`) tampoco están en la imagen base, así que enumere aquí las que importe su aplicación.

> **Lo que la plataforma proporciona y espera.** Tenga en cuenta estas suposiciones al escribir su aplicación:
>
> - **`panel` y `bokeh` están preinstalados** en la imagen base de la plataforma. No los enumere en `requirements.txt` y evite fijar una versión anterior de Panel: la reconexión de actualización en vivo depende de una versión reciente.
> - **Las bibliotecas cliente de PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) están preinstaladas.** Importe `plaidcloud.rpc` o `plaidcloud.utilities` directamente; no las enumere en `requirements.txt`.
> - **`requirements.txt` puede estar en la raíz del repositorio o junto a su punto de entrada.** En un repositorio compartido (monorrepositorio), mantenga las dependencias de cada aplicación en su propia carpeta. Un archivo en la raíz, si existe, también se instala: coloque allí las dependencias compartidas y las específicas de la aplicación junto a ella.
> - **La aplicación se ejecuta como un usuario sin privilegios de administrador en un sistema de archivos de solo lectura.** Solo `/tmp` admite escritura, así que escriba allí los archivos temporales (la mayoría de las bibliotecas ya respetan `$TMPDIR`).
> - **No codifique de forma fija el puerto, el prefijo de URL ni el host.** PlaidCloud los asigna y los inyecta en el momento de la implementación: simplemente llame a `.servable()`.

Para obtener el aspecto de PlaidCloud y filtros, cuadrículas y gráficos listos para usar, cree su aplicación con [el kit de aplicaciones de Panel](/es/guides/panel-apps/app-kit/).

### Definir el tema: claro, oscuro o un interruptor

De forma predeterminada, las aplicaciones de servidor se muestran con el diseño moderno **Fast** de PlaidCloud: un aspecto limpio, al estilo Fluent, aplicado en toda la plataforma. En el cuadro de diálogo de publicación, **Diseño** controla esa capa de la plataforma:

- **FAST**: el valor predeterminado de PlaidCloud. Úselo para aplicaciones nuevas y aplicaciones creadas con plantillas Fast.
- **Predeterminado**: el estilo predeterminado de Panel. Úselo cuando el CSS o los elementos visuales de una aplicación existente se rompan con FAST.

Lo que usted controla en el código de su aplicación es el **tema**: claro, oscuro o un interruptor que quien visualiza puede alternar.

El tema es una propiedad de la **plantilla** que usted sirve. Las plantillas Fast (`FastListTemplate`, de una sola columna, y `FastGridTemplate`, una cuadrícula adaptable) admiten dos configuraciones para ello:

- **`theme`**: `"default"` para claro o `"dark"`. Al establecerlo, la aplicación queda fijada a ese tema, incluso si quien visualiza agrega `?theme=dark` a la URL.
- **`theme_toggle`**: `True` muestra un interruptor claro/oscuro en el encabezado; `False` lo oculta. El valor predeterminado es `True`. Ocultar el interruptor no fija el tema por sí solo: fíjelo con `theme` (arriba); establezca `theme_toggle=False` una vez que lo haya hecho, para que quienes visualizan no vean un interruptor que no puede cambiar nada.

Elija el patrón que se ajuste a su aplicación.

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

**Que elija quien visualiza**: el valor predeterminado es claro, con un interruptor en el encabezado. Omita `theme` para que siga el interruptor:

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Si permite el modo oscuro, haga que sus tablas lo admitan.** Un `Tabulator` fijado a un tema de tabla claro (`theme="bootstrap"`), o un CSS personalizado con colores claros codificados de forma fija como `background: #fff`, se muestra como un bloque blanco ilegible en una página oscura. Use un tema de tabla que siga a la aplicación (`pn.widgets.Tabulator(..., theme="fast")`) y evite los colores claros codificados de forma fija. Si un informe tiene un estilo manual muy orientado a lo claro, fíjelo en claro (el primer patrón anterior).

Una aplicación simple sin plantilla (`pn.Column(...).servable()`) sigue el valor predeterminado de Panel y no se ve afectada por estas configuraciones; recurra a una plantilla cuando quiera un control explícito.

Su repositorio debe ser accesible mediante una **conexión de git** en PlaidCloud. Si su código está en [PlaidCloud Git](/es/guides/git/), cree una conexión administrada de **PlaidCloud Git** en **Tools > Connections**: no necesita URL de servidor ni credenciales. Para ver todo el recorrido desde un repositorio vacío hasta una aplicación servida, consulte [Implementar una aplicación de Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/).

### Publicación de la aplicación

1. Elija **Nueva aplicación** > **Basada en servidor** para abrir el cuadro de diálogo **Publicar aplicación Panel de servidor**. Su configuración está agrupada en secciones.
2. En **Configuración del directorio**:
   - **Nombre de la aplicación**: el nombre para mostrar que aparece en la lista.
   - **Slug de URL**: es tanto la URL de la aplicación como su nombre interno, por lo que debe ser una etiqueta DNS válida: letras minúsculas, dígitos y guiones, que empiece por una letra y tenga 40 caracteres o menos (por ejemplo, `sales-dashboard`). El cuadro de diálogo lo comprueba antes de que publique.
   - **Nota**: una descripción opcional.
   - **Proyecto**: el proyecto propietario de la aplicación. Aporta la [marca](/es/guides/panel-apps/branding/) de la aplicación y es el proyecto predeterminado de sus tablas. No puede cambiarlo aquí después de publicar; utilice [Assign](/es/guides/panel-apps/branding/#para-aplicaciones-existentes).
3. En **Conexión de Git y observador de publicación**:
   - **Conexión de Git**: la conexión que contiene el repositorio de su aplicación.
   - **Rama**: la rama desde la que compilar. Los envíos a esta rama vuelven a compilar y a implementar la aplicación automáticamente.
   - **Punto de entrada**: el archivo `.py` que Panel debe servir (su `app.py`).
4. En **Tiempo de ejecución**:
   - **CPU** y **Memoria** que debe solicitar el contenedor de la aplicación.

     > Menos recursos (menos CPU / memoria) permiten que la aplicación se programe y arranque en frío más rápido.

   - **Diseño**: elija **FAST** para el diseño moderno de PlaidCloud, o **Predeterminado** si el CSS de la aplicación espera el estilo predeterminado de Panel.
   - **Inactividad (minutos)**: cuánto tiempo permanece activa la aplicación sin tráfico antes de reducirse a cero. El valor predeterminado es 5 minutos.
   - **Permitir acceso público**: márquelo para permitir el acceso sin autenticación; de lo contrario, quienes visualizan deben iniciar sesión en su inquilino.
5. En **Avanzado (servicio incrustado)**, opcional. De forma predeterminada, la aplicación se sirve solo desde su inquilino de PlaidCloud. Para incrustarla en otro sitio, haga clic en **Agregar dominio** e introduzca cada dominio al que se permite cargarla, uno por fila: solo el host, sin esquema ni ruta (por ejemplo, `example.com` o `app.example.com:8443`). Deje la lista vacía a menos que vaya a incrustar la aplicación en otro lugar.
6. Haga clic en **Publicar**.

Después de publicar, la aplicación se **compila**: su **Estado** aparece en la lista y se actualiza automáticamente. Consulte [Uso de una aplicación de Panel](/es/guides/panel-apps/using/) para saber qué significan los estados, cómo abrir la aplicación cuando esté lista y cómo activar una recompilación sin anular la publicación.

> La URL de la aplicación solo funciona cuando su estado de compilación es **Lista**, y la primera solicitud después de un período de inactividad la reactiva (unos 15 segundos).

### Avanzado: reproducir PlaidCloud en local

Los usuarios técnicos pueden compilar y probar la aplicación con las mismas entradas que usa PlaidCloud. Esta es la comprobación local más cercana antes de publicar o de hacer clic en **Recompilar**.

PlaidCloud compila a partir de la rama de git seleccionada con este Dockerfile generado. Utilice el mismo contenido en local como `Dockerfile.plaidcloud-panel`:

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
3. Coloque las dependencias opcionales en un `requirements.txt`, en la raíz del repositorio o junto a su punto de entrada. Se instalan ambos, el de la carpeta de la aplicación en último lugar (para que prevalezca una fijación por aplicación).
4. Utilice la misma ruta de punto de entrada que selecciona en **Punto de entrada**.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

La imagen implementada no reemplaza el punto de entrada de la imagen base. Ejecuta `panel serve` a partir de las variables de entorno que inyecta PlaidCloud. Pruebe la imagen compilada con el mismo contrato de ejecución:

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

- **Punto de entrada** se corresponde con `APP_PATH=/app/<entry-point>`.
- **CPU** y **Memoria** se corresponden con los límites `--cpus` y `--memory` de Docker.
- **Diseño: FAST** se corresponde con `PLAID_PANEL_DESIGN=fast`.
- **Diseño: Predeterminado** significa omitir `PLAID_PANEL_DESIGN`.
- **Inactividad (minutos)** se corresponde con la ventana de reducción de escala de la implementación. Docker local no la aplica, pero la aplicación sigue usando la misma configuración de keepalive de websocket y de limpieza de sesiones de Panel.
- Los dominios de **Servicio incrustado** se corresponden con `PANEL_ORIGIN`; use una lista separada por espacios si necesita probar más de un host.

Si no necesita un contenedor, aún puede probar la capa de servicio desde un entorno local de Python. Instale el mismo `requirements.txt`, defina las variables de entorno de la plataforma y luego ejecute `panel serve` con las mismas opciones que usa la imagen implementada.

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

Utilice `PLAID_PANEL_DESIGN=fast` para reproducir el aspecto implementado predeterminado. Para probar la opción de diseño **Predeterminado** del cuadro de diálogo de publicación, deje `PLAID_PANEL_DESIGN` sin definir y ejecute el mismo comando. Mantenga `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive` y `--unused-session-lifetime`; forman parte del contrato de ejecución implementado.

## Creación de una aplicación WASM

Una aplicación WASM se ejecuta en el navegador a partir de un archivo HTML precompilado.

1. Elija **Nueva aplicación** > **Solo navegador** para abrir el cuadro de diálogo **Publicar aplicación Panel sin servidor**.
2. Introduzca un **Nombre de la aplicación** y una **Versión**.
3. Elija la **Ubicación HTML de la aplicación**: el archivo HTML de una cuenta de documentos.
4. Introduzca un **Slug de URL de la aplicación** y una **Nota** opcional.
5. Haga clic en **Publicar**. Una aplicación WASM no tiene paso de compilación y se sirve de inmediato.
