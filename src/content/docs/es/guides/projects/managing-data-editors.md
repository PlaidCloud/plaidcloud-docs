---
title: Administración de editores de datos
description: Administre las asignaciones de editores de datos en proyectos de PlaidCloud para controlar quién puede modificar los datos de las tablas directamente a través de la interfaz de datos.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-data-editors.md
---

PlaidCloud ofrece la posibilidad de organizar y administrar editores de datos, incluidas las etiquetas. Los editores de datos permiten editar los datos de una tabla o crear datos mediante la interacción del usuario.



PlaidCloud usa un sistema basado en rutas para organizar los editores de datos, como el que se usa para navegar por una serie de carpetas, lo que permite una organización más flexible y lógica (jerarquía de control) de los editores de datos. Con este sistema, los editores de datos pueden moverse dentro de una jerarquía de control. Se pueden crear varias referencias a un mismo editor de datos desde distintas ubicaciones de la jerarquía de control (jerarquías alternativas). La posibilidad de administrar los editores de datos con este método permite que la estructura refleje las necesidades operativas, de informes y de control.




## Creación de un editor de datos a partir de una tabla


Puede crear un editor de datos listo para usar directamente a partir de una tabla existente. PlaidCloud examina las columnas de la tabla y preconfigura el editor: elige un control de entrada para cada columna y convierte en listas de selección desplegables las columnas que contienen un conjunto reducido de valores repetidos.


Para crear un editor de datos a partir de una tabla:


1. Abra la vista **Tablas** del proyecto y seleccione una sola tabla
2. Abra **Crear editor de datos a partir de tabla**, desde el menú **Nuevo** de la barra de herramientas o haciendo clic con el botón derecho en la tabla
3. PlaidCloud perfila la tabla y abre la ventana **Configuración del editor de datos** con todo rellenado previamente: establece como origen y destino la tabla seleccionada, de modo que sus ediciones se guarden directamente en ella, y asigna a cada columna de la pestaña **Columnas del formulario** un control que coincide con su tipo de datos y sus valores
4. Revise las columnas y ajuste los controles que sea necesario
5. Haga clic en **Guardar** o en **Guardar y cerrar**

Al guardar se crea el editor; al hacer clic en **Cancelar** no se agrega nada.

Cuando una columna se asigna a una dimensión, elija una jerarquía para ella en la pestaña Columnas del formulario antes de guardar. PlaidCloud bloquea el guardado mientras una columna de dimensión no tenga jerarquía.


## Cómo configura PlaidCloud las columnas


Cuando crea un editor a partir de una tabla, o usa **Rellenar desde el origen**, PlaidCloud configura cada columna automáticamente:


