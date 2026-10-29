---
title: TRIM (Lakehouse v2)
description: TRIM — usuwa z początku i końca ciągu białe znaki lub wskazane znaki.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/trim.md
---

Usuwa z początku i końca ciągu białe znaki lub wskazane znaki.

## Składnia Analyze

```python
func.trim(<str>)
```

## Przykłady Analyze

```python
func.trim('  hello  ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Składnia SQL

```sql
TRIM(<str>)
```

## Przykłady SQL

```sql
SELECT TRIM('  hello  ');

┌───────┐
│ hello  │
└───────┘
```
