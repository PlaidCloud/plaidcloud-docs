---
title: "[ NOT ] BETWEEN (Lakehouse v1)"
description: "[ NOT ] BETWEEN：如果数值、字符串或日期值位于（或不位于）给定范围内，则为真。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/between.md
---

如果给定的数值或字符串 ` <expr>` 位于所定义的下限和上限之间，则返回 `true`。

## Analyze 语法

```python
table.column.between(<lower_limit>, <upper_limit>
```

## Analyze 示例

```python
table.column.between(0, 5)
```

## SQL 语法

```sql
<expr> [ NOT ] BETWEEN <lower_limit> AND <upper_limit>
```

## SQL 示例

```sql
SELECT 'true' WHERE 5 BETWEEN 0 AND 5;

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘

SELECT 'true' WHERE 'data' BETWEEN 'data' AND 'databendcloud';

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘
```
