---
title: Archivar un proyecto
description: Archive proyectos de PlaidCloud para conservar el trabajo terminado, liberar recursos del espacio de trabajo y mantener limpio el entorno de proyectos.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/archive-a-project.md
---

## Creación de un archivo


Los proyectos suelen contener procesos y lógica críticos, que es importante archivar. Si alguna vez necesita restaurar el proyecto a un estado concreto, disponer de archivos es esencial. 



PlaidCloud le permite archivar proyectos en cualquier momento. La creación de archivos complementa el seguimiento integrado de puntos en el tiempo de PlaidCloud, al permitir capturar momentos específicos. Esto puede ser especialmente útil antes de un cambio importante o para conservar el estado exacto de un entorno de producción como registro histórico.



**Copia de seguridad completa**: incluye todas las tablas de datos de un proyecto. El archivo puede ser muy grande, según el volumen de datos del proyecto.


**Copia de seguridad parcial:** puede usarse si todos los datos del proyecto se pueden derivar de otras fuentes. En ese caso, no es necesario archivar los datos del proyecto, ya que permanecen en otro lugar. Los archivos parciales ahorran tiempo y espacio de almacenamiento al crear el archivo.



Para archivar un proyecto:


1. Abra Analyze
2. Seleccione la pestaña “Proyectos”
3. Seleccione el proyecto y luego elija **Exportar archivo del proyecto** en el menú **Acciones** (o haga clic con el botón derecho en el proyecto y elija **Exportar archivo del proyecto**)

La ventana muestra en su barra de título el proyecto que va a archivar, de modo que puede confirmar que es el correcto antes de comenzar.

### Mientras se ejecuta el archivado

La ventana de exportación se cierra en cuanto PlaidCloud acepta la solicitud, y a partir de ahí una ventana de progreso sigue el archivado. Puede dejar abierta esa ventana de progreso para observarlo, o enviarla a segundo plano y seguir trabajando: el archivado se ejecuta en la plataforma de cualquier manera, y cerrar la ventana de progreso no lo detiene.

Una notificación le indica cómo terminó: que el archivo se escribió, qué tablas se incluyeron sin sus datos o, si falló, el motivo. No es necesario mantener la ventana abierta para recibirla.

:::note
Un proyecto grande puede tardar desde unos segundos hasta una hora en archivarse, según la cantidad de datos de tablas que incluya. Un archivado de larga duración es normal y no significa que algo haya salido mal: espere la notificación en lugar de iniciar una segunda exportación, que volvería a archivar el proyecto desde cero.
:::

### Tablas cuyos datos no se pueden incluir

En ocasiones, una tabla incluida en un proyecto ya no tiene datos detrás, por ejemplo, una tabla que nunca se creó o cuyos datos se eliminaron fuera del proyecto. El archivo se escribe de todos modos: esas tablas se omiten de los datos de tablas y la exportación termina con un mensaje que las nombra. Todo lo demás (la configuración del proyecto, los flujos de trabajo, las definiciones de tablas y los datos de todas las demás tablas) se archiva con normalidad.

El archivo registra qué tablas se incluyeron sin sus datos, y al restaurarlo se vuelven a nombrar al final de la restauración en lugar de presentarlas como completas. Una tabla cuya definición aún se podía leer vuelve con sus columnas y sin filas; una cuya definición también se había perdido vuelve como una entrada sin tabla detrás. Vuelva a ejecutar el flujo de trabajo que crea una tabla para rellenarla.

:::note
Un archivado programado registra las tablas omitidas en el registro del sistema en lugar de mostrarle un mensaje, ya que no hay nada en pantalla donde mostrarlo. Revise el mensaje de exportación cuando le importe saber qué tablas se incluyeron.
:::

### Si no puede leer las tablas del proyecto

Leer las tablas de un proyecto es un permiso distinto de leer el propio proyecto, y un archivo depende de ambos. Si puede abrir un proyecto pero no tiene acceso de lectura a las tablas, el archivo se escribe de todos modos, pero no contiene datos de tablas ni tampoco definiciones de tablas, ya que ambos dependen de ese mismo permiso. La exportación termina con un mensaje que nombra las tablas omitidas, identificadas por sus ids internos en lugar de por sus nombres, porque los nombres proceden de las definiciones que el archivo no incluyó.

Un archivo creado de esta manera es una copia de la configuración del proyecto (sus flujos de trabajo, variables, dimensiones, vistas y diseños, en la medida en que usted tenga derecho a leer cada uno de ellos) y no de sus datos. **Al restaurarlo no se recrea ninguna tabla**, por lo que no es una copia de seguridad a partir de la cual pueda reconstruir los datos del proyecto. Revise el mensaje de exportación antes de confiar en uno de estos archivos.

A diferencia de las tablas descritas anteriormente, esto no se corrige volviendo a ejecutar un flujo de trabajo: los datos nunca se leyeron en primer lugar. Pida a un administrador del espacio de trabajo que le conceda acceso de lectura a las tablas del proyecto y luego vuelva a crear el archivo.

