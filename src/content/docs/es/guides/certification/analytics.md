---
title: Ruta de aprendizaje de Analítica
description: Qué leer antes de los laboratorios Profesional y Experto de Analítica de PlaidCloud, y qué le pide cada laboratorio.
sidebar:
  label: Analítica
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/analytics.md
---

La ruta de Analítica trata de métricas que dan una única respuesta correcta sea cual sea el desglose, y de significados compartidos entre tablas. Empiece por la ruta de [Fundamentos](/es/guides/certification/foundations/). Para saber cómo funcionan los laboratorios, consulte [Certificación de PlaidCloud](/es/guides/certification/).

## Profesional

### Lea en este orden

1. [Ejecutar un flujo de trabajo](/es/guides/workflows/run-a-workflow/)
2. [Ver el registro del flujo de trabajo](/es/guides/workflows/viewing-workflow-log/)
3. [Definiciones de métricas](/es/integrations/ai-coding-agents/metric-definitions/), incluido cómo derivar una métrica de otras
4. [Crear un panel de control a partir de una tabla publicada](/es/get-started/tutorials/build-a-dashboard/), para el panel de control opcional

### Qué le pide el laboratorio

El laboratorio se llama *Analítica: definir métricas para tres preguntas*.

Usted ejecuta un flujo de trabajo que prepara una tabla de ventas y después define métricas sobre esa tabla, cada una con región y canal en su granularidad: ingresos por región, valor promedio del pedido por canal, derivado de un recuento de pedidos, y costo como porcentaje de los ingresos por región, derivado de una métrica de costo. Cada métrica se construye sobre la tabla preparada, no sobre la tabla sin procesar. Un panel de control con las tres respuestas es un buen siguiente paso, pero no se califica.

El laboratorio comprueba que el flujo de trabajo se ejecuta y que cada una de las tres métricas da la respuesta correcta.

## Experto

El laboratorio Experto tiene tiempo límite: dispone de 4 horas desde el momento en que lo inicia.

### Lea en este orden

1. [Definiciones de métricas](/es/integrations/ai-coding-agents/metric-definitions/)
2. [Modelo de datos y elementos del proyecto](/es/guides/projects/data-model/)
3. [Rutas de análisis](/es/integrations/ai-coding-agents/analysis-paths/)

### Qué le pide el laboratorio

El laboratorio se llama *Analítica Experto: métricas que coinciden*.

Dos métricas dan respuestas distintas según cómo se desglosan, y el total de ingresos es mayor que la suma de los pedidos. Usted las repara para que cada una devuelva una única respuesta correcta por región y por producto, conservando sus nombres. Después convierte las columnas que significan lo mismo en un elemento compartido: uno para región, en todas las tablas que la contienen con nombres de columna distintos, y otro para producto.

El laboratorio comprueba que el flujo de trabajo se ejecuta, que los ingresos por región y por producto y las unidades por producto son correctos, y que los elementos abarcan las columnas correctas.
