---
title: BIT_LENGTH (Lakehouse v1)
description: BIT_LENGTH — 문자열의 길이를 비트 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bit-length.md
---

문자열의 길이를 비트 단위로 반환합니다.

## Analyze 구문

```python
func.bit_length(<expr>)
```

## Analyze 예제

```python
func.bit_length('Word')
┌─────────────────────────┐
│ func.bit_length('Word') │
├─────────────────────────┤
│                      32 │
└─────────────────────────┘
```

## SQL 구문

```sql
BIT_LENGTH(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------| ----------- |
| `<expr>`  | 문자열입니다. |

## 반환 형식

`BIGINT`

## SQL 예제

```sql
SELECT BIT_LENGTH('Word');
┌────────────────────────────┐
│ SELECT BIT_LENGTH('Word'); │
├────────────────────────────┤
│ 32                         │
└────────────────────────────┘
```
