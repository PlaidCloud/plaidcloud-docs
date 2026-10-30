---
title: Administrar tablas y vistas
description: Administre tablas y vistas dentro de los proyectos de PlaidCloud, incluidas su creación, configuración, permisos y la organización de los objetos de datos.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud ofrece la posibilidad de organizar y administrar tablas, incluidas las etiquetas. Las tablas están disponibles para todos los flujos de trabajo de un proyecto y tienen muchas herramientas y opciones.


Además de las tablas, PlaidCloud ofrece también vistas basadas en los datos de las tablas. Las vistas permiten actualizaciones instantáneas cuando cambian las tablas subyacentes, además de ahorrar espacio de almacenamiento de datos.



Las opciones incluyen:


* La misma tabla puede existir en varias rutas de la jerarquía (jerarquías alternativas)
* Las tablas se pueden etiquetar para facilitar la búsqueda y su inclusión en los procesos de PlaidCloud
* Las tablas pueden tener versiones
* Las tablas se pueden publicar para que estén disponibles para las visualizaciones de los paneles de control

PlaidCloud usa un sistema basado en rutas para organizar las tablas, como el que se usaría para navegar por una serie de carpetas, lo que permite una organización de las tablas más flexible y lógica. Con este sistema, las tablas se pueden mover dentro de una jerarquía, o se pueden crear varias referencias a una misma tabla desde distintas ubicaciones de la jerarquía (jerarquías alternativas). La capacidad de administrar las tablas con este método permite que la estructura refleje las necesidades operativas, de informes y de control.



## Buscar tablas


Use el cuadro de filtro de la parte inferior izquierda de la jerarquía para buscar en los nombres y las etiquetas de las tablas. Las coincidencias se muestran en la jerarquía situada encima.


### Por flujo de trabajo

La carpeta **Por flujo de trabajo** al final de la pestaña **Tablas** agrupa las tablas bajo cada flujo de trabajo que las lee o las escribe. Abra un flujo de trabajo para ver sus tablas. La carpeta es una vista de las mismas tablas, por lo que no puede mover ni copiar nada desde ella.


### Por columna

Escriba el nombre de una columna en el cuadro de búsqueda de columnas de la pestaña **Tablas** y pulse Intro, o seleccione la lupa que hay junto a él, para mostrar solo las tablas que tienen una columna con ese nombre. La búsqueda lee los nombres de las columnas, no los datos, por lo que es rápida. Seleccione **Contiene** para coincidir con una parte del nombre de la columna en lugar del nombre completo. Borre el cuadro para volver a mostrar todas las tablas. Una búsqueda larga puede devolver los resultados por páginas, y la línea de estado indica cuándo todavía está buscando o puede estar incompleta.

Seleccione **Árbol de columnas** para buscar desde una ventana propia. Cada tabla que tiene la columna se abre con dos listas:

* **Alimentada por**: las tablas que suministran la columna
* **Alimenta a**: las tablas a las que la columna sigue alimentando

Un asistente de IA conectado mediante MCP encuentra las mismas tablas con `table_find(column=...)`, buscando el nombre completo o una parte de él.


### Buscar valores

Para encontrar qué tablas contienen un valor, elija **Buscar valores en los datos… (lento)** en el menú **Acciones** de la pestaña **Tablas**, o haga clic con el botón derecho en una tabla y elíjalo para buscar solo en esa tabla. Introduzca el valor, elija **Contiene** para coincidir con una parte de un valor y seleccione **Buscar**. Cada tabla que contiene el valor se enumera con las columnas en las que aparece y algunos de los valores coincidentes. Haga doble clic en una tabla, o pulse Intro sobre ella, para abrirla en el Explorador de tablas. Una columna abre la tabla filtrada por las filas que coinciden. Si el cuadro de búsqueda de columnas contiene texto, lo usa como valor que se debe buscar.

Antes de buscar, tenga en cuenta que:

* La búsqueda lee todas las filas de todas las tablas buscadas, por lo que puede ser muy lenta y usar muchos recursos del almacén de datos. La ventana se lo advierte, y los botones de búsqueda permanecen desactivados hasta que termina una búsqueda.
* Solo ve las filas que ya podría abrir. La seguridad a nivel de fila se aplica a todas las búsquedas.
* El historial de consultas de su almacén de datos registra los valores que busca.
* La búsqueda abarca las columnas de texto de las tablas. Las tablas que no se han compilado se omiten y se nombran en una advertencia.
* Los resultados llegan por páginas. Cuando la línea de estado indica que la búsqueda se detuvo antes de tiempo, elija **Buscar más** para continuar con las tablas que aún no se han buscado.

Un asistente de IA conectado mediante MCP usa `table_value_search`. Devuelve las tablas y las columnas que contienen el valor, nunca los valores en sí. Cuando pide al asistente de IA de un proyecto que encuentre un valor, Weave envía los nombres de las tablas y las columnas coincidentes al proveedor del modelo de lenguaje.



## Importar un archivo CSV

**Para convertir un archivo CSV en una tabla nueva de este proyecto:**

1. Arrastre el archivo desde su equipo a la lista **Tablas** del proyecto, o elija **Nuevo** > **Tabla desde archivo CSV** en la barra de herramientas y suelte el archivo en el cuadro o haga clic en **Elegir un archivo CSV**.
2. PlaidCloud carga el archivo en su **Personal Temp Drive**, o en el **Temp Drive** del espacio de trabajo si no tiene uno, y lo importa a una tabla nueva en el nivel superior de la lista, con el nombre del archivo: `Sales Data.csv` se convierte en `sales_data`. Si el proyecto ya tiene una tabla con ese nombre, la nueva recibe un número, como `sales_data_2`.
3. La lista se actualiza con la tabla nueva seleccionada, y **Sus datos de un vistazo** se abre sobre ella. Consulte [Comenzar con su propio CSV](/es/get-started/quickstart/#comience-con-su-propio-csv) para ver lo que muestra el panel.

Solo se aceptan archivos que terminen en `.csv`. Necesita permiso para crear tablas y para escribir en el almacenamiento de documentos, y un proyecto bloqueado no acepta un CSV hasta que se desbloquea. Si la importación falla, la ventana indica el motivo y su proyecto queda como estaba. PlaidCloud elimina el archivo cargado de la unidad temporal una vez terminada la importación, haya tenido éxito o no; si no lo hace, la unidad temporal lo elimina al cabo de un día.

## Mover


**Para mover una tabla:**


1. Arrástrela a la carpeta donde desea que se ubique

## Cambiar el nombre


**Para cambiar el nombre de una tabla:**


1. Haga clic con el botón derecho en la tabla
2. Seleccione la opción de cambiar nombre
3. Escriba el nombre nuevo y guárdelo
4. La tabla ya tiene el nombre nuevo, pero conserva su identificador único original.

## Borrar


**Para borrar una tabla:**


1. Seleccione las tablas en la jerarquía
2. Haga clic en el botón de borrar de la barra de herramientas superior.

*Nota: Puede borrar una sola tabla o varias tablas*



## Eliminar


**Para eliminar una tabla:**


1. Seleccione las tablas en la jerarquía
2. Haga clic en el botón de eliminar de la barra de herramientas superior
3. La operación de eliminación comprobará si la tabla está en uso en pasos de flujos de trabajo o en vistas. Si es así, se le pedirá que quite esas asociaciones antes de poder eliminarla.

*Nota: También puede forzar la eliminación de las tablas. La eliminación forzada de las tablas dejará referencias rotas, por lo que debe usarse con moderación.*


### Última lectura

La ventana de eliminación muestra cuándo se leyó la tabla por última vez, por ejemplo **Last read 3 days ago by** una persona o un paso, para que pueda distinguir una tabla que nadie usa de una que sigue en uso. PlaidCloud obtiene esto del propio historial de consultas de su almacén de datos y excluye las lecturas realizadas por sus propias tareas de mantenimiento.

| Almacén de datos | Qué se necesita |
| --- | --- |
| Snowflake | Las lecturas proceden de Access History, que Snowflake registra con hasta unas 3 horas de retraso. El rol de la conexión necesita el rol de base de datos `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` en la base de datos `SNOWFLAKE` también funciona). La edición Standard de Snowflake no tiene Access History. |
| Databricks | Las lecturas proceden de la tabla de linaje, que Databricks también registra con retraso, por lo que es posible que una lectura reciente aún no aparezca. La identidad de la conexión necesita `USE CATALOG` en `system`, `USE SCHEMA` en `system.access` y `SELECT` en `system.access.table_lineage`. |
| PlaidCloud Lakehouse | El historial de lecturas aún no está disponible. La ventana muestra **Read history incomplete**. |

