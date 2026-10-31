---
title: Carga y descarga de dimensiones
description: Cargue y descargue datos de dimensiones en PlaidCloud, incluidas las importaciones masivas, la actualización de datos y la sincronización con orígenes de datos externos.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/loading-unloading.md
---

Las dimensiones se pueden mantener desde operaciones de flujo de trabajo mediante la carga de datos. Además, los datos dimensionales se pueden aplanar en datos tabulares y almacenar en tablas. Esto suele ser útil para enriquecer los datos de informes y análisis.


## Carga de dimensiones

Como las dimensiones representan estructuras de datos jerárquicas, el proceso de carga debe transmitir las relaciones de los datos. PlaidCloud admite dos estructuras de datos distintas para cargar dimensiones:
 * Elemento padre-elemento hijo: los datos se organizan verticalmente, con una columna *Parent* y una columna *Child* que definen el elemento padre de cada elemento hijo en toda la estructura
 * Niveles: los datos se organizan horizontalmente, y cada columna representa un nivel de la jerarquía de izquierda a derecha

 Además de la estructura, el proceso de carga puede incluir otra información de la dimensión, como valores, alias y propiedades.

 Una carga por niveles (plana) toma una consolidación predeterminada, que reciben todos los nodos intermedios que crea la carga, y puede indicar una columna de hoja: cuando lo hace, esa columna decide qué nodo lleva los alias, las propiedades y los valores de la fila; de lo contrario, el último nivel completado es la hoja.

 El tipo de consolidación predeterminado de una carga de elemento padre-elemento hijo se aplica a toda fila cuya propia consolidación esté en blanco o no se reconozca, por lo que debe ser uno de los tipos válidos incluso cuando la tabla también indica una columna de consolidación. La jerarquía a la que apunta una carga no debe compartir nombre con una columna que la carga asigna: una columna con ese nombre se interpreta como la jerarquía a la que pertenece cada fila, por lo que una carga que indica ambas se rechaza en lugar de seguir una interpretación e ignorar la otra.

 Una carga de alias, propiedades o valores comprueba el miembro de cada fila antes de escribir nada. Si alguna fila nombra un miembro que la dimensión no contiene, la carga falla e informa de esos nombres, y no se almacena nada de esa carga. Cargue primero la estructura, o incluya en ella los miembros que faltan, y después cargue los atributos.

 Consulte el paso de flujo de trabajo [Dimension Load](/es/reference/workflow-steps/dimensions/dimension-load) para obtener más información.


## Descarga (exportación) de dimensiones

La exportación de dimensiones a tablas admite dos enfoques estructurales:
 * Elemento padre-elemento hijo: los datos se organizan verticalmente, con una columna *Parent* y una columna *Child* que definen el elemento padre de cada elemento hijo en toda la estructura
 * Niveles: los datos se organizan horizontalmente, y cada columna representa un nivel de la jerarquía de izquierda a derecha

Las propiedades y los valores también se pueden incluir en los datos tabulares aplanados.

 Consulte el paso de flujo de trabajo [Dimension Export](/es/reference/workflow-steps/dimensions/dimension-export) para obtener más información.
