---
title: Call SAP RFC (paso)
description: Llame a módulos de función RFC de SAP desde un paso de flujo de trabajo de PlaidCloud para integrarse directamente con sistemas SAP ECC y S/4HANA.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-rfc.md
---

## Descripción


Llama a una función remota (RFC) de SAP ECC / S/4HANA y recupera los datos en forma tabular. Estos datos quedan disponibles para los procesos de transformación en PlaidCloud.


## Destino de los datos

Guarde el resultado de la RFC como un archivo o en una tabla.

**Archivo** escribe el resultado como **JSON**, **Delimitado por comas**, **Delimitado por tabulaciones**, **Delimitado por barras verticales** o **Parquet**. Un archivo Parquet conserva los mismos tipos de columna que una tabla.

**Tabla** guarda el resultado en una **Tabla de destino**, con los tipos tomados de las definiciones de campo de la propia función RFC:

| Tipo de campo de SAP | Se guarda como |
|---|---|
| Fecha | Fecha. Una fecha en blanco o inicial se guarda vacía. Una fecha no válida se guarda vacía y el paso finaliza con una advertencia que indica la columna. |
| Decimal empaquetado | Decimal exacto. Si tiene más de 10 posiciones decimales o 28 dígitos enteros, se guarda como texto y el paso finaliza con una advertencia que indica la columna. |
| Entero | Entero. |
| `FLOAT` | Doble. |
| Decimal flotante | Texto exacto. |
| `NUMC`, `CHAR` | Texto, con los ceros iniciales conservados. |
| Hora | Texto, con el formato `HH:MM:SS`. |
| Bytes sin procesar | Texto hexadecimal. |
| `UTCLONG` | Texto. |

Si SAP no puede describir los campos de la función, los decimales se guardan como texto exacto.

Cuando SAP describe la función, cada parámetro se convierte al tipo que espera: las fechas a `YYYYMMDD`, las horas a `HHMMSS`, los enteros y decimales a números, los campos de texto a texto, y los parámetros de estructura y de tabla campo por campo. Un valor que no se puede convertir a un parámetro entero o decimal hace fallar el paso.

## Ejemplos


### Parámetros RFC


Seleccione Agente que usar. Seleccione Directorio de destino en la lista desplegable y busque más abajo la carpeta secundaria de destino correcta para el archivo. A continuación, asigne un nombre adecuado a “Target File Name”. En “Function Call Information”, introduzca la función, el Parámetro de valor devuelto y seleccione los parámetros.

Puede elegir Insertar fila o Anexar fila en la sección Parámetros, así como nombrar los parámetros y asignarles valores. Elija el número de Máx. de solicitudes simultáneas y seleccione Wait for RFC to Complete. Haga clic en Guardar y ejecutar.



### Iteración avanzada de valores


Si lo desea, puede seleccionar “No Iterators” en la parte superior de esta pestaña y luego hacer clic en Guardar y ejecutar, o bien puede especificar iteradores.


Aquí puede seleccionar “Specify Argument Values” en Iterar sobre y crear argumentos para pasar después al Valor de iteración.


Junto a Seleccione el argumento iterador cuyos valores se editarán, hay opciones para Insertar fila, Anexar fila, Eliminar fila, Bajar fila o Mover al final la fila. 
Más abajo puede elegir Iteradores de rango con el mismo menú desplegable. La última sección se titula “Exclusions for Selected Range Iteration” 
y ofrece las mismas opciones por fila para agregar, eliminar, etc. Los valores excluidos se pueden introducir más abajo. Haga clic en Guardar y ejecutar.
