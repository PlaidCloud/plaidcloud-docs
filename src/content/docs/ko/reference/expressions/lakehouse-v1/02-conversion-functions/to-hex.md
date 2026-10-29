---
title: TO_HEX (Lakehouse v1)
description: TO_HEX — 문자열 인수 str에 대해 str의 각 문자의 각 바이트를 두 자리 16진수로 변환한 16진수 문자열 표현을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-hex.md
---

문자열 인수 str의 경우, TO_HEX()는 str에 있는 각 문자의 각 바이트를 두 자리 16진수로 변환한 16진수 문자열 표현을 반환합니다. 이 연산의 역연산은 UNHEX() 함수가 수행합니다.

숫자 인수 N의 경우, TO_HEX()는 N의 값을 longlong(BIGINT) 숫자로 취급한 16진수 문자열 표현을 반환합니다.

## Analyze 구문

```python
func.to_hex(<expr>)
```

## Analyze 예제

```python
func.to_hex('abc')

┌────────────────────┐
│ func.to_hex('abc') │
├────────────────────┤
│ 616263             │
└────────────────────┘
```

## SQL 구문

```sql
TO_HEX(<expr>)
```

## 별칭

- [HEX](../../06-string-functions/hex)

## SQL 예제

```sql
SELECT HEX('abc'), TO_HEX('abc');

┌────────────────────────────┐
│ hex('abc') │ to_hex('abc') │
├────────────┼───────────────┤
│ 616263     │ 616263        │
└────────────────────────────┘

SELECT HEX(255), TO_HEX(255);

┌────────────────────────┐
│ hex(255) │ to_hex(255) │
├──────────┼─────────────┤
│ ff       │ ff          │
└────────────────────────┘
```
