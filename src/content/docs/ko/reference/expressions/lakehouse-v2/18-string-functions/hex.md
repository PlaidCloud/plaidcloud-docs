---
title: HEX (Lakehouse v2)
description: HEX — 문자열 또는 숫자의 16진수 표현을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex.md
---

문자열 또는 숫자의 16진수 표현을 반환합니다.

## Analyze 구문

```python
func.hex(<expr>)
```

## Analyze 예제

```python
func.hex(255)

┌──────┐
│ 'FF'  │
└──────┘
```

## SQL 구문

```sql
HEX(<expr>)
```

## SQL 예제

```sql
SELECT HEX(255);

┌────┐
│ FF  │
└────┘
```
