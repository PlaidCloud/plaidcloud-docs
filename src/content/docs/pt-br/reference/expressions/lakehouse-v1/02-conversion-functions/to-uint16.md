---
title: TO_UINT16 (Lakehouse v1)
description: TO_UINT16 converte um valor para o tipo de dados UINT16.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint16.md
---

Converte um valor para o tipo de dados UINT16.

## Sintaxe do Analyze

```python
func.to_uint16( <expr> )
```

## Exemplos do Analyze

```python
func.to_uint16('123')

┌───────────────────────┐
│ func.to_uint16('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## Sintaxe SQL

```sql
TO_UINT16( <expr> )
```

## Exemplos de SQL

```sql
SELECT TO_UINT16('123');

┌──────────────────┐
│ to_uint16('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
