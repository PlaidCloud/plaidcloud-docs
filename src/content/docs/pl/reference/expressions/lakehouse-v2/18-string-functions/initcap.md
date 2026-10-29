---
title: INITCAP (Lakehouse v2)
description: INITCAP — zamienia pierwszą literę każdego słowa w ciągu na wielką.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/initcap.md
---

Zamienia pierwszą literę każdego słowa w ciągu na wielką.

## Składnia Analyze

```python
func.initcap(<str>)
```

## Przykłady Analyze

```python
func.initcap('hello world')

┌───────────────┐
│ 'Hello World'  │
└───────────────┘
```

## Składnia SQL

```sql
INITCAP(<str>)
```

## Przykłady SQL

```sql
SELECT INITCAP('hello world');

┌─────────────┐
│ Hello World  │
└─────────────┘
```
