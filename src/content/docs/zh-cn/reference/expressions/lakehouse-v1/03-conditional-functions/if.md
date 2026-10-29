---
title: IF（Lakehouse v1）
description: IF——如果 <cond1> 为 TRUE，则返回 <expr1>。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/if.md
---

如果 `<cond1>` 为 TRUE，则返回 `<expr1>`。否则，如果 `<cond2>` 为 TRUE，则返回 `<expr2>`，依此类推。

## Analyze 语法

```python
func.if_(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## Analyze 示例

```python
func.if_((1 > 2), 3, (4 < 5), 6, 7)

┌─────────────────────────────────────┐
│ func.if_((1 > 2), 3, (4 < 5), 6, 7) │
├─────────────────────────────────────┤
│                                   6 │
└─────────────────────────────────────┘
```

## SQL 语法

```sql
IF(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## SQL 示例

```sql
SELECT IF(1 > 2, 3, 4 < 5, 6, 7);

┌───────────────────────────────┐
│ if((1 > 2), 3, (4 < 5), 6, 7) │
├───────────────────────────────┤
│                             6 │
└───────────────────────────────┘
```
