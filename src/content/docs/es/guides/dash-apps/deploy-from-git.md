---
title: Implementar una aplicación Dash desde PlaidCloud Git
description: "La ruta completa para servir una aplicación de Plotly Dash en PlaidCloud: coloque su código en un repositorio de PlaidCloud Git, conéctelo con una conexión administrada sin credenciales y publíquelo."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

Esta es la ruta completa desde el código de una aplicación Dash en su equipo hasta una URL activa, con **[PlaidCloud Git](/es/guides/git/)**, el servicio de Git administrado integrado en su espacio de trabajo, como origen. Como PlaidCloud Git es un servicio administrado, la conexión desde la que se implementa su aplicación **no necesita URL del servidor, nombre de usuario ni token**: PlaidCloud se autentica en su nombre.

Son cinco pasos:

1. Escribir una aplicación Dash mínima.
2. Colocarla en un repositorio de PlaidCloud Git.
3. Crear una conexión administrada de PlaidCloud Git.
4. Publicar una aplicación Dash que apunte al repositorio.
5. Abrir la aplicación servida y leer los registros de compilación si no se inicia.

Este tutorial es casi idéntico a [Implementar una aplicación Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/): ambas son aplicaciones de Python del lado del servidor compiladas desde Git y servidas de la misma manera. La diferencia es el código de la aplicación y un campo del cuadro de diálogo de publicación.

## Antes de comenzar

- Abra **Git** desde su espacio de trabajo para confirmar que puede acceder a PlaidCloud Git. De forma predeterminada, la organización de su espacio de trabajo incluye un repositorio **`apps`**, que también es el lugar natural para las aplicaciones Dash.
- Tenga `git` instalado de forma local si desea enviar código desde su equipo (también puede agregar archivos en la interfaz web de Git).

## 1. Escribir una aplicación Dash mínima

Su aplicación necesita un **punto de entrada**, es decir, un archivo de Python que construya una aplicación Dash y exponga su servidor Flask, y, de forma opcional, un archivo **`requirements.txt`** para paquetes adicionales, ya sea en la raíz del repositorio o junto a su punto de entrada.

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

