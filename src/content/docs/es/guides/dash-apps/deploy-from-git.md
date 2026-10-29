---
title: Implementar una aplicación Dash desde PlaidCloud Git
description: "El camino completo para servir una aplicación Plotly Dash en PlaidCloud: coloque su código en un repositorio de PlaidCloud Git, conéctelo con una conexión administrada sin credenciales y publíquelo en vivo."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

Este es el camino completo desde el código de una aplicación Dash en su equipo hasta una URL en vivo, usando como origen **[PlaidCloud Git](/es/guides/git/)**, el servicio de Git administrado integrado en su espacio de trabajo. Como PlaidCloud Git es administrado, la conexión desde la que se implementa su aplicación **no necesita URL del servidor, nombre de usuario ni token**: PlaidCloud se autentica en su nombre.

Hay cinco pasos:

1. Escribir una aplicación Dash mínima.
2. Colocarla en un repositorio de PlaidCloud Git.
3. Crear una conexión administrada de PlaidCloud Git.
4. Publicar una aplicación Dash que apunte al repositorio.
5. Abrir la aplicación servida y leer los registros de compilación si no se inicia.

Este recorrido es casi idéntico a [Implementar una aplicación Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/): ambas son aplicaciones de Python del lado del servidor compiladas desde Git y servidas de la misma manera. La diferencia está en el código de la propia aplicación y en un campo del cuadro de diálogo de publicación.

## Antes de empezar

- Abra **Git** desde su espacio de trabajo para confirmar que puede acceder a PlaidCloud Git. De forma predeterminada, la organización de su espacio de trabajo incluye un repositorio **`apps`**, el lugar natural también para las aplicaciones Dash.
- Tenga `git` instalado localmente si desea enviar código desde su equipo (también puede agregar archivos en la interfaz web de Git).

## 1. Escribir una aplicación Dash mínima

Su aplicación necesita un **punto de entrada** (un archivo de Python que construya una aplicación Dash y exponga su servidor Flask) y, opcionalmente, un **`requirements.txt`** para paquetes adicionales, ya sea en la raíz del repositorio o junto a su punto de entrada.

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Cree `app.py`:

```python
import plaidcloud_dash as pcd
from dash import Dash, Input, Output, html

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you

app.layout = html.Div(
    [
        html.H1("Hello from PlaidCloud Git"),
        html.P(id="whoami"),
        html.Button("Who am I?", id="whoami-btn", n_clicks=0),
    ]
)


@app.callback(Output("whoami", "children"), Input("whoami-btn", "n_clicks"))
def _whoami(n_clicks):
    if not n_clicks:
        return ""
    return f"Signed in as {pcd.current_user()!r}"


if __name__ == "__main__":
    app.run(debug=True)
```

