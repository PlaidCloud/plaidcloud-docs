---
title: BITNOT (Lakehouse v2)
description: BITNOT — 숫자 값의 비트 NOT 연산 결과를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitnot.md
---

숫자 값의 비트 NOT 연산 결과를 반환합니다.

## Analyze 구문

```python
func.bitnot(<x>)
```

## Analyze 예제

```python
func.bitnot(0)

┌──────┐
│ '-1'  │
└──────┘
```

## SQL 구문

```sql
BITNOT(<x>)
```

## SQL 예제

```sql
SELECT BITNOT(0);

┌────┐
│ -1  │
└────┘
```
