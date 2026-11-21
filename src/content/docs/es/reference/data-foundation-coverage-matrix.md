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
| **Completo¹** | Se lee directamente cuando el sistema lo contiene. Un sistema sin los datos no detiene la carga. Una conexión sin acceso a ellos deja vacío ese conjunto de datos o hace que falle solo ese conjunto de datos, y el resto se carga. |
| **Archivo** | El sistema no aporta este conjunto de datos. Agréguelo como archivo. |

## SAP, Oracle y Dynamics 365

| Conjunto de datos | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendario fiscal | Completo | Completo | Completo | Completo | Completo | Completo |
| Plan de cuentas | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo | Completo | Completo | Completo | Completo |
| Centros de beneficio | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Archivo | Completo¹ |
| Sitios | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Proyectos | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| Representantes de ventas | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| Productos | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Clientes | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Proveedores | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Libro mayor | Completo | Completo | Completo | Completo | Completo | Completo |
| Balance de comprobación | Completo | Completo | Completo | Completo | Completo | Completo |
| Saldo de fin de mes | Archivo | Completo¹ | Archivo | Completo¹ | Completo¹ | Archivo |
| Saldos bancarios | Archivo | Completo¹ | Archivo | Completo¹ | Completo¹ | Completo¹ |
| Líneas de ventas | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pipeline | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| Líneas de facturas de proveedor | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pedidos de compra | Completo¹ | Completo¹ | Archivo | Completo¹ | Completo¹ | Archivo |
| Partidas abiertas | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pagos | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Saldos de inventario | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Costos estándar | Completo¹ | Completo¹ | Archivo | Completo¹ | Completo¹ | Archivo |
| Activos fijos | Completo¹ | Completo¹ | Archivo | Completo¹ | Completo¹ | Archivo |
| Movimientos de activos | Completo¹ | Completo¹ | Archivo | Completo¹ | Completo¹ | Archivo |
| Presupuesto | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Inductores de asignación | Completo¹ | Completo¹ | Archivo | Archivo | Archivo | Archivo |
| Tipos de cambio | Completo | Completo | Completo | Completo | Completo | Completo |
| Valores de segmento | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| CO-PA por valoración | Completo¹ | Completo¹ | Archivo | Archivo | Archivo | Archivo |

## Sistemas financieros de mercado medio y en la nube

| Conjunto de datos | Business Central | Sage 100 | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendario fiscal | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Plan de cuentas | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo¹ | Completo | Archivo | Completo¹ | Completo | Completo |
| Centros de beneficio | Completo¹ | Archivo | Completo¹ | Completo¹ | Completo¹ | Archivo | Completo¹ |
| Sitios | Completo¹ | Archivo | Completo¹ | Completo¹ | Completo¹ | Archivo | Completo¹ |
| Proyectos | Archivo | Archivo | Completo¹ | Archivo | Archivo | Archivo | Archivo |
| Representantes de ventas | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo | Completo¹ |
| Productos | Completo | Archivo | Completo | Completo¹ | Completo¹ | Completo¹ | Completo |
| Clientes | Completo | Archivo | Completo | Completo¹ | Completo¹ | Completo¹ | Completo |
| Proveedores | Completo¹ | Archivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Libro mayor | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Balance de comprobación | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Saldo de fin de mes | Completo¹ | Archivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Archivo |
| Saldos bancarios | Completo¹ | Archivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Líneas de ventas | Completo¹ | Archivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo |
| Pipeline | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| Líneas de facturas de proveedor | Completo¹ | Archivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Partidas abiertas | Completo¹ | Archivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pagos | Completo¹ | Archivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pedidos de compra | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| Saldos de inventario | Completo¹ | Archivo | Archivo | Completo¹ | Archivo | Archivo | Completo¹ |
| Costos estándar | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| Activos fijos | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| Movimientos de activos | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |
| Presupuesto | Completo¹ | Archivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Inductores de asignación | Completo¹ | Archivo | Completo¹ | Archivo | Archivo | Completo¹ | Completo |
| Tipos de cambio | Completo | Archivo | Completo | Completo¹ | Archivo | Completo | Completo¹ |
| Valores de segmento | Archivo | Archivo | Archivo | Archivo | Archivo | Completo¹ | Completo¹ |
| CO-PA por valoración | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo | Archivo |

## Orígenes de CRM, consolidación y planificación