Esa es una aplicación completa. `dash`, `plotly`, `dash-mantine-components`, `dash-ag-grid` y las bibliotecas cliente de PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) vienen preinstalados, así que en `requirements.txt` indique solo los paquetes *adicionales*. No pase `requests_pathname_prefix` ni `url_base_pathname` a `Dash(__name__)`: la plataforma establece el prefijo de URL automáticamente mediante `DASH_URL_BASE_PATHNAME`, y establecer ambos genera un error de configuración al iniciar. Para conocer el contrato completo de la aplicación y los asistentes de acceso a datos, consulte [el contrato de la aplicación](/es/guides/dash-apps/#contrato-de-la-aplicación) y [Lectura de datos y del usuario con sesión iniciada en una aplicación Dash](/es/guides/dash-apps/accessing-data/).

## 2. Colocar su aplicación en un repositorio de PlaidCloud Git

Use el repositorio **`apps`** existente de su espacio de trabajo, o [cree uno nuevo](/es/guides/git/repositories/#crear-un-repositorio). Luego suba su código a él.

Como inicia sesión a través de PlaidCloud, su cuenta de Git no tiene una contraseña independiente: [genere un token de acceso personal](/es/guides/git/repositories/#generar-un-token-de-acceso-personal) (**your avatar → Settings → Applications**) con los ámbitos de **lectura** y **escritura** del repositorio, y úselo como contraseña cuando Git se la solicite. Copie la URL de clonación **HTTPS** del repositorio desde su botón **Código** y luego:

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

Anote la ruta del repositorio, `<org>/apps`, donde `<org>` es el nombre de la organización de su espacio de trabajo. La introducirá en el paso siguiente. Los detalles completos de clonación, confirmación y envío están en [Repositorios](/es/guides/git/repositories/).

> **El token de aquí es solo para que *usted* envíe código.** La conexión que creará a continuación es administrada y no necesita token: no confunda ambos.

## 3. Crear una conexión administrada de PlaidCloud Git

Una **conexión** le indica a una implementación de Dash dónde reside su código. Para PlaidCloud Git la conexión es *administrada*: PlaidCloud proporciona el host y las credenciales, así que usted solo introduce el destino del repositorio. Es el mismo tipo de conexión que usa una aplicación Panel de servidor.

1. Abra **Tools > Connections**, haga clic en **Nueva conexión** y elija **PlaidCloud Git**.
2. Asigne a la conexión un **Nombre de la cuenta** (por ejemplo, `Apps Repo`).
3. Establezca **Repository Path** en `<org>/apps` (la ruta que anotó en el paso 2) y **Rama predeterminada** en `main`. Deje **Ruta de inicio** en blanco, a menos que sus aplicaciones residan en un subdirectorio.
4. Haga clic en **Crear**.

No hay ningún campo de URL del servidor, usuario, contraseña ni SSL/SSH: PlaidCloud Git es administrado, así que la plataforma se encarga del host y de la autenticación. Para ver el formulario completo, incluidos el **Uso** y el **Modelo de seguridad** de la conexión (quién en el espacio de trabajo puede usarla), consulte [Conexión de PlaidCloud Git](/es/guides/connections/plaidcloud-git/).

## 4. Publicar la aplicación Dash

Ahora apunte una implementación de Dash a esa conexión.

1. Abra **Mis aplicaciones Panel** y haga clic en **Nueva aplicación Dash**.
2. En **Configuración del directorio**, establezca un **Nombre de la aplicación** y un **Slug de URL**; el slug es la URL y el nombre interno de la aplicación, así que use letras minúsculas, dígitos y guiones, empezando por una letra y con 40 caracteres o menos (por ejemplo, `hello-dash`). Una **Nota** opcional describe la aplicación.
3. En **Conexión de Git y observador de publicación**:
   - **Conexión de Git**: la conexión de PlaidCloud Git que creó en el paso 3.
   - **Rama**: `main`. Los envíos a esta rama recompilan y vuelven a implementar la aplicación automáticamente.
   - **Punto de entrada**: `app.py`.
4. En **Tiempo de ejecución**, elija la ventana de **CPU**, **Memoria** e **Inactividad (minutos)**. Marque **Permitir acceso público** solo si la aplicación debe ser accesible sin iniciar sesión. No hay ninguna opción de **Diseño**: es una opción específica de Panel.
5. En **Avanzado (servicio incrustado)**, opcional. Déjelo vacío, a menos que esté incrustando la aplicación en otro sitio.
6. Haga clic en **Publicar**.

## 5. Abrir la aplicación y leer los registros si no se inicia

Después de publicar, la aplicación se **compila**: PlaidCloud clona la rama, instala su `requirements.txt` y crea una imagen de contenedor a partir de la imagen `platform-dash-base`. Su **Estado** se muestra en la lista **Mis aplicaciones Panel** y se actualiza automáticamente.

- Cuando el Estado es **Lista**, abra la aplicación en `https://<your-tenant-host>/serve/<slug>/`. La primera solicitud después de un período de inactividad la pone en marcha y muestra brevemente una pantalla de carga de PlaidCloud mientras tanto.
- Si la compilación falla, abra la aplicación y revise sus registros de **Compilación**: una dependencia faltante o un error de importación aparecen allí. Consulte [Uso de una aplicación Dash](/es/guides/dash-apps/using/) para saber qué significa cada estado, cómo leer los registros y cómo activar una recompilación.

A partir de ahora, **cada envío a la rama de la conexión recompila y vuelve a implementar la aplicación automáticamente**: edite `app.py`, ejecute `git push` y su cambio se publica. (A menos que la aplicación esté **bloqueada**, en cuyo caso los envíos se omiten hasta que la desbloquee; consulte [Uso de una aplicación Dash](/es/guides/dash-apps/using/#bloquear-una-aplicación)).

## Pasos siguientes

- [Lectura de datos y del usuario con sesión iniciada en una aplicación Dash](/es/guides/dash-apps/accessing-data/): consulte los datos de PlaidCloud como la persona que está viendo la aplicación.
- [Uso de una aplicación Dash](/es/guides/dash-apps/using/): estado de compilación, registros, bloqueo y eliminación de la aplicación.
- [Conexión de PlaidCloud Git](/es/guides/connections/plaidcloud-git/): el formulario completo de la conexión, su uso y su modelo de seguridad.
- [Repositorios](/es/guides/git/repositories/): ramas, tokens y colaboración en PlaidCloud Git.
