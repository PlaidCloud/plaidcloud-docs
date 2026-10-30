---
title: NVL2 (Lakehouse v1)
description: NVL2 — <expr1>이 NULL이 아니면 <expr2>를 반환하고, 그렇지 않으면 <expr3>을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nvl2.md
---

`<expr1>`이 NULL이 아니면 `<expr2>`를 반환하고, 그렇지 않으면 `<expr3>`을 반환합니다.

## Analyze 구문

```python
func.nvl2(<expr1> , <expr2> , <expr3>)
```

## Analyze 예시

```python
func.nvl2('a', 'b', 'c'), func.nvl2(null, 'b', 'c')

┌──────────────────────────────────────────────────────┐
│ func.nvl2('a', 'b', 'c') │ func.nvl2(null, 'b', 'c') │
├──────────────────────────┼───────────────────────────┤
│ b                        │ c                         │
└──────────────────────────────────────────────────────┘

func.nvl2(1, 2, 3), func.nvl2(null, 2, 3)

┌────────────────────────────────────────────┐
│ func.nvl2(1, 2, 3) │ func.nvl2(null, 2, 3) │
├────────────────────┼───────────────────────┤
│                  2 │                     3 │
└────────────────────────────────────────────┘
```

## SQL 구문

```sql
NVL2(<expr1> , <expr2> , <expr3>)
```

## SQL 예시

```sql
SELECT NVL2('a', 'b', 'c'), NVL2(NULL, 'b', 'c');

┌────────────────────────────────────────────┐
│ nvl2('a', 'b', 'c') │ nvl2(null, 'b', 'c') │
├─────────────────────┼──────────────────────┤
│ b                   │ c                    │
└────────────────────────────────────────────┘

SELECT NVL2(1, 2, 3), NVL2(NULL, 2, 3);

┌──────────────────────────────────┐
│ nvl2(1, 2, 3) │ nvl2(null, 2, 3) │
├───────────────┼──────────────────┤
│             2 │                3 │
└──────────────────────────────────┘
```