| Conjunto de datos | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entidades | Archivo | Archivo | Archivo |
| Calendario fiscal | Completo¹ | Archivo | Archivo |
| Plan de cuentas | Archivo | Archivo | Archivo |
| Departamentos | Archivo | Archivo | Archivo |
| Centros de beneficio | Archivo | Archivo | Archivo |
| Proyectos | Completo¹ | Archivo | Archivo |
| Representantes de ventas | Completo¹ | Archivo | Archivo |
| Productos | Completo¹ | Archivo | Archivo |
| Clientes | Completo¹ | Archivo | Archivo |
| Libro mayor | Archivo | Archivo | Archivo |
| Balance de comprobación | Archivo | Archivo | Archivo |
| Líneas de ventas | Archivo | Archivo | Archivo |
| Pipeline | Completo¹ | Archivo | Archivo |
| Pedidos de venta | Completo¹ | Archivo | Archivo |
| Saldos de inventario | Archivo | Archivo | Archivo |
| Presupuesto | Archivo | Completo | Completo |
| Inductores de asignación | Archivo | Completo¹ | Completo¹ |
| Tipos de cambio | Archivo | Archivo | Archivo |
| Valores de segmento | Archivo | Archivo | Archivo |
| CO-PA por valoración | Archivo | Archivo | Archivo |

## Notas por sistema

- **Pedidos de venta, contratos, ingresos diferidos y movimientos de inventario** no se leen de ningún sistema, salvo los pedidos de Salesforce. Agréguelos como archivos.
- **Salesforce** es un origen de CRM. Aporta clientes, productos, el pipeline de ventas, los representantes de ventas (usuarios), las campañas como proyectos, sus meses fiscales y sus pedidos, nunca el libro mayor. Los pedidos requieren que Orders esté habilitado en Salesforce. Cuando Salesforce rechaza la lectura de pedidos, solo fallan los meses de pedidos, que conservan lo que cargaron por última vez.
- **OneStream** es un origen de resultados. Aporta el conjunto de datos de presupuesto, incorporando sus resultados consolidados para que Data Foundation pueda conciliar con ellos las pérdidas y ganancias del grupo, y un escenario de presupuesto o de pronóstico como plan. Un segundo adaptador opcional aporta la plantilla de personal y las unidades planificadas como inductores de asignación.
- **Anaplan** es un origen de planes. Aporta el conjunto de datos de presupuesto, a partir de un plan de presupuesto, de pronóstico o consolidado, e inductores de asignación a partir de una segunda exportación opcional.
- **SAP S/4HANA y SAP ECC** leen los mismos datos maestros, proveedores, facturas de proveedor, pedidos de compra, partidas abiertas, pagos, el registro de activos fijos y los costos estándar. ECC lee su libro mayor a partir de las partidas de contabilidad financiera y de controlling, y sus totales y su saldo de fin de mes a partir de la tabla de totales del libro mayor. Los centros de beneficio y las plantas (sitios) se leen cuando el sistema los contiene. Las líneas de ventas son documentos de facturación. CO-PA por valoración se lee de la tabla de partidas individuales del área de resultados que usted indique; si no indica ninguna, agréguelo como archivo.
- **Oracle E-Business Suite** lee los sitios y los centros de beneficio del segmento del plan de cuentas que usted indique para cada uno.
- **Oracle Fusion** lee cada conjunto de datos opcional de su propio informe de BI Publisher. Un informe de clientes, productos, sitios o proveedores que usted no implemente deja ese conjunto de datos vacío con una advertencia; el conjunto de datos de cualquier otro informe falla y conserva lo que cargó por última vez; todo lo demás se carga.
- **Workday** no tiene un servicio directo de asientos ni de saldos. Data Foundation le proporciona los informes que debe crear y los lee. Los valores de segmento (worktags), los clientes, los productos, los proveedores, las líneas de ventas, los libros auxiliares, los saldos bancarios, los presupuestos y los inductores provienen de informes opcionales, y el saldo de fin de mes, del saldo final del informe de saldos iniciales.
- **Sage 100** se lee mediante un agente de PlaidLink, una empresa por conexión. Lleva su contabilidad en una sola moneda, por lo que no aporta tipos de cambio, y Data Foundation no lee sus productos, clientes ni líneas de ventas. Los departamentos se leen del segmento de departamento de la cuenta cuando la máscara de cuenta tiene uno.
- **Xero** no aporta tipos de cambio. Agréguelos como archivo si sus entidades usan más de una moneda. Los departamentos, los sitios y los centros de beneficio son las opciones de las categorías de seguimiento llamadas exactamente Department, Site y Profit centre. Xero permite dos categorías de seguimiento, por lo que una organización tiene como máximo dos de las tres.
- **QuickBooks Online** no tiene departamentos: sus ubicaciones se leen como sitios y sus clases como centros de beneficio. Los clientes, los productos, los proveedores, los tipos de cambio, los presupuestos, el inventario, las ventas y las compras se leen cuando la empresa los contiene, y el inventario solo cuando la empresa lleva el control de la cantidad disponible.
- **NetSuite** lee los segmentos personalizados como valores de segmento, las clases como centros de beneficio y las ubicaciones como sitios. Los tipos de cambio y el inventario se leen cuando la cuenta los ofrece, y los presupuestos cuando la cuenta usa NetSuite Budgets y el rol puede leerlos.

