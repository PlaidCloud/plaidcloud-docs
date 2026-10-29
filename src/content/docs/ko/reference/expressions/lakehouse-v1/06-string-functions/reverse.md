---
title: REVERSE (Lakehouse v1)
description: REVERSE — 문자열 str의 문자 순서를 뒤집은 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/reverse.md
---

문자열 str의 문자 순서를 뒤집은 문자열을 반환합니다.

## Analyze 구문

```python
func.reverse(<str>)
```

## Analyze 예제

```python
func.reverse('abc')
┌──────────────────────┐
│ func..reverse('abc') │
├──────────────────────┤
│ cba                  │
└──────────────────────┘
```

## SQL 구문

```sql
REVERSE(<str>)
```

## 인수

| 인수 | 설명 |
|-----------|-------------------|
| `<str>`   | 문자열 값입니다. |

## 반환 형식

`VARCHAR`

## SQL 예제

```sql
SELECT REVERSE('abc');
┌────────────────┐
│ REVERSE('abc') │
├────────────────┤
│ cba            │
└────────────────┘
```
