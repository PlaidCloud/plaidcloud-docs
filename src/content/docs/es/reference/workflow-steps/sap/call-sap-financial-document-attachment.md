---
title: Paso Call SAP Financial Document Attachment
description: Recupere los adjuntos de documentos financieros de SAP desde un paso de flujo de trabajo de PlaidCloud para la extracción y el procesamiento automatizados de documentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Descripción



Adjunta un archivo a un documento FI (Contabilidad financiera) específico de SAP ECC / S/4HANA mediante una RFC (llamada a función remota). Es útil para contabilizar documentación de respaldo (facturas escaneadas, flujos de aprobación, copias de contratos) junto con los asientos financieros que respalda.

Requiere las credenciales RFC de SAP configuradas en el conector de SAP y el número del documento FI de destino (sociedad, número de documento, ejercicio fiscal).


## Qué se comprueba al guardar

El paso lee la ruta de cada archivo de una columna `relative_file_path` entre las columnas de salida de su pestaña **Columnas**, y esa columna debe ser de texto. Se rechaza el guardado si no existe: *Las columnas de salida deben incluir relative_file_path, la ruta de cada archivo que se va a adjuntar.* o si tiene otro tipo: *La columna relative_file_path debe ser de texto, no de tipo entero.*

Si se guarda con una tabla de origen elegida pero sin columnas de origen o sin columnas de destino, se rellena el lado vacío a partir del origen, igual que lo haría **Rellenar ambas tablas de asignación**.


## Ejemplos


### Parámetros RFC


Seleccione Agente que usar. Seleccione Directorio de destino en la barra desplegable y busque abajo la carpeta secundaria de destino correcta para el archivo. A continuación, asigne el nombre adecuado a “Target File Name”. En “Function Call Information”, introduzca la función, el Parámetro de valor devuelto y seleccione los parámetros.



Puede elegir Insertar fila o Anexar fila en la sección Parámetros, así como nombrar los parámetros y asignarles valores. Elija el número de Máx. de solicitudes simultáneas y seleccione “Wait for RFC to Complete”. Guardar y ejecutar el paso.
