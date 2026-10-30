---
title: Administración de tablas y vistas
description: Administre tablas y vistas dentro de los proyectos de PlaidCloud, incluidas su creación, configuración, permisos y la organización de los objetos de datos.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud ofrece la posibilidad de organizar y administrar tablas, incluidas las etiquetas. Las tablas están disponibles para todos los flujos de trabajo de un proyecto y cuentan con muchas herramientas y opciones.


Además de las tablas, PlaidCloud también ofrece vistas basadas en los datos de las tablas. Usar vistas permite actualizaciones instantáneas cuando cambian las tablas subyacentes, además de ahorrar espacio de almacenamiento de datos.



Las opciones incluyen:


* La misma tabla puede existir en varias rutas de la jerarquía (jerarquías alternativas)
* Las tablas se pueden etiquetar para facilitar la búsqueda y su inclusión en los procesos de PlaidCloud
* Las tablas pueden tener versiones
* Las tablas se pueden publicar para que estén disponibles para las visualizaciones de los paneles de control

PlaidCloud usa un sistema basado en rutas para organizar las tablas, similar al que se usa para navegar por una serie de carpetas, lo que permite una organización de las tablas más flexible y lógica. Con este sistema, las tablas se pueden mover dentro de una jerarquía, o se pueden crear varias referencias a una misma tabla desde distintas ubicaciones de la jerarquía (jerarquías alternativas). La posibilidad de administrar las tablas con este método permite que la estructura refleje las necesidades operativas, de informes y de control.



## Búsqueda de tablas


Use el cuadro de filtro situado en la parte inferior izquierda de la jerarquía para buscar en los nombres y las etiquetas de las tablas. Las coincidencias se muestran en la jerarquía de arriba.


### Por flujo de trabajo

La carpeta **By Workflow** situada al final de la pestaña **Tablas** agrupa las tablas bajo cada flujo de trabajo que las lee o las escribe. Abra un flujo de trabajo para ver sus tablas. La carpeta es una vista de las mismas tablas, por lo que no puede mover ni copiar nada desde ella.


### Por columna

Escriba el nombre de una columna en el cuadro de búsqueda de columnas de la pestaña **Tablas** para mostrar solo las tablas que tienen una columna con ese nombre. Seleccione **Contiene** para buscar coincidencias con una parte del nombre de la columna en lugar del nombre completo. Borre el cuadro para volver a mostrar todas las tablas. Una búsqueda larga puede devolver los resultados por páginas, y la línea de estado indica cuándo sigue buscando o puede estar incompleta.

Seleccione **Column Tree** para buscar desde una ventana propia. Cada tabla que tiene la columna se abre con dos listas:

* **Fed by**: las tablas que suministran la columna
* **Feeds**: las tablas a las que la columna sigue alimentando

Un asistente de IA conectado mediante MCP encuentra las mismas tablas con `table_find(column=...)`, buscando coincidencias con el nombre completo o con una parte.


### Búsqueda de valores

Para saber qué tablas contienen un valor, seleccione **Search Values** en la pestaña **Tablas**, o haga clic con el botón derecho en una tabla y elija **Search Value** para buscar solo en esa tabla. Introduzca el valor, elija **Contiene** para buscar coincidencias con una parte de un valor y seleccione **Buscar**. Cada tabla que contiene el valor aparece en la lista con las columnas en las que figura y algunos de los valores coincidentes.

Antes de buscar, tenga en cuenta que:

* Solo ve las filas que ya podría abrir. La seguridad a nivel de fila se aplica a todas las búsquedas.
* El historial de consultas de su almacén registra los valores que busca.
* La búsqueda abarca las columnas de texto de las tablas. Las tablas que no se han creado se omiten y se nombran en una advertencia.
* Los resultados llegan por páginas. Cuando la línea de estado indica que la búsqueda se detuvo antes de tiempo, elija **Search more** para continuar con las tablas que aún no se han buscado.

Un asistente de IA conectado mediante MCP usa `table_value_search`. Devuelve las tablas y las columnas que contienen el valor, nunca los valores en sí. Cuando le pide al asistente de IA de un proyecto que busque un valor, Weave envía los nombres de las tablas y las columnas coincidentes al proveedor del modelo de lenguaje.



## Importación de un archivo CSV

**Para convertir un archivo CSV en una tabla nueva de este proyecto:**

