---
title: TO_BASE64 (Lakehouse v1)
description: TO_BASE64 — 문자열 인수를 base-64 인코딩 형태로 변환하고 결과를 문자열로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/to-base64.md
---

문자열 인수를 base-64 인코딩 형태로 변환하고 결과를 문자열로 반환합니다.
인수가 문자열이 아니면 변환하기 전에 문자열로 변환됩니다.
인수가 NULL이면 결과는 NULL입니다.

## Analyze 구문

```python
func.to_base64(<v>)
```

## Analyze 예제

```python
func.to_base64('abc')
┌───────────────────────┐
│ func.to_base64('abc') │
├───────────────────────┤
│ YWJj                  │
└───────────────────────┘
```

## SQL 구문

```sql
TO_BASE64(<v>)
```

## 인수

| 인수 | 설명 |
|-----------|-------------|
| `<v>`     | 값입니다.  |

## 반환 형식

`VARCHAR`

## SQL 예제

```sql
SELECT TO_BASE64('abc');
┌──────────────────┐
│ TO_BASE64('abc') │
├──────────────────┤
│ YWJj             │
└──────────────────┘
```
