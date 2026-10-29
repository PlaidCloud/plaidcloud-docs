---
title: TO_UINT32 (Lakehouse v1)
description: TO_UINT32 converte um valor para o tipo de dados UINT32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint32.md
---

Converte um valor para o tipo de dados UINT32.

## Sintaxe do Analyze

```python
func.to_uint32( <expr> )
```

## Exemplos do Analyze

```python
func.to_uint32('123')

┌───────────────────────┐
│ func.to_uint32('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## Sintaxe SQL

```sql
TO_UINT32( <expr> )
```

## Exemplos de SQL

```sql
SELECT TO_UINT32('123');

┌──────────────────┐
│ to_uint32('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