1. Arrastre el archivo desde su computadora a la lista **Tablas** del proyecto, o elija **Nuevo** > **Tabla desde archivo CSV** en la barra de herramientas y suelte el archivo en el cuadro o haga clic en **Elegir un archivo CSV**.
2. PlaidCloud carga el archivo en su **Personal Temp Drive**, o en la **Temp Drive** del espacio de trabajo si usted no tiene una, y lo importa en una tabla nueva en el nivel superior de la lista, con el nombre del archivo: `Sales Data.csv` se convierte en `sales_data`. Si el proyecto ya tiene una tabla con ese nombre, la nueva recibe un número, como `sales_data_2`.
3. La lista se actualiza con la tabla nueva seleccionada, y **Sus datos de un vistazo** se abre sobre ella. Consulte [Comience con su propio CSV](/es/get-started/quickstart/#comience-con-su-propio-csv) para ver lo que muestra el panel.

Solo se aceptan archivos que terminen en `.csv`. Necesita permiso para crear tablas y para escribir en el almacenamiento de documentos, y un proyecto bloqueado no acepta un CSV hasta que se desbloquea. Si la importación falla, la ventana indica el motivo y su proyecto queda como estaba. PlaidCloud elimina el archivo cargado de la unidad temporal cuando termina la importación, haya tenido éxito o no; si no lo hace, la unidad temporal lo elimina al cabo de un día.

## Mover


**Para mover una tabla:**


1. Arrástrela a la carpeta en la que desea que se encuentre

## Cambiar el nombre


**Para cambiar el nombre de una tabla:**


1. Haga clic con el botón derecho en la tabla
2. Seleccione la opción de cambiar el nombre
3. Escriba el nombre nuevo y guárdelo
4. La tabla ya tiene el nombre nuevo, pero conserva su identificador único original.

## Borrar


**Para borrar una tabla:**


1. Seleccione las tablas en la jerarquía ‘
2. Haga clic en el botón de borrar de la barra de herramientas superior.

*Nota: Puede borrar una sola tabla o varias tablas*



## Eliminar


**Para eliminar una tabla:**


1. Seleccione las tablas en la jerarquía
2. Haga clic en el botón de eliminar de la barra de herramientas superior
3. La operación de eliminación comprobará si la tabla la usan pasos de flujo de trabajo o vistas. Si es así, se le pedirá que quite esas asociaciones antes de poder eliminarla.

*Nota: También puede forzar la eliminación de las tablas. La eliminación forzada de las tablas dejará referencias rotas, por lo que debe usarse con moderación.*


### Última lectura

La ventana de eliminación muestra cuándo se leyó la tabla por última vez, por ejemplo **Last read 3 days ago by** una persona o un paso, para que pueda distinguir una tabla que nadie usa de una que sigue en uso. PlaidCloud toma este dato del propio historial de consultas de su almacén y excluye las lecturas hechas por sus propias tareas de mantenimiento.

| Almacén | Qué se necesita |
| --- | --- |
| Snowflake | Las lecturas provienen de Access History, que Snowflake registra con un retraso de hasta unas 3 horas. El rol de la conexión necesita el rol de base de datos `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` en la base de datos `SNOWFLAKE` también funciona). La edición Standard de Snowflake no tiene Access History. |
| Databricks | Las lecturas provienen de la tabla de linaje, que Databricks también registra con retraso, por lo que es posible que una lectura reciente aún no aparezca. La identidad de la conexión necesita `USE CATALOG` en `system`, `USE SCHEMA` en `system.access` y `SELECT` en `system.access.table_lineage`. |
| PlaidCloud Lakehouse | El historial de lecturas aún no está disponible. La ventana muestra **Read history incomplete**. |

