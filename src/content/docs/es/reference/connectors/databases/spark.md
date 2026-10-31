---
title: Apache Spark
description: Configure una conexión a una base de datos Apache Spark en PlaidCloud para ejecutar consultas distribuidas e integrar big data en los flujos de trabajo.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/spark.md
---

**Apache Spark** es el motor de cómputo distribuido que se usa habitualmente para ETL sobre grandes conjuntos de datos. Use este conector para leer y escribir datos mediante puntos de conexión de Spark SQL (normalmente Spark Thrift Server). Para Spark administrado por Databricks, es preferible el conector [Azure Databricks](../azure-databricks/).

## Documentación del proveedor
[La documentación de Apache Spark](https://spark.apache.org/documentation.html).

El [proyecto Apache](https://spark.apache.org/).

## Configuración

Este conector usa un flujo de autenticación específico del proveedor y se configura directamente desde la pantalla **Conexiones** de su espacio de trabajo. Los campos de configuración que se muestran dependen de las credenciales que el administrador de su inquilino haya aprovisionado para la integración.

Consulte la [documentación de Spark](https://spark.apache.org/docs/latest/) del proveedor para conocer los detalles de configuración más recientes.

Si necesita ayuda para configurar este conector en su inquilino, comuníquese con su equipo de cuenta: las credenciales específicas del conector, las URL del entorno y cualquier aprovisionamiento previo necesario normalmente deben coordinarse con el soporte de PlaidCloud.
