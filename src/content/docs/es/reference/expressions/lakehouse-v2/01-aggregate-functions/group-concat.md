---
title: "GROUP_CONCAT (agregación, Lakehouse v2)"
description: GROUP_CONCAT concatena los valores de un grupo en una sola cadena con un separador.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/group-concat.md
---

Concatena los valores de un grupo en una sola cadena con un separador.

## Sintaxis de Analyze

```python
func.group_concat(get_column(table, 'name'), literal(','))
```

## Ejemplos de Analyze

```python
func.group_concat(get_column(table, 'name'))
```

## Sintaxis de SQL

```sql
GROUP_CONCAT(<name>, literal(','))
```

## Ejemplos de SQL

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
