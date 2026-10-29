---
title: OCT (Lakehouse v1)
description: OCT — N의 8진수 값을 문자열 표현으로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/oct.md
---

N의 8진수 값을 문자열 표현으로 반환합니다.

## Analyze 구문

```python
func.oct(<expr>)
```

## Analyze 예제

```python
func.oct(12)
┌─────────────────┐
│ func.oct(12)    │
├─────────────────┤
│ 014             │
└─────────────────┘
```

## SQL 구문

```sql
OCT(<expr>)
```

## SQL 예제

```sql
SELECT OCT(12);
┌─────────┐
│ OCT(12) │
├─────────┤
│ 014     │
└─────────┘
```
