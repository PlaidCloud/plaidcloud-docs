---
title: Por qué son útiles las asignaciones
description: Descubra por qué las asignaciones de costos son útiles en PlaidCloud para el costeo basado en actividades, el cargo interno y el análisis de rentabilidad.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/why-are-allocations-useful.md
---

Las asignaciones distribuyen un conjunto de valores (normalmente costos, aunque sirve para cualquier agregado) entre los consumidores según un inductor medible. Responden a la pregunta: *si incurrimos en este costo, ¿cómo debe asignarse a lo que lo consume?*

## Casos de uso comunes

### Costeo basado en actividades

Usted conoce su gasto total de marketing de un trimestre. Quiere atribuirlo a productos específicos según algo medible: horas de campaña, clientes potenciales generados, oportunidades calificadas. Una asignación distribuye el conjunto de marketing entre los productos con el inductor que usted elija y le da a cada producto un costo completamente cargado.

### Cargo interno de TI

Usted gasta $X en operar infraestructura compartida (cómputo, almacenamiento, licencias). Cada unidad de negocio consume una cantidad distinta. Una asignación distribuye el costo de TI entre las unidades según métricas de uso (horas de VM, GB de almacenamiento, licencias de usuario), de modo que el estado de pérdidas y ganancias de cada unidad refleje lo que realmente consumió.

### Distribución de servicios compartidos

Finanzas, recursos humanos, asuntos legales, instalaciones: funciones centrales que atienden a toda la empresa. Las asignaciones distribuyen su costo entre las divisiones a las que prestan servicio, normalmente según el número de empleados, los ingresos o una combinación ponderada.

### Precios de transferencia

En organizaciones con varias entidades, las asignaciones modelan cómo se fijan los precios de los servicios internos entre entidades. El resultado alimenta los asientos de diario entre empresas del grupo.

### Análisis de rentabilidad

Usted tiene ingresos a nivel de producto o de cliente. Tiene costos en varios conjuntos (ventas, soporte, infraestructura, costo de ventas). Las asignaciones reúnen todo al nivel de detalle de producto o cliente para que pueda ver el margen real.

### Costeo de la lista de materiales

El costo fluye hacia abajo por una jerarquía de componentes. Cada paso de la lista de materiales es una asignación: los costos de los subensambles se distribuyen a los ensambles, los ensambles a los productos terminados y los productos terminados a los SKU.

## De qué le libran las asignaciones

Sin un motor de asignaciones, estos modelos se construirían en hojas de cálculo: frágiles, difíciles de auditar y difíciles de repetir con datos actualizados. Las asignaciones de PlaidCloud le ofrecen:

- **Modelos reproducibles** que se vuelven a ejecutar automáticamente cuando se actualizan los datos de origen
- **Pista de auditoría** que muestra qué filas de origen contribuyeron a qué filas de destino
- **Asignaciones en capas**, donde los resultados alimentan otras asignaciones
- **Integración dimensional** para que las asignaciones respeten sus jerarquías existentes

## Pasos siguientes

- [Inicio rápido de asignaciones](/es/guides/allocations/getting-started/allocations-quick-start/) — cree una en 30 minutos
- [Etiquetado basado en reglas](/es/guides/allocations/getting-started/rule-based-tagging/) — controle el comportamiento de la asignación por fila
- [Configurar una asignación](/es/guides/allocations/setup/configure-an-allocation/) — referencia completa de configuración
