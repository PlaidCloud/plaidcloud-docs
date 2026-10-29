---
title: SLEEP (Lakehouse v1)
description: SLEEP espera el número de segundos indicado en cada bloque de datos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-test-functions/sleep.md
---

Espera `seconds` segundos en cada bloque de datos.

!!! warning 
    Solo se usa en pruebas en las que se requiere una espera.


## Sintaxis de SQL

```sql
SLEEP(seconds)
```

## Argumentos

| Argumentos  | Descripción |
| ----------- | ----------- |
| seconds  | Debe ser una columna constante de cualquier número no negativo o de tipo float.｜

## Tipo de retorno

UInt8

## Ejemplos de SQL

```sql
SELECT sleep(2);
┌──────────┐
│ sleep(2) │
├──────────┤
│        0 │
└──────────┘
```
