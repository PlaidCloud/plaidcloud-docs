---
title: BIN (Lakehouse v1)
description: BIN — N의 이진 값을 문자열 표현으로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bin.md
---

N의 이진 값을 문자열 표현으로 반환합니다.

## Analyze 구문

```python
func.bin(<expr>)
```

## Analyze 예제

```python
func.bin(12)
┌──────────────┐
│ func.bin(12) │
├──────────────┤
│ 1100         │
└──────────────┘
```

## SQL 구문

```sql
BIN(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|-------------|
| `<expr>`  | 숫자입니다. |

## 반환 형식

`VARCHAR`

## SQL 예제

```sql
SELECT BIN(12);
┌─────────┐
│ BIN(12) │
├─────────┤
│ 1100    │
└─────────┘
```
