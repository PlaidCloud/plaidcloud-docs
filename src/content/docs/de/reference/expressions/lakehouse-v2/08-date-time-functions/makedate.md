---
title: MAKEDATE (Lakehouse v2)
description: MAKEDATE – erstellt aus einem Jahr und einem Tag des Jahres ein Datum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/makedate.md
---

Erstellt aus einem Jahr und einem Tag des Jahres ein Datum.

## Analyze-Syntax

```python
func.makedate(<year>, <dayofyear>)
```

## Analyze-Beispiele

```python
func.makedate(2024, 100)

┌──────────────┐
│ '2024-04-09'  │
└──────────────┘
```

## SQL-Syntax

```sql
MAKEDATE(<year>, <dayofyear>)
```

## SQL-Beispiele

```sql
SELECT MAKEDATE(2024, 100);

┌────────────┐
│ 2024-04-09  │
└────────────┘
```
