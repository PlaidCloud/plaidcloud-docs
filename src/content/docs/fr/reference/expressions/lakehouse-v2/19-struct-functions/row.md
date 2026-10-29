---
title: ROW (Lakehouse v2)
description: ROW — crée une structure à partir d'une liste de valeurs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/row.md
---

Crée une structure à partir d'une liste de valeurs.

## Syntaxe Analyze

```python
func.row(<val1>[, <val2>, ...])
```

## Exemples Analyze

```python
func.row('Alice', 30)

┌────────────────────────────┐
│ {'col1':'Alice','col2':30}  │
└────────────────────────────┘
```

## Syntaxe SQL

```sql
ROW(<val1>[, <val2>, ...])
```

## Exemples SQL

```sql
SELECT ROW('Alice', 30);

┌────────────────────────────┐
│ {"col1":"Alice","col2":30}  │
└────────────────────────────┘
```
