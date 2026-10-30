---
title: IF (Lakehouse v1)
description: IF — <cond1>이 TRUE이면 <expr1>을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/if.md
---

`<cond1>`이 TRUE이면 `<expr1>`을 반환합니다. 그렇지 않고 `<cond2>`가 TRUE이면 `<expr2>`를 반환하며, 이후도 같은 방식으로 처리합니다.

## Analyze 구문

```python
func.if_(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## Analyze 예시

```python
func.if_((1 > 2), 3, (4 < 5), 6, 7)

┌─────────────────────────────────────┐
│ func.if_((1 > 2), 3, (4 < 5), 6, 7) │
├─────────────────────────────────────┤
│                                   6 │
└─────────────────────────────────────┘
```

## SQL 구문

```sql
IF(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## SQL 예시

```sql
SELECT IF(1 > 2, 3, 4 < 5, 6, 7);

┌───────────────────────────────┐
│ if((1 > 2), 3, (4 < 5), 6, 7) │
├───────────────────────────────┤
│                             6 │
└───────────────────────────────┘
```
