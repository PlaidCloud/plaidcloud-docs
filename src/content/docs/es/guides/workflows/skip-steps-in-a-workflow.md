---
title: Omitir pasos en un flujo de trabajo
description: Omita pasos específicos de un flujo de trabajo de PlaidCloud para evitar operaciones durante las pruebas, la depuración o las ejecuciones de procesamiento selectivas.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/skip-steps-in-a-workflow.md
---

Los pasos del flujo de trabajo se pueden configurar para que se omitan durante la ejecución. Esto puede resultar útil si hay pasos de depuración o pasos antiguos que aún no está preparado para eliminar por completo del flujo de trabajo.

Para establecer esta opción, desmarque la casilla **Habilitado** del paso en la tabla del flujo de trabajo. El cambio se guarda en cuanto hace clic, sin necesidad de un Guardar aparte. El paso dejará de ejecutarse como parte del flujo de trabajo, pero aún se puede ejecutar mediante el proceso de ejecución de un solo paso.



Los pasos que se han configurado como deshabilitados muestran un indicador de deshabilitado en la tabla de la jerarquía de pasos del flujo de trabajo.
