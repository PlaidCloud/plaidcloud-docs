---
title: LIKE（Lakehouse v1）
description: LIKE——使用 SQL 模式进行模式匹配。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/like.md
---

使用 SQL 模式进行模式匹配。返回 1（TRUE）或 0（FALSE）。如果 expr 或 pat 为 NULL，则结果为 NULL。

## Analyze 语法

```python
<column>.like('plaid%')
```

## Analyze 示例

```python
my_clothes.like('plaid%)
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants     │
│ plaid hat       │
│ plaid shirt     │
└─────────────────┘
```

## SQL 语法

```sql
<expr> LIKE <pattern>
```

## SQL 示例

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' ORDER BY name;
┌──────────┬────────────┐
│ name     │ category   │
├──────────┼────────────┤
│ touint16 │ conversion │
│ touint32 │ conversion │
│ touint64 │ conversion │
│ touint8  │ conversion │
└──────────┴────────────┘
```
