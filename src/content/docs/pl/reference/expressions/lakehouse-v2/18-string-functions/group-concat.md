---
title: "GROUP_CONCAT (tekst, Lakehouse v2)"
description: GROUP_CONCAT — łączy wartości z grupy w jeden ciąg znaków, rozdzielając je separatorem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/group-concat.md
---

Łączy wartości z grupy w jeden ciąg znaków, rozdzielając je separatorem.

## Składnia Analyze

```python
func.group_concat(<expr> [SEPARATOR '<sep>'])
```

## Przykłady Analyze

```python
func.group_concat(get_column(table, 'name'))

┌─────────────────────┐
│ 'Alice,Bob,Charlie'  │
└─────────────────────┘
```

## Składnia SQL

```sql
GROUP_CONCAT(<expr> [SEPARATOR '<sep>'])
```

## Przykłady SQL

```sql
SELECT GROUP_CONCAT(name ORDER BY name SEPARATOR ', ') FROM employees;

┌─────────────────────┐
│ Alice, Bob, Charlie  │
└─────────────────────┘
```
