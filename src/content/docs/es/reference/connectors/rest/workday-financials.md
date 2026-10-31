---
title: Conector de Workday Financials
description: Configure una conexión de Workday Financials en PlaidCloud con un usuario del sistema de integración para importar datos mediante un informe RaaS y contabilizar asientos de diario por SOAP.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday-financials.md
---

## Documentación de la API

Los [servicios web SOAP](https://community.workday.com/sites/default/files/file-hosting/productionapi/) de Workday y [Report-as-a-Service (RaaS)](https://doc.workday.com/) documentan las interfaces que utiliza este conector.

## Cómo funciona la autenticación

La conexión se autentica con un **usuario del sistema de integración (ISU)**, un tipo de usuario de Workday creado para la integración entre sistemas, protegido por un grupo de seguridad del sistema de integración que le concede únicamente el acceso que necesita este conector (acceso a informes para las lecturas y el proceso de negocio Submit Accounting Journal para las contabilizaciones). Las solicitudes llevan el nombre de usuario y la contraseña del ISU; no hay inicio de sesión interactivo.

## Configuración

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| Host del tenant | Texto | Su host de Workday, por ejemplo `wd5-impl.workday.com`. |
| Nombre del tenant | Texto | El nombre de su tenant de Workday. |
| Nombre de usuario del ISU | Texto | El nombre de usuario del usuario del sistema de integración. |
| Contraseña del ISU | Texto | La contraseña del usuario del sistema de integración. Se almacena cifrada. |

## Importación de datos

Workday Financials no tiene un conjunto fijo de entidades predefinidas. En su lugar, el paso **Import Workday Entity** llama a un **informe Report-as-a-Service (RaaS)** que usted crea en Workday y publica con acceso a servicios web; usted proporciona su URL. El paso admite filtros sobre `company`, `ledger`, `period`, `accounting_date` (rango), `ledger_account` (rango) y `cost_center`, cada uno transmitido como parámetro del informe, por lo que un filtro solo funciona si su informe define un aviso coincidente. Consulte [Import Workday Entity](/es/reference/workflow-steps/workday-financials/import-workday-entity/) para ver la referencia completa de campos.

## Contabilización de asientos de diario

El paso **Workday Financials: Post Journal Entry** contabiliza asientos contables a través de la canalización de escritura de ERP compartida de PlaidCloud, mediante la operación SOAP `Submit_Accounting_Journal` de Workday, y sondea el estado del proceso de negocio del asiento hasta un estado terminal antes de informar de que se contabilizó. Una corrección contabiliza un nuevo asiento de reversión con débito y crédito intercambiados, en lugar de editar el original. Consulte [Workday Financials: Post Journal Entry](/es/reference/workflow-steps/workday-financials/workday-post/) para ver la referencia de campos y [Conectar con Workday Financials](/es/guides/connections/workday-financials/) para ver el tutorial completo de contabilización.

## Limitaciones conocidas

| Limitación | Qué significa |
|---|---|
| La forma de la importación depende de su informe RaaS | PlaidCloud no tiene entidades predefinidas para Workday Financials: los campos, los avisos y el control de acceso del informe residen en Workday. Un cambio en el informe allí puede cambiar la forma de su importación sin ningún cambio en PlaidCloud. |
| La aprobación del proceso de negocio añade latencia | Un asiento que pasa por un paso de aprobación en su proceso de negocio Submit Accounting Journal permanece `pending` hasta que se aprueba en Workday; el sondeo del estado terminal espera a que eso ocurra. |
## Información relacionada

- [Conectar con Workday Financials (guía)](/es/guides/connections/workday-financials/): paso a paso: cree la conexión, pruébela, importe un informe y contabilice un asiento de diario.
- [Import Workday Entity](/es/reference/workflow-steps/workday-financials/import-workday-entity/)
- [Workday Financials: Post Journal Entry](/es/reference/workflow-steps/workday-financials/workday-post/)
- [Revisar el historial de contabilizaciones de ERP](/es/guides/connections/erp-post-history/)
- [Conector REST de Workday](/es/reference/connectors/rest/workday/): el conector genérico y independiente de Workday para datos REST de RR. HH. y nómina.
