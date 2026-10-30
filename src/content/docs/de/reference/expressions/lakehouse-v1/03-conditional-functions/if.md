---
title: IF (Lakehouse v1)
description: IF – wenn <cond1> TRUE ist, wird <expr1> zurückgegeben.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/if.md
---

Wenn `<cond1>` TRUE ist, wird `<expr1>` zurückgegeben. Andernfalls wird `<expr2>` zurückgegeben, wenn `<cond2>` TRUE ist, und so weiter.

## Analyze-Syntax

```python
func.if_(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## Analyze-Beispiele

```python
func.if_((1 > 2), 3, (4 < 5), 6, 7)

┌─────────────────────────────────────┐
│ func.if_((1 > 2), 3, (4 < 5), 6, 7) │
├─────────────────────────────────────┤
│                                   6 │
└─────────────────────────────────────┘
```

## SQL-Syntax

```sql
IF(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## SQL-Beispiele

```sql
SELECT IF(1 > 2, 3, 4 < 5, 6, 7);

┌───────────────────────────────┐
│ if((1 > 2), 3, (4 < 5), 6, 7) │
├───────────────────────────────┤
│                             6 │
└───────────────────────────────┘
```
