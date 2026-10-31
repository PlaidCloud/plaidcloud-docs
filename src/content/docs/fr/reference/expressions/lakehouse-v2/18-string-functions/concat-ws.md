---
title: CONCAT_WS (Lakehouse v2)
description: CONCAT_WS — concatène des chaînes à l'aide d'un séparateur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat-ws.md
---

Concatène des chaînes à l'aide d'un séparateur.

## Syntaxe Analyze

```python
func.concat_ws(<sep>, <str1>, <str2>[, ...])
```

## Exemples Analyze

```python
func.concat_ws('-', '2024', '01', '15')

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
CONCAT_WS(<sep>, <str1>, <str2>[, ...])
```

## Exemples SQL

```sql
SELECT CONCAT_WS('-', '2024', '01', '15');

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
