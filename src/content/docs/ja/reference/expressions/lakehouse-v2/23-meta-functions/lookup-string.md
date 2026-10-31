---
title: LOOKUP_STRING（Lakehouse v2）
description: LOOKUP_STRING — ディクショナリ内で文字列を検索し、対応する ID を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/lookup-string.md
---

ディクショナリ内で文字列を検索し、対応する ID を返します。

## Analyze 構文

```python
func.lookup_string(<dict_table>, <value>)
```

## Analyze の例

```python
func.lookup_string('status_dict', 'Active')

┌───┐
│ 1  │
└───┘
```

## SQL 構文

```sql
LOOKUP_STRING(<dict_table>, <value>)
```

## SQL の例

```sql
SELECT LOOKUP_STRING('status_dict', 'Active');

┌───┐
│ 1  │
└───┘
```