- Las columnas **Booleano** se convierten en una casilla de verificación, o en una lista de verdadero/falso cuando la columna admite valores vacíos
- Las columnas **Fecha** se convierten en un selector de fecha
- Las columnas **Numérico** se convierten en un campo numérico
- Las columnas que se asignan a una **dimensión** se convierten en un selector de dimensión, donde usted elige la jerarquía: al editar una celda se abre el mismo árbol selector de miembros descrito en [Propiedades de tipo dimensión y selector de miembros](/es/guides/dimensions/dimensions/#propiedades-de-tipo-dimensión-y-el-selector-de-miembros), con **Expandir todo**, **Contraer todo**, **Aplicar**, **Borrar** y **Cancelar**
- Las columnas cuyos valores se repiten en un conjunto reducido, por ejemplo un código de estado o de región, se convierten en una **lista desplegable** con los valores encontrados en la columna
- Las demás columnas de **texto** se convierten en un campo de texto, o en un área de texto para valores largos
- PlaidCloud incluye las columnas de tipo clave, como los ID generados automáticamente, pero las marca como de solo lectura

En las tablas muy grandes, PlaidCloud estima la lista de valores a partir de una muestra de filas. Después puede cambiar el control de cualquier columna.

En la pestaña **Columnas del formulario**, seleccione una columna para ver una breve explicación de por qué PlaidCloud eligió su control.


## Ajuste del límite de la lista de selección


PlaidCloud convierte una columna en una lista desplegable solo cuando sus valores se repiten en un conjunto reducido. Puede cambiar ese límite y volver a derivar las columnas:


1. En la pestaña **Columnas del formulario**, defina **Máximo de valores de la lista de selección** con el mayor número de valores distintos que puede tener una columna y aun así convertirse en una lista desplegable
2. Haga clic en **Volver a perfilar**

PlaidCloud vuelve a examinar la tabla de origen con el nuevo valor y reconstruye las columnas. Si el editor ya tiene columnas, al volver a perfilar se reemplazan, por lo que PlaidCloud le pide que lo confirme.


## Relleno de un editor existente a partir de una tabla


Puede aplicar la misma configuración automática a un editor que ya está editando:


1. Abra la configuración del editor de datos y vaya a la pestaña **Origen y destino**
2. Establezca el origen como una tabla
3. En la pestaña **Columnas del formulario**, haga clic en **Rellenar desde el origen**

PlaidCloud agrega una columna configurada por cada columna de la tabla de origen. Conserva las columnas que ya personalizó y le solicita que quite las columnas que ya no están en el origen.


## Búsqueda


Para buscar editores de datos:


1. Use el cuadro de filtro situado en la parte inferior izquierda de la jerarquía de control

El filtro de búsqueda busca coincidencias en los nombres y las etiquetas de los editores de datos y muestra los resultados en la jerarquía de control que aparece arriba.




## Mover


Para mover un editor de datos dentro de la jerarquía de control:


1. Arrástrelo a la carpeta en la que desea colocarlo

## Cambiar nombre


Para cambiar el nombre de un editor de datos:


1. Haga clic con el botón derecho en el editor de datos
2. Seleccione la opción de cambiar nombre
3. Escriba el nombre nuevo y guárdelo

El editor de datos tendrá ahora otro nombre, pero conservará su identificador único original.




## Eliminar


Puede eliminar un solo editor de datos o varios.


Para eliminar un editor de datos:


1. Seleccione los editores de datos en la jerarquía de control
2. Haga clic en el botón de eliminar de la barra de herramientas superior


## Creación de una estructura de directorios nueva


Para agregar una carpeta nueva a la jerarquía de control:


1. Haga clic en el botón Carpeta nueva de la barra de herramientas

Para agregar una carpeta a una carpeta existente:


1. Haga clic con el botón derecho en la carpeta
2. Seleccione Carpeta nueva


## Marcado de la jerarquía para los roles de visualización


La visualización de los editores de datos por parte de los distintos roles:


1. Haga clic en las casillas Explorador o Gerente

Para actualizar varios editores de datos:


1. Seleccione los editores de datos en la jerarquía de control
2. Seleccione el rol de visualización deseado en el menú Acciones de la barra de herramientas superior


## Notas para describir el contenido de las tablas


Para agregar una nota a un editor de datos:


1. Seleccione el editor de datos
2. Actualice la nota en el formulario de contexto de la derecha


## Visualización de atributos adicionales de la jerarquía


Para ver y editar atributos adicionales del editor de datos:


1. Seleccione el editor de datos y consulte el formulario de contexto del editor de datos a la derecha


## Duplicación de un editor de datos


Para duplicar un editor de datos:


1. Seleccione el editor de datos
2. Haga clic en el botón Duplicar de la barra de herramientas superior


## Escritura mediante el asistente de IA o MCP

Además de las pantallas de configuración, `editor_upsert` puede definir el origen, el destino y los controles de un editor de datos, y escribir filas en él directamente: `data` es una lista de objetos de fila con la clave del id de cada control. Una fecha no válida se rechaza antes de que nada llegue a la tabla de destino, de modo que una escritura incorrecta nunca se aplica de forma parcial.
