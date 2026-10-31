---
title: RTRIM (Lakehouse v2)
description: RTRIM — usuwa z końca ciągu białe znaki lub wskazane znaki.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rtrim.md
---

Usuwa z końca ciągu białe znaki lub wskazane znaki.

## Składnia Analyze

```python
func.rtrim(<str>)
```

## Przykłady Analyze

```python
func.rtrim('hello   ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Składnia SQL

```sql
RTRIM(<str>)
```

## Przykłady SQL

```sql
SELECT RTRIM('hello   ');

┌───────┐
│ hello  │
└───────┘
```
