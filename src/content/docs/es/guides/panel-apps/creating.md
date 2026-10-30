---
title: Creación de una aplicación Panel
description: Publique en PlaidCloud una aplicación Panel de HoloViz del lado del servidor desde un repositorio git (con un ejemplo de hola mundo), o una aplicación WASM estática desde un archivo.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Abra **Mis aplicaciones Panel**. La barra de herramientas ofrece dos formas de publicar, una por [tiempo de ejecución](/es/guides/panel-apps/):

- **Nueva aplicación de servidor**: compile y ejecute una aplicación desde un repositorio git.
- **Agregar aplicación WASM**: publique una aplicación estática dentro del navegador desde un archivo.

Para escribir la aplicación en PlaidCloud, sin necesidad de configurar un repositorio, use [Panel Studio](/es/guides/panel-apps/studio/).

## Creación de una aplicación de servidor

Una aplicación de servidor se compila desde un repositorio git y se sirve en `https://<your-tenant-host>/serve/<slug>/`. Usted indica a PlaidCloud una rama de un repositorio; PlaidCloud compila el código en un contenedor, ejecuta `panel serve` sobre él y vuelve a compilar automáticamente cada vez que usted hace push a esa rama.

### Preparar el repositorio de su aplicación

Su repositorio necesita dos cosas: un **punto de entrada** (un archivo Python que crea una aplicación Panel y la marca como `.servable()`) y, opcionalmente, un **`requirements.txt`** que enumere los paquetes adicionales, ya sea en la raíz del repositorio o junto a su punto de entrada.

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Hola mundo

Cree `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

Esa es una aplicación completa. La llamada a `.servable()` es lo que PlaidCloud sirve: todo lo que desee mostrar debe marcarse como servable (directamente, o estando dentro de un diseño servable).

#### Un ejemplo algo más completo

Las aplicaciones Panel son interactivas. Esta agrega un control deslizante que actualiza una tabla en vivo:

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

PlaidCloud las instala con `pip` cuando compila la imagen. Las bibliotecas de visualización habituales (`plotly`, `holoviews`, `hvplot`) tampoco están en la imagen base, así que enumere aquí las que importe su aplicación.

> **Lo que la plataforma proporciona y espera.** Tenga en cuenta estos supuestos al escribir su aplicación:
>
> - **`panel` y `bokeh` están preinstalados** en la imagen base de la plataforma. No los enumere en `requirements.txt` y evite fijar una versión anterior de Panel: la reconexión de actualización en vivo depende de una versión reciente.
> - **Las bibliotecas cliente de PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) están preinstaladas.** Importe `plaidcloud.rpc` o `plaidcloud.utilities` directamente; no las enumere en `requirements.txt`.
> - **`requirements.txt` puede estar en la raíz del repositorio o junto a su punto de entrada.** En un repositorio compartido (monorrepositorio), mantenga las dependencias de cada aplicación en su propia carpeta. Si existe un archivo en la raíz, también se instala: ponga allí las dependencias compartidas y las específicas de la aplicación junto a ella.
> - **La aplicación se ejecuta como un usuario sin privilegios de administrador en un sistema de archivos de solo lectura.** Solo `/tmp` admite escritura, así que escriba allí los archivos temporales (la mayoría de las bibliotecas ya respetan `$TMPDIR`).
> - **No codifique de forma fija el puerto, el prefijo de URL ni el host.** PlaidCloud los asigna y los inyecta en el momento de la implementación: simplemente llame a `.servable()`.

Para obtener el aspecto de PlaidCloud y filtros, cuadrículas y gráficos listos para usar, cree su aplicación con [el kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/).

### Definir el tema: claro, oscuro o con interruptor

Las aplicaciones de servidor se muestran de forma predeterminada con el moderno diseño **Fast** de PlaidCloud, un aspecto limpio al estilo Fluent aplicado en toda la plataforma. En el cuadro de diálogo de publicación, **Diseño** controla esa capa de la plataforma:

- **FAST**: el valor predeterminado de PlaidCloud. Úselo para aplicaciones nuevas y para aplicaciones creadas con plantillas Fast.
- **Predeterminado**: el estilo predeterminado de Panel. Úselo cuando el CSS o los elementos visuales de una aplicación existente fallen con FAST.

Lo que usted controla en el código de su aplicación es el **tema**: claro, oscuro o un interruptor que el visualizador puede cambiar.

El tema es una propiedad de la **plantilla** que usted sirve. Las plantillas Fast (`FastListTemplate`, de una sola columna, y `FastGridTemplate`, una cuadrícula adaptable) admiten dos parámetros para ello:

- **`theme`**: `"default"` para claro o `"dark"`. Al establecerlo, la aplicación queda fijada a ese tema, incluso si un visualizador agrega `?theme=dark` a la URL.
- **`theme_toggle`**: `True` muestra un interruptor claro/oscuro en el encabezado; `False` lo oculta. De forma predeterminada es `True`. Ocultar el interruptor no fija el tema por sí solo: fíjelo con `theme` (arriba); establezca `theme_toggle=False` una vez que lo haya hecho, para que los visualizadores no vean un interruptor que no cambia nada.

Elija el patrón que se ajuste a su aplicación.

**Solo claro**: lo mejor para informes densos y tablas financieras, que normalmente se diseñan a mano para un fondo claro:

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

**Que elija el visualizador**: el valor predeterminado es claro, con un interruptor en el encabezado. Omita `theme` para que siga el interruptor:

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Si permite el modo oscuro, haga que sus tablas lo reconozcan.** Un `Tabulator` fijado a un tema de tabla claro (`theme="bootstrap"`), o un CSS personalizado con colores claros fijos como `background: #fff`, se muestra como un bloque blanco ilegible en una página oscura. Use un tema de tabla que siga a la aplicación (`pn.widgets.Tabulator(..., theme="fast")`) y evite los colores claros fijos. Si un informe está muy diseñado a mano para el modo claro, fíjelo en claro (el primer patrón anterior).

