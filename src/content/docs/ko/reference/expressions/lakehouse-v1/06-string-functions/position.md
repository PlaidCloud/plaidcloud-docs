---
title: POSITION (Lakehouse v1)
description: POSITION — POSITION(substr IN str)은 LOCATE(substr,str)의 동의어입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/position.md
---

POSITION(substr IN str)은 LOCATE(substr,str)의 동의어입니다.
문자열 str에서 부분 문자열 substr이 처음 나타나는 위치를 반환합니다.
substr이 str에 없으면 0을 반환합니다. 인수 중 하나라도 NULL이면 NULL을 반환합니다.

## Analyze 구문

```python
func.position(<substr>, <str>)
```

## Analyze 예제

```python
func.position('bar', 'foobarbar')
┌───────────────────────────────────┐
│ func.position('bar', 'foobarbar') │
├───────────────────────────────────┤
│                                 4 │
└───────────────────────────────────┘
```

## SQL 구문

```sql
POSITION(<substr> IN <str>)
```

## 인수

| 인수 | 설명 |
|------------|----------------|
| `<substr>` | 부분 문자열입니다. |
| `<str>`    | 문자열입니다.    |

## 반환 형식

`BIGINT`

## SQL 예제

```sql
SELECT POSITION('bar' IN 'foobarbar')
┌────────────────────────────┐
│ POSITION('bar' IN 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT POSITION('xbar' IN 'foobar')
┌──────────────────────────┐
│ POSITION('xbar' IN 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘
```
