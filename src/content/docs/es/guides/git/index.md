---
title: PlaidCloud Git
description: Aloje, versione y colabore en repositorios de Git dentro de PlaidCloud, con incidencias, solicitudes de incorporación de cambios, tableros de proyecto, versiones y wikis, e inicio de sesión único integrado.
sidebar:
  label: Resumen
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git es un servicio de Git privado integrado en su espacio de trabajo. Cada espacio de trabajo tiene su propio servidor de Git para almacenar código, configuración, cuadernos y cualquier otro archivo versionado, junto con las incidencias, las solicitudes de incorporación de cambios y los tableros de proyecto que su equipo usa para colaborar en ellos.

Usted inicia sesión con su cuenta de PlaidCloud, por lo que no hay un nombre de usuario ni una contraseña independientes que configurar. Los repositorios nuevos son privados de forma predeterminada y solo los ven los miembros a quienes usted conceda acceso.

## Abrir Git

Seleccione **Git** en la lista de aplicaciones de su espacio de trabajo. La pestaña **Git** muestra los repositorios de su espacio de trabajo con el nombre, la descripción, la rama predeterminada y la fecha de la última actualización de cada uno, y una línea en la parte superior indica qué puede hacer. Seleccione un repositorio para abrirlo, o **View all in Git** para ir a la interfaz web de Git. Use **← Back to** su espacio de trabajo en Git para volver a PlaidCloud.

Para clonar un repositorio, seleccione **Copy clone URL** en su fila. La primera vez, una sugerencia muestra lo que necesita:

1. Git debe estar instalado en su equipo.
2. Cree un token de acceso en Git, en **Configuración → Aplicaciones**, con el permiso **write:repository**. La sugerencia enlaza a esa página.
3. Cuando Git solicite una contraseña, pegue el token, no su contraseña de PlaidCloud.
4. Ejecute los dos comandos `git config --global user.name` y `user.email` que se muestran, los cuales ya contienen su nombre y su correo electrónico.

Consulte [Repositorios](/es/guides/git/repositories/) para ver el tutorial completo. Si no puede copiar una URL de clonación, tiene acceso de lectura; consulte más abajo.

## Niveles de acceso

Todas las personas con acceso a Git pueden leer los repositorios compartidos del espacio de trabajo. Otros dos niveles permiten enviar cambios.

| Nivel | Qué puede hacer | Lo otorga |
|---|---|---|
| **Leer** | Ver y clonar los repositorios compartidos. | Predeterminado para todos los miembros. |
| **Colaborador** | Todo lo de Leer, y enviar cambios al repositorio `apps`, donde reside el código de las aplicaciones de [Panel](/es/guides/panel-apps/deploy-from-git/) y [Dash](/es/guides/dash-apps/deploy-from-git/). | El grupo de seguridad **Git Contributors**. |
| **Administrador** | Todo lo de Colaborador, y enviar cambios a todos los repositorios, incluido `udfs`, y crear organizaciones. | El grupo de seguridad **Git Administration**. |

El repositorio `udfs` está limitado a los administradores porque las funciones definidas por el usuario se ejecutan con la identidad del flujo de trabajo que las llama.

Si tiene acceso de lectura, la pestaña **Git** nombra hasta tres administradores del espacio de trabajo a quienes puede pedir que lo agreguen a **Git Contributors**.

## Git desde aplicaciones y UDF

La ventana de una aplicación Panel o Dash tiene una sección **Repositorio** que muestra su repositorio, su rama y el estado de compilación, con **Edit in browser** y **Copy clone URL** para los miembros que pueden enviar cambios. La barra de herramientas de una UDF respaldada por Git tiene **Open**, que abre el repositorio en su rama en Git,, y **Edit in browser** para los administradores.

## Conceder acceso a Git

Los administradores del espacio de trabajo conceden acceso en **Identidad**, agregando miembros a un grupo de seguridad o agregando el permiso a un grupo propio.

1. Agregue al miembro a **Git Contributors** para que pueda enviar código de aplicaciones, o a **Git Administration** para convertirlo en administrador de Git.
2. Para dar a cada miembro nuevo acceso de envío al código de aplicaciones, agregue **Git Contributors** a sus grupos predeterminados. **Git Administration** no puede ser un grupo predeterminado.
3. Para comprobar qué puede hacer un miembro, abra el miembro y seleccione la pestaña **Git**. Muestra el nombre de usuario de Git del miembro, su nivel y el grupo que lo otorga.

Un cambio se aplica la próxima vez que el miembro inicie sesión en Git o abra la pestaña **Git**. El personal de soporte de PlaidCloud tiene acceso de administrador automáticamente.

## Contenido de esta sección

- [Repositorios](/es/guides/git/repositories/): cree un repositorio y luego clone, confirme y envíe su trabajo
- [Incidencias](/es/guides/git/issues/): dé seguimiento a tareas, errores e ideas con etiquetas, hitos y responsables
- [Solicitudes de incorporación de cambios](/es/guides/git/pull-requests/): proponga cambios en una rama y revíselos antes de combinarlos
- [Tableros de proyecto](/es/guides/git/projects/): organice incidencias y solicitudes de incorporación de cambios en un tablero Kanban
- [Versiones y etiquetas](/es/guides/git/releases-and-tags/): marque y publique instantáneas versionadas de un repositorio
- [Wikis](/es/guides/git/wikis/): mantenga documentación extensa junto a su código
- [Paquetes](/es/guides/git/packages/): publique e instale artefactos de compilación desde el registro del repositorio
- [Búsqueda de código](/es/guides/git/searching-code/): encuentre código, incidencias y solicitudes de incorporación de cambios en todos sus repositorios

## Información relacionada

- [Implementar una aplicación Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/): sirva una aplicación HoloViz Panel directamente desde un repositorio, con una conexión administrada sin credenciales
- [Implementar una aplicación Dash desde PlaidCloud Git](/es/guides/dash-apps/deploy-from-git/): sirva una aplicación de Plotly Dash de la misma manera
- [Administración de acceso](/es/administration/access/): cómo la pertenencia al espacio de trabajo y los grupos de seguridad determinan quién puede ver y editar repositorios
