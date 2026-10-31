---
title: ROW (Lakehouse v2)
description: ROW — Crea una estructura a partir de una lista de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/row.md
---

Crea una estructura a partir de una lista de valores.

## Sintaxis de Analyze

```python
func.row(<val1>[, <val2>, ...])
```

## Ejemplos de Analyze

```python
func.row('Alice', 30)

┌────────────────────────────┐
│ {'col1':'Alice','col2':30}  │
└────────────────────────────┘
```

## Sintaxis de SQL

```sql
ROW(<val1>[, <val2>, ...])
```

## Ejemplos de SQL

```sql
SELECT ROW('Alice', 30);

┌────────────────────────────┐
│ {"col1":"Alice","col2":30}  │
└────────────────────────────┘
```
