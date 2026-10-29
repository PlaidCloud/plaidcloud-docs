---
title: Uso de una aplicación Panel
description: Consulte el estado de compilación, abra, recompile, bloquee, vea los registros y las métricas de uso, edite y quite aplicaciones HoloViz Panel publicadas desde la pantalla Mis aplicaciones Panel de PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Cada aplicación publicada aparece en la pantalla **Mis aplicaciones Panel** con su **Tiempo de ejecución**, **Estado**, **Slug** y marcas de tiempo. La columna situada más a la izquierda abre la aplicación; los demás iconos de la fila le permiten bloquearla para evitar cambios accidentales, editarla, quitarla y, en el caso de las aplicaciones de servidor, recompilarla, ver sus registros y ver las métricas de uso. El icono de apertura refleja el tiempo de ejecución de la aplicación, de modo que las aplicaciones WASM y las de servidor se distinguen a simple vista.

## Estado de compilación (aplicaciones de servidor)

La columna **Estado** de una aplicación de servidor refleja su compilación, y la lista se actualiza sola mientras hay una compilación en curso:

- **Compilando…**: PlaidCloud está compilando su repositorio en un contenedor. La aplicación todavía no tiene URL.
- **Lista**: la compilación se completó correctamente. La URL de la aplicación está activa y el icono **Abrir** aparece en su fila.
- **Error**: la compilación no se completó. Revise el punto de entrada y la rama, y luego edite la aplicación para volver a publicarla.

Las aplicaciones WASM no tienen paso de compilación y están disponibles en cuanto se publican.

## Recompilación de una aplicación de servidor

Haga clic en el icono **Recompilar** de la fila de una aplicación de servidor para recompilarla y volver a implementarla sin cambiar su configuración. El estado de la aplicación vuelve a **Compilando…** mientras PlaidCloud compila de nuevo la misma rama y el mismo punto de entrada, y después cambia a **Lista** cuando la nueva compilación está activa.

Use **Recompilar** después de cambios en las dependencias, actualizaciones de la imagen base o una compilación fallida transitoria. Editar y guardar una aplicación de servidor también la recompila, pero para recompilarla no es necesario abrir el formulario de edición.

