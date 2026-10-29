---
title: NULLIF（Lakehouse v1）
description: NULLIF——如果两个表达式相等，则返回 NULL。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nullif.md
---

如果两个表达式相等，则返回 NULL，否则返回 expr1。两者必须具有相同的数据类型。

## Analyze 语法

```python
func.nullif(<expr1>, <expr2>)
```

## Analyze 示例

```python
func.nullif(0, null) 

┌──────────────────────┐
│ func.nullif(0, null) │
├──────────────────────┤
│                    0 │
└──────────────────────┘
```

## SQL 语法

```sql
NULLIF(<expr1>, <expr2>)
```

## SQL 示例

```sql
SELECT NULLIF(0, NULL);

┌─────────────────┐
│ nullif(0, null) │
├─────────────────┤
│               0 │
└─────────────────┘
```
