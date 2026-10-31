---
title: COALESCE (Lakehouse v2)
description: COALESCE — 式のリストから、最初の NULL でない式を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/coalesce.md
---

式のリストから、最初の NULL でない式を返します。

## Analyzeの構文

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'))
```

## Analyzeの例

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'), 'Unknown')
```

## SQLの構文

```sql
COALESCE(<nickname>, <name>)
```

## SQLの例

```sql
SELECT COALESCE(nickname, first_name, 'Unknown') AS display_name FROM users;

┌──────────────┐
│ display_name │
├──────────────┤
│ Bob          │
│ Alice        │
│ Unknown      │
└──────────────┘
```
