---
title: REPEAT (Lakehouse v2)
description: REPEAT — Repite una cadena el número de veces especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/repeat.md
---

Repite una cadena el número de veces especificado.

## Sintaxis de Analyze

```python
func.repeat(<str>, <n>)
```

## Ejemplos de Analyze

```python
func.repeat('ab', 3)

┌──────────┐
│ 'ababab'  │
└──────────┘
```

## Sintaxis de SQL

```sql
REPEAT(<str>, <n>)
```

## Ejemplos de SQL

```sql
SELECT REPEAT('ab', 3);

┌────────┐
│ ababab  │
└────────┘
```
