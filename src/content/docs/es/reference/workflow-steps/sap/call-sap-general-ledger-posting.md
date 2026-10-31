---
title: Call SAP General Ledger Posting (paso)
description: Llama a una función remota (RFC) de SAP ECC / S/4HANA diseñada para contabilizar un asiento de diario, incluidos los impuestos aplicables de IVA y de retención.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-general-ledger-posting.md
---

## Descripción


Llama a una función remota (RFC) de SAP ECC / S/4HANA diseñada para contabilizar un asiento de diario, incluidos los impuestos aplicables de IVA y de retención. También puede ejecutarse en modo de prueba, que realiza el proceso de contabilización pero no lo completa. Esto permite recopilar errores detectables, como una cuenta cerrada o un cliente que no existe en la sociedad especificada. La comprobación de errores es sólida y puede devolver varios errores detectados en una sola prueba.


## Ejemplos


### Parámetros RFC


Seleccione Agente que usar. Seleccione Directorio de destino en la lista desplegable y busque más abajo la carpeta secundaria de destino correcta para el archivo. A continuación, asigne un nombre adecuado a “Target File Name”. En “Function Call Information”, introduzca la función, el Parámetro de valor devuelto y seleccione los parámetros. 



Puede elegir Insertar fila o Anexar fila en la sección Parámetros, así como nombrar los parámetros y asignarles valores. Elija el número de Máx. de solicitudes simultáneas y seleccione Wait for RFC to Complete. Haga clic en Guardar y ejecutar.
