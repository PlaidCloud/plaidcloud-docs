---
title: TO_VARIANT (Lakehouse v1)
description: TO_VARIANT — converte um valor para o tipo de dados VARIANT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-variant.md
---

Converte um valor para o tipo de dados VARIANT.

## Sintaxe do Analyze

```python
func.to_variant( <expr> )
```

## Exemplos do Analyze

```python
func.to_variant(to_bitmap('100,200,300'))

┌───────────────────────────────────────────┐
│ func.to_variant(to_bitmap('100,200,300')) │
├───────────────────────────────────────────┤
│ [100,200,300]                             │
└───────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_VARIANT( <expr> )
```

## Exemplos SQL

```sql
SELECT TO_VARIANT(TO_BITMAP('100,200,300'));

┌──────────────────────────────────────┐
│ to_variant(to_bitmap('100,200,300')) │
├──────────────────────────────────────┤
│ [100,200,300]                        │
└──────────────────────────────────────┘
```
