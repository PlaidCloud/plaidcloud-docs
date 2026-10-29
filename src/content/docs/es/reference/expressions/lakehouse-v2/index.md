---
title: Expresiones de Lakehouse v2
description: Expresiones de Lakehouse v2 basadas en las funciones SQL de StarRocks 4.1, con referencias de SQLAlchemy.
sidebar:
  label: Lakehouse v2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/index.md
---

Lakehouse v2 está construido sobre [StarRocks](https://www.starrocks.io/) 4.1. Para cada función que aparece a continuación, este sitio ofrece la sintaxis y los ejemplos adaptados a PlaidCloud; para la referencia original de StarRocks (con todos los casos límite y variantes de argumentos), consulte la **[referencia de funciones SQL de StarRocks](https://docs.starrocks.io/docs/sql-reference/sql-functions/)**.

## Funciones de agregación

- [Funciones de agregación](./01-aggregate-functions) — Calculan resúmenes como suma, promedio, recuento, etc.
- [Funciones de percentil](./15-percentile-functions) — Calculan valores de percentil y administran estados de percentil

## Funciones escalares

- [Funciones de matriz](./02-array-functions) — Realizan operaciones con matrices
- [Funciones binarias](./03-binary-functions) — Convierten entre formatos binarios y de cadena
- [Funciones de bits](./04-bit-functions) — Realizan operaciones bit a bit
- [Funciones de mapa de bits](./05-bitmap-functions) — Realizan operaciones y manipulaciones con mapas de bits
- [Funciones de condición](./06-condition-functions) — Implementan lógica condicional e instrucciones CASE
- [Funciones criptográficas](./07-cryptographic-functions) — Cifran, descifran y generan hash de datos
- [Funciones de fecha y hora](./08-date-time-functions) — Manipulan y dan formato a fechas y horas
- [Funciones de diccionario](./09-dictionary-functions) — Buscan valores en tablas de diccionario
- [Funciones de hash](./10-hash-functions) — Generan valores hash con MurmurHash y xxHash
- [Funciones JSON](./11-json-functions) — Crean, consultan y manipulan datos JSON
- [Funciones de mapa](./12-map-functions) — Crean y manipulan estructuras de datos de mapa
- [Funciones matemáticas](./13-math-functions) — Realizan cálculos y operaciones numéricas
- [Funciones de coincidencia de patrones](./14-pattern-matching-functions) — Comparan cadenas con LIKE y expresiones regulares
- [Funciones escalares (HLL)](./16-scalar-functions) — Funciones de estimación de cardinalidad de HyperLogLog
- [Funciones espaciales](./17-spatial-functions) — Gestionan y manipulan datos geoespaciales
- [Funciones de cadena](./18-string-functions) — Manipulan cadenas y realizan operaciones de texto
- [Funciones de estructura](./19-struct-functions) — Crean y trabajan con tipos de datos de estructura
- [Funciones de variante](./22-variant-functions) — Consultan e inspeccionan tipos de datos VARIANT

## Funciones de tabla

- [Funciones de tabla](./20-table-functions) — Devuelven resultados en formato tabular

## Funciones de utilidad y meta

- [Funciones de utilidad](./21-utility-functions) — Acceden a información del sistema y a utilidades de sesión
- [Funciones meta](./23-meta-functions) — Inspeccionan vistas materializadas, memoria y diagnósticos

## Administración de Lakehouse

- [Administración de Lakehouse](./lakehouse-management/) — ejecute consultas, explore el catálogo, administre almacenes y supervise el cómputo