Una aplicación simple sin plantilla (`pn.Column(...).servable()`) sigue el valor predeterminado de Panel y no se ve afectada por estas opciones; recurra a una plantilla cuando desee un control explícito.

Su repositorio debe ser accesible a través de una **conexión de Git** en PlaidCloud. Si su código está en [PlaidCloud Git](/es/guides/git/), cree una conexión administrada de **PlaidCloud Git** en **Tools > Connections**: no necesita URL de servidor ni credenciales. Para ver todo el recorrido, desde un repositorio vacío hasta una aplicación servida, consulte [Implementar una aplicación Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/).

### Publicar la aplicación

1. Haga clic en **Nueva aplicación de servidor** para abrir el cuadro de diálogo **Publicar aplicación Panel de servidor**. Su configuración está agrupada en secciones.
2. En **Configuración del directorio**:
   - **Nombre de la aplicación**: el nombre para mostrar que aparece en la lista.
   - **Slug de URL**: es tanto la URL de la aplicación como su nombre interno, por lo que debe ser una etiqueta DNS válida: letras minúsculas, dígitos y guiones, que empiece con una letra, de 40 caracteres o menos (por ejemplo, `sales-dashboard`). El cuadro de diálogo lo comprueba antes de publicar.
   - **Nota**: una descripción opcional.
   - **Proyecto**: el proyecto propietario de la aplicación. Proporciona la [marca](/es/guides/panel-apps/branding/) de la aplicación y es el proyecto predeterminado para sus tablas. No puede cambiarlo aquí después de publicar; use [Asignar](/es/guides/panel-apps/branding/#para-aplicaciones-existentes).
3. En **Conexión de Git y observador de publicación**:
   - **Conexión de Git**: la conexión que contiene el repositorio de su aplicación.
   - **Rama**: la rama desde la que se compila. Los push a esta rama vuelven a compilar y a implementar la aplicación automáticamente.
   - **Punto de entrada**: el archivo `.py` que Panel debe servir (su `app.py`).
4. En **Tiempo de ejecución**:
   - **CPU** y **Memoria** que debe solicitar el contenedor de la aplicación.

     > Menos recursos (menor CPU o memoria) permiten que la aplicación se programe y arranque en frío más rápido.

   - **Diseño**: elija **FAST** para el diseño moderno de PlaidCloud, o **Predeterminado** si el CSS de la aplicación espera el estilo predeterminado de Panel.
   - **Inactividad (minutos)**: cuánto tiempo permanece activa la aplicación sin tráfico antes de reducirse a cero. El valor predeterminado es 5 minutos.
   - **Permitir acceso público**: márquelo para permitir el acceso sin autenticación; de lo contrario, los visualizadores deben iniciar sesión en su inquilino.
5. En **Avanzado (servicio incrustado)**, que es opcional. De forma predeterminada, la aplicación se sirve solo desde su inquilino de PlaidCloud. Para incrustarla en otro sitio, haga clic en **Agregar dominio** e ingrese cada dominio autorizado para cargarla, uno por fila: solo un host, sin esquema ni ruta (por ejemplo, `example.com` o `app.example.com:8443`). Deje la lista vacía a menos que vaya a incrustar la aplicación en otro lugar.
6. Haga clic en **Publicar**.

Después de publicar, la aplicación se **compila**: su **Estado** aparece en la lista y se actualiza automáticamente. Consulte [Uso de una aplicación Panel](/es/guides/panel-apps/using/) para saber qué significan los estados, cómo abrir la aplicación cuando está lista y cómo activar una nueva compilación sin anular la publicación.

> La URL de la aplicación funciona solo cuando su estado de compilación es **Lista**, y la primera solicitud después de un período de inactividad la reactiva (~15 segundos).

### Avanzado: reproducir PlaidCloud en local

Los usuarios técnicos pueden compilar y probar la aplicación con las mismas entradas que usa PlaidCloud. Esta es la comprobación local más cercana antes de publicar o de hacer clic en **Recompilar**.

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
3. Ponga las dependencias opcionales en un `requirements.txt`, en la raíz del repositorio o junto a su punto de entrada. Se instalan ambos, el de la carpeta de la aplicación en último lugar (para que prevalezca la versión fijada por aplicación).
4. Use la misma ruta de punto de entrada que selecciona en **Punto de entrada**.

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

Haga coincidir la configuración del cuadro de diálogo de publicación cuando pruebe:

- **Punto de entrada** corresponde a `APP_PATH=/app/<entry-point>`.
- **CPU** y **Memoria** corresponden a los límites `--cpus` y `--memory` de Docker.
- **Diseño: FAST** corresponde a `PLAID_PANEL_DESIGN=fast`.
- **Diseño: Predeterminado** significa omitir `PLAID_PANEL_DESIGN`.
- **Inactividad (minutos)** corresponde a la ventana de reducción de la implementación. Docker local no la aplica, pero la aplicación sigue usando la misma configuración de keepalive de websocket y de limpieza de sesiones de Panel.
- Los dominios de **Avanzado (servicio incrustado)** corresponden a `PANEL_ORIGIN`; use una lista separada por espacios si necesita probar más de un host.

Si no necesita un contenedor, aún puede probar la capa de servicio desde un entorno local de Python. Instale el mismo `requirements.txt`, establezca las variables de entorno de la plataforma y luego ejecute `panel serve` con los mismos indicadores que usa la imagen implementada.

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

Use `PLAID_PANEL_DESIGN=fast` para reproducir el aspecto predeterminado implementado. Para probar la opción de diseño **Predeterminado** del cuadro de diálogo de publicación, deje `PLAID_PANEL_DESIGN` sin establecer y ejecute el mismo comando. Mantenga `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive` y `--unused-session-lifetime`; forman parte del contrato de ejecución implementado.

## Creación de una aplicación WASM

Una aplicación WASM se ejecuta en el navegador desde un archivo HTML precompilado.

1. Haga clic en **Agregar aplicación WASM** para abrir el cuadro de diálogo **Publicar aplicación Panel sin servidor**.
2. Escriba un **Nombre de la aplicación** y una **Versión**.
3. Elija la **Ubicación HTML de la aplicación**: el archivo HTML en una cuenta de documentos.
4. Escriba un **Slug de URL de la aplicación** y una **Nota** opcional.
5. Haga clic en **Publicar**. Una aplicación WASM no tiene paso de compilación y se sirve de inmediato.