## Saldo de fin de mes

Data Foundation lee el saldo de cierre que el propio sistema informa al final de cada mes (consulte [¿Se puede confiar en las cifras?](/es/guides/projects/data-foundation-proof/)) a partir de:

| Sistema | Origen del saldo de fin de mes |
| --- | --- |
| SAP ECC | La tabla de totales del libro mayor (`FAGLFLEXT`, o `GLT0` en el libro mayor clásico) |
| Oracle E-Business Suite | `GL_BALANCES`, que debe contener todos los períodos |
| Oracle Fusion | El informe PlaidCloudBalances, que abarca todos los períodos |
| Business Central | El balance de comprobación al final de cada mes |
| Sage Intacct | Los saldos de cuenta (el saldo final de cada mes) |
| QuickBooks Online | El informe de balance de comprobación al final de cada mes |
| Xero | El informe de balance de comprobación al final de cada mes |
| Workday | El saldo final del informe de saldos iniciales (Beginning Balances) |

SAP S/4HANA, SAP S/4HANA Cloud, Dynamics 365 Finance and Operations, NetSuite y Sage 100 no informan ningún saldo independiente que Data Foundation lea. Se cargan y funcionan como de costumbre. Cuando Business Central rechaza su balance de comprobación al final de un mes, el saldo de ese mes falla y conserva lo que cargó por última vez.

## Detalle de asientos

Además de los importes, cada línea del libro mayor lleva el tipo de asiento, su fecha de documento, quién lo registró y cuándo, quién lo aprobó, el asiento que revierte y su impuesto, cuando el sistema los contiene. El calendario fiscal lleva el estado de cada período.

| Sistema | Tipo de asiento | Fecha de documento | Registrado por y cuándo | Aprobador | Reversión | Impuesto | Estado del período |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SAP S/4HANA | Sí | Sí | Sí | No | No | Código | Sí |
| SAP ECC | Sí | Sí | Sí | No | Sí | Código e importe | Sí |
| SAP S/4HANA Cloud | Sí | Sí | Sí | No | Sí | No | No |
| Oracle E-Business Suite | Sí | Sí | Sí | Sí | Sí | No | Sí |
| Oracle Fusion | Sí | Sí | Sí | Sí | Sí | No | Sí |
| Dynamics 365 Finance and Operations | Sí | Sí | Sí | No | No | No | Sí |
| Business Central | Sí | Sí | Sí | No | Sí | No | Sí |
| Sage 100 | No | No | No | No | No | No | Cerrado una vez que termina el período |
| Sage Intacct | Sí | Sí | Sí | Sí | Sí | No | Sí |
| QuickBooks Online | Sí | Sí | Sí | No | No | No | La fecha de cierre de libros |
| Xero | Sí | Sí | Solo cuándo | No | No | No | La fecha de bloqueo |
| Workday | Sí | Sí | Sí | Sí | Sí | Código e importe | Sí |
| NetSuite | Sí | Sí | Sí | No | No | No | Sí |

SAP S/4HANA Cloud lee quién registró un asiento y qué revierte a partir del servicio Journal Entry; Sage Intacct, a partir de los lotes de asientos, y Oracle E-Business Suite lee el aprobador a partir de `GL_JE_BATCHES`. Una conexión que no puede leerlos deja esas columnas vacías.

## Temas relacionados

- [Data Foundation](/es/guides/projects/data-foundation/)
- [Primeros pasos con Data Foundation](/es/guides/projects/data-foundation-getting-started/)
- [Agregar archivos para datos que no están en su ERP](/es/guides/projects/data-foundation/#agregar-archivos-para-datos-fuera-de-su-erp)
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
  - [Sage 100](/es/guides/connections/sage-100/)
  - [Sage Intacct](/es/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/es/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/es/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/es/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/es/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/es/guides/connections/anaplan/#anaplan-como-origen-de-data-foundation)
