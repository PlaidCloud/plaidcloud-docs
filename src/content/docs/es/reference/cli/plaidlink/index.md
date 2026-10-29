---
title: PlaidLink
description: Instale y configure agentes de PlaidLink para acceder de forma segura a sistemas protegidos por firewalls, lo que permite consultas remotas y transferencias de archivos.
sidebar:
  label: PlaidLink
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/index.md
---

PlaidLink proporciona acceso indirecto a los sistemas y procesos de los clientes que están protegidos por firewalls o tras otras restricciones que dificultan las conexiones directas desde PlaidCloud. Mediante un Agente de PlaidCloud instalado dentro del área aislada, PlaidCloud puede solicitar al agente que realice acciones como ejecutar consultas, descargar o cargar archivos, comprobar condiciones de sensores, interactuar con SAP y mucho más.

Como el agente inicia el contacto con PlaidCloud y se comunica mediante protocolos de red HTTPS estándar, normalmente puede funcionar con una configuración mínima. Además, el agente puede ejecutarse como un usuario sin privilegios para controlar los derechos de acceso dentro de un entorno restringido.

## Temas

- [Instalar](/es/reference/cli/plaidlink/install/): cómo poner en marcha PlaidLink en Windows, Linux, macOS o en un contenedor
- [Configurar](/es/reference/cli/plaidlink/configure/): configuración de la conexión, credenciales y opciones de ejecución
- [Agentes](/es/reference/cli/plaidlink/agents/): administración de varios agentes y sus capacidades
- [Actualizar](/es/reference/cli/plaidlink/upgrade/): cómo pasar a una compilación más reciente de PlaidLink
