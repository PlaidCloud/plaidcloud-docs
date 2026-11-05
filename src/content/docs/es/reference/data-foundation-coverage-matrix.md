---
title: Matriz de cobertura de Data Foundation
description: Qué conjunto de datos del Common Finance Model aporta directamente cada sistema al que se conecta Data Foundation y cuáles agrega usted como archivo.
sidebar:
  label: Cobertura de Data Foundation
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/data-foundation-coverage-matrix.md
---

Data Foundation lee directamente cada sistema ERP e instancia que usted conecta en un único Common Finance Model. Los archivos completan todo lo que un sistema no contiene, por lo que cada conjunto de datos de las tablas siguientes también puede aportarse como archivo.

## Leyenda

| Marca | Significado |
| --- | --- |
| **Completo** | Data Foundation lee el conjunto de datos directamente del sistema. |
| **Completo¹** | Se lee directamente cuando el sistema lo contiene. Un sistema sin los datos, o una conexión sin acceso a ellos, no detiene la carga. |
| **Archivo** | El sistema no aporta este conjunto de datos. Agréguelo como archivo. |

## SAP, Oracle y Dynamics 365

| Conjunto de datos | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendario fiscal | Completo | Completo | Completo | Completo | Completo | Completo |
| Plan de cuentas | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo | Completo | Completo | Completo | Completo |
| Centros de beneficio | Completo¹ | Completo¹ | Archivo | Archivo | Archivo | Archivo |
| Productos | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Clientes | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Libro mayor | Completo | Completo | Completo | Completo | Completo | Completo |
| Balance de comprobación | Completo | Completo | Completo | Completo | Completo | Completo |
| Líneas de ventas | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pipeline | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| Saldos de inventario | Completo¹ | Completo¹ | Completo¹ | Archivo | Archivo | Completo¹ |
| Presupuesto | Completo¹ | Completo¹ | Completo¹ | Archivo | Archivo | Completo¹ |
| Inductores de asignación | Completo¹ | Completo¹ | Archivo | Archivo | Archivo | Archivo |
| Tipos de cambio | Completo | Completo | Completo | Completo | Completo | Completo |
| Valores de segmento | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| CO-PA por valoración | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |

## Sistemas financieros de mercado medio y en la nube

| Conjunto de datos | Business Central | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendario fiscal | Completo | Completo | Completo | Completo | Completo | Completo |
| Plan de cuentas | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo | Completo¹ | Completo | Completo | Completo |
| Centros de beneficio | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| Productos | Completo | Completo | Completo¹ | Completo | Completo¹ | Completo |
| Clientes | Completo | Completo | Completo¹ | Completo | Completo¹ | Completo |
| Libro mayor | Completo | Completo | Completo | Completo | Completo | Completo |
| Balance de comprobación | Completo | Completo | Completo | Completo | Completo | Completo |
| Líneas de ventas | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo |
| Pipeline | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| Saldos de inventario | Archivo | Archivo | Completo¹ | Archivo | Archivo | Completo¹ |
| Presupuesto | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Archivo | Completo¹ |
| Inductores de asignación | Completo¹ | Completo¹ | Archivo | Archivo | Completo¹ | Completo |
| Tipos de cambio | Completo | Completo | Completo¹ | Archivo | Completo | Completo¹ |
| Valores de segmento | Archivo | Archivo | Archivo | Archivo | Completo¹ | Completo |
| CO-PA por valoración | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |

## Orígenes de CRM, consolidación y planificación

