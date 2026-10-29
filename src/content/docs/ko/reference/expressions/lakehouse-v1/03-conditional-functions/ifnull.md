---
title: IFNULL (Lakehouse v1)
description: IFNULL — <expr1>이 NULL이면 <expr2>를 반환하고, 그렇지 않으면 <expr1>을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/ifnull.md
---

`<expr1>`이 NULL이면 `<expr2>`를 반환하고, 그렇지 않으면 `<expr1>`을 반환합니다.

## Analyze 구문

```python
func.ifnull(<expr1>, <expr2>)
```

## Analyze 예시

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

## SQL 구문

```sql
IFNULL(<expr1>, <expr2>)
```

## 별칭

- [NVL](../nvl)

## SQL 예시

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