En una aplicación de [App Runner](/es/guides/workflows/use-converted-alteryx-apps/#mantener-la-aplicación-al-día), es decir, el formulario de entrada generado para una aplicación de Alteryx convertida, **Recompilar** y guardar una edición primero actualizan sus archivos generados a la versión actual de App Runner y después la compilan. PlaidCloud también hace esto con todas las aplicaciones de App Runner que no están bloqueadas cuando se actualiza PlaidCloud; una aplicación bloqueada necesita una acción **Recompilar** después de que usted la desbloquee.

## Bloqueo de una aplicación

Haga clic en el icono de **candado** de la fila de una aplicación para protegerla de cambios accidentales. Mientras una aplicación está bloqueada:

- **Editar**, **Quitar** y **Recompilar** se niegan a ejecutarse y le indican que la aplicación está bloqueada.
- **Un push a la rama de una aplicación de servidor no la recompila**: la recompilación automática se omite hasta que desbloquee la aplicación. No se ejecuta ninguna compilación para un push omitido, así que no aparece nada nuevo en los registros de compilación de la aplicación; vuelva a hacer push (o use **Recompilar**) después de desbloquearla para aplicar el cambio.
- Abrir la aplicación, ver sus registros y ver sus métricas de uso siguen funcionando: el bloqueo solo impide los cambios, nunca a los visitantes.

Haga clic de nuevo en el icono para desbloquear. El icono muestra el estado actual de la aplicación: cerrado cuando está bloqueada, abierto cuando no lo está.

El bloqueo es una protección contra accidentes (una edición equivocada, una eliminación involuntaria o un push de git que llega a una aplicación que está presentando en una demostración), igual que el bloqueo de los flujos de trabajo y de los pasos de flujo de trabajo. **No** es un control de seguridad: cualquiera que pueda editar aplicaciones Panel también puede desbloquearlas.

> El bloqueo no cubre dos cosas: una **compilación que ya está en curso** cuando bloquea la aplicación termina igualmente y se activa, y los archivos de una aplicación **WASM** residen en su cuenta de documentos, de modo que reemplazar esos archivos cambia la aplicación en ejecución sin tocar el registro bloqueado.

## Apertura de una aplicación

Haga clic en el icono **Abrir** al comienzo de la fila de una aplicación lista para iniciarla en una pestaña nueva.

- Una aplicación de servidor se sirve en `https://<your-tenant-host>/serve/<slug>/`.
- El icono **Abrir** solo aparece cuando una aplicación de servidor está **Lista**.

Una aplicación de servidor se reduce a cero cuando está inactiva para ahorrar recursos, de modo que la primera apertura después de un período de inactividad tiene que ponerla en marcha. Mientras eso ocurre, verá una **pantalla de carga de PlaidCloud** (con el nombre de su aplicación, un indicador de progreso y los detalles de su espacio de trabajo) en lugar de una pestaña en blanco. La aplicación aparece por sí sola en cuanto está lista (normalmente en unos segundos, hasta aproximadamente un minuto en un arranque en frío) y después responde con normalidad hasta que vuelva a quedar inactiva.

> Si una aplicación no puede iniciarse, la pantalla de carga se convierte en un mensaje **“Esta aplicación no se inició”** con un botón **Intentar de nuevo** en lugar de girar indefinidamente. Si eso sigue ocurriendo, edite la aplicación para revisar su punto de entrada y su rama y vuelva a publicarla, o comuníquese con el administrador de PlaidCloud.

### Apariencia

Las aplicaciones Panel de servidor usan de forma predeterminada el diseño moderno **FAST** de PlaidCloud, pero la opción **Diseño** de la aplicación permite volver al estilo **Predeterminado** de Panel cuando el CSS existente depende de él. El tema (claro, oscuro o un conmutador claro/oscuro que los visitantes pueden alternar) se define en la plantilla de su aplicación. Consulte [Definir el tema](/es/guides/panel-apps/creating/#definir-el-tema-claro-oscuro-o-con-interruptor) en la guía de creación para ver los patrones. Si las tablas o los estilos personalizados de su aplicación están pensados para un fondo claro, manténgala fijada en claro.

## Visualización de registros (aplicaciones de servidor)

Haga clic en el icono **Ver registros** de la fila de una aplicación de servidor para abrir su visor de registros. (Las aplicaciones WASM se ejecutan por completo en el navegador y no tienen registros de servidor, por lo que el icono solo aparece en las filas de aplicaciones de servidor.)

El visor tiene dos pestañas:

- **Tiempo de ejecución** (se muestra primero): la salida propia de la aplicación en ejecución, es decir, todo lo que registra, todo lo que imprime y los errores no controlados. Se conservan incluso después de que la aplicación se reduzca a cero, de modo que puede revisar lo que hizo una sesión anterior.
- **Compilación**: la salida de la compilación del contenedor de la aplicación. Úsela para ver *por qué* una compilación muestra **Error**, por ejemplo, una dependencia que no se pudo instalar.

Cada pestaña ofrece filtros **Información / Advertencia / Error**, un intervalo de tiempo **Registros desde** (desde la última hora hasta 30 días, o todos), un botón **Actualizar** y **Actualización automática** para consultar periódicamente las entradas nuevas, algo útil mientras observa una aplicación activa o una compilación en curso. Las entradas más recientes aparecen primero.

> Si no se pudo capturar la salida de la compilación, la pestaña Compilación muestra una nota breve que explica el motivo en lugar de aparecer vacía.

### Lectura de un mensaje de registro completo

La tabla de registros recorta las líneas largas para que la lista siga siendo legible. Seleccione una fila de registro para abrir un **panel de detalles** junto a la tabla que muestra el mensaje completo de la entrada. Es la forma más sencilla de leer algo que no cabe en la tabla (un mensaje de error largo o un seguimiento de pila completo) sin que se corte.

### Copia de líneas de registro

Puede seleccionar varias filas de registro a la vez y hacer clic en **Copiar** para colocarlas en el portapapeles. Esto resulta útil para pegar los registros en una conversación con un asistente de IA cuando depura su aplicación, o en un mensaje para su equipo o para el soporte de PlaidCloud.

### Quién generó una línea de registro

Cuando su aplicación inicia la sesión de los visitantes, cada línea de registro se etiqueta con el **usuario** cuya sesión la generó, de modo que puede saber qué visitante encontró un error o una advertencia concretos. El etiquetado se hace en la medida de lo posible: algunas líneas del marco de trabajo y del arranque se ejecutan antes de que intervenga ningún visitante y puede que no muestren un usuario.

## Métricas de uso (aplicaciones de servidor)

Haga clic en el icono **Métricas de uso** de la fila de una aplicación de servidor, junto a **Ver registros**, para ver cómo se está usando la aplicación. La vista resume lo siguiente:

- **Usuarios únicos**: cuántas personas distintas han abierto la aplicación.
- **Sesiones**: cuántas veces se ha abierto.
- **Duración promedio y mediana de la sesión**: aproximadamente cuánto dura una visita.
- **Último uso**: cuándo se abrió la aplicación por última vez.

Debajo del resumen encontrará un desglose **por usuario** y **por día**, para que pueda ver quién usa la aplicación y cómo evoluciona el uso con el tiempo.

> Las duraciones son aproximadas. Las aplicaciones de servidor quedan inactivas y se reducen cuando nadie las usa, así que no siempre se observa el final exacto de una sesión: interprete las cifras de duración como una referencia, no como una medición exacta.

## Edición de una aplicación

Haga clic en el icono de **lápiz** de la fila de una aplicación para editarla. El formulario de edición corresponde al tiempo de ejecución de la aplicación.

En una aplicación de **servidor** puede cambiar el nombre, el slug, la rama, el punto de entrada, la CPU, la memoria, el diseño, el período de inactividad, el indicador público, los dominios de servicio incrustado y la nota. La **Conexión de Git** queda fija una vez creada la aplicación y se muestra en modo de solo lectura. Al guardar se recompila la aplicación: su estado vuelve a **Compilando…** hasta que la nueva compilación esté lista.

## Eliminación de una aplicación

Haga clic en el icono de **menos** de la fila de una aplicación y confirme; eliminar o anular la publicación de una aplicación siempre le pide confirmación primero. Quitar una aplicación de servidor desmonta su compilación y su implementación; quitar una aplicación WASM anula la publicación del archivo estático. La URL de la aplicación deja de funcionar de inmediato.

La herramienta MCP `panel_deployment_manage` ya no ofrece la anulación de publicación. En su lugar, quite la aplicación desde esta lista.
