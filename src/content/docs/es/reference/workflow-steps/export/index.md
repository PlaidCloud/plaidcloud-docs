---
title: Pasos de exportación
description: "Pasos de flujo de trabajo que escriben tablas de proyecto en destinos externos: formatos de archivo, cuentas de documentos y bases de datos externas."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/index.md
---

Pasos de flujo de trabajo que escriben tablas de proyecto en destinos externos: formatos de archivo, cuentas de documentos y bases de datos externas.

## Pasos

- [Archivar tablas](/es/reference/workflow-steps/export/archive-tables/)
- [Export External Database Tables](/es/reference/workflow-steps/export/export-external-tables/)
- [Exportar Kafka](/es/reference/workflow-steps/export/export-kafka/)
- [Exportar MongoDB](/es/reference/workflow-steps/export/export-mongodb/)
- [Exportar archivo del proyecto](/es/reference/workflow-steps/export/export-project-archive/)
- [Export Project Table](/es/reference/workflow-steps/export/export-project-table/)
- [Export Quandl](/es/reference/workflow-steps/export/export-quandl/)
- [Exportar SQL](/es/reference/workflow-steps/export/export-sql/)
- [Export Templated](/es/reference/workflow-steps/export/export-templated/)
- [Export to Avro](/es/reference/workflow-steps/export/export-to-avro/)
- [Export To CSV](/es/reference/workflow-steps/export/export-to-csv/)
- [Export To Excel](/es/reference/workflow-steps/export/export-to-excel/)
- [Export To Excel Sheets](/es/reference/workflow-steps/export/export-to-excel-sheets/)
- [Export To Google Spreadsheet](/es/reference/workflow-steps/export/export-to-google-spreadsheet/)
- [Export To HDF](/es/reference/workflow-steps/export/export-to-hdf/)
- [Export To JSON](/es/reference/workflow-steps/export/export-to-json/)
- [Export to ORC](/es/reference/workflow-steps/export/export-to-orc/)
- [Export to Parquet](/es/reference/workflow-steps/export/export-to-parquet/)
- [Export to PDF](/es/reference/workflow-steps/export/export-to-pdf/)
- [Export To Table Archive](/es/reference/workflow-steps/export/export-to-table-archive/)
- [Export To XML](/es/reference/workflow-steps/export/export-to-xml/)
- [Contabilizar documentos](/es/reference/workflow-steps/export/post-documents/) — contabilice una tabla de documentos en cualquier sistema ERP que haya configurado
- [Exportación de archivo espacial](/es/reference/workflow-steps/spatial/spatial-file-export/)
- [Publish to Tableau](/es/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/es/reference/workflow-steps/export/export-hyper/)

## Columnas escritas

La mayoría de los pasos de exportación escriben todas las columnas de la tabla de origen, tal como está cuando se ejecuta el paso y en el orden de columnas de la tabla, cuando el asignador de datos no enumera columnas de destino, es decir, cuando la tabla de la derecha de la pestaña **Columnas** está vacía. Por lo tanto, un paso configurado a medias exporta la tabla completa a su destino en lugar de fallar, así que revise el asignador de datos antes de ejecutar una exportación a un destino externo.

Si no hay columnas asignadas y la tabla de origen no tiene ninguna, una exportación de CSV, JSON, SQL, Excel, PDF, Google Spreadsheet o Kafka no escribe nada y termina con una advertencia. En una exportación de varias tablas, como XML, Parquet, ORC, Avro o Excel Sheets, esa tabla se omite con una advertencia que la indica. Exportar MongoDB, Export External Database Tables, Tableau Hyper Export, Exportación de archivo espacial y Run SAP PCM Hyper Loader hacen lo mismo: terminan correctamente con una advertencia que nombra el origen o el destino, y una tabla externa conserva sus filas anteriores.