| Conjunto de datos | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entidades | Archivo | Archivo | Archivo |
| Calendario fiscal | Archivo | Archivo | Archivo |
| Plan de cuentas | Archivo | Archivo | Archivo |
| Departamentos | Archivo | Archivo | Archivo |
| Centros de beneficio | Archivo | Archivo | Archivo |
| Productos | Completo¹ | Archivo | Archivo |
| Clientes | Completo¹ | Archivo | Archivo |
| Libro mayor | Archivo | Archivo | Archivo |
| Balance de comprobación | Archivo | Archivo | Archivo |
| Líneas de ventas | Archivo | Archivo | Archivo |
| Pipeline | Completo¹ | Archivo | Archivo |
| Saldos de inventario | Archivo | Archivo | Archivo |
| Presupuesto | Archivo | Completo | Completo |
| Inductores de asignación | Archivo | Archivo | Archivo |
| Tipos de cambio | Archivo | Archivo | Archivo |
| Valores de segmento | Archivo | Archivo | Archivo |
| CO-PA por valoración | Archivo | Archivo | Archivo |

## Notas por sistema

- **Salesforce** es un origen de CRM. Aporta clientes, productos y el pipeline de ventas, nunca el libro mayor.
- **OneStream** es un origen de resultados. Aporta únicamente el conjunto de datos de presupuesto, incorporando sus resultados consolidados para que Data Foundation pueda conciliar con ellos las pérdidas y ganancias del grupo.
- **Anaplan** es un origen de planes. Aporta únicamente el conjunto de datos de presupuesto, a partir de un plan de presupuesto, de pronóstico o consolidado.
- **SAP S/4HANA y SAP ECC** leen los mismos datos maestros. ECC lee su libro mayor a partir de las partidas de contabilidad financiera y de controlling, y sus totales a partir de las tablas de totales del libro mayor. Los centros de beneficio se leen cuando el sistema los contiene. Las líneas de ventas son documentos de facturación, no CO-PA.
- **CO-PA por valoración** no se lee directamente de ningún sistema. Agréguelo como archivo.
- **Workday** no tiene un servicio directo de asientos ni de saldos. Data Foundation le proporciona los informes que debe crear y los lee. Los valores de segmento (worktags), los clientes, los productos, las líneas de ventas y los inductores de plantilla de personal provienen de informes opcionales. Los presupuestos siguen siendo archivos.
- **Xero** no aporta tipos de cambio. Agréguelos como archivo si sus entidades usan más de una moneda.
- **QuickBooks Online** lee departamentos, clientes, productos, tipos de cambio, presupuestos, inventario y líneas de ventas cuando el archivo de la empresa los contiene.
- **NetSuite** lee los segmentos personalizados como valores de segmento. Los tipos de cambio y el inventario se leen cuando la cuenta los ofrece, y los presupuestos cuando la cuenta usa NetSuite Budgets y el rol puede leerlos.

## Temas relacionados

- [Data Foundation](/es/guides/projects/data-foundation/)
- [Primeros pasos con Data Foundation](/es/guides/projects/data-foundation-getting-started/)
- [Agregar archivos para datos que no están en su ERP](/es/guides/projects/data-foundation/#agregar-archivos-para-datos-que-no-están-en-su-erp)
- Guías de acceso de conexión:
  - [NetSuite](/es/guides/connections/netsuite-access-for-data-foundation/)
  - [Salesforce](/es/guides/connections/salesforce-access-for-data-foundation/)
  - [SAP S/4HANA](/es/guides/connections/sap-s4hana-access-for-data-foundation/)
  - [SAP ECC](/es/guides/connections/sap-ecc-access-for-data-foundation/)
  - [SAP S/4HANA Cloud](/es/guides/connections/s4hana-cloud-access-for-data-foundation/)
  - [Oracle E-Business Suite](/es/guides/connections/oracle-ebs-access-for-data-foundation/)
  - [Oracle Fusion](/es/guides/connections/oracle-fusion-access-for-data-foundation/)
  - [Dynamics 365 Finance and Operations](/es/guides/connections/dynamics-365-fo-access-for-data-foundation/)
  - [Business Central](/es/guides/connections/business-central-access-for-data-foundation/)
  - [Sage Intacct](/es/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/es/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/es/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/es/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/es/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/es/guides/connections/anaplan/#anaplan-como-origen-de-data-foundation)
