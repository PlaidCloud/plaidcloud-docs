---
title: Lectura de datos y del usuario con sesión iniciada en una aplicación Dash
description: "Conecte una aplicación Dash a PlaidCloud como la persona que la está viendo: lea datos del proyecto y use la identidad del espectador para el comportamiento por usuario y la seguridad a nivel de fila."
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/accessing-data.md
---

Una aplicación Dash puede leer sus datos de PlaidCloud, y lo hace **como la persona que la está viendo**, igual que una aplicación Panel de servidor. Cuando alguien abre la aplicación, PlaidCloud le inicia sesión con el mismo inicio de sesión único que usa el resto de la plataforma, y cada llamada que realiza su aplicación se ejecuta con **los permisos propios de ese espectador**. No hay ninguna cuenta de servicio compartida, y la aplicación nunca puede ver datos que el espectador no podría ver por sí mismo.

Los asistentes se encuentran en `plaidcloud_dash`, que forma parte de la imagen base de Dash:

```python
from plaidcloud_dash import current_user, get_connection
```

## Conectarse a PlaidCloud

Llame a `get_connection()` desde dentro de un callback de Dash, indicando el proyecto cuyos datos desea leer:

```python
from plaidcloud_dash import get_connection

conn = get_connection(project_id="<your-project-id>")
```

Esa es toda la configuración que necesita. **No** debe proporcionar un token, un nombre de usuario ni una contraseña: `get_connection()` se autentica automáticamente como el espectador con sesión iniciada, usando el token de acceso de su sesión actual. Encuentre el id de su proyecto en la URL del proyecto o en su página de configuración.

> **Llámela desde dentro de un callback.** `get_connection()` lee el token del espectador de la sesión de Flask de la solicitud actual, que solo está disponible mientras un callback atiende la solicitud de ese espectador. Si envía una llamada bloqueante a un subproceso en segundo plano, un grupo de subprocesos sin procesar no transportará la sesión: lea el token dentro del callback y páselo de forma explícita. Llamar a `get_connection()` fuera de una solicitud (o con la autenticación desactivada) genera un `RuntimeError` en lugar de devolver sin avisar una conexión sin ninguna identidad detrás.

> **Indique su proyecto en el código.** El cuadro de diálogo de publicación no tiene ninguna opción de proyecto: una aplicación Dash lee el proyecto que usted indique en `get_connection(project_id=...)`, igual que `PlaidConnection(project_id=...)` en una aplicación Panel de servidor; consulte [Lectura de datos y del usuario con sesión iniciada](/es/guides/panel-apps/accessing-data/). Un `get_connection()` sin `project_id` es válido para una aplicación que nunca toca datos del proyecto (una que solo llama a `current_user()`, por ejemplo); si invoca una operación con alcance de proyecto en esa conexión sin un id de proyecto real y accesible, se genera `Project Id has not been set`. (Para leer de más de un proyecto, abra una conexión por proyecto).

### Leer una tabla

Con una conexión, cargue una tabla en un DataFrame de pandas por su nombre:

```python
df = conn.get_dataframe("Sales Ledger")
```

Como la conexión es el espectador, esto devuelve solo las filas que el espectador puede ver, y genera un error de permisos si no tiene ningún acceso al proyecto.

