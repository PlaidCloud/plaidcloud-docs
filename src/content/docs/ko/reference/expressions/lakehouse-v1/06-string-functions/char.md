---
title: CHAR (Lakehouse v1)
description: CHAR — 전달한 각 정수에 해당하는 문자를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/char.md
---

전달한 각 정수에 해당하는 문자를 반환합니다.

## Analyze 구문

```python
func.char(N,...)
```

## Analyze 예제

```python
func.char(77,121,83,81,76)
┌─────────────────────────────┐
│ func.char(77,121,83,81,76) │
├─────────────────────────────┤
│ 4D7953514C                  │
└─────────────────────────────┘
```

## SQL 구문

```sql
CHAR(N, ...)
```

## 인수

| 인수 | 설명 |
|-----------|----------------|
| N         | 숫자 열 |

## 반환 형식

`BINARY`

## SQL 예제

이 예제는 반환된 이진 값과 문자열 표현을 모두 보여 줍니다.

```sql
SELECT CHAR(77,121,83,81,76) as a, a::String;
┌────────────────────────┐
│      a     │ a::string │
│   Binary   │   String  │
├────────────┼───────────┤
│ 4D7953514C │ MySQL     │
└────────────────────────┘
```
