---
title: Implementar una aplicación Panel desde PlaidCloud Git
description: "El camino completo para servir una aplicación HoloViz Panel en PlaidCloud: coloque su código en un repositorio de PlaidCloud Git, conéctelo con una conexión administrada sin credenciales y publíquelo en vivo."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Este es el camino completo desde el código de la aplicación Panel en su equipo hasta una URL en vivo, usando **[PlaidCloud Git](/es/guides/git/)**, el servicio de Git administrado integrado en su espacio de trabajo, como origen. Como PlaidCloud Git es administrado, la conexión desde la que se implementa su aplicación **no necesita URL del servidor, nombre de usuario ni token**: PlaidCloud se autentica en su nombre.

Son cinco pasos:

1. Escribir una aplicación Panel mínima.
2. Colocarla en un repositorio de PlaidCloud Git.
3. Crear una conexión administrada de PlaidCloud Git.
4. Publicar una aplicación de servidor que apunte al repositorio.
5. Abrir la aplicación servida y leer los registros de compilación si no se inicia.

Cada paso enlaza a la guía más detallada sobre esa parte; esta página los une en un solo camino.

## Antes de comenzar

- Abra **Git** desde su espacio de trabajo para confirmar que puede acceder a PlaidCloud Git. De forma predeterminada, la organización de su espacio de trabajo incluye un repositorio **`apps`** (y uno **`udfs`**), el lugar natural para las aplicaciones Panel.
- Tenga `git` instalado localmente si desea enviar código desde su equipo (también puede agregar archivos en la interfaz web de Git).

## 1. Escribir una aplicación Panel mínima

Su aplicación necesita un **punto de entrada**, un archivo de Python que crea una aplicación Panel y la marca como `.servable()`, y, opcionalmente, un archivo **`requirements.txt`** para paquetes adicionales, ya sea en la raíz del repositorio o junto a su punto de entrada.

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

Eso es una aplicación completa: la llamada a `.servable()` es lo que PlaidCloud sirve. `panel`, `bokeh` y las bibliotecas de cliente de PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) vienen preinstalados, por lo que en `requirements.txt` incluya solo los paquetes *adicionales*. Para ver ejemplos más completos, dependencias y temas claro/oscuro, consulte [Crear una aplicación Panel](/es/guides/panel-apps/creating/).

## 2. Colocar su aplicación en un repositorio de PlaidCloud Git

