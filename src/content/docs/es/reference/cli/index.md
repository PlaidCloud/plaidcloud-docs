---
title: Herramientas de CLI
description: "Referencia de las herramientas de línea de comandos de PlaidCloud: el agente PlaidLink, el complemento PlaidXL para Excel y la CLI de Jupyter para la integración con cuadernos."
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloud ofrece tres herramientas de línea de comandos y de instalación local para trabajar con los espacios de trabajo fuera de la interfaz web:

## PlaidLink

[PlaidLink](/es/reference/cli/plaidlink/) es un agente que se ejecuta dentro de su red para conectar los flujos de trabajo de PlaidCloud con recursos protegidos por un cortafuegos, como bases de datos, recursos compartidos de archivos y otros sistemas a los que PlaidCloud no puede acceder directamente. Se instala como servicio de Windows, daemon de Unix/Linux/Mac, contenedor o pod de Kubernetes.

- [Instalar](/es/reference/cli/plaidlink/install/)
- [Configurar](/es/reference/cli/plaidlink/configure/)
- [Agentes](/es/reference/cli/plaidlink/agents/)
- [Actualizar](/es/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/es/reference/cli/plaidxl/) es el complemento de PlaidCloud para Microsoft Excel. Recupera tablas y dimensiones de proyecto en hojas de cálculo, las actualiza cuando usted lo pide, agrega fórmulas `PLAIDXL` que calculan valores acumulados y métricas gobernadas a partir de los datos de PlaidCloud, y escribe de vuelta los valores planificados.

- [Instalar](/es/reference/cli/plaidxl/install/)
- [Iniciar sesión](/es/reference/cli/plaidxl/connect/)
- [Trabajar con tablas y dimensiones](/es/reference/cli/plaidxl/retrieve/)
- [Funciones personalizadas](/es/reference/cli/plaidxl/functions/)
- [Crear un informe](/es/reference/cli/plaidxl/build-a-report/)
- [Desglosar, elegir miembros y explicar números](/es/reference/cli/plaidxl/drill/)
- [Escribir valores en PlaidCloud](/es/reference/cli/plaidxl/write-values/)
- [Preguntar a Weave en Excel](/es/reference/cli/plaidxl/weave/)
- [La cinta de PlaidCloud](/es/reference/cli/plaidxl/ribbon/)
- [Solución de problemas](/es/reference/cli/plaidxl/troubleshooting/)

## CLI de Jupyter

La [CLI de Jupyter](/es/reference/cli/jupyter/) permite a los científicos de datos trabajar con los datos de proyecto de PlaidCloud desde cuadernos de Jupyter mediante una CLI compatible con PlaidCloud y utilidades de Python.

- [Línea de comandos](/es/reference/cli/jupyter/command-line/)
- [Cuaderno de Jupyter](/es/reference/cli/jupyter/jupyter-notebook/)
- [Configuración de OAuth](/es/reference/cli/jupyter/oauth-setup/)
