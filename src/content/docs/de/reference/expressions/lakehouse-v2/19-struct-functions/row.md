---
title: ROW (Lakehouse v2)
description: ROW — erstellt ein Struct aus einer Liste von Werten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/row.md
---

Erstellt ein Struct aus einer Liste von Werten.

## Analyze-Syntax

```python
func.row(<val1>[, <val2>, ...])
```

## Analyze-Beispiele

```python
func.row('Alice', 30)

┌────────────────────────────┐
│ {'col1':'Alice','col2':30}  │
└────────────────────────────┘
```

## SQL-Syntax

```sql
ROW(<val1>[, <val2>, ...])
```

## SQL-Beispiele

```sql
SELECT ROW('Alice', 30);

┌────────────────────────────┐
│ {"col1":"Alice","col2":30}  │
└────────────────────────────┘
```
