---
title: "GROUP_CONCAT (Zeichenfolge, Lakehouse v2)"
description: GROUP_CONCAT — verkettet die Werte einer Gruppe mit einem Trennzeichen zu einer einzelnen Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/group-concat.md
---

Verkettet die Werte einer Gruppe mit einem Trennzeichen zu einer einzelnen Zeichenfolge.

## Analyze-Syntax

```python
func.group_concat(<expr> [SEPARATOR '<sep>'])
```

## Analyze-Beispiele

```python
func.group_concat(get_column(table, 'name'))

┌─────────────────────┐
│ 'Alice,Bob,Charlie'  │
└─────────────────────┘
```

## SQL-Syntax

```sql
GROUP_CONCAT(<expr> [SEPARATOR '<sep>'])
```

## SQL-Beispiele

```sql
SELECT GROUP_CONCAT(name ORDER BY name SEPARATOR ', ') FROM employees;

┌─────────────────────┐
│ Alice, Bob, Charlie  │
└─────────────────────┘
```
