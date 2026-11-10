---
title: Uso de una aplicación Panel
description: Supervise el estado de compilación y abra, recompile, bloquee, consulte los registros y las métricas de uso, edite y quite aplicaciones de HoloViz Panel publicadas desde la pantalla Mis aplicaciones Panel de PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Cada aplicación publicada aparece en la pantalla **Mis aplicaciones Panel** con su **Tiempo de ejecución**, **Estado**, **Slug** y marcas de tiempo. La columna situada más a la izquierda abre la aplicación; los demás iconos de la fila le permiten bloquearla frente a cambios accidentales, editarla, quitarla y, en el caso de las aplicaciones de servidor, recompilarla, consultar sus registros y ver sus métricas de uso. El icono para abrir refleja el tiempo de ejecución de la aplicación, por lo que las aplicaciones WASM y las de servidor se distinguen fácilmente de un vistazo.

## Estado de compilación (aplicaciones de servidor)

La columna **Estado** de una aplicación de servidor muestra el progreso de su compilación, y la lista se actualiza sola mientras hay una compilación en curso:

- **Compilando…**: PlaidCloud está compilando su repositorio en un contenedor. La aplicación todavía no tiene URL.
- **Lista**: la compilación se completó correctamente. La URL de la aplicación ya está activa y aparece el icono **Abrir** en su fila.
- **Error**: la compilación no se completó. Compruebe el punto de entrada y la rama y, a continuación, edite la aplicación para volver a publicarla.

Las aplicaciones WASM no tienen fase de compilación y están disponibles en cuanto se publican.

## Recompilar una aplicación de servidor

Haga clic en el icono **Recompilar** de la fila de una aplicación de servidor para recompilarla y volver a implementarla sin cambiar su configuración. El estado de la aplicación vuelve a **Compilando…** mientras PlaidCloud compila de nuevo la misma rama y el mismo punto de entrada, y cambia otra vez a **Lista** cuando la nueva compilación está activa.

Use **Recompilar** después de cambiar dependencias, de actualizar la imagen base o tras un error de compilación transitorio. Editar y guardar una aplicación de servidor también la recompila, pero para recompilarla no hace falta abrir el formulario de edición.

