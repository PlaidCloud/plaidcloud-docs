---
title: Conexiones
description: Configure y administre las conexiones de PlaidCloud, configuraciones guardadas que permiten a los flujos de trabajo acceder a bases de datos externas, almacenamiento en la nube, ERP y API REST.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

Una **conexión** es una configuración guardada que permite a PlaidCloud acceder a un sistema externo: una base de datos, una cuenta de almacenamiento en la nube, un ERP o una API REST. Los pasos de flujo de trabajo que necesitan leer de ese sistema o escribir en él hacen referencia a la conexión, de modo que las credenciales y los detalles del punto de conexión se encuentran en un solo lugar.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="Muchos pasos de flujo de trabajo hacen referencia a una conexión guardada, que contiene las credenciales y el punto de conexión en un solo lugar y llega al sistema externo: una base de datos, almacenamiento en la nube, un ERP o una API REST." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">pasos de flujo de trabajo</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Paso de importación</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Paso de exportación</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Paso de búsqueda</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Conexión</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">credenciales + punto de conexión, una vez</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">sistema externo</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">BD · almacenamiento · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Configure la conexión una sola vez; cada paso que lee del sistema externo o escribe en él apunta a ella, de modo que las credenciales y los detalles del punto de conexión no se duplican entre pasos.</figcaption>
</figure>

## Guías

- [Crear y administrar una conexión](/es/guides/connections/create-connection/): cree, edite, pruebe y controle el acceso a una conexión, y configúrela por entorno.
- [Use su propio almacén](/es/guides/connections/external-lakehouse/): conecte usted mismo su propio almacén de Snowflake o Databricks, inicie sesión con su propia identidad, administre varios almacenes y consulte lo que cuesta cada ejecución.
- [Conexión de PlaidCloud Git](/es/guides/connections/plaidcloud-git/): conéctese al servidor Git administrado de su espacio de trabajo sin URL de servidor ni credenciales, y automatice a partir de él las compilaciones de aplicaciones de Panel.
- [Clonar una conexión](/es/guides/connections/clone-connection/): duplique una conexión existente para un nuevo entorno o inquilino.
- [Data Foundation: el Common Finance Model](/es/guides/projects/data-foundation/): el Common Finance Model reúne los datos de ERP de varios sistemas e instancias de ERP en un solo modelo, con un único plan de cuentas, un único conjunto de entidades y una única moneda de informe, que leen los informes, las métricas y los asistentes de IA.
- [Orígenes de Singer](/es/guides/connections/singer-sources/): conéctese a orígenes como Stripe, GitHub, Slack y BigQuery con taps de Singer y luego importe sus datos en tablas de proyecto.
- [Conectar con NetSuite](/es/guides/connections/netsuite/): configure una conexión de NetSuite y obtenga datos financieros y operativos con SuiteQL.
- [Acceso a NetSuite para Data Foundation](/es/guides/connections/netsuite-access-for-data-foundation/): lo que configura su administrador de NetSuite para que Data Foundation pueda leer NetSuite directamente, y qué debe enviar de vuelta.
- [Importar datos financieros de NetSuite](/es/guides/connections/import-netsuite-financials/): obtenga saldos, detalle del libro mayor y datos maestros con los pasos de importación de NetSuite predefinidos, sin tener que escribir SuiteQL.
- [Contabilizar un asiento de diario de NetSuite](/es/guides/connections/post-netsuite-journal-entries/): asigne tablas de encabezado y de líneas, obtenga una vista previa y contabilice asientos de diario en NetSuite.
- [Conectar con Acumatica](/es/guides/connections/acumatica/): configure una conexión de Acumatica, importe entidades y contabilice transacciones de diario, facturas, facturas de proveedor y pagos.
- [Conectar con Business Central](/es/guides/connections/business-central/): configure una conexión de Business Central con Azure AD, importe entidades OData y contabilice líneas del diario general.
- [Conectar con Dynamics 365 Finance & Operations](/es/guides/connections/dynamics-365-fo/): configure una conexión de D365 F&O con Azure AD, importe entidades OData/DMF y contabilice asientos de diario.
- [Conectar con Oracle Fusion](/es/guides/connections/oracle-fusion/): configure una conexión de Oracle Fusion, importe saldos del libro mayor y lotes de asientos de diario, y contabilice asientos mediante FBDI.
- [Conectar con Workday Financials](/es/guides/connections/workday-financials/): configure una conexión de Workday Financials con un Usuario del sistema de integración, importe un informe RaaS y contabilice asientos de diario.
- [Conectar con SAP S/4HANA Cloud](/es/guides/connections/s4hana-cloud/): configure una conexión directa de S/4HANA Cloud con OAuth2, importe el balance de comprobación y las partidas de asientos de diario, y contabilice asientos de diario mediante SOAP.
- [Extracciones ad hoc de SAP ECC / S/4HANA](/es/guides/connections/sap-adhoc-extract/): busque en SAP por tabla, código de transacción o consulta de SAP guardada, obtenga una vista previa y planifique la extracción, y cárguela en una tabla mediante un agente de PlaidLink.
- [Conectar con Sage Intacct](/es/guides/connections/sage-intacct/): configure una conexión de Sage Intacct y obtenga datos financieros y contables.
- [Conectar con Xero](/es/guides/connections/xero/): autorice una organización de Xero con un solo clic, importe entidades de la API de contabilidad y contabilice asientos manuales, facturas, facturas de proveedor, pagos y notas de crédito.
- [Conectar con Salesforce](/es/guides/connections/salesforce/): configure una aplicación de cliente externa de Salesforce y un usuario de ejecución, y luego extraiga objetos de CRM en tablas de proyecto.
- [Extraer de HFM / FCCS (ad hoc)](/es/guides/connections/hfm-fccs/): conéctese a Oracle FCCS y obtenga por autoservicio un segmento de datos con un selector de punto de vista, sin abrir un ticket con el equipo de HFM.
- [Conectar con TM1](/es/guides/connections/tm1/): conéctese a un servidor IBM TM1 / Planning Analytics y lea datos de cubos por vista o MDX, segmentados por período.
- [Conectar con Anaplan](/es/guides/connections/anaplan/): conéctese a Anaplan y lea una vista guardada, ejecute una acción de exportación ya existente o cargue listas en una dimensión de PlaidCloud. Solo lectura.
- [OneStream para Data Foundation](/es/guides/connections/onestream-for-data-foundation/): lo que configura su administrador de OneStream para que Data Foundation pueda leer resultados consolidados mediante un adaptador de datos.
- [Conectar con QuickBooks](/es/guides/connections/quickbooks/): requisitos previos y limitaciones actuales de QuickBooks Online.
- [Revisar el registro de asientos](/es/guides/connections/posting-register/): una consola a nivel de inquilino para que finanzas y contabilidad revisen las contabilizaciones de ERP de todos los proyectos y conexiones que pueden ver.

## Relacionado

- [Referencia de conectores](/es/reference/connectors/): el catálogo completo de sistemas compatibles y los campos que necesita cada uno.
