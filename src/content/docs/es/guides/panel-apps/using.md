---
title: Uso de una aplicación de Panel
description: Siga el estado de compilación, abra, recompile, bloquee, consulte los registros y las métricas de uso, edite y quite aplicaciones de HoloViz Panel publicadas desde la pantalla Mis aplicaciones Panel de PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Cada aplicación publicada aparece en la pantalla **Mis aplicaciones Panel** con su **Tiempo de ejecución**, **Estado**, **Slug** y marcas de tiempo. La columna situada más a la izquierda abre la aplicación; los demás iconos de la fila permiten bloquearla frente a cambios accidentales, editarla, quitarla y, en el caso de las aplicaciones de servidor, recompilarla, consultar sus registros y ver las métricas de uso. El icono de apertura refleja el tiempo de ejecución de la aplicación, de modo que las aplicaciones WASM y de servidor se distinguen fácilmente de un vistazo.

## Estado de compilación (aplicaciones de servidor)

La columna **Estado** de una aplicación de servidor sigue su compilación, y la lista se actualiza automáticamente mientras hay una compilación en curso:

- **Compilando…**: PlaidCloud está compilando su repositorio en un contenedor. La aplicación todavía no tiene URL.
- **Lista**: la compilación se realizó correctamente. La URL de la aplicación está activa y el icono **Abrir** aparece en su fila.
- **Error**: la compilación no se completó. Compruebe el punto de entrada y la rama y, a continuación, edite la aplicación para volver a publicarla.

Las aplicaciones WASM no tienen paso de compilación y están disponibles en cuanto se publican.

## Recompilación de una aplicación de servidor

Haga clic en el icono **Recompilar** de la fila de una aplicación de servidor para recompilarla y volver a implementarla sin cambiar su configuración. El estado de la aplicación vuelve a **Compilando…** mientras PlaidCloud compila de nuevo la misma rama y el mismo punto de entrada, y después vuelve a **Lista** cuando la nueva compilación está activa.

Use **Recompilar** después de cambios en las dependencias, actualizaciones de la imagen base o una compilación fallida transitoria. Editar y guardar una aplicación de servidor también la recompila, pero una recompilación no requiere abrir el formulario de edición.

