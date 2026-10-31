---
title: Conector de PlaidCloud Git
description: Conecte una aplicación de Panel, una aplicación de Dash o un flujo de trabajo a un repositorio de PlaidCloud Git, el servicio de Git administrado e integrado, sin URL de servidor ni credenciales que configurar.
sidebar:
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/plaidcloud-git.md
---

**PlaidCloud Git** es el servicio de Git administrado integrado en su espacio de trabajo. Una conexión de PlaidCloud Git dirige una implementación de Panel o Dash, o un flujo de trabajo, a uno de sus repositorios. Como el servicio es administrado, **no necesita URL de servidor, nombre de usuario ni token**: PlaidCloud proporciona el host y se autentica en su nombre.

Para consultar el tutorial completo sobre cómo servir una aplicación desde una de estas conexiones, vea [Implementar una aplicación de Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/) o [Implementar una aplicación de Dash desde PlaidCloud Git](/es/guides/dash-apps/deploy-from-git/). Para crear repositorios y enviar código, consulte las [guías de PlaidCloud Git](/es/guides/git/).

## Configuración

En **Herramientas > Conexiones**, haga clic en **Nueva conexión** y elija **PlaidCloud Git**. El formulario omite las secciones de autenticación, SSL y SSH que muestran los proveedores de Git externos, porque las credenciales las deriva la plataforma, y deja la identidad de la conexión, su uso y el repositorio de destino.

### Identificación

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre de la cuenta | Texto | Nombre para mostrar de esta conexión. |
| Memo | Texto | Nota opcional sobre la finalidad de la conexión. |

### Repositorio

| Campo | Tipo | Descripción |
|---|---|---|
| Repositorio | Selector | El repositorio que se va a usar. Haga clic en **Actualizar** para mostrar los repositorios de su espacio de trabajo, por ejemplo `apps` o `udfs`, y elija uno. |
| Rama predeterminada | Selector | La rama de la que se lee, elegida entre las ramas del repositorio seleccionado. |
| Ruta de inicio | Selector | Opcional. Explore el repositorio seleccionado y elija una carpeta para limitar todas las búsquedas de archivos a un subdirectorio. |

**Uso** (`Active` / `Read Only`) y el **Modelo de seguridad** (quién del espacio de trabajo puede usar la conexión) son la configuración estándar de las conexiones; consulte la [guía de la conexión](/es/guides/connections/plaidcloud-git/) y [Crear y administrar una conexión](/es/guides/connections/create-connection/).

## Usos habituales

- Servir una [aplicación de HoloViz Panel](/es/guides/panel-apps/deploy-from-git/) o una [aplicación de Plotly Dash](/es/guides/dash-apps/deploy-from-git/) desde el repositorio `apps` de su espacio de trabajo.
- Obtener funciones definidas por el usuario, configuración o archivos con plantillas que residen en PlaidCloud Git.

## Temas relacionados

- [Conexión de PlaidCloud Git](/es/guides/connections/plaidcloud-git/) — guía de tareas para crear la conexión, con el uso y el modelo de seguridad
- [Implementar una aplicación de Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/) — el recorrido completo desde el repositorio hasta la aplicación servida
- [Implementar una aplicación de Dash desde PlaidCloud Git](/es/guides/dash-apps/deploy-from-git/) — el mismo recorrido para una aplicación de Plotly Dash
- [Guías de PlaidCloud Git](/es/guides/git/) — repositorios, incidencias, solicitudes de incorporación de cambios y más
- [Conexiones a repositorios de Git](/es/reference/connectors/git/) — proveedores de Git externos (GitHub, GitLab y otros)
