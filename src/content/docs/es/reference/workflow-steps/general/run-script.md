---
title: Ejecutar operación de aplicación
description: Invoque desde un flujo de trabajo una operación de aplicación registrada, con la posibilidad de pasar una ruta de documento y parámetros.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/run-script.md
---

## Descripción

Invoca una operación de aplicación registrada desde un flujo de trabajo. Úsela para desencadenar trabajo de la plataforma que no es una transformación de datos: las operaciones que una aplicación expone para su automatización.

## Configuración

### Operación de aplicación que se ejecutará

La operación que se invocará.

### Ruta del archivo

Para las operaciones que reciben un archivo:

- **Directorio de documentos**: la cuenta de documentos y la ruta que se pasarán.
- **Nombre del parámetro de archivo**: el parámetro con el que la operación espera la ruta. El valor predeterminado es `document_path`; cámbielo solo si la operación lo nombra de otra manera.

### Parámetros opcionales

Pares nombre/valor que se pasan a la operación junto con la ruta del archivo.

## Relacionado

- [Pasos generales](/es/reference/workflow-steps/general/)
- [User Defined Transform](/es/reference/workflow-steps/general/user-defined-transform/)
- [Run Remote Python](/es/reference/workflow-steps/general/run-remote-python/)
