---
title: ROW (Lakehouse v2)
description: ROW — cria um struct a partir de uma lista de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/row.md
---

Cria um struct a partir de uma lista de valores.

## Sintaxe do Analyze

```python
func.row(<val1>[, <val2>, ...])
```

## Exemplos do Analyze

```python
func.row('Alice', 30)

┌────────────────────────────┐
│ {'col1':'Alice','col2':30}  │
└────────────────────────────┘
```

## Sintaxe SQL

```sql
ROW(<val1>[, <val2>, ...])
```

## Exemplos SQL

```sql
SELECT ROW('Alice', 30);

┌────────────────────────────┐
│ {"col1":"Alice","col2":30}  │
└────────────────────────────┘
```