En una aplicación [App Runner](/es/guides/workflows/use-converted-alteryx-apps/#mantener-la-aplicación-al-día) (el formulario de entrada generado para una aplicación de Alteryx convertida), **Recompilar** y guardar una edición primero actualizan sus archivos generados a la versión actual de App Runner y después la compilan. PlaidCloud también lo hace con todas las aplicaciones App Runner que no están bloqueadas cuando se actualiza el propio PlaidCloud; una aplicación bloqueada necesita **Recompilar** después de desbloquearla.

## Bloquear una aplicación

Haga clic en el icono de **candado** de la fila de una aplicación para protegerla de cambios accidentales. Mientras una aplicación está bloqueada:

- **Editar**, **Quitar** y **Recompilar** no se ejecutan y le indican que la aplicación está bloqueada.
- Un **push a la rama de una aplicación de servidor no la recompila**: la recompilación automática se omite hasta que desbloquee la aplicación. No se ejecuta ninguna compilación para un push omitido, por lo que no aparece nada nuevo en los registros de compilación de la aplicación; después de desbloquearla, vuelva a hacer push (o use **Recompilar**) para incorporar el cambio.
- Abrir la aplicación, consultar sus registros y ver sus métricas de uso siguen funcionando: el bloqueo solo impide cambios, nunca el acceso de quienes la visualizan.

Haga clic de nuevo en el icono para desbloquearla. El icono muestra el estado actual de la aplicación: cerrado cuando está bloqueada y abierto cuando no lo está.

El bloqueo es una protección frente a accidentes (una edición errónea, una eliminación involuntaria o un git push que llega a una aplicación que está mostrando en una demostración), igual que el bloqueo de los flujos de trabajo y de los pasos de los flujos de trabajo. **No** es un control de seguridad: cualquier persona que pueda editar aplicaciones de Panel también puede desbloquearlas.

> Hay dos casos que el bloqueo no cubre: una **compilación ya en curso** en el momento de bloquear la aplicación termina igualmente y se pone en marcha, y los archivos de una aplicación **WASM** residen en su cuenta de documentos, por lo que sustituir esos archivos cambia la aplicación en ejecución sin tocar el registro bloqueado.

## Abrir una aplicación

Haga clic en el icono **Abrir** al principio de la fila de una aplicación lista para iniciarla en una pestaña nueva. **Abrir** también es la primera opción del menú **⋯** de la fila. Consulte [El menú de acciones de la fila](/es/guides/dashboards/using-dashboards/#el-menú-de-acciones-de-fila).

- Una aplicación de servidor se publica en `https://<your-tenant-host>/serve/<slug>/`.
- El icono **Abrir** solo aparece cuando una aplicación de servidor está **Lista**.

Una aplicación de servidor escala a cero cuando está inactiva para ahorrar recursos, por lo que la primera vez que se abre tras un período de inactividad tiene que arrancar. Mientras tanto, verá una **pantalla de carga de PlaidCloud** en lugar de una pestaña en blanco: el nombre de su aplicación, su progreso por las fases **Iniciando**, **Preparando** y **Cargando aplicación**, y el ID de su espacio de trabajo, con su tema claro u oscuro. La aplicación aparece sola en cuanto está lista (normalmente en unos segundos y hasta aproximadamente un minuto en un arranque en frío) y, a partir de ahí, responde con normalidad hasta que vuelve a quedar inactiva.

> Si una aplicación no puede iniciarse, la pantalla de carga se convierte en un mensaje que indica que la aplicación no se inició y en qué fase se detuvo, con un botón **Intentar de nuevo**, en lugar de quedarse cargando indefinidamente. Si esto se repite, edite la aplicación para comprobar su punto de entrada y su rama y vuelva a publicarla, o póngase en contacto con su administrador de PlaidCloud.

### Apariencia

Las aplicaciones Panel de servidor usan de forma predeterminada el diseño moderno **Fast** de PlaidCloud, pero la opción **Diseño** de la aplicación puede volver al estilo **Predeterminado** de Panel cuando el CSS existente depende de él. El tema (claro, oscuro o un conmutador claro/oscuro que los usuarios pueden cambiar) se define en la plantilla de la aplicación. Consulte [Establecer el tema](/es/guides/panel-apps/creating/#definir-el-tema-claro-oscuro-o-con-interruptor) en la guía de creación para ver los patrones. Si las tablas o el estilo personalizado de su aplicación están pensados para un fondo claro, manténgala fijada en el tema claro.

## Consultar los registros (aplicaciones de servidor)

Haga clic en el icono **Ver registros** de la fila de una aplicación de servidor para abrir su visor de registros. (Las aplicaciones WASM se ejecutan íntegramente en el navegador y no tienen registros de servidor, por lo que el icono solo aparece en las filas de aplicaciones de servidor).

El visor tiene dos pestañas:

- **Tiempo de ejecución** (se muestra primero): la salida propia de la aplicación en ejecución, es decir, todo lo que registra, todo lo que imprime y cualquier error no capturado. Se conserva incluso después de que la aplicación escale a cero, de modo que puede revisar lo que hizo una sesión anterior.
- **Compilación**: la salida de la compilación del contenedor de la aplicación. Úsela para ver *por qué* una compilación muestra **Error**; por ejemplo, una dependencia que no se pudo instalar.

Cada pestaña ofrece los filtros **Información / Advertencia / Error**, un intervalo de tiempo **Registros desde** (desde la última hora hasta 30 días, o todo), un botón **Actualizar** y **Actualización automática** para consultar periódicamente si hay entradas nuevas, algo útil mientras observa una aplicación activa o una compilación en curso. Las entradas más recientes aparecen primero.

> Si no se pudo capturar la salida de la compilación, la pestaña Compilación muestra una breve nota que explica el motivo en lugar de aparecer vacía.

### Leer un mensaje de registro completo

La tabla de registros recorta las líneas largas para que la lista sea legible. Seleccione una fila del registro para abrir un **panel de detalles** junto a la tabla que muestra el mensaje completo de la entrada. Es la forma más sencilla de leer algo demasiado largo para la tabla, como un mensaje de error extenso o un seguimiento de pila completo, sin que quede cortado.

### Copiar líneas del registro

Puede seleccionar varias filas del registro a la vez y hacer clic en **Copiar** para llevarlas al portapapeles. Resulta útil para pegar registros en una conversación con un asistente de IA mientras depura su aplicación, o en un mensaje para su equipo o para el soporte de PlaidCloud.

### Quién generó una línea del registro

Cuando su aplicación autentica a los usuarios, cada línea del registro se etiqueta con el **usuario** cuya sesión la generó, para que pueda saber qué usuario se encontró con un error o una advertencia concretos. El etiquetado se hace en la medida de lo posible: algunas líneas del framework y del arranque se ejecutan antes de que intervenga ningún usuario y es posible que no muestren uno.

## Usage Metrics (aplicaciones de servidor)

Haga clic en el icono **Usage Metrics** de la fila de una aplicación de servidor, junto a **Ver registros**, para ver cómo se está usando la aplicación. La vista resume:

- **Usuarios únicos**: cuántas personas distintas han abierto la aplicación.
- **Sesiones**: cuántas veces se ha abierto.
- **Duración media y mediana de la sesión**: cuánto dura aproximadamente una visita.
- **Último uso**: cuándo se abrió la aplicación por última vez.

Debajo del resumen se muestra un desglose **por usuario** y **por día**, para que pueda ver quién usa la aplicación y cómo evoluciona su uso a lo largo del tiempo.

> Las duraciones son aproximadas. Las aplicaciones de servidor quedan inactivas y se reducen cuando nadie las usa, por lo que no siempre se registra el final exacto de una sesión: interprete las cifras de duración como una orientación, no como una medición exacta.

## Editar una aplicación

Haga clic en el icono de **lápiz** de la fila de una aplicación para editarla. El formulario de edición se corresponde con el tiempo de ejecución de la aplicación.

En una aplicación de **servidor**, puede cambiar el nombre, el slug, la rama, el punto de entrada, la CPU, la memoria, el diseño, el período de inactividad, el indicador de acceso público, los dominios de publicación incrustada y el memo. La **Conexión de Git** queda fijada al crear la aplicación y se muestra en modo de solo lectura. Al guardar, la aplicación se recompila: su estado vuelve a **Compilando…** hasta que la nueva compilación está lista.

## Quitar una aplicación

Haga clic en el icono de **menos** de la fila de una aplicación y confirme; eliminar o anular la publicación de una aplicación siempre pide confirmación antes. Al quitar una aplicación de servidor se eliminan su compilación y su implementación; al quitar una aplicación WASM se anula la publicación del archivo estático. La URL de la aplicación deja de funcionar de inmediato.

La herramienta de MCP `panel_deployment_manage` ya no ofrece la opción de anular la publicación. En su lugar, quite la aplicación de esta lista.
