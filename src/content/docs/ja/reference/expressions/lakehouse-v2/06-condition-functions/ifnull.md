---
title: IFNULL (Lakehouse v2)
description: IFNULL — 1 つ目の式が NULL でなければその式を返し、NULL の場合は 2 つ目の式を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/ifnull.md
---

1 つ目の式が NULL でなければその式を返し、NULL の場合は 2 つ目の式を返します。

## Analyzeの構文

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Analyzeの例

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## SQLの構文

```sql
IFNULL(<phone>, 'N/A')
```

## SQLの例

```sql
SELECT name, IFNULL(phone, 'N/A') AS phone FROM contacts;

┌─────────┬──────────┐
│ name    │ phone    │
├─────────┼──────────┤
│ Alice   │ 555-1234 │
│ Bob     │ N/A      │
└─────────┴──────────┘
```
