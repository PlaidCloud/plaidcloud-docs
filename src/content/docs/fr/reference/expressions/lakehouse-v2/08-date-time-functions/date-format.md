---
title: DATE_FORMAT (Lakehouse v2)
description: DATE_FORMAT — met en forme une valeur de date ou de date-heure selon une chaîne de format.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-format.md
---

Met en forme une valeur de date ou de date-heure selon une chaîne de format.

## Syntaxe Analyze

```python
func.date_format(<date>, <format>)
```

## Exemples Analyze

```python
func.date_format('2024-06-15', '%Y/%m/%d')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
DATE_FORMAT(<date>, <format>)
```

## Exemples SQL

```sql
SELECT DATE_FORMAT('2024-06-15', '%Y/%m/%d');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
