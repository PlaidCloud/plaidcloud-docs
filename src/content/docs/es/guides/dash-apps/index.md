---
title: Aplicaciones de Dash
description: Cree e implemente aplicaciones de datos de Plotly Dash del lado del servidor en PlaidCloud, publicadas desde un repositorio de Git y servidas con autenticación por usuario y escalado a cero, con paridad respecto de las aplicaciones de Panel de servidor.
sidebar:
  label: Aplicaciones de Dash
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/index.md
---

Las aplicaciones de Dash le permiten publicar aplicaciones interactivas de [Plotly Dash](https://dash.plotly.com/) (callbacks, gráficos y cuadrículas de datos como `dash-ag-grid` y `dash-mantine-components`) directamente desde PlaidCloud. Las administra desde la pantalla **Mis aplicaciones Panel**, junto con sus aplicaciones de Panel, donde cada fila muestra su entorno de ejecución, el estado de compilación y la URL.

## Dónde encaja Dash

Una aplicación de Dash se aloja exactamente igual que una **aplicación de Panel de servidor**: usted indica a PlaidCloud una rama de un repositorio de Git, este compila su código en un contenedor, y el contenedor permanece inactivo con cero réplicas, se activa con la primera solicitud, atiende y vuelve a escalar a cero cuando queda inactivo. No existe un entorno de ejecución "WASM" independiente para Dash: toda aplicación de Dash es una aplicación de servidor.

Recurra a una aplicación de Dash cuando su aplicación esté escrita con Plotly Dash en lugar de HoloViz Panel, por ejemplo, si ya tiene una base de código de Dash o si su equipo prefiere el modelo de callbacks de Dash y su ecosistema de `dash-ag-grid` y `dash-mantine-components`. Si empieza desde cero y no tiene una preferencia previa, consulte [Aplicaciones de Panel](/es/guides/panel-apps/) como alternativa.

Todo lo que obtiene una aplicación de Panel de servidor, lo obtiene también una aplicación de Dash:

- **Identidad por usuario.** Cada espectador inicia sesión con el inicio de sesión único de la plataforma, y cada llamada que la aplicación realiza para leer datos se ejecuta como *ese espectador*: el mismo modelo de [Lectura de datos y el usuario con sesión iniciada](/es/guides/panel-apps/accessing-data/), con la API auxiliar propia de Dash. Consulte [Lectura de datos y el usuario con sesión iniciada en una aplicación de Dash](/es/guides/dash-apps/accessing-data/).
- **Escalado a cero.** La aplicación pasa a cero réplicas tras el período de inactividad configurado y se activa con la siguiente solicitud, con una breve pantalla de carga de PlaidCloud durante el arranque en frío; consulte [Uso de una aplicación de Dash](/es/guides/dash-apps/using/#abrir-una-aplicación-dash).
- **Recompilaciones automáticas.** Cada push a la rama conectada recompila y vuelve a implementar la aplicación.
- **Registros de ejecución y de compilación**, cada uno etiquetado con el espectador cuya sesión generó una línea.

Hay dos cosas que una aplicación de Dash **no** tiene, ambas por diseño y ambas coincidentes con lo que tampoco tiene una aplicación de Panel:

- **Sin configuración de diseño ni de temas.** La opción **Diseño** del cuadro de diálogo de publicación de Panel (FAST frente a Predeterminado) es específica de Panel: las aplicaciones de Dash se estilizan por completo mediante los componentes que usted elige (`dash-mantine-components`, CSS personalizado, etc.), por lo que el formulario de publicación no tiene un campo equivalente.
- **Sin lista de acceso por aplicación.** El acceso lo controla el inicio de sesión único del espacio de trabajo: cualquier persona con sesión iniciada en su tenant puede abrir la aplicación (o, si habilita **Permitir acceso público**, cualquier persona). No hay una capa de ACL independiente por aplicación para ninguno de los dos tipos de aplicación.

## Contrato de la aplicación

El archivo de entrada de una aplicación de Dash debe llamarse `app.py` y debe exponer un `server`; ese es todo el contrato:

```python
from dash import Dash

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you
```

- **Llame al archivo `app.py`.** El iniciador de PlaidCloud importa su aplicación como el módulo `app` y lee su objeto `server`, por lo que, sea cual sea la ruta que indique en **Punto de entrada** (la raíz del repositorio o una subcarpeta), el archivo en esa ruta debe llamarse `app.py`.
- **Exponga `server = app.server`** en el nivel de módulo. Ese es el objeto que importa la plataforma.
- **No necesita configurar usted el inicio de sesión.** La plataforma protege automáticamente cada solicitud con inicio de sesión único por usuario: no necesita llamar a `init_auth` ni importar `plaidcloud_dash` solo para obtener la identidad. (Una aplicación anterior que *sí* llame a `plaidcloud_dash.init_auth(server, url_base_pathname=os.environ["DASH_URL_BASE_PATHNAME"])` sigue funcionando sin cambios: esa llamada es idempotente, por lo que coexiste con la configuración propia de la plataforma).
- **No establezca `requests_pathname_prefix` ni `url_base_pathname` en `Dash(__name__)`.** Toda aplicación de Dash se sirve bajo un prefijo de URL obligatorio (`/serve/<slug>/`), y la plataforma lo establece por usted mediante la variable de entorno `DASH_URL_BASE_PATHNAME`, que es la variable de configuración nativa de Dash y se lee antes que cualquier argumento del constructor. Si además pasa el prefijo de forma explícita, entra en conflicto con la propia configuración de Dash y la aplicación no se inicia.
- **`Entry Point` puede apuntar a una subcarpeta.** Antes de iniciar la aplicación, el host establece el directorio de trabajo del contenedor en la carpeta del propio archivo de entrada, de modo que las importaciones de archivos hermanos de la misma carpeta (`import data`) y las rutas de archivo relativas de su aplicación se resuelven respecto de esa carpeta, igual que al ejecutar `python app.py` desde dentro de ella.
- **No lea datos al importar.** Realice las lecturas de PlaidCloud dentro de los callbacks, no en el ámbito del módulo; consulte [Lectura de datos y el usuario con sesión iniciada en una aplicación de Dash](/es/guides/dash-apps/accessing-data/). El módulo de su aplicación se ejecuta una sola vez, al iniciarse el contenedor, antes de que ningún espectador haya iniciado sesión; una lectura de conexión o de tabla en ese momento no tiene ningún espectador en cuyo nombre actuar y hace fallar la aplicación al arrancar.

PlaidCloud ejecuta su aplicación con **gunicorn con múltiples hilos**, por lo que atiende a varios espectadores simultáneos desde un solo proceso: no necesita hacer nada adicional para que más de una persona use la aplicación a la vez.

## Cómo elegir entre Panel y Dash

| | Aplicaciones de Panel | Aplicaciones de Dash |
|---|---|---|
| Marco de trabajo | HoloViz Panel | Plotly Dash |
| Entornos de ejecución | WASM (en el navegador) o servidor | Solo servidor |
| Modelo de identidad | SSO por usuario (aplicaciones de servidor) | SSO por usuario |
| Escalado a cero | Solo aplicaciones de servidor | Sí |
| Configuración de diseño/temas | Sí (FAST / Predeterminado) | No: se estiliza con sus propios componentes |
| Lista de acceso por aplicación | No: control de SSO del espacio de trabajo | No: control de SSO del espacio de trabajo |

## Próximos pasos

- [Implementar una aplicación de Dash desde PlaidCloud Git](/es/guides/dash-apps/deploy-from-git/): el camino completo desde el repositorio hasta una aplicación servida, con una conexión administrada sin credenciales.
- [Lectura de datos y el usuario con sesión iniciada en una aplicación de Dash](/es/guides/dash-apps/accessing-data/): consulte los datos de PlaidCloud como la persona que está viendo la aplicación.
- [Uso de una aplicación de Dash](/es/guides/dash-apps/using/): estado de compilación, apertura de la aplicación, registros y eliminación.
