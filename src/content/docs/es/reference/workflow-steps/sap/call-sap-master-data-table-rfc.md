---
title: Call SAP Master Data Table RFC (paso)
description: Llama a una función remota (RFC) de SAP ECC / S/4HANA diseñada para acceder a tablas de datos maestros y recupera los datos en forma tabular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-master-data-table-rfc.md
---

## Descripción


Llama a una función remota (RFC) de SAP ECC / S/4HANA diseñada para acceder a tablas de datos maestros y recupera los datos en forma tabular. Estos datos quedan disponibles para los procesos de transformación en PlaidCloud. También permite exportar la estructura de la tabla de datos maestros a un archivo aparte que incluye los nombres de las columnas, los tipos de datos y el orden de las columnas.


## Ejemplos


### Parámetros RFC


Seleccione Agente que usar. Seleccione Directorio de destino en la lista desplegable y busque más abajo la carpeta secundaria de destino correcta para el archivo. A continuación, asigne un nombre adecuado a “Target File Name”. En “Function Call Information”, introduzca la función, el Parámetro de valor devuelto y seleccione los parámetros.



Puede elegir Insertar fila o Anexar fila en la sección Parámetros, así como nombrar los parámetros y asignarles valores. Elija el número de Máx. de solicitudes simultáneas y seleccione Wait for RFC to Complete. Haga clic en Guardar y ejecutar.
