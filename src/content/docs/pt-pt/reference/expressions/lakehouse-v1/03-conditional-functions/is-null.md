---
title: IS_NULL (Lakehouse v1)
description: IS_NULL — verifica se um valor é NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-null.md
---

Verifica se um valor é NULL.

## Sintaxe do Analyze

```python
func.is_null(<expr>)
```

## Exemplos do Analyze

```python
func.is_null(1)

┌─────────────────┐
│ func.is_null(1) │
├─────────────────┤
│ false           │
└─────────────────┘
```

## Sintaxe SQL

```sql
IS_NULL(<expr>)
```

## Exemplos SQL

```sql
SELECT IS_NULL(1);

┌────────────┐
│ is_null(1) │
├────────────┤
│ false      │
└────────────┘
```
