---
title: Resultados de asignación
description: "Analice los resultados de las asignaciones de PlaidCloud: revise los datos de salida, verifique las distribuciones y valide la exactitud de la asignación."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/allocation-results.md
---

Después de ejecutar un paso de asignación, la salida es una tabla de resultados que usted puede inspeccionar, verificar y utilizar en los pasos posteriores.

## Qué contiene la tabla de resultados

Una fila de resultado de asignación típica incluye:

- **Identificador de origen** — la fila de la tabla de origen de la que proviene esta asignación
- **Identificador de destino** — la fila de la dimensión o tabla de destino que recibió la distribución
- **Monto asignado** — la parte del monto de origen asignada a este destino
- **Valor del inductor** — el número del inductor que justificó la distribución (por ejemplo, el número de empleados, los ingresos, las horas)
- **Tasa de asignación** — la participación del inductor como proporción del total
- **Monto de origen** — el total original que se distribuye (se conserva para fines de auditoría)
- **Referencia de conjunto / etiqueta / regla** — si se usó el etiquetado basado en reglas, la regla que generó esta fila

Las columnas exactas dependen del tipo de paso de asignación y de su configuración.

## Lista de verificación

Antes de confiar en los resultados:

1. **Conciliación** — la suma de los montos asignados es igual a la suma de los montos de origen (dentro de la tolerancia de punto flotante). Si no es así, algo no se distribuyó.
2. **Sin filas de origen huérfanas** — cada fila de origen generó al menos una fila de asignación. Las filas huérfanas suelen indicar que ningún dato de inductor coincidió con la etiqueta o el miembro de dimensión del origen.
3. **Sin destinos huérfanos** — si esperaba que todos los destinos recibieran algo, compruebe que cada miembro de la dimensión de destino aparezca en los resultados.
4. **Tasas razonables** — las tasas de asignación deben sumar 1.0 (100%) por conjunto de origen. Las tasas muy alejadas de ese valor indican problemas en los datos de los inductores.
5. **Comprobación puntual de totales** — elija una fila de origen de alto valor y verifique que su asignación coincida con lo que calcularía a mano.

## Patrones comunes que debe buscar

- **Asignaciones en cero** — un destino que no recibió nada suele significar que faltaba la fila del inductor o que tenía un valor cero
- **Concentración masiva** — que la mayor parte de la distribución recaiga en un solo destino suele significar que la columna del inductor tiene un valor muy grande (a menudo un problema de calidad de datos en un paso anterior)
- **Inductores negativos** — según el paso de asignación, los valores negativos de los inductores pueden producir distribuciones invertidas. Verifique que sea lo que pretende.

## Pasos siguientes

- [Analizar asignaciones con un agente de IA](/es/guides/allocations/results/analyzing-allocations-with-ai/) — pregunte, mediante MCP, por qué cambió un resultado, qué lo determina y qué efecto tendría un cambio
- [Solución de problemas de asignaciones](/es/guides/allocations/results/troubleshooting-allocations/) — qué hacer cuando falla la conciliación
- [Publicar datos](/es/guides/data/publish/) — cuando confíe en los resultados, publíquelos para los paneles de control y otros consumidores posteriores
