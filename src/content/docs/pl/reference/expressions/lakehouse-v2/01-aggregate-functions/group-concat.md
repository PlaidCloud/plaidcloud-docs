---
title: "GROUP_CONCAT (funkcja agregująca, Lakehouse v2)"
description: GROUP_CONCAT — łączy wartości z grupy w jeden ciąg znaków, rozdzielając je separatorem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/group-concat.md
---

Łączy wartości z grupy w jeden ciąg znaków, rozdzielając je separatorem.

## Składnia Analyze

```python
func.group_concat(get_column(table, 'name'), literal(','))
```

## Przykłady Analyze

```python
func.group_concat(get_column(table, 'name'))
```

## Składnia SQL

```sql
GROUP_CONCAT(<name>, literal(','))
```

## Przykłady SQL

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
