---
title: Expresiones de Lakehouse v1
description: Expresiones de Lakehouse v1 basadas en las funciones SQL de Databend, con referencias de SQLAlchemy que usan el prefijo func.
sidebar:
  label: Lakehouse v1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/index.md
---

Lakehouse v1 está construido sobre el motor SQL [Databend](https://databend.com/). Para cada función que aparece a continuación, este sitio ofrece la sintaxis y los ejemplos adaptados a PlaidCloud; para la referencia original completa (con todos los casos límite y variantes de argumentos), consulte la **[referencia de funciones SQL de Databend](https://docs.databend.com/sql/sql-functions/)**.

## Funciones escalares

- [Funciones de matriz](./00-array-functions): realizan operaciones con matrices
- [Funciones de expresiones bit a bit](./01-bitmap-functions): realizan operaciones y manipulaciones bit a bit
- [Funciones de expresiones condicionales](./03-conditional-functions): implementan lógica condicional y sentencias case
- [Funciones de contexto](./15-context-functions): proporcionan información sobre el contexto de ejecución SQL actual
- [Funciones de conversión](./02-conversion-functions): convierten tipos de datos y transforman valores
- [Funciones de fecha y hora](./05-datetime-functions): manipulan y dan formato a fechas y horas
- [Funciones geoespaciales](./09-geo-functions): gestionan y manipulan datos geoespaciales
- [Funciones de geometría](./09-geometry-functions): gestionan y manipulan datos de geometría geoespacial
- [Funciones de intervalo](./05-interval-functions): crean y manipulan intervalos de tiempo
- [Funciones de mapa](./10-map-functions): crean y manipulan estructuras de datos de tipo mapa
- [Funciones numéricas](./04-numeric-functions): realizan cálculos y operaciones numéricas
- [Funciones de búsqueda](./10-search-functions): encuentran valores mediante expresiones
- [Funciones de datos semiestructurados y estructurados](./10-semi-structured-functions): trabajan con JSON y otros formatos de datos estructurados
- [Funciones de cadena](./06-string-functions): manipulan cadenas y realizan operaciones con expresiones regulares

## Funciones de agregación

- [Funciones de agregación](./07-aggregate-functions): calculan resúmenes como suma, promedio, recuento, etc.
- [Funciones de ventana](./08-window-functions): proporcionan cálculos de agregación sobre un intervalo de filas especificado

## Funciones de IA

- [Funciones de IA](./11-ai-functions): aprovechan las capacidades de IA y aprendizaje automático

## Funciones especializadas

- [Funciones hash](./12-hash-functions): generan valores hash para la seguridad y la comparación de datos
- [Funciones de dirección IP](./14-ip-address-functions): manipulan y analizan datos de direcciones IP
- [Funciones UUID](./13-uuid-functions): generan y manipulan UUID

## Funciones de sistema y de tabla

- [Funciones de secuencia](./18-sequence-functions): generan valores secuenciales
- [Funciones del sistema](./16-system-functions): acceden a información a nivel de sistema y realizan operaciones de control
- [Funciones de tabla](./17-table-functions): devuelven resultados en formato tabular

## Otras funciones

- [Funciones de diccionario](./19-dictionary-functions): trabajan con estructuras de datos de diccionario
- [Otras funciones diversas](./20-other-functions): una colección de otras funciones variadas
- [Funciones de prueba](./19-test-functions): funciones que se usan con fines de prueba
