---
title: TO_INT32 (Lakehouse v1)
description: TO_INT32 — converte um valor para o tipo de dados INT32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int32.md
---

Converte um valor para o tipo de dados INT32.

## Sintaxe do Analyze

```python
func.to_int32( <expr> )
```

## Exemplos do Analyze

```python
func.to_int32('123')

┌──────────────────────┐
│ func.to_int32('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Sintaxe SQL

```sql
TO_INT32( <expr> )
```

## Exemplos SQL

```sql
SELECT TO_INT32('123');

┌─────────────────┐
│ to_int32('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
