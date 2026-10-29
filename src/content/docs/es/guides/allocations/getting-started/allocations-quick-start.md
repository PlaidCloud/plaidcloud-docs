---
title: Inicio rápido de asignaciones
description: Configure rápidamente una asignación de costos básica en PlaidCloud con esta guía paso a paso que abarca orígenes, inductores y asignación de destinos.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/allocations-quick-start.md
---

Este tutorial le lleva de los datos de costos sin procesar a un modelo de asignación funcional en unos 30 minutos.

## Qué necesitará

- Un proyecto con al menos dos tablas:
  - **Valores que asignar**: los costos (o ingresos, o volúmenes) que desea distribuir. Una fila por unidad de origen y una columna con el importe.
  - **Datos de inductores**: la base para distribuir. Número de empleados, superficie en metros cuadrados, recuentos de transacciones, ingresos; lo que sea *según* lo cual quiera asignar.
- Una dimensión que vincule el origen y el destino (centros de costo, departamentos, productos: la taxonomía que se ajuste a su modelo).

Si aún no tiene todo eso, las guías [Tablas y vistas](/es/guides/data/) y [Dimensiones](/es/guides/dimensions/) explican cómo cargar los datos de entrada.

## Pasos

1. **Abra el proyecto** que contiene sus tablas de valores e inductores.
2. **Cree un flujo de trabajo nuevo.** Las asignaciones siempre se ejecutan dentro de un flujo de trabajo; no operan directamente sobre las tablas fuera de uno.
3. **Agregue un paso de asignación.** Dentro del flujo de trabajo, agregue un paso de la categoría **Allocation**. El punto de partida más habitual es **Allocation Rules**, para una distribución sencilla basada en inductores.
4. **Configure el origen.** Apunte el paso a su tabla de valores y elija la columna que contiene el importe que se va a asignar.
5. **Configure el inductor.** Apunte el paso a la tabla de inductores y elija la columna que contiene los valores del inductor.
6. **Asigne la dimensión.** Identifique qué columna de cada tabla representa los miembros de la dimensión. El paso de asignación las usa para hacer coincidir las filas de origen con las filas de inductores.
7. **Ejecute el paso.** El resultado es una tabla nueva con una fila por cada importe distribuido.
8. **Inspeccione los resultados.** Compruebe que los totales coinciden con lo esperado: la suma de los importes asignados debe ser igual a la suma de los importes de origen (dentro de la tolerancia de redondeo).

## Siguientes pasos habituales

- **Distribuir de forma recursiva**: si un destino contiene a su vez inductores para otra asignación, consulte [Asignaciones recursivas](/es/guides/allocations/setup/recursive-allocations/).
- **Etiquetar filas para la asignación**: para controlar *qué* filas se asignan a qué destinos, consulte [Etiquetado basado en reglas](/es/guides/allocations/getting-started/rule-based-tagging/).
- **Investigar resultados inesperados**: si los totales no cuadran o algunas filas parecen incorrectas, consulte [Solución de problemas de asignaciones](/es/guides/allocations/results/troubleshooting-allocations/).

## Pasos siguientes

- [¿Por qué son útiles las asignaciones?](/es/guides/allocations/getting-started/why-are-allocations-useful/): cuándo usarlas
- [Configurar una asignación](/es/guides/allocations/setup/configure-an-allocation/): referencia de configuración más detallada
- [Tipos de pasos de asignación](/es/reference/workflow-steps/allocation/): todos los pasos de flujo de trabajo de la categoría Allocation
