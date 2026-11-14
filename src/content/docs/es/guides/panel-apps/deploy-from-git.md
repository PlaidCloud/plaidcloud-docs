---
title: Implementar una aplicación de Panel desde PlaidCloud Git
description: "El recorrido completo para servir una aplicación de HoloViz Panel en PlaidCloud: coloque su código en un repositorio de PlaidCloud Git, conéctelo con una conexión administrada sin credenciales y publíquelo en vivo."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Este es el recorrido completo desde el código de una aplicación de Panel en su equipo hasta una URL en vivo, usando como origen **[PlaidCloud Git](/es/guides/git/)**, el servicio Git administrado integrado en su espacio de trabajo. Como PlaidCloud Git es administrado, la conexión desde la que se implementa su aplicación **no necesita URL de servidor, nombre de usuario ni token**: PlaidCloud se autentica en su nombre.

Hay cinco pasos:

1. Escribir una aplicación de Panel mínima.
2. Colocarla en un repositorio de PlaidCloud Git.
3. Crear una conexión administrada de PlaidCloud Git.
4. Publicar una aplicación de servidor que apunte al repositorio.
5. Abrir la aplicación servida y leer los registros de compilación si no se inicia.

Cada paso enlaza con la guía más detallada sobre esa parte; esta página los une en un solo recorrido.

## Antes de empezar

- Abra **Git** desde su espacio de trabajo para confirmar que puede acceder a PlaidCloud Git. De forma predeterminada, la organización de su espacio de trabajo incluye un repositorio **`apps`** (y uno **`udfs`**), el lugar natural para las aplicaciones de Panel.
- Tenga `git` instalado en local si desea enviar código desde su equipo (también puede agregar archivos en la interfaz web de Git).

## 1. Escribir una aplicación de Panel mínima

Su aplicación necesita un **punto de entrada**, un archivo de Python que crea una aplicación de Panel y la marca con `.servable()`, y, opcionalmente, un **`requirements.txt`** para paquetes adicionales, ya sea en la raíz del repositorio o junto a su punto de entrada.

