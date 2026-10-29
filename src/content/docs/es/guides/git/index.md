---
title: PlaidCloud Git
description: Aloje, versione y colabore en repositorios de Git dentro de PlaidCloud, con incidencias, solicitudes de incorporación de cambios, tableros de proyecto, versiones y wikis, y con inicio de sesión único integrado.
sidebar:
  label: Descripción general
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git es un servicio de Git privado integrado en su espacio de trabajo. Cada espacio de trabajo recibe su propio servidor de Git para almacenar código, configuración, notebooks y cualquier otro archivo con control de versiones, junto con las incidencias, las solicitudes de incorporación de cambios y los tableros de proyecto que su equipo usa para colaborar en ellos.

Usted inicia sesión con su cuenta de PlaidCloud, por lo que no hay que configurar un nombre de usuario ni una contraseña aparte. Abra **Git** desde su espacio de trabajo y ya habrá iniciado sesión. Los repositorios nuevos son privados de forma predeterminada y solo los ven los miembros a quienes usted otorgue acceso.

## Administración de Git

Cualquier miembro puede crear repositorios, pero **crear organizaciones**, es decir, espacios compartidos que agrupan repositorios y equipos, requiere el permiso **Git Administration**. Otórguelo en **Identidad** agregando el permiso a un grupo de seguridad, o agregando miembros al grupo integrado **Git Administration**. Cualquier persona que pertenezca a un grupo con el permiso se convierte en administrador de Git la próxima vez que inicie sesión en Git. El personal de soporte de PlaidCloud lo tiene automáticamente.

Si un administrador recién autorizado nunca ha abierto Git, es posible que deba iniciar sesión en Git **dos veces** para que el acceso de administrador surta efecto: el primer inicio de sesión crea su cuenta de Git y el permiso se aplica en el siguiente.

## Contenido de esta sección

- [Repositorios](/es/guides/git/repositories/) — cree un repositorio y luego clone, confirme y envíe su trabajo
- [Incidencias](/es/guides/git/issues/) — dé seguimiento a tareas, errores e ideas con etiquetas, hitos y responsables
- [Solicitudes de incorporación de cambios](/es/guides/git/pull-requests/) — proponga cambios en una rama y revíselos antes de fusionarlos
- [Tableros de proyecto](/es/guides/git/projects/) — organice incidencias y solicitudes de incorporación de cambios en un tablero Kanban
- [Versiones y etiquetas](/es/guides/git/releases-and-tags/) — marque y publique instantáneas versionadas de un repositorio
- [Wikis](/es/guides/git/wikis/) — mantenga documentación extensa junto a su código
- [Paquetes](/es/guides/git/packages/) — publique e instale artefactos de compilación desde el registro del repositorio
- [Búsqueda de código](/es/guides/git/searching-code/) — encuentre código, incidencias y solicitudes de incorporación de cambios en todos sus repositorios

## Información relacionada

- [Implementar una aplicación Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/) — sirva una aplicación Panel de HoloViz directamente desde un repositorio, con una conexión administrada que no requiere credenciales
- [Implementar una aplicación de Dash desde PlaidCloud Git](/es/guides/dash-apps/deploy-from-git/) — sirva una aplicación de Plotly Dash de la misma manera
- [Administración de acceso](/es/administration/access/) — cómo la pertenencia al espacio de trabajo y los grupos de seguridad rigen quién puede ver y editar repositorios
