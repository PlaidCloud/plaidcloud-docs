---
title: BITOR (Lakehouse v2)
description: BITOR — 두 숫자 값의 비트 OR 연산 결과를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitor.md
---

두 숫자 값의 비트 OR 연산 결과를 반환합니다.

## Analyze 구문

```python
func.bitor(<x>, <y>)
```

## Analyze 예제

```python
func.bitor(12, 10)

┌────┐
│ 14  │
└────┘
```

## SQL 구문

```sql
BITOR(<x>, <y>)
```

## SQL 예제

```sql
SELECT BITOR(12, 10);

┌────┐
│ 14  │
└────┘
```
