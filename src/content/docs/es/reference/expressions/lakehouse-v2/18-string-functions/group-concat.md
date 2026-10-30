---
title: "GROUP_CONCAT (String, Lakehouse v2)"
description: GROUP_CONCAT — Concatena los valores de un grupo en una sola cadena con un separador.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/group-concat.md
---

Concatena los valores de un grupo en una sola cadena con un separador.

## Sintaxis de Analyze

```python
func.group_concat(<expr> [SEPARATOR '<sep>'])
```

## Ejemplos de Analyze

```python
func.group_concat(get_column(table, 'name'))

┌─────────────────────┐
│ 'Alice,Bob,Charlie'  │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
GROUP_CONCAT(<expr> [SEPARATOR '<sep>'])
```

## Ejemplos de SQL

```sql
SELECT GROUP_CONCAT(name ORDER BY name SEPARATOR ', ') FROM employees;

┌─────────────────────┐
│ Alice, Bob, Charlie  │
└─────────────────────┘
```
