---
title: MAKEDATE (Lakehouse v2)
description: MAKEDATE — tworzy datę na podstawie roku i dnia roku.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/makedate.md
---

Tworzy datę na podstawie roku i dnia roku.

## Składnia Analyze

```python
func.makedate(<year>, <dayofyear>)
```

## Przykłady Analyze

```python
func.makedate(2024, 100)

┌──────────────┐
│ '2024-04-09'  │
└──────────────┘
```

## Składnia SQL

```sql
MAKEDATE(<year>, <dayofyear>)
```

## Przykłady SQL

```sql
SELECT MAKEDATE(2024, 100);

┌────────────┐
│ 2024-04-09  │
└────────────┘
```
