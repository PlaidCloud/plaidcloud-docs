---
title: Explorador de flujos de trabajo
description: Use el Explorador de flujos de trabajo de PlaidCloud para ver los detalles del flujo de trabajo, las configuraciones de los pasos, el historial de ejecuciones y la información de dependencias.
sidebar:
  order: 1.1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/workflow-explorer.md
---

Para ver los detalles dentro de un flujo de trabajo, búsquelo en el proyecto y haga doble clic en él para abrirlo en el explorador.

![Explorador de flujos de trabajo](/images/workflow_explorer.png)

Desde aquí puede administrar los pasos del flujo de trabajo, lo que incluye crear o modificar pasos existentes, cambiar el orden, ejecutar pasos, etcétera.

## Crear un paso

Haga clic en **Crear paso** y elija un tipo de paso. Si hay un paso seleccionado en la lista, un paso nuevo Table Extract, Table Inner Join, Table Outer Join, Table Anti Join, Table Cross Join o Table Lookup parte de la tabla que escribe ese paso: pasa a ser el origen del paso nuevo (**Table 1** en una combinación) y las columnas se rellenan como lo haría **Inspeccionar origen**. Una nota al pie del formulario lo indica. Cambie el origen si el paso nuevo debe leer otra cosa. No se guarda nada hasta que guarde el paso.
