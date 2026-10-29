---
title: SLEEP (Lakehouse v2)
description: SLEEP — Pausa la ejecución durante un número especificado de segundos. Devuelve 0 si se completa correctamente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/sleep.md
---

Pausa la ejecución durante un número especificado de segundos. Devuelve 0 si se completa correctamente.

## Sintaxis de Analyze

```python
func.sleep(<seconds>)
```

## Ejemplos de Analyze

```python
func.sleep(1)

┌───┐
│ 0  │
└───┘
```

## Sintaxis de SQL

```sql
SLEEP(<seconds>)
```

## Ejemplos de SQL

```sql
SELECT SLEEP(1);

┌───┐
│ 0  │
└───┘
```
