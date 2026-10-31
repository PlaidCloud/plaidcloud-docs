---
title: STR2DATE (Lakehouse v2)
description: STR2DATE — convertit une chaîne en date à l'aide d'une chaîne de format. Alias de `STR_TO_DATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str2date.md
---

Convertit une chaîne en date à l'aide d'une chaîne de format. Alias de `STR_TO_DATE`.

## Syntaxe Analyze

```python
func.str2date(<str>, <format>)
```

## Exemples Analyze

```python
func.str2date('2024/06/15', '%Y/%m/%d')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
STR2DATE(<str>, <format>)
```

## Exemples SQL

```sql
SELECT STR2DATE('2024/06/15', '%Y/%m/%d');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
