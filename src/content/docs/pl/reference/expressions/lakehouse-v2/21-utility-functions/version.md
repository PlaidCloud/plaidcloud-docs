---
title: VERSION (Lakehouse v2)
description: VERSION — zwraca wersję protokołu MySQL w StarRocks.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/version.md
---

Zwraca wersję protokołu MySQL w StarRocks.

## Składnia Analyze

```python
func.version()
```

## Przykłady Analyze

```python
func.version()

┌─────────┐
│ '5.1.0'  │
└─────────┘
```

## Składnia SQL

```sql
VERSION()
```

## Przykłady SQL

```sql
SELECT VERSION();

┌───────┐
│ 5.1.0  │
└───────┘
```
