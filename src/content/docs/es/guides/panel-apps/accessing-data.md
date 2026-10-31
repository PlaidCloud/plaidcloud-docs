---
title: Lectura de datos y usuario con sesión iniciada
description: "Conecte una aplicación Panel de servidor a PlaidCloud como la persona que la está viendo: lea datos del proyecto y use la identidad del visualizador para el comportamiento por usuario y la seguridad a nivel de fila."
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/accessing-data.md
---

Una aplicación Panel de servidor puede leer sus datos de PlaidCloud, y lo hace **como la persona que la está viendo**. Cuando alguien abre la aplicación, PlaidCloud inicia su sesión con el mismo inicio de sesión único que usa el resto de la plataforma, y cada llamada que hace su aplicación se ejecuta con **los permisos propios de ese visualizador**. No hay una cuenta de servicio compartida, y la aplicación nunca puede ver datos que el visualizador no podría ver por sí mismo.

Esto se aplica solo a las aplicaciones de **Servidor**. Las aplicaciones WASM se ejecutan por completo en el navegador y no tienen conexión del lado del servidor.

## Conectarse a PlaidCloud

Use `PlaidConnection` e indique el proyecto cuyos datos desea leer:

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection(project_id="<your-project-id>")
```

Eso es toda la configuración que necesita. **No** proporciona un token, un nombre de usuario ni una contraseña: la conexión se autentica automáticamente como el visualizador con sesión iniciada. Encuentre el id de su proyecto en la URL del proyecto o en su página de configuración.

> **Asigne un proyecto a su aplicación.** Una aplicación publicada con un proyecto en el selector **Proyecto** lee ese proyecto de forma predeterminada, y la [API de datos](/es/guides/panel-apps/data-api/) lo usa para `table("name")`. Para una aplicación sin proyecto, pase `project_id` a `PlaidConnection` como se muestra arriba; un `PlaidConnection()` sin argumentos no tiene ningún proyecto que leer.

### Leer una tabla

Con una conexión, cargue una tabla en un DataFrame de pandas por su nombre:

```python
df = conn.get_dataframe("Sales Ledger")
```

Como la conexión es el visualizador, esto devuelve solo las filas que el visualizador puede ver, y genera un error de permisos si no tiene ningún acceso al proyecto.

> **Lea las tablas por nombre, no escribiendo SQL.** En un proyecto donde un administrador ha activado el [acceso a filas](/es/administration/access/managing-security-groups-and-assignments/#acceso-a-filas-y-consultas-que-usted-escribe), la lectura por nombre aplica las concesiones de filas de cada visualizador, mientras que una consulta que su aplicación compone por sí misma se rechaza para cualquiera que no sea Arquitecto del proyecto: no existe una única tabla a la que se puedan aplicar los filtros de las concesiones. Leer por nombre mantiene su aplicación funcionando en ambos casos.

## Identificar al visualizador

Para adaptar lo que muestra la aplicación a **quién la está viendo** (un saludo personalizado, ocultar una pestaña o la seguridad a nivel de fila), lea el usuario con sesión iniciada desde Panel:

```python
import panel as pn

viewer = pn.state.user          # the viewer's email address
token  = pn.state.access_token  # their JWT, if you need claims or group membership
```

`pn.state.user` es el correo electrónico del visualizador, tomado de su inicio de sesión verificado; puede confiar en él como su identidad. `pn.state.access_token` es su token de acceso sin procesar, útil si necesita decodificar las declaraciones (claims) de grupo o de rol para reglas más detalladas.

### Seguridad a nivel de fila

Combine ambos: lea el visualizador y luego filtre cada consulta por él. Por ejemplo, para mostrar a cada gerente regional solo su propia región:

```python
import panel as pn
from plaidcloud.utilities.connect import PlaidConnection

pn.extension()

viewer = pn.state.user
conn = PlaidConnection(project_id="<your-project-id>")

sales = conn.get_dataframe("Regional Sales")
mine = sales[sales["manager_email"] == viewer]

pn.Column(
    f"# Sales for {viewer}",
    pn.pane.DataFrame(mine, index=False),
).servable()
```

Como la conexión ya aplica los permisos del visualizador sobre el proyecto, este filtrado es un ajuste *adicional* sobre lo que se les permite ver, no un sustituto del control de acceso propio de PlaidCloud.

> **Haga las llamadas de datos desde el flujo principal de la aplicación.** El visualizador con sesión iniciada está disponible mientras el código de su aplicación se ejecuta para su sesión (que es donde ocurre el trabajo de `.servable()`). Si traslada una llamada bloqueante a un subproceso en segundo plano, use `asyncio.to_thread`: un grupo de subprocesos sin procesar no transporta la identidad de la sesión, y la conexión fallará de forma explícita en lugar de leer los datos equivocados.

## Aplicaciones públicas

Si publicó con **Permitir acceso público**, la aplicación se sirve sin inicio de sesión, por lo que no hay ningún visualizador como quien actuar: `pn.state.user` está vacío y un `PlaidConnection()` no tiene a nadie con quien autenticarse. Limite las aplicaciones públicas a datos que sean seguros para cualquier persona, o deje desactivado el acceso público para que los visualizadores inicien sesión y se aplique el modelo por usuario descrito arriba.