Esa es una aplicación completa. `dash`, `plotly`, `dash-mantine-components`, `dash-ag-grid` y las bibliotecas cliente de PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) vienen preinstalados, por lo que en `requirements.txt` solo debe incluir los paquetes *adicionales*. No pase `requests_pathname_prefix` ni `url_base_pathname` a `Dash(__name__)`: la plataforma establece el prefijo de la URL mediante `DASH_URL_BASE_PATHNAME` de forma automática, y definir ambos genera un error de configuración al iniciar. Para conocer el contrato completo de la aplicación y los asistentes de acceso a datos, consulte [El contrato de la aplicación](/es/guides/dash-apps/#contrato-de-la-aplicación) y [Lectura de datos y del usuario con sesión iniciada en una aplicación Dash](/es/guides/dash-apps/accessing-data/).

## 2. Colocar su aplicación en un repositorio de PlaidCloud Git

Utilice el repositorio **`apps`** existente de su espacio de trabajo, o [cree uno nuevo](/es/guides/git/repositories/#crear-un-repositorio). Luego, coloque su código en él.

Como usted inicia sesión mediante PlaidCloud, su cuenta de Git no tiene una contraseña independiente: [genere un token de acceso personal](/es/guides/git/repositories/#generar-un-token-de-acceso-personal) (**su avatar → Configuración → Aplicaciones**) con el permiso **write:repository** y úselo como contraseña cuando Git se la solicite. Para enviar cambios a `apps` se necesita acceso de **Colaborador**; pida a un administrador del espacio de trabajo que lo agregue a **Git Contributors** si la pestaña **Git** lo muestra como **Visualizador**. Use el botón de copiar junto a la dirección de clonación del repositorio en la pestaña **Git** y luego ejecute:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

Anote la ruta del repositorio, `<org>/apps`, donde `<org>` es el nombre de la organización de su espacio de trabajo. La introducirá en el paso siguiente. Los detalles completos para clonar, confirmar y enviar cambios están en [Repositorios](/es/guides/git/repositories/).

> **El token de aquí es solo para que *usted* envíe código.** La conexión que creará a continuación es administrada y no necesita ningún token; no los confunda.

## 3. Crear una conexión administrada de PlaidCloud Git

Una **conexión** le indica a una implementación de Dash dónde está su código. En PlaidCloud Git la conexión es *administrada*: PlaidCloud proporciona el host y las credenciales, por lo que usted solo introduce el destino del repositorio. Es el mismo tipo de conexión que utiliza una aplicación Panel de servidor.

1. Abra **Tools > Connections**, haga clic en **Nueva conexión** y elija **PlaidCloud Git**.
2. Asigne a la conexión un **Nombre de la cuenta** (por ejemplo, `Apps Repo`).
3. Establezca **Repository Path** en `<org>/apps`, la ruta que anotó en el paso 2, y **Rama predeterminada** en `main`. Deje **Ruta de inicio** en blanco, a menos que sus aplicaciones estén en un subdirectorio.
4. Haga clic en **Crear**.

No hay campo de URL del servidor, usuario, contraseña ni SSL/SSH: PlaidCloud Git es administrado, por lo que la plataforma se encarga del host y de la autenticación. Para ver el formulario completo, incluidos el **Uso** y el **Modelo de seguridad** de la conexión (quién en el espacio de trabajo puede usarla), consulte [Conexión de PlaidCloud Git](/es/guides/connections/plaidcloud-git/).

## 4. Publicar la aplicación Dash

Ahora haga que una implementación de Dash apunte a esa conexión.

1. Abra **Mis aplicaciones Panel** y haga clic en **Nueva aplicación Dash**.
2. En **Configuración del directorio**, establezca un **Nombre de la aplicación** y un **Slug de URL**: el slug es la URL de la aplicación y su nombre interno, así que use letras minúsculas, dígitos y guiones, comience con una letra y no supere los 40 caracteres (por ejemplo, `hello-dash`). Una **Nota** opcional describe la aplicación.
3. En **Conexión de Git y observador de publicación**:
   - **Conexión de Git**: la conexión de PlaidCloud Git que creó en el paso 3.
   - **Rama**: `main`. Los envíos a esta rama recompilan y vuelven a implementar la aplicación de forma automática.
   - **Punto de entrada**: `app.py`.
4. En **Tiempo de ejecución**, elija la **CPU**, la **Memoria** y el intervalo de **Inactividad (minutos)**. Marque **Permitir acceso público** solo si la aplicación debe ser accesible sin iniciar sesión. No existe la opción **Diseño**; es una opción exclusiva de Panel.
5. En **Avanzado (servicio incrustado)**, opcional. Déjelo vacío, salvo que vaya a incrustar la aplicación en otro sitio.
6. Haga clic en **Publicar**.

## 5. Abrir la aplicación y leer los registros si no se inicia

Después de publicar, la aplicación se **compila**: PlaidCloud clona la rama, instala su `requirements.txt` y crea una imagen de contenedor a partir de la imagen `platform-dash-base`. Su **Estado** aparece en la lista **Mis aplicaciones Panel** y se actualiza automáticamente.

- Cuando el Estado sea **Lista**, abra la aplicación en `https://<your-tenant-host>/serve/<slug>/`. La primera solicitud tras un período de inactividad la pone en marcha y muestra brevemente una pantalla de carga de PlaidCloud mientras lo hace.
- Si la compilación falla, abra la aplicación y revise sus registros de **Compilación**: una dependencia faltante o un error de importación aparecen allí. Consulte [Uso de una aplicación Dash](/es/guides/dash-apps/using/) para saber qué significa cada estado, cómo leer los registros y cómo activar una recompilación.

A partir de ese momento, **cada envío a la rama de la conexión recompila y vuelve a implementar la aplicación automáticamente**: edite `app.py`, ejecute `git push` y su cambio entra en vigor. (Salvo que la aplicación esté **bloqueada**, en cuyo caso los envíos se omiten hasta que la desbloquee; consulte [Uso de una aplicación Dash](/es/guides/dash-apps/using/#bloquear-una-aplicación).)

## Pasos siguientes

- [Lectura de datos y del usuario con sesión iniciada en una aplicación Dash](/es/guides/dash-apps/accessing-data/): consulte los datos de PlaidCloud como la persona que ve la aplicación.
- [Uso de una aplicación Dash](/es/guides/dash-apps/using/): estado de la compilación, registros, bloqueo y eliminación de la aplicación.
- [Conexión de PlaidCloud Git](/es/guides/connections/plaidcloud-git/): el formulario completo de la conexión, su uso y su modelo de seguridad.
- [Repositorios](/es/guides/git/repositories/): ramas, tokens y colaboración en PlaidCloud Git.
