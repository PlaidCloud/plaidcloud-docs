---
title: STR_TO_JODATIME (Lakehouse v2)
description: STR_TO_JODATIME — convertit une chaîne en date-heure à l'aide de motifs de format Joda-Time.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-jodatime.md
---

Convertit une chaîne en date-heure à l'aide de motifs de format Joda-Time.

## Syntaxe Analyze

```python
func.str_to_jodatime(<str>, <pattern>)
```

## Exemples Analyze

```python
func.str_to_jodatime('2024/06/15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
STR_TO_JODATIME(<str>, <pattern>)
```

## Exemples SQL

```sql
SELECT STR_TO_JODATIME('2024/06/15', 'yyyy/MM/dd');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
