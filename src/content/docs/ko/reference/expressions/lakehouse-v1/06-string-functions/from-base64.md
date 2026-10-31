---
title: FROM_BASE64 (Lakehouse v1)
description: FROM_BASE64 — base-64 인코딩 규칙으로 인코딩된 문자열을 받아 디코딩한 결과를 이진 값으로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/from-base64.md
---

base-64 인코딩 규칙으로 인코딩된 문자열을 받아 디코딩한 결과를 이진 값으로 반환합니다.
인수가 NULL이거나 유효한 base-64 문자열이 아니면 결과는 NULL입니다.

## Analyze 구문

```python
func.from_base64(<expr>)
```

## Analyze 예제

```python
func.from_base64('YWJj')
┌──────────────────────────┐
│ func.from_base64('YWJj') │
├──────────────────────────┤
│ abc                      │
└──────────────────────────┘
```

## SQL 구문

```sql
FROM_BASE64(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|-------------------|
| `<expr>`  | 문자열 값입니다. |

## 반환 형식

`BINARY`

## SQL 예제

```sql
SELECT TO_BASE64('abc'), FROM_BASE64(TO_BASE64('abc')) as b, b::String;
┌───────────────────────────────────────┐
│ to_base64('abc') │    b   │ b::string │
│      String      │ Binary │   String  │
├──────────────────┼────────┼───────────┤
│ YWJj             │ 616263 │ abc       │
└───────────────────────────────────────┘
```
