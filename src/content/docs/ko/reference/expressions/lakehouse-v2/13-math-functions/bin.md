---
title: BIN (Lakehouse v2)
description: BIN — 정수의 이진 문자열 표현을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/bin.md
---

정수의 이진 문자열 표현을 반환합니다.

## Analyze 구문

```python
func.bin(<x>)
```

## Analyze 예제

```python
func.bin(10)

┌────────┐
│ '1010'  │
└────────┘
```

## SQL 구문

```sql
BIN(<x>)
```

## SQL 예제

```sql
SELECT BIN(10);

┌──────┐
│ 1010  │
└──────┘
```
