---
title: "GROUP_CONCAT (String, Lakehouse v2)"
description: GROUP_CONCAT — concatène les valeurs d'un groupe en une seule chaîne à l'aide d'un séparateur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/group-concat.md
---

Concatène les valeurs d'un groupe en une seule chaîne à l'aide d'un séparateur.

## Syntaxe Analyze

```python
func.group_concat(<expr> [SEPARATOR '<sep>'])
```

## Exemples Analyze

```python
func.group_concat(get_column(table, 'name'))

┌─────────────────────┐
│ 'Alice,Bob,Charlie'  │
└─────────────────────┘
```

## Syntaxe SQL

```sql
GROUP_CONCAT(<expr> [SEPARATOR '<sep>'])
```

## Exemples SQL

```sql
SELECT GROUP_CONCAT(name ORDER BY name SEPARATOR ', ') FROM employees;

┌─────────────────────┐
│ Alice, Bob, Charlie  │
└─────────────────────┘
```