Para una aplicación de [App Runner](/es/guides/workflows/use-converted-alteryx-apps/#mantener-la-aplicación-al-día), el formulario de entrada generado para una aplicación de Alteryx convertida, **Recompilar** y guardar una edición primero actualizan sus archivos generados a la versión actual de App Runner y después la compilan. PlaidCloud también hace esto con todas las aplicaciones de App Runner que no están bloqueadas cuando se actualiza PlaidCloud; una aplicación bloqueada necesita **Recompilar** después de desbloquearla.

## Bloqueo de una aplicación

Haga clic en el icono de **candado** de la fila de una aplicación para protegerla frente a cambios accidentales. Mientras una aplicación está bloqueada:

- **Editar**, **Quitar** y **Recompilar** se niegan a ejecutarse y le indican que la aplicación está bloqueada.
- **Un push a la rama de una aplicación de servidor no la recompila**: la recompilación automática se omite hasta que desbloquee la aplicación. No se ejecuta ninguna compilación para un push omitido, por lo que no aparece nada nuevo en los registros de compilación de la aplicación; vuelva a hacer push (o use **Recompilar**) después de desbloquear para incorporar el cambio.
- Abrir la aplicación, consultar sus registros y ver sus métricas de uso siguen funcionando: el bloqueo solo impide los cambios, nunca a los visualizadores.

Haga clic de nuevo en el icono para desbloquear. El icono muestra el estado actual de la aplicación: cerrado cuando está bloqueada, abierto cuando no lo está.

El bloqueo es una protección contra accidentes (una edición equivocada, una eliminación involuntaria o un push de git que llega a una aplicación que está mostrando en una demostración), igual que el bloqueo de los flujos de trabajo y de los pasos de flujo de trabajo. **No** es un control de seguridad: cualquier persona que pueda editar aplicaciones de Panel también puede desbloquearlas.

> Dos cosas que el bloqueo no cubre: una **compilación ya en curso** cuando bloquea la aplicación sigue terminando y se activa, y los archivos de una aplicación **WASM** residen en su cuenta de documentos, por lo que reemplazar esos archivos cambia la aplicación en ejecución sin tocar el registro bloqueado.

## Apertura de una aplicación

Haga clic en el icono **Abrir** al principio de la fila de una aplicación lista para iniciarla en una pestaña nueva. **Abrir** es también el primer elemento del menú **⋯** de la fila. Consulte [El menú de acciones de fila](/es/guides/dashboards/using-dashboards/#el-menú-de-acciones-de-fila).

- Una aplicación de servidor se sirve en `https://<your-tenant-host>/serve/<slug>/`.
- El icono **Abrir** aparece solo cuando una aplicación de servidor está **Lista**.

Una aplicación de servidor se reduce a cero cuando está inactiva para ahorrar recursos, por lo que la primera apertura después de un período de inactividad tiene que ponerla en marcha. Mientras eso sucede, verá una **pantalla de carga de PlaidCloud** (el nombre de su aplicación, un indicador de progreso y los detalles de su espacio de trabajo) en lugar de una pestaña en blanco. La aplicación aparece automáticamente en cuanto está lista (normalmente en unos segundos, hasta aproximadamente un minuto en un arranque en frío) y después responde con normalidad hasta que vuelve a quedar inactiva.

> Si una aplicación no puede iniciarse, la pantalla de carga se convierte en un mensaje **“This app didn't start”** con un botón **Intentar de nuevo**, en lugar de girar indefinidamente. Si esto sigue ocurriendo, edite la aplicación para comprobar su punto de entrada y su rama y vuelva a publicarla, o póngase en contacto con el administrador de PlaidCloud.

### Apariencia

Las aplicaciones de Panel de servidor usan de forma predeterminada el diseño moderno **Fast** de PlaidCloud, pero la opción **Diseño** de la aplicación puede volver al estilo **Predeterminado** de Panel cuando el CSS existente depende de él. El tema (claro, oscuro o un interruptor claro/oscuro que los visualizadores pueden cambiar) se define en la plantilla de su aplicación. Consulte [Definir el tema](/es/guides/panel-apps/creating/#definir-el-tema-claro-oscuro-o-con-interruptor) en la guía de creación para ver los patrones. Si las tablas o los estilos personalizados de su aplicación están diseñados para un fondo claro, manténgala fija en claro.

## Consulta de los registros (aplicaciones de servidor)

Haga clic en el icono **Ver registros** de la fila de una aplicación de servidor para abrir su visor de registros. (Las aplicaciones WASM se ejecutan por completo en el navegador y no tienen registros de servidor, por lo que el icono aparece solo en las filas de aplicaciones de servidor.)

El visor tiene dos pestañas:

- **Tiempo de ejecución** (se muestra primero): la salida propia de la aplicación en ejecución, es decir, todo lo que registra, todo lo que imprime y cualquier error no detectado. Se conservan incluso después de que la aplicación se reduzca a cero, por lo que puede revisar lo que hizo una sesión anterior.
- **Compilación**: la salida de la compilación del contenedor de la aplicación. Úsela para ver *por qué* una compilación muestra **Error**, por ejemplo, una dependencia que no se pudo instalar.

Cada pestaña ofrece filtros **Información / Advertencia / Error**, un intervalo de tiempo **Registros desde** (desde la última hora hasta 30 días, o todos), un botón **Actualizar** y **Actualización automática** para consultar periódicamente las nuevas entradas, útil mientras observa una aplicación activa o una compilación en curso. Las entradas más recientes aparecen primero.

> Si no se pudo capturar la salida de la compilación, la pestaña Compilación muestra una breve nota que explica el motivo en lugar de aparecer vacía.

### Lectura de un mensaje de registro completo

La tabla de registros recorta las líneas largas para mantener la lista legible. Seleccione una fila del registro para abrir un **panel de detalles** junto a la tabla que muestra el **Mensaje de registro** completo de la entrada. Esta es la forma más sencilla de leer algo demasiado largo para la tabla (un mensaje de error largo o un seguimiento de pila completo) sin que se corte.

### Copia de líneas de registro

Puede seleccionar varias filas del registro a la vez y hacer clic en **Copiar** para ponerlas en el portapapeles. Esto resulta útil para pegar registros en una conversación con un asistente de IA cuando depura su aplicación, o en un mensaje para su equipo o para el soporte de PlaidCloud.

### Quién desencadenó una línea de registro

Cuando su aplicación inicia sesión a los visualizadores, cada línea de registro se etiqueta con el **usuario** cuya sesión la produjo, de modo que pueda saber qué visualizador encontró un error o una advertencia concretos. El etiquetado se hace en la medida de lo posible: algunas líneas del marco de trabajo y del inicio se ejecutan antes de que intervenga ningún visualizador y pueden no mostrar un usuario.

## Métricas de uso (aplicaciones de servidor)

Haga clic en el icono **Métricas de uso** de la fila de una aplicación de servidor, junto a **Ver registros**, para ver cómo se está usando la aplicación. La vista resume:

- **Usuarios únicos**: cuántas personas distintas han abierto la aplicación.
- **Sesiones**: cuántas veces se ha abierto.
- **Duración media y mediana de las sesiones**: aproximadamente cuánto dura una visita.
- **Último uso**: cuándo se abrió la aplicación por última vez.

Debajo del resumen aparece un desglose **por usuario** y **por día**, para que pueda ver quién usa la aplicación y cómo evoluciona el uso con el tiempo.

> Las duraciones son aproximadas. Las aplicaciones de servidor quedan inactivas y se reducen cuando nadie las usa, por lo que no siempre se observa el final exacto de una sesión: interprete las cifras de duración como una guía, no como una medición exacta.

## Edición de una aplicación

Haga clic en el icono del **lápiz** de la fila de una aplicación para editarla. El formulario de edición corresponde al tiempo de ejecución de la aplicación.

En una aplicación de **servidor** puede cambiar el nombre, el slug, la rama, el punto de entrada, la CPU, la memoria, el diseño, el período de inactividad, el indicador de público, los dominios de servicio incrustado y la nota. La **Conexión de Git** queda fija una vez creada la aplicación y se muestra en solo lectura. Al guardar se recompila la aplicación: su estado vuelve a **Compilando…** hasta que la nueva compilación está lista.

## Eliminación de una aplicación

Haga clic en el icono del **signo menos** de la fila de una aplicación y confirme; eliminar o anular la publicación de una aplicación siempre pide confirmación primero. Quitar una aplicación de servidor desmonta su compilación y su implementación; quitar una aplicación WASM anula la publicación del archivo estático. La URL de la aplicación deja de funcionar de inmediato.

La herramienta MCP `panel_deployment_manage` ya no ofrece anular la publicación. En su lugar, quite la aplicación de esta lista.
