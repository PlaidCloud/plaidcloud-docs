---
title: Pasos de flujo de trabajo
description: "Todos los tipos de paso de flujo de trabajo de PlaidCloud: importación, exportación, transformaciones, asignaciones, dimensiones, documentos, notificaciones y más."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

Los pasos de flujo de trabajo son los bloques de construcción de la automatización de PlaidCloud. Cada paso realiza una operación (importar un CSV, combinar dos tablas, enviar una notificación) y los pasos se componen en flujos de trabajo que se ejecutan de forma secuencial, en paralelo, condicional o en bucles.

## Categorías

### Movimiento de datos

- [Importar](/es/reference/workflow-steps/import/): incorpore datos desde CSV, Excel, Parquet, JSON, ORC, Delta Lake, SQL, BigQuery, MongoDB, Kafka, SPSS, orígenes Singer y más
- [Exportar](/es/reference/workflow-steps/export/): envíe datos a CSV, XML, SQL, Excel, Google Sheets, Parquet, ORC, MongoDB, Kafka, archivos de tablas y más

### Transformaciones de tablas

- [Tablas](/es/reference/workflow-steps/tables/): combinaciones, uniones, filtros, búsquedas, tablas dinámicas, fusiones, actualizaciones dirigidas, concesiones de Acceso a filas desde una tabla de origen, restauración a un momento determinado
- [Operaciones comunes](/es/reference/workflow-steps/common/): patrones compartidos de asignación y filtrado de datos

### Geoespacial

- [Geoespacial](/es/reference/workflow-steps/spatial/): importe y exporte archivos espaciales, cree áreas de influencia, haga coincidir, mida, reproyecte y construya geometrías; cobertura completa de las herramientas espaciales de Alteryx

### Modelado

- [Asignación](/es/reference/workflow-steps/allocation/): reparto basado en inductores, asignaciones divididas, etiquetado basado en reglas
- [Dimensiones](/es/reference/workflow-steps/dimensions/): cargue, ordene, borre, exporte y administre jerarquías
- [Optimización](/es/reference/workflow-steps/optimization/): pasos de solucionador lineal y de enteros mixtos
- [Aprendizaje automático](/es/reference/workflow-steps/machine-learning/): entrene modelos, incluidos XGBoost y los aprendices de KNIME, y puntúe tablas con ellos

### Documentos y archivos

- [Documento](/es/reference/workflow-steps/document/): operaciones con archivos, listado de directorios, cifrado, manipulación de PDF, procesamiento de imágenes, conversión de codificación, actualización de celdas de Excel
- [Texto y documentos](/es/reference/workflow-steps/text-documents/): extracción de texto de PDF, OCR de imágenes, lectura y escritura de blobs, análisis de sentimiento, modelado de temas, nubes de palabras

### Comunicación

- [Notificaciones](/es/reference/workflow-steps/notifications/): correo electrónico, Slack, Teams, SMS, webhook, Twitter, registro
- [Informes](/es/reference/workflow-steps/reports/): genere informes PDF individuales o por lotes a partir de plantillas RML

### Control del flujo de trabajo

- [Control del flujo de trabajo](/es/reference/workflow-steps/workflow-control/): variables, bucles, subflujos de trabajo, macros, gestión de errores, verificación del recuento de filas
- [General](/es/reference/workflow-steps/general/): paso LLM, Pass, Esperar, transformación definida por el usuario, ejecución remota de Python, Ejecutor de Alteryx
- [Macros empaquetadas](/es/reference/workflow-steps/macros/): equivalentes de las macros empaquetadas de Alteryx: Create Samples, DateTime Now, Heat Map, Pie Wedge Trade Area

### Integraciones empresariales

- [Agente](/es/reference/workflow-steps/agent/): operaciones del agente de PlaidLink para recursos locales
- [NetSuite](/es/reference/workflow-steps/netsuite/): importe saldos, detalle del libro mayor, datos maestros o su propia [consulta SuiteQL](/es/reference/workflow-steps/netsuite/import-suiteql-query/); contabilice asientos de diario en NetSuite
- [Acumatica](/es/reference/workflow-steps/acumatica/): importe entidades maestras y transaccionales; contabilice transacciones de diario, facturas, facturas de proveedores y pagos
- [Business Central](/es/reference/workflow-steps/business-central/): importe entidades OData; contabilice líneas del diario general
- [Xero](/es/reference/workflow-steps/xero/): importe entidades de la API de contabilidad; contabilice diarios manuales, facturas, facturas de proveedores, pagos y notas de crédito
- [Dynamics 365 F&O](/es/reference/workflow-steps/dynamics-365-fo/): importe entidades OData/DMF; contabilice asientos de diario
- [Oracle Fusion](/es/reference/workflow-steps/oracle-fusion/): importe saldos del libro mayor y lotes de diario; contabilice asientos de diario mediante FBDI
- [Oracle EPM (HFM / FCCS)](/es/reference/workflow-steps/oracle-epm/): obtenga por autoservicio un segmento de datos ad hoc de Oracle FCCS con un selector de punto de vista; carga periódica programada opcional
- [Oracle Essbase](/es/reference/workflow-steps/essbase/): ejecute una consulta MDX en vivo contra un cubo, o cargue el esquema de una dimensión como dimensión de PlaidCloud; directo desde la nube
- [IBM TM1 / Planning Analytics](/es/reference/workflow-steps/ibm-planning-analytics/): lea un cubo mediante una vista guardada o MDX, o una jerarquía de dimensión; directo desde la nube o mediante un agente local
- [Anaplan](/es/reference/workflow-steps/anaplan/): lea una vista guardada, ejecute una acción de exportación existente o cargue una o más listas en una dimensión de PlaidCloud; directo desde la nube, solo lectura
- [Workday Financials](/es/reference/workflow-steps/workday-financials/): importe un informe RaaS; contabilice diarios contables
- [Salesforce](/es/reference/workflow-steps/salesforce/): extraiga cualquier objeto de CRM estándar o personalizado a una tabla de proyecto mediante Bulk API 2.0, con el objeto y la lista de campos leídos de la organización
- [Sage Intacct](/es/reference/workflow-steps/sage-intacct/): importe saldos, facturas de proveedores, consultas ad hoc y objetos de libro mayor y dimensiones; contabilice asientos de diario
- [SAP S/4HANA Cloud](/es/reference/workflow-steps/s4hana-cloud/): importe el balance de comprobación y las partidas de asientos de diario mediante OData; contabilice asientos de diario mediante SOAP
- [SAP](/es/reference/workflow-steps/sap/): llamadas RFC de SAP ECC / S/4HANA
- [SAP-PCM](/es/reference/workflow-steps/sap-pcm/): control de modelos de SAP Profitability and Cost Management
