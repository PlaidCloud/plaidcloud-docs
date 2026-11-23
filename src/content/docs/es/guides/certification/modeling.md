---
title: Ruta de aprendizaje de Modelado
description: Qué leer antes de los laboratorios Profesional y Experto de Modelado de PlaidCloud, y qué le pide cada laboratorio.
sidebar:
  label: Modelado
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/modeling.md
---

La ruta de Modelado trata de dimensiones y asignaciones: construir jerarquías, repartir costos con inductores y comprobar que los resultados cuadran. Empiece por la ruta de [Fundamentos](/es/guides/certification/foundations/). Para saber cómo funcionan los laboratorios, consulte [Certificación de PlaidCloud](/es/guides/certification/).

## Profesional

### Lea en este orden

1. [Introducción a las dimensiones](/es/guides/dimensions/getting-started/)
2. [Administrar jerarquías](/es/guides/projects/managing-hierarchies/)
3. [Diseñar una jerarquía de la dimensión](/es/get-started/tutorials/design-a-dimension/)
4. [Inicio rápido de asignaciones](/es/guides/allocations/getting-started/allocations-quick-start/)
5. [Allocation Split](/es/reference/workflow-steps/allocation/allocation-split/)
6. [Crear un modelo de asignación](/es/get-started/tutorials/build-an-allocation/)
7. [Resultados de la asignación](/es/guides/allocations/results/allocation-results/)
8. [Ver el registro del flujo de trabajo](/es/guides/workflows/viewing-workflow-log/)

### Qué le pide el laboratorio

El laboratorio se llama *Modelado: asignar el costo compartido de TI*.

Una tabla enumera cada departamento y su departamento superior. Usted construye una dimensión cuya jerarquía principal sea exactamente ese árbol. Después, en el flujo de trabajo del laboratorio, asigna un fondo de costos a los departamentos en proporción a su número de empleados, con una fila de resultado por departamento. También hay una segunda tabla de inductores, que no es el inductor de este fondo.

El laboratorio comprueba que el flujo de trabajo se ejecuta, que la jerarquía es correcta, que el total asignado cuadra con el origen y que cada departamento recibe el importe correcto.

## Experto

El laboratorio Experto tiene tiempo límite: dispone de 4 horas desde el momento en que lo inicia.

### Lea en este orden

1. [Configurar una asignación](/es/guides/allocations/setup/configure-an-allocation/)
2. [Solución de problemas de asignaciones](/es/guides/allocations/results/troubleshooting-allocations/)
3. [Rastrear asignaciones con un agente de IA conectado por MCP](/es/integrations/ai-coding-agents/tracing-allocations/)
4. [Resultados de la asignación](/es/guides/allocations/results/allocation-results/)
5. [Probar un escenario hipotético de inductor](/es/guides/allocations/results/driver-what-if/)
6. [Administrar jerarquías](/es/guides/projects/managing-hierarchies/)

### Qué le pide el laboratorio

El laboratorio se llama *Modelado Experto: reparar el modelo de asignación*.

Un modelo de asignación de dos etapas ya no cuadra con el libro mayor y algunos departamentos son claramente incorrectos. Usted rastrea la causa y corrige el modelo: cada etapa asigna exactamente su fondo, los totales por departamento son correctos y suman lo que indica el libro mayor, y la dimensión de departamentos contiene solo los departamentos que existen. No se puede usar ninguna fila de equilibrio para hacer que algo cuadre. Después agrega un paso que muestra cuánto costaría TI a cada departamento si se asignara por superficie en lugar de por número de empleados.

El laboratorio comprueba que el flujo de trabajo se ejecuta, que la jerarquía es correcta, que cada etapa y los totales por departamento cuadran con el libro mayor, que cada departamento recibe el total correcto y que el escenario de superficie es correcto.
