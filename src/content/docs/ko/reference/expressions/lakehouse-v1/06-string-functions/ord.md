---
title: ORD (Lakehouse v1)
description: ORD — 문자열의 가장 왼쪽 문자의 문자 코드를 반환합니다(단일 바이트는 ASCII 값, 멀티바이트는 계산된 값).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ord.md
---

가장 왼쪽 문자가 멀티바이트 문자가 아니면 ORD()는 ASCII() 함수와 같은 값을 반환합니다.

문자열 str의 가장 왼쪽 문자가 멀티바이트 문자이면 구성 바이트의 숫자 값으로 다음 공식에 따라
계산한 해당 문자의 코드를 반환합니다.

```sql
  (1st byte code)
+ (2nd byte code * 256)
+ (3rd byte code * 256^2) ...
```

## Analyze 구문

```python
func.ord(<str>)
```

## Analyze 예제

```python
func.ord('2')
┌────────────────┐
│ func.ord('2)   │
├────────────────┤
│             50 │
└────────────────┘
```

## SQL 구문

```sql
ORD(<str>)
```

## 인수

| 인수 | 설명 |
|-----------|-------------|
| `<str>`   | 문자열입니다. |

## 반환 형식

`BIGINT`

## SQL 예제

```sql
SELECT ORD('2')
┌────────┐
│ ORD(2) │
├────────┤
│     50 │
└────────┘
```
