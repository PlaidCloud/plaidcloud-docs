---
title: TO_FLOAT32 (Lakehouse v1)
description: TO_FLOAT32 — converte um valor para o tipo de dados FLOAT32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float32.md
---

Converte um valor para o tipo de dados FLOAT32.

## Sintaxe do Analyze

```python
func.to_float32( <expr> )
```

## Exemplos do Analyze

```python
func.to_float32('1.2')

┌─────────────────────────┐
│ func.to_float32('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Sintaxe SQL

```sql
TO_FLOAT32( <expr> )
```

## Exemplos SQL

```sql
SELECT TO_FLOAT32('1.2');

┌───────────────────┐
│ to_float32('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
