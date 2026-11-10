---
title: PlaidCloud Git
description: Aloje, versione y colabore en repositorios Git dentro de PlaidCloud, con incidencias, solicitudes de incorporación de cambios, tableros de proyecto, versiones y wikis, y con inicio de sesión único integrado.
sidebar:
  label: Resumen
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git es un servicio Git privado integrado en su espacio de trabajo. Cada espacio de trabajo dispone de su propio servidor Git para almacenar código, configuración, cuadernos y cualquier otro archivo con control de versiones, junto con las incidencias, las solicitudes de incorporación de cambios y los tableros de proyecto que su equipo usa para colaborar en ellos.

Usted inicia sesión con su cuenta de PlaidCloud, por lo que no hace falta configurar un nombre de usuario ni una contraseña aparte. Los repositorios nuevos son privados de forma predeterminada y solo los ven los miembros a quienes usted conceda acceso.

## Abrir Git

Seleccione **Git** en la lista de aplicaciones de su espacio de trabajo. Se abre la pestaña **Git** con el host del espacio de trabajo, su rol y una lista de **Repositories**. Use **View all in Git** para ir a la interfaz web de Git, **Manage who can push** (si puede administrar grupos) para abrir la administración de grupos y el botón de actualizar para volver a cargar. Use **← Back to** your workspace in Git para volver a PlaidCloud.

Un indicador de rol muestra su nivel: **Administrador**, **Colaborador** o **Visualizador**, con una línea que explica lo que le permite hacer. Cada fila de repositorio muestra su nombre, su descripción (cuando la tiene), **Actualizado** con la fecha, un campo de clonación de solo lectura con un botón de copiar y **Abrir**, que abre el repositorio en Git. Los repositorios que usted crea como privados están directamente en Git, no en esta lista.

Si Git no está configurado para su espacio de trabajo o no se puede acceder a él, la pestaña **Git** muestra **Git no está disponible** con el motivo, y **Intentar de nuevo** vuelve a comprobarlo.

## Clonar un repositorio

Copie la dirección de clonación del repositorio desde su fila. La primera vez que copie, aparece una tarjeta **Set up Git on your computer** con los pasos siguientes. Seleccione **Descartar** para ocultarla y **How to clone** en el encabezado para volver a mostrarla.

1. Git debe estar instalado en su equipo.
2. Cree un token en **Configuración → Aplicaciones** con el permiso **write:repository**. La tarjeta enlaza a esa página.
3. Indique a Git quién es usted con los dos comandos `git config --global user.name` y `user.email` que se muestran, que ya contienen su nombre y su correo electrónico.
4. Clone el repositorio con el comando `git clone` que se muestra. Cuando Git pida una contraseña, pegue ese token, no su contraseña de PlaidCloud.

Cada comando tiene su propio botón de copiar. Consulte [Repositorios](/es/guides/git/repositories/) para ver el recorrido completo. Copiar requiere acceso de envío y una cuenta de Git activada: si el botón de copiar está deshabilitado, abra cualquier repositorio una vez para activar su cuenta o, como **Visualizador**, solicite acceso de envío como se describe a continuación.

## Niveles de acceso

Todos los usuarios con acceso a Git pueden leer los repositorios compartidos del espacio de trabajo. Dos niveles adicionales permiten enviar cambios.

| Rol | Qué puede hacer | Concedido por |
|---|---|---|
| **Visualizador** | Ver y clonar los repositorios compartidos. | Predeterminado para todos los miembros. |
| **Colaborador** | Todo lo de Leer, y enviar cambios al repositorio `apps`, donde reside el código de las aplicaciones de [Panel](/es/guides/panel-apps/deploy-from-git/) y [Dash](/es/guides/dash-apps/deploy-from-git/). | El grupo de seguridad **Git Contributors**. |
| **Administrador** | Todo lo del Colaborador, y enviar cambios a todos los repositorios, incluido `udfs`, y crear organizaciones. | El grupo de seguridad **Git Administration**. |

El repositorio `udfs` está limitado a los administradores porque las funciones definidas por el usuario se ejecutan con la identidad del flujo de trabajo que las llama.

Si es **Visualizador**, la pestaña **Git** nombra hasta tres administradores del espacio de trabajo a quienes puede pedir que lo agreguen a **Git Contributors**.

## Git desde aplicaciones y UDF

La ventana de una aplicación Panel o Dash tiene una sección **Repositorio** que muestra su repositorio, su rama y el estado de la compilación, con **Edit in browser** y **Copy clone URL** para los miembros que pueden enviar cambios. La barra de herramientas de una UDF respaldada por Git tiene **Abrir**, que abre el repositorio en su rama en Git, y **Edit in browser** para los administradores.

## Conceder acceso a Git

Los administradores del espacio de trabajo conceden acceso en **Identidad** agregando miembros a un grupo de seguridad o agregando el permiso a un grupo propio.

1. Agregue al miembro a **Git Contributors** para que pueda enviar código de aplicaciones, o a **Git Administration** para convertirlo en administrador de Git.
2. Para dar a cada miembro nuevo acceso de envío al código de aplicaciones, agregue **Git Contributors** a sus grupos predeterminados. **Git Administration** no puede ser un grupo predeterminado.
3. Para comprobar lo que puede hacer un miembro, abra el miembro y seleccione la pestaña **Git**. Muestra el nombre de usuario de Git del miembro, su nivel y el grupo que lo concede.

Un cambio se aplica la próxima vez que el miembro inicia sesión en Git o abre la pestaña **Git**. La cuenta de Git de un miembro sigue su pertenencia a PlaidCloud. Desactivar o quitar a un miembro bloquea su cuenta de Git, incluidos sus tokens y claves SSH, en aproximadamente una hora, y reactivarlo la desbloquea. No se elimina nada: sus repositorios y su historial se conservan. Iniciar sesión en Git con inicio de sesión único abre la cuenta propia del miembro. El personal de soporte de PlaidCloud tiene acceso de administrador automáticamente.

## Contenido de esta sección

- [Repositorios](/es/guides/git/repositories/): cree un repositorio y luego clone, confirme y envíe su trabajo
- [Incidencias](/es/guides/git/issues/): haga seguimiento de tareas, errores e ideas con etiquetas, hitos y responsables
- [Solicitudes de incorporación de cambios](/es/guides/git/pull-requests/): proponga cambios en una rama y revíselos antes de fusionarlos
- [Tableros de proyecto](/es/guides/git/projects/): organice incidencias y solicitudes de incorporación de cambios en un tablero Kanban
- [Versiones y etiquetas](/es/guides/git/releases-and-tags/): marque y publique instantáneas versionadas de un repositorio
- [Wikis](/es/guides/git/wikis/): mantenga documentación extensa junto a su código
- [Paquetes](/es/guides/git/packages/): publique e instale artefactos de compilación desde el registro del repositorio
- [Búsqueda de código](/es/guides/git/searching-code/): encuentre código, incidencias y solicitudes de incorporación de cambios en todos sus repositorios

## Temas relacionados

- [Implementar una aplicación Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/): sirva una aplicación HoloViz Panel directamente desde un repositorio, con una conexión administrada sin credenciales
- [Implementar una aplicación Dash desde PlaidCloud Git](/es/guides/dash-apps/deploy-from-git/): sirva una aplicación Plotly Dash de la misma manera
- [Administración de acceso](/es/administration/access/): cómo la pertenencia al espacio de trabajo y los grupos de seguridad determinan quién puede ver y editar los repositorios
