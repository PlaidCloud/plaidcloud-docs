---
title: TO_INT64 (Lakehouse v1)
description: TO_INT64 converte um valor para o tipo de dados INT64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int64.md
---

Converte um valor para o tipo de dados INT64.

## Sintaxe do Analyze

```python
func.to_int64( <expr> )
```

## Exemplos do Analyze

```python
func.to_int64('123')

┌──────────────────────┐
│ func.to_int64('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Sintaxe SQL

```sql
TO_INT64( <expr> )
```

## Exemplos de SQL

```sql
SELECT TO_INT64('123');

┌─────────────────┐
│ to_int64('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