> **Lea las tablas por nombre, no escribiendo SQL.** En un proyecto donde un administrador ha activado el [Acceso a filas](/es/administration/access/managing-security-groups-and-assignments/#acceso-a-filas-y-consultas-que-usted-escribe), leer por nombre aplica los permisos de fila de cada espectador, mientras que una consulta que su aplicación compone por sí misma se rechaza para cualquiera que no sea Arquitecto del proyecto, porque no existe una única tabla que los permisos puedan filtrar. Leer por nombre mantiene su aplicación funcionando en ambos casos.

## Leer dentro de un callback, nunca en el ámbito de importación o de proceso

Un solo proceso atiende a todos los espectadores. Lograr un aislamiento correcto de los datos se reduce a dos reglas:

- **Nunca abra una conexión ni lea una tabla en el ámbito del módulo (al importar).** Su `app.py` y cualquier módulo que importe se ejecutan **una sola vez**, cuando se inicia el contenedor, antes de que nadie haya iniciado sesión. Un `get_connection()` o `PlaidConnection()` allí no tiene ningún espectador con el que autenticarse y hace fallar la aplicación al arrancar (esta es la causa más común de un bucle de fallos de “la aplicación no se inició”). Mantenga toda lectura dentro de un callback, donde está presente la solicitud del espectador y, con ella, su token de sesión.

- **Nunca almacene en caché un resultado por espectador en el ámbito del módulo o del proceso.** El worker de gunicorn con subprocesos comparte un único proceso de Python entre todos los espectadores simultáneos, por lo que un DataFrame que guarde en una variable a nivel de módulo, en un diccionario global o en un `lru_cache` es visible para *todos* los demás espectadores: las filas de una persona se filtran a la vista de otra. Calcule los datos por espectador dentro del callback y deje que salgan del ámbito cuando el callback termine:

  ```python
  # WRONG — a module/process-global cache is shared across all viewers
  _CACHE = {}

  @app.callback(...)
  def _load(n):
      viewer = current_user()
      if viewer not in _CACHE:                      # still process-global; leaks under load
          _CACHE[viewer] = get_connection(project_id="…").get_dataframe("Sales")
      return _CACHE[viewer].to_dict("records")

  # RIGHT — read inside the callback, no shared state
  @app.callback(...)
  def _load(n):
      conn = get_connection(project_id="…")          # this viewer, this request
      return conn.get_dataframe("Sales").to_dict("records")
  ```

### Datos de referencia compartidos

Si varios espectadores necesitan realmente los *mismos* datos de referencia (una tabla de búsqueda, una lista de productos), no intente compartirlos mediante una caché a nivel de proceso. Otorgue esas tablas a los usuarios de la aplicación mediante los [permisos de proyecto y el Acceso a filas](/es/administration/access/managing-security-groups-and-assignments/) normales de PlaidCloud, y deje que cada espectador las lea con su propio `get_connection()`. Todos obtienen las mismas filas de referencia porque a todos se les concedió el mismo acceso, no porque la lectura de un espectador se reutilice para otro.

## Identificar al espectador

Para adaptar lo que muestra la aplicación a **quién la está viendo** (un saludo personalizado, ocultar una pestaña o la seguridad a nivel de fila), llame a `current_user()`:

```python
from plaidcloud_dash import current_user

viewer = current_user()  # the viewer's identifier
```

`current_user()` devuelve el identificador del espectador con sesión iniciada (su nombre de usuario o, si no hay una declaración de nombre de usuario, su correo electrónico y después su id de cuenta), tomado de su inicio de sesión verificado, de modo que puede confiar en él como su identidad. Nunca genera una excepción; si se llama con la autenticación desactivada o fuera de una solicitud, devuelve una cadena vacía.

### Seguridad a nivel de fila

Combine ambas cosas: lea el espectador y luego filtre cada consulta por él. Por ejemplo, para mostrar a cada gerente regional solo su propia región:

```python
from dash import Input, Output
from plaidcloud_dash import current_user, get_connection


@app.callback(Output("sales-table", "children"), Input("load-btn", "n_clicks"))
def _load_my_region(n_clicks):
    viewer = current_user()
    conn = get_connection(project_id="<your-project-id>")

    sales = conn.get_dataframe("Regional Sales")
    mine = sales[sales["manager_email"] == viewer]

    return mine.to_dict("records")
```

Como la conexión ya aplica los permisos de proyecto del espectador, este filtrado es un ajuste *adicional* sobre lo que se le permite ver, no un sustituto del control de acceso propio de PlaidCloud.

## Aplicaciones públicas

Si publicó con **Permitir acceso público**, la aplicación se sirve sin inicio de sesión, por lo que no hay ningún espectador como el cual actuar: `current_user()` devuelve una cadena vacía y `get_connection()` no tiene ningún token de sesión con el que autenticarse, por lo que genera un error. Limite las aplicaciones públicas a datos que sean seguros para cualquier persona, o deje desactivado el acceso público para que los espectadores inicien sesión y se aplique el modelo por usuario descrito arriba.
