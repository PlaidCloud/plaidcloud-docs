---
title: TO_INT8 (Lakehouse v1)
description: TO_INT8 converte um valor para o tipo de dados INT8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int8.md
---

Converte um valor para o tipo de dados INT8.

## Sintaxe do Analyze

```python
func.to_int8( <expr> )
```

## Exemplos do Analyze

```python
func.to_int8('123')

┌─────────────────────┐
│ func.to_int8('123') │
├─────────────────────┤
│                 123 │
└─────────────────────┘
```

## Sintaxe SQL

```sql
TO_INT8( <expr> )
```

## Exemplos de SQL

```sql
SELECT TO_INT8('123');

┌────────────────┐
│ to_int8('123') │
│      UInt8     │
├────────────────┤
│            123 │
└────────────────┘
```
