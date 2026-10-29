---
title: ROW (Lakehouse v2)
description: ROW — tworzy strukturę na podstawie listy wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/row.md
---

Tworzy strukturę na podstawie listy wartości.

## Składnia Analyze

```python
func.row(<val1>[, <val2>, ...])
```

## Przykłady Analyze

```python
func.row('Alice', 30)

┌────────────────────────────┐
│ {'col1':'Alice','col2':30}  │
└────────────────────────────┘
```

## Składnia SQL

```sql
ROW(<val1>[, <val2>, ...])
```

## Przykłady SQL

```sql
SELECT ROW('Alice', 30);

┌────────────────────────────┐
│ {"col1":"Alice","col2":30}  │
└────────────────────────────┘
```
