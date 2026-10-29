---
title: Conector REST de Sage Intacct
description: Configure una conexión a la API REST de Sage Intacct en PlaidCloud para integrar datos financieros y contables en sus flujos de trabajo.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/sage-intacct.md
---

## Documentación de la API

La documentación de la API REST de Sage Intacct está disponible en el [sitio para desarrolladores de Sage](https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started/quick-start).


## Requisitos de seguridad

PlaidCloud ofrece una conexión **Intacct** dedicada dentro de la familia de conexiones REST (que aparece como **REST - Intacct**). Se autentica con credenciales de cliente OAuth2 contra la API REST de Intacct: el par de ID de remitente y contraseña de remitente de **Web Services** de Sage Intacct se introducen como **ID de cliente** y **Secreto de cliente** de la conexión, además de un nombre de usuario del servicio web y un ID de empresa. El soporte de Sage debe habilitar las credenciales de remitente para su empresa; el usuario de Web Services debe tener permisos para cada objeto de Intacct que lea el conector.

Trate el ID de cliente y el secreto de cliente como secretos: almacénelos únicamente en el área **Credenciales** de PlaidCloud y haga referencia a ellos desde la conexión.


## Obtener las credenciales

1. Abra el área **Company Setup** de Sage Intacct
2. Habilite Web Services para el ID de remitente que proporciona Sage
3. Cree o seleccione un usuario de Web Services para PlaidCloud
4. Conceda al usuario permisos sobre cada objeto que tenga previsto consultar
5. Anote el ID de empresa, el nombre de usuario del servicio web, el ID de remitente y la contraseña de remitente


## Crear el conector de Sage Intacct

1. Vaya a **Herramientas > Conexiones** y haga clic en `Add Connection`
2. En **REST**, seleccione **Intacct** (que aparece como **REST - Intacct**)
3. Introduzca:
    * **Nombre de la conexión** — nombre descriptivo que se muestra en los pasos del flujo de trabajo
    * **ID de cliente** — su ID de remitente de Intacct
    * **Secreto de cliente** — su contraseña de remitente de Intacct
    * **Nombre de usuario del servicio web** — el inicio de sesión del usuario de Web Services
    * **ID de empresa** — la empresa de Intacct a la que se conecta
4. Haga clic en `Test` para validar las credenciales
5. Haga clic en `Save`


## Usar en pasos del flujo de trabajo

La misma conexión sirve tanto para leer de Intacct como para contabilizar en él. Se puede seleccionar desde:

* [Import Sage AP (paso)](../../../workflow-steps/sage-intacct/import-sage-ap/) — encabezados de facturas de cuentas por pagar
* [Import Sage AP Lines (paso)](../../../workflow-steps/sage-intacct/import-sage-ap-lines/) — detalle de las líneas de facturas de cuentas por pagar
* [Import Sage Intacct Query (paso)](../../../workflow-steps/sage-intacct/import-intacct-query/) — consulta genérica sobre cualquier objeto de Intacct
* [Import Intacct Entity (paso)](../../../workflow-steps/sage-intacct/import-intacct-entity/) — detalle del libro mayor, saldos, asientos y maestros de dimensiones, con paginación automática
* [Intacct: contabilizar asiento de diario](../../../workflow-steps/sage-intacct/export-to-sage/) — contabilizar asientos de diario