:::caution
Esto también se aplica a los archivados programados, que se ejecutan como un miembro determinado. Cuando ese miembro no tiene acceso de lectura a las tablas, todos los archivos que produce la programación contienen solo la configuración, y la deficiencia se registra en el registro del sistema en lugar de mostrarse a alguien. Si conserva archivados programados como copias de seguridad, confirme que el miembro con el que se ejecutan puede leer las tablas del proyecto.
:::

### Si el proyecto usa acceso a filas

Crear un archivo lee las tablas del proyecto, por lo que el [acceso a filas](/es/administration/access/managing-security-groups-and-assignments/#administración-del-acceso-a-filas) se aplica igual que a cualquier otra lectura. En cada columna de control, el archivo incluye las filas que se conceden a sus grupos. Cuando no tiene ninguna concesión en una columna, lo que obtiene depende de cómo se declaró esa columna: una configurada para denegar de forma predeterminada no le da ninguna fila, y una declarada para permitir todo de forma predeterminada deja esa columna sin filtrar. Una tabla que no contiene ninguna de las columnas de control se archiva completa, y un Arquitecto del proyecto archiva todas las filas, sea cual sea el contenido de las concesiones. Un archivado programado se ejecuta con la identidad propia del proyecto y no con la suya, por lo que archiva todas las filas.

Un archivo creado por un miembro que solo tiene algunas de las concesiones es una copia parcial de los datos del proyecto, y una columna configurada para denegar de forma predeterminada implica que una tabla puede volver vacía en lugar de simplemente reducida. Al restaurar un archivo así, el proyecto se reconstruye sin esas filas, y nada en la restauración lo indica, porque, en lo que respecta al archivo, las filas nunca estuvieron allí.

:::caution
Cuando necesite un archivo a partir del cual pueda reconstruir todo el proyecto, créelo como un miembro que lea el proyecto completo.
:::

### Si la exportación falla

Una exportación que falla ahora informa del error. Anteriormente, un archivo podía figurar como terminado sin haberse escrito, y usted descubría después la falta del archivo, casi siempre cuando iba a restaurarlo. Ahora una exportación fallida lo indica, de modo que considere genuino un éxito informado y revise el mensaje de cualquier exportación que informe de un error. Lo mismo se aplica a los demás tipos de exportación, no solo a los archivos de proyecto.

## Restauración de un archivo


Una vez que tiene un archivo, es posible que desee restaurarlo. Puede restaurar un archivo en un proyecto nuevo o en un proyecto existente.



Para restaurar un archivo:


1. Abra Analyze
2. Seleccione la pestaña “Proyectos”
3. Elija **Importar archivo de proyecto** en el menú **Acciones** (o en la barra de herramientas) y seleccione el archivo que desea restaurar
4. Elija entre **Crear proyecto nuevo** o **Importar en un proyecto existente**, y seleccione qué traer del árbol de selección
5. Haga clic en **Importar proyecto**

La importación se ejecuta en segundo plano. Una ventana de progreso muestra cuánto ha avanzado, y un mensaje le avisa cuando termina, con un correo electrónico además si se omitió algo. Si la importación no puede iniciarse (por ejemplo, porque el proyecto que eligió está bloqueado), la ventana permanece abierta y le indica el motivo.


Un archivo se comprueba al abrirse. Si contiene algo que un archivo de proyecto nunca incluye (un archivo que quedaría fuera de la propia carpeta del archivo, un vínculo que apunta fuera de ella o una configuración que intenta crear algo distinto de datos simples), se rechaza antes de restaurar nada.


No tiene que traer el archivo completo. El árbol de selección enumera lo que contiene el archivo por tipo (flujos de trabajo, pasos, tablas, dimensiones, editores de datos, funciones definidas por el usuario) y todo lo que marque trae consigo sus dependencias.


### Cuando una parte de un archivo no se importa


Una importación continúa cuando una parte del archivo no se puede restaurar. Siempre que el archivo se pueda leer y el proyecto en sí se pueda configurar, el proyecto se importa, y todo lo que no se pudo restaurar aparece en su resultado de la importación. Si el archivo no se puede leer, o el proyecto en sí no se puede configurar, la importación falla y le indica el motivo, y se elimina el proyecto nuevo. Una importación en un proyecto existente también puede detenerse antes de terminar. Todo lo que ya se había restaurado permanece en el proyecto. El mensaje y el correo electrónico indican que la importación se detuvo, y el resultado de la importación indica cuándo y por qué, y enumera lo que no pudo restaurar hasta ese momento.

Cuando se omitió algo, el mensaje y el correo electrónico al final de la importación lo indican, y el mensaje enlaza con la ventana **Resultado de la importación**. La ventana nombra cada elemento por tipo y nombre, indica el motivo y agrupa los elementos bajo estos encabezados:

- **No importado**: el elemento no está en el proyecto.
- **Creadas sin datos**: la tabla, la vista o la dimensión está en el proyecto pero no contiene datos, porque no se pudieron leer ni cargar.
- **Advertencias**: el elemento se importó, pero hay algo que revisar, como columnas que el almacén convirtió a los tipos de columna de la tabla.
- **Variables que conservaron el valor de este proyecto**: el proyecto ya tenía una variable con ese nombre, por lo que conservó su propio valor.

Los elementos más graves aparecen primero, y la ventana lo indica cuando hay más de los que muestra. Para volver a abrir la ventana más adelante, seleccione el proyecto en la pestaña **Proyectos** y elija **Ver resultado de la importación o la copia** en el menú **Acciones**, o haga clic con el botón derecho en el proyecto.

El resultado permanece en el proyecto hasta que alguien lo descarte o hasta que una importación posterior en el mismo proyecto lo reemplace. Haga clic en **Descartar resultado** para quitarlo para todos los que puedan abrir el proyecto; no cambia nada en el proyecto. Descartarlo requiere acceso de edición al proyecto, y el proyecto no debe estar bloqueado.


### Importación en un proyecto existente


Importar en un proyecto que ya existe agrega contenido en lugar de reemplazarlo. Dos cosas deciden lo que ocurre cuando el archivo y el proyecto contienen el mismo elemento.


**Debe poder modificar el proyecto de destino.** Se rechaza una importación en un proyecto sobre el que no tenga ningún rol, así como en un proyecto bloqueado para impedir cambios; esto se comprueba antes de leer o escribir nada, de modo que una importación rechazada deja el proyecto intacto.


**El proyecto conserva su propia configuración.** Su nombre, identificador, entorno de conexión de datos, valores predeterminados de almacenamiento, cuenta de documentos, tipo de acceso, listas de acceso y concesiones de acceso a filas se dejan como están. Solo se trae el contenido que seleccionó.

Un paso configurado como **Predeterminado del proyecto** traslada ese ajuste, no una cuenta: una vez restaurado, se resuelve con el valor predeterminado que tenga el proyecto, no con el que tenía cuando se archivó.


### Elementos duplicados


Cuando un elemento entrante es el mismo que uno que ya está en el proyecto, usted elige qué ocurre con él:


- **Sobrescribir los elementos duplicados con los datos entrantes**: la versión del archivo reemplaza a la del proyecto.
- **Crear una copia nueva de los elementos duplicados**: el proyecto conserva lo que tiene y el elemento entrante se agrega junto a él con ` copy` añadido a su nombre (y un contador, si ese nombre también está ocupado). Esto se aplica a flujos de trabajo, pasos, tablas, dimensiones, editores de datos, vistas y funciones definidas por el usuario.


**Las variables del proyecto y del flujo de trabajo son la excepción.** Una variable se identifica por su nombre, así que no hay forma de agregar una segunda copia sin cambiarle el nombre a algo a lo que nada hace referencia. Cuando el proyecto ya define una variable que el archivo también contiene, se conserva el valor propio del proyecto y el resultado de la importación enumera las variables que se dejaron sin tocar. Si desea el valor del archivo, establézcalo después en la variable.


Algo que conviene saber: esta coincidencia se basa en la identidad, no en el nombre. Un elemento que proviene originalmente del mismo proyecto (cualquier cosa de la que se exportó el archivo, o una copia de ella) se reconoce como el mismo elemento. Dos elementos que simplemente comparten un nombre se tratan como elementos distintos, y ambos estarán presentes después de la importación.

### Si una tabla vuelve sin sus datos


Restaurar los datos de una tabla depende de que sus columnas coincidan con la tabla de destino: los mismos nombres en el mismo orden, porque eso es lo que usa una carga. Cuando no coinciden, los datos de esa tabla se omiten y la tabla aparece en el resultado de la importación en **Creadas sin datos**, igual que una tabla cuyos datos no estaban en el archivo. Una diferencia únicamente en el tipo almacenado de una columna no retiene los datos: los datos se cargan y la tabla aparece en **Advertencias** con las columnas que el almacén convirtió.


Una importación en la que todas las tablas no lograron cargar sus datos conserva el proyecto de todos modos. Su mensaje de cierre indica que no se pudo cargar ninguno de los datos de las tablas, y el resultado de la importación también. Si una importación termina con todos los flujos de trabajo, tablas y dimensiones en su lugar, lea su mensaje de cierre antes de suponer que las filas llegaron con ellos.


## Programación del archivado


Los archivos también pueden servir como copia de seguridad periódica de su proyecto. PlaidCloud le permite administrar la programación de las copias de seguridad y establecer el período de retención de los archivos de copia de seguridad según le resulte más conveniente o deseable.


Dado que todos los cambios en un proyecto se registran automáticamente, el archivado no es necesario para revertir cambios. Sin embargo, proporciona instantáneas específicas del estado del proyecto, lo que suele ser útil para fines de control o para poder recuperar un punto conocido.



Para establecer una programación de archivado:


1. Abra Analyze
2. Seleccione la pestaña “Proyectos”
3. Haga clic en el icono de copia de seguridad
4. Elija un directorio de destino en una cuenta de **Documento**
5. Elija la frecuencia y la retención de las copias de seguridad
6. Elija los elementos de los que desea hacer copia de seguridad
7. Haga clic en “Actualizar”
