---
title: IFNULL（Lakehouse v1）
description: IFNULL——如果 <expr1> 为 NULL，则返回 <expr2>，否则返回 <expr1>。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/ifnull.md
---

如果 `<expr1>` 为 NULL，则返回 `<expr2>`，否则返回 `<expr1>`。

## Analyze 语法

```python
func.ifnull(<expr1>, <expr2>)
```

## Analyze 示例

```python
func.ifnull(null, 'b'), func.ifnull('a', 'b')

┌────────────────────────────────────────────────┐
│ func.ifnull(null, 'b') │ func.ifnull('a', 'b') │
├────────────────────────┼───────────────────────┤
│ b                      │ a                     │
└────────────────────────────────────────────────┘

func.ifnull(null, 2), func.ifnull(1, 2)

┌──────────────────────────────────────────┐
│ func.ifnull(null, 2) │ func.ifnull(1, 2) │
├──────────────────────┼───────────────────┤
│                    2 │                 1 │
└──────────────────────────────────────────┘
```

## SQL 语法

```sql
IFNULL(<expr1>, <expr2>)
```

## 别名

- [NVL](../nvl)

## SQL 示例

```sql
SELECT IFNULL(NULL, 'b'), IFNULL('a', 'b');

┌──────────────────────────────────────┐
│ ifnull(null, 'b') │ ifnull('a', 'b') │
├───────────────────┼──────────────────┤
│ b                 │ a                │
└──────────────────────────────────────┘

SELECT IFNULL(NULL, 2), IFNULL(1, 2);

┌────────────────────────────────┐
│ ifnull(null, 2) │ ifnull(1, 2) │
├─────────────────┼──────────────┤
│               2 │            1 │
└────────────────────────────────┘
```
