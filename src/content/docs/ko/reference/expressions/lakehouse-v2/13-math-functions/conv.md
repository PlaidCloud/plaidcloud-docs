---
title: CONV (Lakehouse v2)
description: CONV — 숫자를 한 진법에서 다른 진법으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/conv.md
---

숫자를 한 진법에서 다른 진법으로 변환합니다.

## Analyze 구문

```python
func.conv(<num>, <from_base>, <to_base>)
```

## Analyze 예제

```python
func.conv('ff', 16, 10)

┌───────┐
│ '255'  │
└───────┘
```

## SQL 구문

```sql
CONV(<num>, <from_base>, <to_base>)
```

## SQL 예제

```sql
SELECT CONV('ff', 16, 10);

┌─────┐
│ 255  │
└─────┘
```