```
apps/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Cree `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello from PlaidCloud Git 👋\n\nServed straight from your workspace repository.").servable()
```

Eso es una aplicación completa: la llamada `.servable()` es lo que PlaidCloud sirve. `panel`, `bokeh` y las bibliotecas cliente de PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) están preinstalados, así que enumere en `requirements.txt` solo los paquetes *adicionales*. Para ver ejemplos más completos, dependencias y temas claro/oscuro, consulte [Creación de una aplicación de Panel](/es/guides/panel-apps/creating/).

## 2. Colocar su aplicación en un repositorio de PlaidCloud Git

Utilice el repositorio **`apps`** existente de su espacio de trabajo o [cree uno nuevo](/es/guides/git/repositories/#crear-un-repositorio). Luego, lleve su código a él. Las aplicaciones que crea en [Panel Studio](/es/guides/panel-apps/studio/#dónde-se-guarda-su-aplicación) ya son carpetas en `apps`, por lo que las encontrará allí junto a la suya.

Como inicia sesión a través de PlaidCloud, su cuenta de Git no tiene una contraseña aparte: [genere un token de acceso personal](/es/guides/git/repositories/#generar-un-token-de-acceso-personal) (**su avatar → Settings → Applications**) con el permiso **write:repository** y utilícelo como contraseña cuando Git se la solicite. Enviar cambios a `apps` requiere acceso de **Contributor**; pida a un administrador del espacio de trabajo que le agregue a **Git Contributors** si la pestaña **Git** le muestra como **Visualizador**. Utilice el botón de copiar situado junto a la dirección de clonación del repositorio en la pestaña **Git** y luego:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Anote la ruta del repositorio, `<org>/apps`, donde `<org>` es el nombre de la organización de su espacio de trabajo. La introducirá en el paso siguiente. Los detalles completos de clonación, confirmación y envío están en [Repositorios](/es/guides/git/repositories/).

> **El token que se usa aquí es solo para que *usted* envíe código.** La conexión que creará a continuación es administrada y no necesita token: no confunda ambas cosas.

## 3. Crear una conexión administrada de PlaidCloud Git

Una **conexión** le indica a una implementación de Panel dónde se encuentra su código. En PlaidCloud Git la conexión es *administrada*: PlaidCloud proporciona el host y las credenciales, de modo que usted solo introduce el destino del repositorio.

1. Abra **Tools > Connections**, haga clic en **Nueva conexión** y elija **PlaidCloud Git**.
2. Asigne a la conexión un **Nombre de la cuenta** (por ejemplo, `Apps Repo`).
3. Establezca **Repository Path** en `<org>/apps` (la ruta que anotó en el paso 2) y **Rama predeterminada** en `main`. Deje **Ruta de inicio** en blanco a menos que sus aplicaciones estén en un subdirectorio.
4. Haga clic en **Crear**.

No hay ningún campo de URL del servidor, usuario, contraseña ni SSL/SSH: PlaidCloud Git es administrado, por lo que la plataforma se ocupa del host y de la autenticación. Para ver el formulario completo, incluidos el **Uso** y el **Modelo de seguridad** de la conexión (quién del espacio de trabajo puede usarla), consulte [Conexión de PlaidCloud Git](/es/guides/connections/plaidcloud-git/).

> **¿Tiene una compilación antigua del espacio de trabajo?** Si el formulario aún muestra una URL del servidor o campos de credenciales, déjelos en blanco: la plataforma se autentica en su nombre en cualquier caso.

## 4. Publicar la aplicación de servidor

Ahora apunte una implementación de servidor a esa conexión.

1. Abra **Aplicaciones** y elija **Nueva aplicación** > **Server based**.
2. En **Configuración del directorio**, establezca un **Nombre de la aplicación** y un **Slug de URL**: el slug es la URL y el nombre interno de la aplicación, así que use letras minúsculas, dígitos y guiones, empezando por una letra, con 40 caracteres o menos (por ejemplo, `hello-panel`).
3. En **Conexión de Git y observador de publicación**:
   - **Conexión de Git**: la conexión de PlaidCloud Git que creó en el paso 3.
   - **Rama**: `main`. Los envíos a esta rama vuelven a compilar y a implementar la aplicación automáticamente.
   - **Punto de entrada**: `app.py`.
4. En **Tiempo de ejecución**, elija la **CPU**, la **Memoria**, el **Diseño** (**FAST** para el aspecto moderno de PlaidCloud) y la ventana de **Idle**. Marque **Permitir acceso público** solo si la aplicación debe ser accesible sin iniciar sesión.
5. Haga clic en **Publicar**.

Todos los campos de este cuadro de diálogo se describen en [Creación de una aplicación de Panel](/es/guides/panel-apps/creating/#publicación-de-la-aplicación).

## 5. Abrir la aplicación y leer los registros si no se inicia

Después de publicar, la aplicación se **compila**: PlaidCloud clona la rama, instala su `requirements.txt` (el de la raíz del repositorio y el de la carpeta de su aplicación, si existen) y crea una imagen de contenedor. Su **Estado** aparece en la lista **Aplicaciones** y se actualiza automáticamente.

- Cuando el estado es **Lista**, abra la aplicación en `https://<your-tenant-host>/serve/<slug>/`. La primera solicitud después de un período de inactividad la reactiva (unos 15 segundos).
- Si la compilación falla, abra la aplicación y revise sus registros de **Build**: una dependencia que falta o un error de importación aparecen allí. Consulte [Uso de una aplicación de Panel](/es/guides/panel-apps/using/) para saber qué significa cada estado, cómo leer los registros y cómo activar una recompilación.

A partir de aquí, **cada envío a la rama de la conexión vuelve a compilar y a implementar la aplicación automáticamente**: edite `app.py`, ejecute `git push` y su cambio se publica en vivo. (A menos que la aplicación esté **bloqueada**, consulte [Bloqueo de una aplicación](/es/guides/panel-apps/using/#bloquear-una-aplicación), en cuyo caso los envíos se omiten hasta que la desbloquee.)

## Pasos siguientes

- [Creación de una aplicación de Panel](/es/guides/panel-apps/creating/): ejemplos más completos, dependencias y temas claro/oscuro
- [Conexión de PlaidCloud Git](/es/guides/connections/plaidcloud-git/): el formulario completo de la conexión, su uso y su modelo de seguridad
- [Lectura de datos y del usuario que inició sesión](/es/guides/panel-apps/accessing-data/): consulte los datos de PlaidCloud como la persona que está viendo la aplicación
- [Repositorios](/es/guides/git/repositories/): ramas, tokens y colaboración en PlaidCloud Git
