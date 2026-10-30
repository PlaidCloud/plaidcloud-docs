---
title: STR_TO_DATE (Lakehouse v2)
description: STR_TO_DATE — convertit une chaîne en date à l'aide d'une chaîne de format.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-date.md
---

Convertit une chaîne en date à l'aide d'une chaîne de format.

## Syntaxe Analyze

```python
func.str_to_date(<str>, <format>)
```

## Exemples Analyze

```python
func.str_to_date('Jun 15 2024', '%b %d %Y')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
STR_TO_DATE(<str>, <format>)
```

## Exemples SQL

```sql
SELECT STR_TO_DATE('Jun 15 2024', '%b %d %Y');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
