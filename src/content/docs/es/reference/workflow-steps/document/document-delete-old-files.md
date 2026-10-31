---
title: Delete Old Files
description: Elimine los archivos de una cuenta de documentos que sean más antiguos o más recientes que una antigüedad elegida, con un listado de prueba antes de quitar nada.
sidebar:
  order: 23
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-delete-old-files.md
---

import { Aside } from '@astrojs/starlight/components';

## Descripción

Elimina archivos de una cuenta de documentos según su antigüedad. Úselo para evitar que una carpeta de exportación o de recepción crezca sin límite: descarte los extractos de ayer o limpie los archivos de más de un año.

## Configuración

### Archivos que eliminar

- **Ruta del archivo**: la cuenta de documentos y la carpeta en las que se trabaja.
- **Antigüedad**: un número más una unidad: minutos, horas, días, meses o años.
- **Antes o después**: elimina los archivos modificados por última vez **antes** de la fecha límite (el sentido habitual de limpieza) o **después** de ella.
- **Recursivo**: desactivado de forma predeterminada. Actívelo para incluir las subcarpetas.
- **Tabla de resultados de la prueba**: la tabla en la que el botón **Probar** del editor del paso escribe
  su vista previa de los archivos coincidentes.

<Aside type="caution" title="Vista previa con Probar, no ejecutando el paso">
  La vista previa procede del botón **Probar** mientras edita el paso.
  Ejecutar el paso en un flujo de trabajo siempre elimina: no hay modo de prueba
  y la tabla de resultados de la prueba no lo desvía. La eliminación no es reversible,
  y una ruta incorrecta con **Recursivo** activado llega más lejos de lo que cabe esperar, así que revise la
  vista previa antes de programar el paso.
</Aside>

## Relacionado

- [Pasos de documento](/es/reference/workflow-steps/document/)
- [Delete Document File](/es/reference/workflow-steps/document/delete-document-file/)
- [Directory Listing](/es/reference/workflow-steps/document/directory-listing/)
