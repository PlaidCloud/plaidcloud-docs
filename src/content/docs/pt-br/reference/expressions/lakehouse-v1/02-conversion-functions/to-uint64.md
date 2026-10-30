---
title: TO_UINT64 (Lakehouse v1)
description: TO_UINT64 converte um valor para o tipo de dados UINT64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint64.md
---

Converte um valor para o tipo de dados UINT64.

## Sintaxe do Analyze

```python
func.to_uint64( <expr> )
```

## Exemplos do Analyze

```python
func.to_uint64('123')

┌───────────────────────┐
│ func.to_uint64('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## Sintaxe SQL

```sql
TO_UINT64( <expr> )
```

## Exemplos de SQL

```sql
SELECT TO_UINT64('123');

┌──────────────────┐
│ to_uint64('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
