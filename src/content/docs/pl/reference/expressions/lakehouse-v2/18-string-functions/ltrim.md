---
title: LTRIM (Lakehouse v2)
description: LTRIM — usuwa z początku ciągu białe znaki lub wskazane znaki.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ltrim.md
---

Usuwa z początku ciągu białe znaki lub wskazane znaki.

## Składnia Analyze

```python
func.ltrim(<str>)
```

## Przykłady Analyze

```python
func.ltrim('   hello')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Składnia SQL

```sql
LTRIM(<str>)
```

## Przykłady SQL

```sql
SELECT LTRIM('   hello');

┌───────┐
│ hello  │
└───────┘
```
