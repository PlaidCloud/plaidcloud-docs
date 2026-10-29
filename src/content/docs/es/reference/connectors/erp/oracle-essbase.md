---
title: Conector de Oracle Essbase
description: Conecte PlaidCloud a Oracle Essbase 21c o a Oracle Analytics Cloud con una cuenta de servicio para ejecutar consultas MDX en vivo sobre cubos de Essbase desde un flujo de trabajo.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-essbase.md
---

## Documentación de la API

Este conector se comunica con la [API REST de Oracle Essbase](https://docs.oracle.com/en/database/other-databases/essbase/), los mismos puntos de conexión `grid/mdx`, de aplicación, de base de datos y de estructura que Oracle documenta para Essbase 21c y Oracle Analytics Cloud (OAC).

## A qué se conecta

Oracle Essbase **21c o posterior** y Essbase de Oracle Analytics Cloud (OAC). Estas versiones exponen Essbase mediante una API REST documentada, que es la que invoca PlaidCloud. Las versiones locales de Essbase anteriores a REST **no son compatibles**: no existe una ruta mediante la API de Java heredada ni un cliente de cuadrícula.

Una vez creada la conexión, el paso [Essbase: consultar cubo](/es/reference/workflow-steps/essbase/essbase-query/) ejecuta MDX en vivo sobre un cubo y carga la cuadrícula de resultados en una tabla, y el paso [Essbase: leer dimensión](/es/reference/workflow-steps/essbase/essbase-dimension-read/) carga la estructura de una dimensión en una dimensión de PlaidCloud.

## Cómo funciona la autenticación

La conexión se autentica con el nombre de usuario y la contraseña de una cuenta de servicio mediante HTTP Basic. El aprovisionamiento de esa cuenta en Essbase controla qué aplicaciones y cubos puede ver y consultar, así que concédale acceso de lectura exactamente a las aplicaciones que desea consultar y nada más.

## Configuración

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| URL base | Texto | El origen del servidor de Essbase, por ejemplo `https://your-host:9001`. Introduzca solo el origen, sin la ruta final `/essbase/...`. |
| Aplicación predeterminada | Texto *(opcional)* | Preselecciona esta aplicación en el formulario del paso Essbase: consultar cubo. |
| Nombre de usuario | Texto | Usuario de la cuenta de servicio para la autenticación HTTP Basic. |
| Contraseña | Texto | Contraseña de la cuenta de servicio. Se almacena cifrada. |
| Verificar SSL | Interruptor | Activado de forma predeterminada. Desactívelo solo para un host con un certificado autofirmado o que no se pueda verificar. |

## Probar la conexión

Use **Probar conexión** en el editor de conexiones. Una prueba correcta llega al servidor de Essbase, enumera las aplicaciones que la cuenta de servicio puede ver e informa de cuántas encontró, lo que confirma tanto la URL base como las credenciales antes de crear una consulta.

## Temas relacionados

- [Essbase: consultar cubo](/es/reference/workflow-steps/essbase/essbase-query/): ejecute una consulta MDX en vivo sobre un cubo y cargue el resultado en una tabla.
- [Essbase: leer dimensión](/es/reference/workflow-steps/essbase/essbase-dimension-read/): cargue la estructura de una dimensión en una dimensión de PlaidCloud.
- [Pasos de Oracle Essbase](/es/reference/workflow-steps/essbase/)
- [Conectarse a Oracle Essbase (guía)](/es/guides/connections/essbase/)
- [Crear y administrar una conexión](/es/guides/connections/create-connection/)
