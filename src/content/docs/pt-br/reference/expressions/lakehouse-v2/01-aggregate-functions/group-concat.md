---
title: "GROUP_CONCAT (agregação, Lakehouse v2)"
description: GROUP_CONCAT — concatena valores de um grupo em uma única string com um separador.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/group-concat.md
---

Concatena valores de um grupo em uma única string com um separador.

## Sintaxe no Analyze

```python
func.group_concat(get_column(table, 'name'), literal(','))
```

## Exemplos no Analyze

```python
func.group_concat(get_column(table, 'name'))
```

## Sintaxe SQL

```sql
GROUP_CONCAT(<name>, literal(','))
```

## Exemplos de SQL

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
