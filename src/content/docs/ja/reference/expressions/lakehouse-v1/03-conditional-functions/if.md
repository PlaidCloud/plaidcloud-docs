---
title: IF（Lakehouse v1）
description: IF — <cond1> が TRUE の場合は <expr1> を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/if.md
---

`<cond1>` が TRUE の場合は `<expr1>` を返します。そうでなく `<cond2>` が TRUE の場合は `<expr2>` を返し、以降も同様です。

## Analyze 構文

```python
func.if_(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## Analyze の例

```python
func.if_((1 > 2), 3, (4 < 5), 6, 7)

┌─────────────────────────────────────┐
│ func.if_((1 > 2), 3, (4 < 5), 6, 7) │
├─────────────────────────────────────┤
│                                   6 │
└─────────────────────────────────────┘
```

## SQL 構文

```sql
IF(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## SQL の例

```sql
SELECT IF(1 > 2, 3, 4 < 5, 6, 7);

┌───────────────────────────────┐
│ if((1 > 2), 3, (4 < 5), 6, 7) │
├───────────────────────────────┤
│                             6 │
└───────────────────────────────┘
```
