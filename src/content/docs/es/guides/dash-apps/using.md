---
title: Uso de una aplicación Dash
description: Siga el estado de compilación, abra, recompile, bloquee, consulte los registros, edite y elimine aplicaciones Plotly Dash publicadas desde la pantalla Mis aplicaciones Panel de PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/using.md
---

Las aplicaciones Dash aparecen en la misma pantalla **Mis aplicaciones Panel** que sus aplicaciones Panel WASM y de servidor, con **Dash** en la columna **Tiempo de ejecución** y su propio ícono para distinguirlas fácilmente. Todo lo de esta página replica [Uso de una aplicación Panel](/es/guides/panel-apps/using/) para una aplicación de servidor, con una excepción indicada más abajo: las aplicaciones Dash todavía no tienen **Usage Metrics**.

## Estado de compilación

La columna **Estado** de una aplicación Dash sigue su compilación, y la lista se actualiza sola mientras hay una compilación en curso:

- **Compilando…**: PlaidCloud está compilando su repositorio en un contenedor. La aplicación todavía no tiene URL.
- **Lista**: la compilación se realizó correctamente. La URL de la aplicación está activa y el ícono **Abrir** aparece en su fila.
- **Error**: la compilación no se completó. Revise el punto de entrada y la rama, y luego edite la aplicación para volver a publicarla.

## Recompilar una aplicación Dash

Haga clic en el ícono **Recompilar** de la fila de una aplicación Dash para recompilarla y volver a implementarla sin cambiar su configuración. El estado de la aplicación vuelve a **Compilando…** mientras PlaidCloud compila de nuevo la misma rama y el mismo punto de entrada, y después pasa otra vez a **Lista** cuando la nueva compilación está activa.

Use **Recompilar** tras cambios de dependencias, actualizaciones de la imagen base o una compilación fallida transitoria. Editar y guardar una aplicación Dash también la recompila, pero una recompilación no requiere abrir el formulario de edición.

## Bloquear una aplicación

Haga clic en el ícono de **candado** de la fila de una aplicación para protegerla de cambios accidentales. Mientras una aplicación Dash está bloqueada:

- **Editar**, **Quitar** y **Recompilar** se niegan a ejecutarse y le indican que la aplicación está bloqueada.
- **Un envío a la rama de la aplicación no la recompila**: la recompilación automática se omite hasta que desbloquee la aplicación. Vuelva a enviar (o use **Recompilar**) después de desbloquear para aplicar el cambio.
- Abrir la aplicación y ver sus registros siguen funcionando: el bloqueo solo impide los cambios, nunca a los espectadores.

Haga clic de nuevo en el ícono para desbloquear. El ícono muestra el estado actual de la aplicación: cerrado cuando está bloqueada, abierto cuando no. El bloqueo es una protección contra accidentes, no un control de seguridad: cualquiera que pueda editar aplicaciones Dash también puede desbloquearlas.

## Abrir una aplicación Dash

Haga clic en el ícono **Abrir** al inicio de la fila de una aplicación lista para iniciarla en una pestaña nueva, en `https://<your-tenant-host>/serve/<slug>/`. El ícono aparece solo cuando la aplicación está **Lista**.

Una aplicación Dash escala a cero cuando está inactiva para ahorrar recursos, por lo que la primera apertura tras un período de inactividad debe ponerla en marcha. Mientras eso ocurre, ve una **pantalla de carga de PlaidCloud** en lugar de una pestaña en blanco, y la aplicación aparece sola cuando está lista. Si una aplicación no puede iniciarse, la pantalla de carga se convierte en un mensaje **“This app didn't start”** con un botón **Intentar de nuevo**; si eso sigue ocurriendo, edite la aplicación para revisar su punto de entrada y su rama, y vuelva a publicarla.

> **Un `dcc.Interval` (o cualquier otro sondeo siempre activo) anula el escalado a cero mientras su pestaña permanezca abierta.** El escalado a cero depende de que la aplicación quede en silencio (sin solicitudes en curso) cuando nadie la está usando activamente. Un componente que sigue haciendo solicitudes con un temporizador, como `dcc.Interval`, mantiene la aplicación activa mientras esa pestaña esté abierta, aunque la persona que la mira se haya alejado. Si desea que una aplicación se reduzca entre visitas, evite el sondeo siempre activo o detenga el intervalo cuando la página lleve un tiempo inactiva.

## Ver registros

Haga clic en el ícono **Ver registros** de la fila de una aplicación Dash para abrir su visor de registros, con las mismas pestañas **Tiempo de ejecución** y **Compilación**, filtros, intervalo de tiempo y panel de detalles que tiene una aplicación Panel de servidor; consulte [Ver registros](/es/guides/panel-apps/using/#visualización-de-registros-aplicaciones-de-servidor) para conocer todos los detalles. Cada línea de registro de ejecución se etiqueta con el **usuario** cuya sesión la produjo, igual que las de una aplicación Panel de servidor.

**Usage Metrics no está disponible para las aplicaciones Dash en esta versión**: el ícono **Usage Metrics** que aparece en la fila de una aplicación Panel de servidor no aparece para las aplicaciones Dash, por lo que todavía no hay un desglose de usuarios únicos y sesiones que consultar.

## Editar una aplicación

Haga clic en el ícono de **lápiz** de la fila de una aplicación Dash para editarla. Puede cambiar el nombre, el slug, la rama, el punto de entrada, la CPU, la memoria, la ventana de inactividad, el indicador de acceso público, los dominios de servicio incrustado y la nota. La **Conexión de Git** queda fija una vez creada la aplicación y se muestra como solo lectura. No hay ningún campo **Diseño** que editar: esa opción es específica de Panel. Al guardar se recompila la aplicación; su estado vuelve a **Compilando…** hasta que la nueva compilación esté lista.

## Eliminar una aplicación

Haga clic en el ícono de **menos** de la fila de una aplicación Dash y confirme. Al eliminarla se desmontan su compilación y su implementación, y la URL de la aplicación deja de funcionar de inmediato.
