---
title: JODATIME_FORMAT (Lakehouse v2)
description: JODATIME_FORMAT — met en forme une date ou une date-heure à l'aide des modèles de format Joda-Time.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/jodatime-format.md
---

Met en forme une date ou une date-heure à l'aide des modèles de format Joda-Time.

## Syntaxe Analyze

```python
func.jodatime_format(<datetime>, <pattern>)
```

## Exemples Analyze

```python
func.jodatime_format('2024-06-15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
JODATIME_FORMAT(<datetime>, <pattern>)
```

## Exemples SQL

```sql
SELECT JODATIME_FORMAT('2024-06-15', 'yyyy/MM/dd');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