Cuando conecta su almacén de datos, [la comprobación de la conexión](/es/guides/connections/external-lakehouse/#3-compruébelo-y-luego-úselo) recomienda los permisos que falten de estos, cada uno con la instrucción que se debe ejecutar. Son recomendados, no obligatorios: sin ellos el almacén de datos se conecta y la ventana muestra **Read history incomplete**.

Cuando PlaidCloud no puede leer todo el historial, la línea dice **Read history incomplete** y nunca informa de "sin lecturas" en su lugar. Cualquier persona con acceso SQL directo a su almacén de datos puede establecer una etiqueta de sesión que cambia cómo se etiquetan sus propias lecturas.

Un asistente de IA conectado mediante MCP obtiene la misma respuesta con `table_describe(include=['last_read'])`.



## Ver las columnas de una tabla


Al seleccionar una tabla se abre su panel de detalles. Su sección **Columnas** enumera cada columna con su **Tipo** y su **Descripción**, que proviene de **Propiedades de la columna**. Señale una fila para leer completa una descripción larga.

Una tabla que ahora mismo no está en el almacén de datos, porque sus datos caducaron o ningún paso la ha compilado, no tiene columnas que enumerar. La sección lo indica y muestra cuántas columnas tiene la tabla. Ejecute un paso que escriba la tabla para enumerarlas.


## Ver dónde se usa una tabla


Al seleccionar una tabla se abre su panel de detalles, que enumera los pasos de flujos de trabajo que la tocan:


* **Tabla creada por**: pasos que escriben en la tabla
* **La tabla contribuye a**: pasos que leen de ella
* **Puede hacer referencia a esta tabla**: pasos que llegan a una tabla mediante una variable que no se puede resolver. Esta sección solo aparece cuando hay tales pasos.


Un paso puede nombrar una tabla directamente o llegar a ella mediante una ruta que contiene una variable, como `/Periods/{period}/Sales`. Cuando esa variable tiene un valor actual, el paso aparece en las dos primeras listas con un icono de información junto a él. Pase el puntero sobre la fila para ver la ruta tal como la almacena el paso.


Trate esas filas como la respuesta más débil que son. Describen lo que tocaría una ejecución iniciada ahora, no todo lo que ha tocado alguna vez la tabla. Cambie la variable y se leerá una tabla distinta.


Algunas variables no se pueden resolver. O bien nada ha establecido la variable, o bien el valor que usa una ejecución no procede de lo almacenado: un Workflow Loop toma sus variables de los datos a medida que itera, un paso de asignación de variables las asigna durante la ejecución, a una macro le entrega las variables el paso que la llama, y una ejecución iniciada por un sensor lleva los detalles propios de ese sensor. En cada caso, lo que se almacena entre ejecuciones es un resto de la última y no un valor fiable. En lugar de resolverlas a una tabla que puede ser la equivocada, PlaidCloud enumera los pasos por nombre en **Puede hacer referencia a esta tabla**, con la variable que no pudo resolver, para que pueda abrirlos y comprobarlos.


Un paso que su rol no puede ver sigue apareciendo en la lista, para que sepa que la tabla está en uso, pero sin su nombre ni su flujo de trabajo, y no puede abrirlo. Sigue contando cuando elimina la tabla. Un paso que sí puede ver aparece sin ningún flujo de trabajo que su rol oculte. Nada se oculta a un Arquitecto.


*Nota: Cuando elimina tablas de la lista **Tablas**, un paso que llega a una tabla mediante una ruta, con o sin variable, cuenta como que la usa, incluso cuando su variable no se puede resolver. La ventana de eliminación enumera el paso, y la eliminación continúa solo si la fuerza.*



## Crear una nueva estructura de directorios


**Para agregar una carpeta nueva:**


1. Haga clic en el botón Carpeta nueva de la barra de herramientas

**Para agregar una carpeta dentro de una carpeta existente:**


1. Haga clic con el botón derecho en la carpeta
2. Seleccione Carpeta nueva


## Ver datos (Explorador de tablas)


Los datos de las tablas se ven con el Explorador de datos. El Explorador de datos ofrece una vista de cuadrícula de los datos, así como un resumen columna por columna de los valores y las estadísticas. Están disponibles el filtrado con apuntar y hacer clic y la exportación a formatos de archivo conocidos. Las selecciones de filtro también se pueden guardar como un paso de extracción que se puede usar en un flujo de trabajo.



## Publicar una tabla para informes


Las visualizaciones de los paneles de control se limitan deliberadamente a las tablas que se han publicado. Al publicar una tabla, puede darle un nombre único que distinga los datos. Esto puede ser útil cuando la tabla tiene un nombre más oscuro en la parte del flujo de trabajo que la generó, pero necesita un nombre más claro para quienes crean paneles de control.


Las tablas publicadas no tienen rutas asociadas. Aparecerán como una lista de tablas para usar en el área de paneles de control.



## Marcar una tabla para roles de visualización


La visualización de las tablas por parte de distintos roles se puede controlar haciendo clic en las casillas Explorador o Gerente. Si es necesario actualizar varias tablas, seleccione las tablas en la jerarquía y elija el rol de visualización deseado en el menú Acciones de la barra de herramientas superior.



## Notas para describir el contenido de las tablas


Agregue una nota a una tabla para ayudar a entender los datos.



## Ver la forma, el tamaño y la hora de la última actualización de una tabla


El número de filas, de columnas y el tamaño de los datos de cada tabla se muestran en la jerarquía de tablas. En las tablas muy grandes (de varios millones de filas), el recuento de filas puede ser estimado y se mostrará un indicador de recuento de filas aproximado.



## Ver atributos adicionales de una tabla


**Para ver y editar otros atributos de la tabla:**


1. Seleccione una tabla
2. Haga clic para ver el formulario de contexto de la tabla a la derecha.


## Duplicar una tabla


**Para duplicar una tabla:**


1. Seleccione la tabla
2. Haga clic en el botón de duplicar de la barra de herramientas superior.


## Crear una aplicación Panel a partir de una tabla


Seleccione una tabla o una vista y elija **Crear aplicación Panel** en el menú **Nuevo** o en el menú contextual del botón derecho. Se abre el cuadro de diálogo **Nueva aplicación Studio** con el proyecto y la tabla ya elegidos. La aplicación toma el nombre de la tabla; cámbielo si lo desea y luego elija **Crear**, y Panel Studio la abre con Weave listo para crear su primera página. El comando está disponible cuando selecciona una sola tabla o vista, tiene acceso de edición al proyecto y el proyecto no es de solo lectura. Consulte [Crear una aplicación de Panel](/es/guides/panel-apps/creating/#comenzar-desde-una-tabla).


## Ver qué almacenan las tablas


La lista **Tablas** muestra las columnas **Datos actuales**, **Historial**, **Días de viaje en el tiempo** y **Nota** junto al tamaño de cada tabla. **Días de viaje en el tiempo** es la configuración propia de la tabla; **1** significa que usa el valor predeterminado del proyecto. La barra de estado situada debajo de la lista da el total del proyecto: cuánto almacena, y cuánto de ello son datos actuales y cuánto es historial. Los tamaños marcados como **Estimado** proceden de la forma de la tabla hasta que PlaidCloud la mide.

Elija **Almacenamiento** en la barra de herramientas para abrir la ventana **Almacenamiento** del proyecto, con sugerencias para liberar espacio y la configuración de time travel. Consulte [Administrar el almacenamiento](/es/guides/projects/managing-storage/#la-ventana-almacenamiento-de-un-proyecto).


## Crear un editor de datos a partir de una tabla


Puede convertir una tabla en un editor de datos configurado en un solo paso: seleccione la tabla y elija **Crear editor de datos a partir de tabla** en el menú **Nuevo** o en el menú contextual del botón derecho. PlaidCloud examina las columnas de la tabla y crea previamente los controles de entrada del editor. Consulte [Crear un editor de datos a partir de una tabla](/es/guides/projects/managing-data-editors/#creación-de-un-editor-de-datos-a-partir-de-una-tabla) para más detalles.
