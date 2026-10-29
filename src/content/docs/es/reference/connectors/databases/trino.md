---
title: Trino
description: Configure una conexión al motor de consultas distribuido Trino en PlaidCloud para ejecutar consultas federadas en varios orígenes de datos.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/trino.md
---

**Trino** (antes PrestoSQL) es el motor de consultas SQL distribuido que se usa habitualmente sobre data lakes. Use este conector para consultar implementaciones de Trino desde los flujos de trabajo de PlaidCloud. La autenticación usa HTTP Basic Auth o JWT; el catálogo y el esquema de destino determinan a qué origen de datos subyacente accede la consulta.

## Documentación del proveedor
[La documentación de Trino](https://trino.io/docs/current/index.html).

## Configuración

Este conector usa un flujo de autenticación específico del proveedor y se configura directamente desde la pantalla **Conexiones** de su espacio de trabajo. Los campos de configuración que se muestran dependen de las credenciales que el administrador de su inquilino haya aprovisionado para la integración.

Consulte la [documentación de Trino](https://trino.io/docs/current/) del proveedor para conocer los detalles de configuración más recientes.

Si necesita ayuda para configurar este conector en su inquilino, comuníquese con su equipo de cuenta: las credenciales específicas del conector, las URL del entorno y cualquier aprovisionamiento previo necesario normalmente deben coordinarse con el soporte de PlaidCloud.
