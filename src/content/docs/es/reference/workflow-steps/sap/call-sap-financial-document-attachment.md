---
title: Call SAP Financial Document Attachment (paso)
description: Recupere los archivos adjuntos de documentos financieros de SAP desde un paso de flujo de trabajo de PlaidCloud para automatizar la extracción y el procesamiento de documentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Descripción



Adjunta un archivo a un documento de FI (Financial Accounting) específico en SAP ECC / S/4HANA mediante una RFC (llamada a función remota). Es útil para contabilizar documentación de respaldo, como facturas escaneadas, flujos de aprobación o copias de contratos, junto con los asientos financieros a los que sustentan.

Requiere las credenciales RFC de SAP configuradas en el conector de SAP y el número del documento de FI de destino (sociedad, número de documento y ejercicio fiscal).


## Qué se comprueba al guardar

El paso lee la ruta de cada archivo de una columna `relative_file_path` entre las columnas de salida de su pestaña **Selección de datos de la tabla**, y esa columna debe ser de texto. Al guardar, se rechaza el paso si falta esa columna — *Las columnas de salida deben incluir relative_file_path, la ruta de cada archivo que se adjuntará.* — o si tiene otro tipo — *La columna relative_file_path debe ser de texto, no de tipo entero.*

Si se guarda con una tabla de origen elegida pero sin columnas de origen o de destino, el lado vacío se rellena a partir del origen, como lo haría **Rellenar ambas tablas de asignación**.


## Ejemplos


### Parámetros RFC


Seleccione Agente que usar. Seleccione Directorio de destino en la lista desplegable y busque más abajo la carpeta secundaria de destino correcta para el archivo. A continuación, asigne un nombre adecuado a “Target File Name”. En “Function Call Information”, introduzca la función, el Parámetro de valor devuelto y seleccione los parámetros.



Puede elegir Insertar fila o Anexar fila en la sección Parámetros, así como nombrar los parámetros y asignarles valores. Elija el número de Máx. de solicitudes simultáneas y seleccione Wait for RFC to Complete. Haga clic en Guardar y ejecutar.
