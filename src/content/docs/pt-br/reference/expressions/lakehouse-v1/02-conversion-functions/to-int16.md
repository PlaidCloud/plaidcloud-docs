---
title: TO_INT16 (Lakehouse v1)
description: TO_INT16 converte um valor para o tipo de dados INT16.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int16.md
---

Converte um valor para o tipo de dados INT16.

## Sintaxe do Analyze

```python
func.to_int16( <expr> )
```

## Exemplos do Analyze

```python
func.to_int16('123')

┌──────────────────────┐
│ func.to_int16('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Sintaxe SQL

```sql
TO_INT16( <expr> )
```

## Exemplos de SQL

```sql
SELECT TO_INT16('123');

┌─────────────────┐
│ to_int16('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
