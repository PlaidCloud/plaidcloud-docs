---
title: "GROUP_CONCAT (Aggregate, Lakehouse v2)"
description: GROUP_CONCAT — concatena os valores de um grupo numa única cadeia de caracteres com um separador.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/group-concat.md
---

Concatena os valores de um grupo numa única cadeia de caracteres com um separador.

## Sintaxe do Analyze

```python
func.group_concat(get_column(table, 'name'), literal(','))
```

## Exemplos do Analyze

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
