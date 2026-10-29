---
title: LOOKUP_STRING (Lakehouse v2)
description: LOOKUP_STRING：在字典中查找字符串，并返回对应的 ID。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/lookup-string.md
---

在字典中查找字符串，并返回对应的 ID。

## Analyze 语法

```python
func.lookup_string(<dict_table>, <value>)
```

## Analyze 示例

```python
func.lookup_string('status_dict', 'Active')

┌───┐
│ 1  │
└───┘
```

## SQL 语法

```sql
LOOKUP_STRING(<dict_table>, <value>)
```

## SQL 示例

```sql
SELECT LOOKUP_STRING('status_dict', 'Active');

┌───┐
│ 1  │
└───┘
```