Use el repositorio **`apps`** existente de su espacio de trabajo, o [cree uno nuevo](/es/guides/git/repositories/#crear-un-repositorio). Luego incorpore su código en él.

Como usted inicia sesión a través de PlaidCloud, su cuenta de Git no tiene una contraseña independiente: [genere un token de acceso personal](/es/guides/git/repositories/#generar-un-token-de-acceso-personal) (**su avatar → Configuración → Aplicaciones**) con el permiso **write:repository** y úselo como contraseña cuando Git la solicite. Enviar cambios a `apps` requiere acceso de **colaborador**; pida a un administrador del espacio de trabajo que lo agregue a **Git Contributors** si la pestaña **Git** indica que tiene acceso de lectura. Seleccione **Copy clone URL** en el repositorio, en la pestaña **Git**, y luego:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Anote la ruta del repositorio, `<org>/apps`, donde `<org>` es el nombre de la organización de su espacio de trabajo. La introducirá en el paso siguiente. Los detalles completos de clonar, confirmar y enviar cambios están en [Repositorios](/es/guides/git/repositories/).

> **El token de aquí es solo para que *usted* envíe código.** La conexión que creará a continuación es administrada y no necesita ningún token; no confunda ambos.

## 3. Crear una conexión administrada de PlaidCloud Git

Una **conexión** indica a una implementación de Panel dónde está su código. Para PlaidCloud Git, la conexión es *administrada*: PlaidCloud proporciona el host y las credenciales, de modo que usted solo introduce el destino del repositorio.

1. Abra **Tools > Connections**, haga clic en **Nueva conexión** y elija **PlaidCloud Git**.
2. Asigne a la conexión un **Nombre de la cuenta** (por ejemplo, `Apps Repo`).
3. Establezca **Repository Path** en `<org>/apps`, la ruta que anotó en el paso 2, y **Rama predeterminada** en `main`. Deje **Ruta de inicio** en blanco, a menos que sus aplicaciones estén en un subdirectorio.
4. Haga clic en **Crear**.

No hay ningún campo de URL del servidor, usuario, contraseña ni SSL/SSH: PlaidCloud Git es administrado, por lo que la plataforma se encarga del host y de la autenticación. Para el formulario completo, incluidos el **Uso** y el **Modelo de seguridad** de la conexión (quién en el espacio de trabajo puede usarla), consulte [Conexión de PlaidCloud Git](/es/guides/connections/plaidcloud-git/).

> **¿Tiene una compilación anterior del espacio de trabajo?** Si el formulario aún muestra una URL del servidor o campos de credenciales, simplemente déjelos en blanco: la plataforma se autentica en su nombre en ambos casos.

## 4. Publicar la aplicación de servidor

Ahora haga que una implementación de servidor apunte a esa conexión.

1. Abra **Mis aplicaciones Panel** y haga clic en **Nueva aplicación de servidor**.
2. En **Configuración del directorio**, establezca un **Nombre de la aplicación** y un **Slug de URL**: el slug es la URL de la aplicación y su nombre interno, así que use letras minúsculas, dígitos y guiones, comenzando con una letra, de 40 caracteres o menos (por ejemplo, `hello-panel`).
3. En **Conexión de Git y observador de publicación**:
   - **Conexión de Git**: la conexión de PlaidCloud Git que creó en el paso 3.
   - **Rama**: `main`. Los envíos a esta rama recompilan y vuelven a implementar la aplicación automáticamente.
   - **Punto de entrada**: `app.py`.
4. En **Tiempo de ejecución**, elija la **CPU**, la **Memoria**, el **Diseño** (**FAST** para el aspecto moderno de PlaidCloud) y la ventana de **Inactividad**. Marque **Permitir acceso público** solo si la aplicación debe ser accesible sin iniciar sesión.
5. Haga clic en **Publicar**.

Cada campo de este cuadro de diálogo se describe en [Crear una aplicación Panel](/es/guides/panel-apps/creating/#publicar-la-aplicación).

## 5. Abrir la aplicación y leer los registros si no se inicia

Después de publicar, la aplicación se **compila**: PlaidCloud clona la rama, instala su `requirements.txt` (el de la raíz del repositorio y el de la carpeta de su aplicación, si existen) y crea una imagen de contenedor. Su **Estado** aparece en la lista **Mis aplicaciones Panel** y se actualiza automáticamente.

- Cuando el Estado es **Lista**, abra la aplicación en `https://<your-tenant-host>/serve/<slug>/`. La primera solicitud tras un período de inactividad la pone en marcha (unos 15 segundos).
- Si la compilación falla, abra la aplicación y revise sus registros de **Compilación**: una dependencia faltante o un error de importación aparece allí. Consulte [Uso de una aplicación Panel](/es/guides/panel-apps/using/) para saber qué significa cada estado, cómo leer los registros y cómo activar una recompilación.

A partir de ahora, **cada envío a la rama de la conexión recompila y vuelve a implementar la aplicación automáticamente**: edite `app.py`, ejecute `git push` y su cambio se publica. (Salvo que la aplicación esté **bloqueada**, consulte [Bloquear una aplicación](/es/guides/panel-apps/using/#bloqueo-de-una-aplicación), en cuyo caso los envíos se omiten hasta que la desbloquee.)

## Pasos siguientes

- [Crear una aplicación Panel](/es/guides/panel-apps/creating/): ejemplos más completos, dependencias y temas claro/oscuro
- [Conexión de PlaidCloud Git](/es/guides/connections/plaidcloud-git/): el formulario completo de la conexión, su uso y su modelo de seguridad
- [Lectura de datos y del usuario con sesión iniciada](/es/guides/panel-apps/accessing-data/): consulte datos de PlaidCloud como la persona que ve la aplicación
- [Repositorios](/es/guides/git/repositories/): ramas, tokens y colaboración en PlaidCloud Git
