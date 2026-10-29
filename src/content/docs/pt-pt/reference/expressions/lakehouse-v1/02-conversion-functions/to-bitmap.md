---
title: TO_BITMAP (Lakehouse v1)
description: TO_BITMAP — converte um valor para o tipo de dados BITMAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-bitmap.md
---

Converte um valor para o tipo de dados BITMAP.

## Sintaxe do Analyze

```python
func.to_bitmap( <expr> )
```

## Exemplos do Analyze

```python
func.to_bitmap('1101')

┌─────────────────────────┐
│ func.to_bitmap('1101')  │
├─────────────────────────┤
│ <bitmap binary>         │
└─────────────────────────┘
```

## Sintaxe SQL

```sql
TO_BITMAP( <expr> )
```

## Exemplos SQL

```sql
SELECT TO_BITMAP('1101');

┌───────────────────┐
│ to_bitmap('1101') │
├───────────────────┤
│ <bitmap binary>   │
└───────────────────┘
```
