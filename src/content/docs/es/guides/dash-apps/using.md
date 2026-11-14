---
title: Uso de una aplicación de Dash
description: Supervise el estado de compilación y abra, recompile, bloquee, consulte los registros, edite y quite aplicaciones de Plotly Dash publicadas desde la pantalla Aplicaciones de PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/using.md
---

Las aplicaciones de Dash aparecen en la misma pantalla **Aplicaciones** que sus aplicaciones Panel WASM y de servidor, con **Dash** en la columna **Tiempo de ejecución** y un icono propio para distinguirlas fácilmente. Todo lo que se describe en esta página es igual que en [Uso de una aplicación Panel](/es/guides/panel-apps/using/) para una aplicación de servidor, con una excepción que se indica más abajo: las aplicaciones de Dash todavía no disponen de **Usage Metrics**.

## Estado de compilación

La columna **Estado** de una aplicación de Dash muestra el progreso de su compilación, y la lista se actualiza sola mientras hay una compilación en curso:

- **Compilando…**: PlaidCloud está compilando su repositorio en un contenedor. La aplicación todavía no tiene URL.
- **Lista**: la compilación se completó correctamente. La URL de la aplicación ya está activa y aparece el icono **Abrir** en su fila.
- **Error**: la compilación no se completó. Compruebe el punto de entrada y la rama y, a continuación, edite la aplicación para volver a publicarla.

## Recompilar una aplicación de Dash

Haga clic en el icono **Recompilar** de la fila de una aplicación de Dash para recompilarla y volver a implementarla sin cambiar su configuración. El estado de la aplicación vuelve a **Compilando…** mientras PlaidCloud compila de nuevo la misma rama y el mismo punto de entrada, y cambia otra vez a **Lista** cuando la nueva compilación está activa.

Use **Recompilar** después de cambiar dependencias, de actualizar la imagen base o tras un error de compilación transitorio. Editar y guardar una aplicación de Dash también la recompila, pero para recompilarla no hace falta abrir el formulario de edición.

## Bloquear una aplicación

Haga clic en el icono de **candado** de la fila de una aplicación para protegerla de cambios accidentales. Mientras una aplicación de Dash está bloqueada:

- **Editar**, **Quitar** y **Recompilar** no se ejecutan y le indican que la aplicación está bloqueada.
- **Un push a la rama de la aplicación no la recompila**: la recompilación automática se omite hasta que desbloquee la aplicación. Después de desbloquearla, vuelva a hacer push (o use **Recompilar**) para incorporar el cambio.
- Abrir la aplicación y consultar sus registros siguen funcionando: el bloqueo solo impide cambios, nunca el acceso de quienes la visualizan.

Haga clic de nuevo en el icono para desbloquearla. El icono muestra el estado actual de la aplicación: cerrado cuando está bloqueada y abierto cuando no lo está. El bloqueo es una protección frente a accidentes, no un control de seguridad: cualquier persona que pueda editar aplicaciones de Dash también puede desbloquearlas.

## Abrir una aplicación de Dash

Haga clic en el icono **Abrir** al principio de la fila de una aplicación lista para iniciarla en una pestaña nueva, en `https://<your-tenant-host>/serve/<slug>/`. El icono solo aparece cuando la aplicación está **Lista**.

Una aplicación de Dash escala a cero cuando está inactiva para ahorrar recursos, por lo que la primera vez que se abre tras un período de inactividad tiene que arrancar. Mientras tanto, verá una **pantalla de carga de PlaidCloud** en lugar de una pestaña en blanco, que muestra el progreso de la aplicación por las fases **Iniciando**, **Preparando** y **Cargando aplicación**, y la aplicación aparece sola en cuanto está lista. Si una aplicación no puede iniciarse, la pantalla de carga se convierte en un mensaje que indica que la aplicación no se inició y en qué fase se detuvo, con un botón **Intentar de nuevo**; si esto se repite, edite la aplicación para comprobar su punto de entrada y su rama, y vuelva a publicarla.

> **Un `dcc.Interval` (o cualquier otro sondeo permanente) impide el escalado a cero mientras su pestaña siga abierta.** El escalado a cero depende de que la aplicación quede en reposo, sin solicitudes en curso, cuando nadie la está usando activamente. Un componente que sigue enviando solicitudes con un temporizador, como `dcc.Interval`, mantiene la aplicación activa mientras esa pestaña esté abierta, aunque la persona que la estaba mirando se haya ausentado. Si quiere que una aplicación se reduzca entre visitas, evite los sondeos permanentes o detenga el intervalo cuando la página lleve un tiempo inactiva.

## Consultar los registros

Haga clic en el icono **Ver registros** de la fila de una aplicación de Dash para abrir su visor de registros, con las mismas pestañas **Tiempo de ejecución** y **Compilación**, filtros, intervalo de tiempo y panel de detalles que tiene una aplicación Panel de servidor; consulte [Consultar los registros](/es/guides/panel-apps/using/#consultar-los-registros-aplicaciones-de-servidor) para ver el funcionamiento completo. Cada línea del registro de tiempo de ejecución se etiqueta con el **usuario** cuya sesión la generó, igual que en una aplicación Panel de servidor.

**Usage Metrics no está disponible para las aplicaciones de Dash en esta versión**: el icono **Usage Metrics** que aparece en la fila de una aplicación Panel de servidor no aparece en las aplicaciones de Dash, por lo que todavía no hay un desglose de usuarios únicos y sesiones que consultar.

## Editar una aplicación

Haga clic en el icono de **lápiz** de la fila de una aplicación de Dash para editarla. Puede cambiar el nombre, el slug, la rama, el punto de entrada, la CPU, la memoria, el período de inactividad, el indicador de acceso público, los dominios de publicación incrustada y el memo. La **Conexión de Git** queda fijada al crear la aplicación y se muestra en modo de solo lectura. No hay ningún campo **Diseño** que editar: esa opción es específica de Panel. Al guardar, la aplicación se recompila: su estado vuelve a **Compilando…** hasta que la nueva compilación está lista.

## Quitar una aplicación

Haga clic en el icono de **menos** de la fila de una aplicación de Dash y confirme. Al quitarla, se eliminan su compilación y su implementación, y la URL de la aplicación deja de funcionar de inmediato.