Cuando conecta su almacén, [la comprobación de la conexión](/es/guides/connections/external-lakehouse/#3-compruébelo-y-luego-úselo) recomienda cualquiera de estos permisos que falte, cada uno con la instrucción que debe ejecutar. Son recomendados, no obligatorios: sin ellos el almacén se conecta y la ventana muestra **Read history incomplete**.

Cuando PlaidCloud no puede leer todo el historial, la línea indica **Read history incomplete** y nunca informa de “ninguna lectura” en su lugar. Cualquier persona con acceso directo por SQL a su almacén puede establecer una etiqueta de sesión que cambie cómo se rotulan sus propias lecturas.

Un asistente de IA conectado mediante MCP obtiene la misma respuesta con `table_describe(include=['last_read'])`.



## Ver dónde se usa una tabla


Al seleccionar una tabla se abre su panel de detalles, que enumera los pasos de flujo de trabajo que la utilizan:


* **Tabla creada por**: pasos que escriben en la tabla
* **La tabla contribuye a**: pasos que leen de ella
* **Puede hacer referencia a esta tabla**: pasos que llegan a una tabla mediante una variable que no se puede resolver. Esta sección solo aparece cuando hay pasos de ese tipo.


Un paso puede nombrar una tabla de forma explícita, o llegar a ella mediante una ruta que contiene una variable, como `/Periods/{period}/Sales`. Cuando esa variable tiene un valor actual, el paso aparece en las dos primeras listas con un icono de información a su lado. Pase el cursor sobre la fila para ver la ruta tal como la almacena el paso.


Trate esas filas como la respuesta más débil que son. Describen lo que tocaría una ejecución que empezara ahora, no todo lo que ha tocado alguna vez la tabla. Si cambia la variable, se lee una tabla distinta.


Algunas variables no se pueden resolver. O bien nada ha establecido la variable, o bien el valor que usa una ejecución no proviene de lo almacenado: un Workflow Loop toma sus variables de los datos a medida que itera, un paso Set Variable asigna durante la ejecución, un macro recibe sus variables del paso que lo llama, y una ejecución iniciada por un sensor lleva los detalles propios de ese sensor. En todos los casos, lo que se almacena entre ejecuciones es un resto de la última y no un valor en el que confiar. En lugar de resolverlas a una tabla que puede ser la equivocada, PlaidCloud enumera los pasos por nombre en **Puede hacer referencia a esta tabla**, con la variable que no pudo resolver, para que pueda abrirlos y comprobarlos.


Un paso que su rol no puede ver aparece igualmente en la lista, para que sepa que la tabla está en uso, pero sin su nombre ni su flujo de trabajo, y no puede abrirlo. Sigue contando al eliminar la tabla. Un paso que sí puede ver aparece sin ningún flujo de trabajo que su rol tenga oculto. No se oculta nada a un Arquitecto.


*Nota: Al eliminar tablas desde la lista **Tablas**, un paso que llega a una tabla mediante una ruta, con variable o sin ella, cuenta como que la usa, incluso cuando su variable no se puede resolver. La ventana de eliminación enumera el paso, y la eliminación solo continúa si usted la fuerza.*



## Creación de una nueva estructura de directorios


**Para agregar una carpeta nueva:**


1. Haga clic en el botón Carpeta nueva de la barra de herramientas

**Para agregar una carpeta dentro de una carpeta existente:**


1. Haga clic con el botón derecho en la carpeta
2. Seleccione Carpeta nueva


## Visualización de datos (Explorador de tablas)


Los datos de las tablas se ven con el Explorador de datos. El Explorador de datos ofrece una vista de cuadrícula de los datos, así como un resumen columna por columna de los valores y las estadísticas. Están disponibles tanto el filtrado con apuntar y hacer clic como la exportación a formatos de archivo conocidos. Las selecciones del filtro también se pueden guardar como un paso Extract que se puede usar en un flujo de trabajo.



## Publicación de una tabla para informes


Las visualizaciones de los paneles de control se limitan a propósito a las tablas que se han publicado. Al publicar una tabla, puede asignarle un nombre único que distinga los datos. Esto puede ser útil cuando la tabla tiene un nombre más oscuro en la parte del flujo de trabajo que la generó, pero necesita un nombre más claro para quienes crean paneles de control.


Las tablas publicadas no tienen rutas asociadas. Aparecerán como una lista de tablas para usar en el área de paneles de control.



## Marcado de una tabla para los roles de visualización


La visualización de las tablas por parte de los distintos roles se puede controlar haciendo clic en las casillas Explorador o Gerente. Si es necesario actualizar varias tablas, seleccione las tablas en la jerarquía y elija el rol de visualización deseado en el menú Acciones de la barra de herramientas superior.



## Notas para describir el contenido de las tablas


Agregue una nota a una tabla para ayudar a comprender los datos.



## Visualización de la forma, el tamaño y la hora de la última actualización de una tabla


El número de filas, de columnas y el tamaño de los datos de cada tabla se muestran en la jerarquía de tablas. En las tablas muy grandes (de varios millones de filas), el recuento de filas puede ser estimado y se mostrará un indicador de recuento de filas aproximado.



## Visualización de otros atributos de una tabla


**Para ver y editar otros atributos de una tabla:**


1. Seleccione una tabla
2. Haga clic para ver el formulario de contexto de la tabla a la derecha.


## Duplicación de una tabla


**Para duplicar una tabla:**


1. Seleccione la tabla
2. Haga clic en el botón de duplicar de la barra de herramientas superior.


## Creación de un editor de datos a partir de una tabla


Puede convertir una tabla en un editor de datos configurado en un solo paso: seleccione la tabla y elija **Crear editor de datos a partir de tabla** en el menú **Nuevo** o en el menú contextual. PlaidCloud examina las columnas de la tabla y precrea los controles de entrada del editor. Consulte [Creación de un editor de datos a partir de una tabla](/es/guides/projects/managing-data-editors/#creación-de-un-editor-de-datos-a-partir-de-una-tabla) para obtener más información.
