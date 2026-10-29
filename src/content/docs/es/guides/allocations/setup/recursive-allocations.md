---
title: Asignaciones recursivas y recíprocas
description: Modele la distribución de costos en varias pasadas y recíproca en PlaidCloud encadenando pasos de asignación en pasadas escalonadas explícitas.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/recursive-allocations.md
---

Algunos modelos de costos necesitan que el destino de una asignación se convierta en el *origen* de la siguiente; por ejemplo, servicios compartidos que se consumen entre sí (TI atiende a RR. HH., pero RR. HH. también atiende a TI). PlaidCloud lo modela **encadenando pasos de asignación en pasadas escalonadas explícitas**, no mediante un único solucionador automático.

## Cuándo necesita varias pasadas

- **Servicios recíprocos**: dos grupos de costos que se consumen entre sí.
- **Reparto por capas**: los costos divisionales se propagan por una jerarquía, y los niveles inferiores deben absorber los superiores antes de volver a asignar.
- **Equilibrio iterativo**: el modelo se acerca a un resultado estable tras varias pasadas (el grupo A asigna una parte a B, B devuelve una parte, y así sucesivamente).

## Cómo modelarlo

PlaidCloud **no tiene un “modo de recursión” integrado ni un solucionador de convergencia automático**. Usted construye la recursión agregando un [paso de división de asignación](/es/reference/workflow-steps/allocation/allocation-split/) distinto para cada pasada y conectándolos en secuencia:

1. Ejecute la primera pasada como una división de asignación normal.
2. Para la siguiente pasada, construya un origen que incluya la salida de la pasada anterior (normalmente uniendo o combinando el resultado previo con el grupo) y vuelva a asignar.
3. Repita tantas pasadas como necesite su modelo.

Como cada pasada es un paso explícito, **usted decide cuántas pasadas se ejecutan**. El motor no resuelve la relación recíproca como una única ecuación simultánea, y no hay ningún ajuste de tolerancia que detenga el bucle automáticamente. Agregue pasadas hasta que el residuo que aún queda por reasignar sea lo bastante pequeño para sus fines.

## Consejos

- Empiece con una asignación de **una sola pasada** y confirme que el modelo simple se comporta como se espera antes de agregar pasadas.
- Después de cada pasada, revise el residuo sin asignar que queda. Si no disminuye de una pasada a otra, revise las relaciones de los inductores: una dependencia circular genuina no se estabilizará por muchas pasadas que agregue.
- Cada pasada vuelve a procesar su origen, por lo que la recursión es costosa en conjuntos de datos grandes. Pruebe con una porción antes de ejecutar sobre el origen completo.

## Temas relacionados

- [Configurar una asignación](/es/guides/allocations/setup/configure-an-allocation/): configuración base
- [Paso Allocation Split](/es/reference/workflow-steps/allocation/allocation-split/): el paso de flujo de trabajo que encadena en cada pasada
- [Solución de problemas de asignaciones](/es/guides/allocations/results/troubleshooting-allocations/): cuando los residuos no tienen sentido
