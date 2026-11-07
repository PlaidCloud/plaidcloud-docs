---
title: PlaidCloud Git
description: Aloje, versione y colabore en repositorios de Git dentro de PlaidCloud, con incidencias, solicitudes de incorporación de cambios, tableros de proyecto, versiones y wikis, e inicio de sesión único integrado.
sidebar:
  label: Resumen
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git es un servicio de Git privado integrado en su espacio de trabajo. Cada espacio de trabajo tiene su propio servidor de Git para almacenar código, configuración, cuadernos y cualquier otro archivo con control de versiones, junto con las incidencias, las solicitudes de incorporación de cambios y los tableros de proyecto que su equipo usa para colaborar en ellos.

Usted inicia sesión con su cuenta de PlaidCloud, por lo que no hay que configurar un nombre de usuario ni una contraseña independientes. Los repositorios nuevos son privados de forma predeterminada y solo los ven los miembros a quienes usted otorgue acceso.

## Abrir Git

Seleccione **Git** en la lista de aplicaciones de su espacio de trabajo. Se abre la pestaña **Git** con el host del espacio de trabajo, su rol y una lista de **Repositorios**. Use **View all in Git** para ir a la interfaz web de Git, **Manage who can push** (si puede administrar grupos) para abrir la administración de grupos y el botón de actualizar para volver a cargar. Use **← Back to** su espacio de trabajo en Git para regresar a PlaidCloud.

Un indicador de rol muestra su nivel: **Administrador**, **Colaborador** o **Visualizador**, con una línea que indica lo que ese nivel le permite hacer. Cada fila de repositorio muestra su nombre, su descripción (cuando la tiene), **Actualizado** con la fecha, un campo de clonación de solo lectura con un botón de copiar y **Abrir**, que abre el repositorio en Git. Los repositorios que usted crea como privados están directamente en Git, no en esta lista.

## Clonar un repositorio

Copie la dirección de clonación del repositorio desde su fila. La primera vez que copie, aparece una tarjeta **Set up Git on your computer** con los pasos siguientes. Seleccione **Descartar** para ocultarla y **How to clone** en el encabezado para volver a mostrarla.

1. Git debe estar instalado en su equipo.
2. Cree un token en **Configuración → Aplicaciones** con el permiso **write:repository**. La tarjeta enlaza a esa página.
3. Indique a Git quién es usted con los dos comandos `git config --global user.name` y `user.email` que se muestran, los cuales ya contienen su nombre y su correo electrónico.
4. Clone el repositorio con el comando `git clone` que se muestra. Cuando Git solicite una contraseña, pegue ese token, no su contraseña de PlaidCloud.

Cada comando tiene su propio botón de copiar. Consulte [Repositorios](/es/guides/git/repositories/) para ver el tutorial completo. Copiar requiere acceso de escritura y una cuenta de Git activada: si el botón de copiar está deshabilitado, abra cualquier repositorio una vez para activar su cuenta o, como **Visualizador**, solicite acceso de escritura como se describe a continuación.

## Niveles de acceso

Todas las personas con acceso a Git pueden leer los repositorios compartidos del espacio de trabajo. Dos niveles adicionales permiten enviar cambios.

| Rol | Qué puede hacer | Lo otorga |
|---|---|---|
| **Visualizador** | Ver y clonar los repositorios compartidos. | Predeterminado para cada miembro. |
| **Colaborador** | Todo lo de Lectura, y enviar cambios al repositorio `apps`, donde reside el código de las aplicaciones de [Panel](/es/guides/panel-apps/deploy-from-git/) y [Dash](/es/guides/dash-apps/deploy-from-git/). | El grupo de seguridad **Git Contributors**. |
| **Administrador** | Todo lo de Colaborador, además de enviar cambios a todos los repositorios, incluido `udfs`, y crear organizaciones. | El grupo de seguridad **Git Administration**. |

El repositorio `udfs` está limitado a los administradores porque las funciones definidas por el usuario se ejecutan con la identidad del flujo de trabajo que las llama.

Si usted es **Visualizador**, la pestaña **Git** nombra hasta tres administradores del espacio de trabajo a quienes puede pedir que lo agreguen a **Git Contributors**.

## Git desde aplicaciones y UDF

La ventana de una aplicación Panel o Dash tiene una sección **Repositorio** que muestra su repositorio, su rama y el estado de la compilación, con **Edit in browser** y **Copy clone URL** para los miembros que pueden enviar cambios. La barra de herramientas de una UDF respaldada por Git tiene **Abrir**, que abre el repositorio en su rama en Git, y **Edit in browser** para los administradores.

## Otorgar acceso a Git

Los administradores del espacio de trabajo otorgan acceso en **Identidad** agregando miembros a un grupo de seguridad, o agregando el permiso a un grupo propio.

1. Agregue al miembro a **Git Contributors** para permitirle enviar código de aplicaciones, o a **Git Administration** para convertirlo en administrador de Git.
2. Para dar a cada miembro nuevo acceso de envío al código de aplicaciones, agregue **Git Contributors** a sus grupos predeterminados. **Git Administration** no puede ser un grupo predeterminado.
3. Para comprobar lo que un miembro puede hacer, abra el miembro y seleccione la pestaña **Git**. Muestra el nombre de usuario de Git del miembro, su nivel y el grupo que se lo otorga.

Un cambio se aplica la próxima vez que el miembro inicie sesión en Git o abra la pestaña **Git**. Desactivar o eliminar a un miembro bloquea su cuenta de Git, incluidos sus tokens y claves SSH, y reactivarlo la desbloquea. El personal de soporte de PlaidCloud tiene acceso de administrador automáticamente.

## Contenido de esta sección

- [Repositorios](/es/guides/git/repositories/): cree un repositorio y luego clone, confirme y envíe su trabajo
- [Incidencias](/es/guides/git/issues/): dé seguimiento a tareas, errores e ideas con etiquetas, hitos y responsables
- [Solicitudes de incorporación de cambios](/es/guides/git/pull-requests/): proponga cambios en una rama y revíselos antes de fusionarlos
- [Tableros de proyecto](/es/guides/git/projects/): organice incidencias y solicitudes de incorporación de cambios en un tablero Kanban
- [Versiones y etiquetas](/es/guides/git/releases-and-tags/): marque y publique instantáneas versionadas de un repositorio
- [Wikis](/es/guides/git/wikis/): mantenga documentación extensa junto a su código
- [Paquetes](/es/guides/git/packages/): publique e instale artefactos de compilación desde el registro del repositorio
- [Búsqueda de código](/es/guides/git/searching-code/): encuentre código, incidencias y solicitudes de incorporación de cambios en todos sus repositorios

## Temas relacionados

- [Implementar una aplicación Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/): sirva una aplicación de HoloViz Panel directamente desde un repositorio, con una conexión administrada sin credenciales
- [Implementar una aplicación Dash desde PlaidCloud Git](/es/guides/dash-apps/deploy-from-git/): sirva una aplicación de Plotly Dash de la misma manera
- [Administración de acceso](/es/administration/access/): cómo la pertenencia al espacio de trabajo y los grupos de seguridad determinan quién puede ver y editar repositorios
