---
title: TO_UINT8 (Lakehouse v1)
description: TO_UINT8 converte um valor para o tipo de dados UINT8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint8.md
---

Converte um valor para o tipo de dados UINT8.

## Sintaxe do Analyze

```python
func.to_uint8( <expr> )
```

## Exemplos do Analyze

```python
func.to_uint8('123')

┌──────────────────────┐
│ func.to_uint8('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Sintaxe SQL

```sql
TO_UINT8( <expr> )
```

## Exemplos de SQL

```sql
SELECT TO_UINT8('123');

┌─────────────────┐
│ to_uint8('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
