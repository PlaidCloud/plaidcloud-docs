---
title: "GROUP_CONCAT (Aggregat, Lakehouse v2)"
description: GROUP_CONCAT verkettet Werte einer Gruppe mit einem Trennzeichen zu einer einzigen Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/group-concat.md
---

Verkettet Werte einer Gruppe mit einem Trennzeichen zu einer einzigen Zeichenfolge.

## Analyze-Syntax

```python
func.group_concat(get_column(table, 'name'), literal(','))
```

## Analyze-Beispiele

```python
func.group_concat(get_column(table, 'name'))
```

## SQL-Syntax

```sql
GROUP_CONCAT(<name>, literal(','))
```

## SQL-Beispiele

```sql
SELECT department, GROUP_CONCAT(name ORDER BY name SEPARATOR ', ')
FROM employees GROUP BY department;

┌────────────┬──────────────────────────┐
│ department │ group_concat(name)       │
├────────────┼──────────────────────────┤
│ Sales      │ Alice, Bob, Charlie      │
│ IT         │ Dave, Eve                │
└────────────┴──────────────────────────┘
```
