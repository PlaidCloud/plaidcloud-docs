---
title: Conector REST de MuleSoft
description: Conecte PlaidCloud a una puerta de enlace de MuleSoft Anypoint y adjunte la definición de la API para que los pasos del flujo de trabajo puedan enumerar sus puntos de conexión.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/mulesoft.md
---

MuleSoft Anypoint es una puerta de enlace de API: se sitúa delante de los servicios que su organización haya publicado detrás de ella, en una dirección específica de su implementación. Por eso, a diferencia de un conector creado para un solo servicio, una conexión de MuleSoft no conoce sus propios puntos de conexión: usted le indica dónde se encuentran la API y su definición.

## Documentación de la API

La documentación de la API de esta conexión es la que documente los servicios que su puerta de enlace tiene detrás.

## Configuración

MuleSoft usa el mismo formulario que la [conexión REST genérica](/es/reference/connectors/rest/generic-rest/): las mismas cuatro pestañas, los mismos campos y el mismo comportamiento en todo momento. Dos son los más importantes aquí:

- **Host o dirección IP** — la dirección de su puerta de enlace de Anypoint. No hay un valor predeterminado, porque una dirección de MuleSoft es específica de su implementación.
- **Tipo de autenticación** — la que espere su puerta de enlace entre `None`, `Basic`, `API Key`, `Bearer Token` u `OAuth 2.0`. No se asume nada por usted.

## Enumerar puntos de conexión en un flujo de trabajo

Como la puerta de enlace no tiene una lista de puntos de conexión integrada, adjunte a la conexión la definición OpenAPI 3.x o Swagger 2.0 de su API en **Definición de la API**: ya sea la dirección en la que está publicada o un archivo `.json` o `.yaml` almacenado en Documentos. Consulte [Definición de la API](/es/reference/connectors/rest/generic-rest/#definición-de-la-api) para ver los campos.

Un [paso Solicitud REST](/es/guides/workflows/rest-request-step/) que use esta conexión puede entonces establecer **Origen de puntos de conexión** en **Desde la definición de API de la conexión** y elegir **Cargar catálogo** para seleccionar entre los puntos de conexión de la API, en lugar de escribir cada ruta a mano.

## Temas relacionados

- [Conexión REST genérica](/es/reference/connectors/rest/generic-rest/) — la referencia completa de campos de este formulario.
- [Crear y administrar una conexión](/es/guides/connections/create-connection/)
- [Paso de flujo de trabajo Solicitud REST](/es/guides/workflows/rest-request-step/)
