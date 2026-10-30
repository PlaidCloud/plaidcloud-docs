---
title: NOT LIKE（Lakehouse v1）
description: NOT LIKE——使用 SQL 模式进行不匹配的模式匹配。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-like.md
---

使用 SQL 模式进行不匹配的模式匹配。返回 1（TRUE）或 0（FALSE）。如果 expr 或 pat 为 NULL，则结果为 NULL。

## Analyze 语法

```python
<column>.not_like(<pattern>)
```

## Analyze 示例

```python
my_clothes.not_like('%pants)
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants XL  │
│ plaid hat       │
│ plaid shirt     │
└─────────────────┘
```

## SQL 语法

```sql
<expr> NOT LIKE <pattern>
```

## SQL 示例

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' AND name not like '%64' ORDER BY name;
┌──────────┬────────────┐
│ name     │ category   │
├──────────┼────────────┤
│ touint16 │ conversion │
│ touint32 │ conversion │
│ touint8  │ conversion │
└──────────┴────────────┘
```
