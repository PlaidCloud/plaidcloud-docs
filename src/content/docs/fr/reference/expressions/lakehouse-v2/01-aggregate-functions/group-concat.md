---
title: "GROUP_CONCAT (agrégation, Lakehouse v2)"
description: GROUP_CONCAT — concatène les valeurs d'un groupe en une seule chaîne avec un séparateur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/group-concat.md
---

Concatène les valeurs d'un groupe en une seule chaîne avec un séparateur.

## Syntaxe Analyze

```python
func.group_concat(get_column(table, 'name'), literal(','))
```

## Exemples Analyze

```python
func.group_concat(get_column(table, 'name'))
```

## Syntaxe SQL

```sql
GROUP_CONCAT(<name>, literal(','))
```

## Exemples SQL

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
