---
title: TO_FLOAT64 (Lakehouse v1)
description: TO_FLOAT64 — converte um valor para o tipo de dados FLOAT64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float64.md
---

Converte um valor para o tipo de dados FLOAT64.

## Sintaxe do Analyze

```python
func.to_float64( <expr> )
```

## Exemplos do Analyze

```python
func.to_float64('1.2')

┌─────────────────────────┐
│ func.to_float64('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Sintaxe SQL

```sql
TO_FLOAT64( <expr> )
```

## Exemplos SQL

```sql
SELECT TO_FLOAT64('1.2');

┌───────────────────┐
│ to_float64('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
