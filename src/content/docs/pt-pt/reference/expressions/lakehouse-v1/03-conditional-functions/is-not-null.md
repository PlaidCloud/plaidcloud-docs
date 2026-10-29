---
title: IS_NOT_NULL (Lakehouse v1)
description: IS_NOT_NULL — verifica se um valor não é NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-not-null.md
---

Verifica se um valor não é NULL.

## Sintaxe do Analyze

```python
func.is_not_null(<expr>)
```

## Exemplos do Analyze

```python
func.is_not_null(1)

┌─────────────────────┐
│ func.is_not_null(1) │
├─────────────────────┤
│ true                │
└─────────────────────┘
```

## Sintaxe SQL

```sql
IS_NOT_NULL(<expr>)
```

## Exemplos SQL

```sql
SELECT IS_NOT_NULL(1);

┌────────────────┐
│ is_not_null(1) │
├────────────────┤
│ true           │
└────────────────┘
```
