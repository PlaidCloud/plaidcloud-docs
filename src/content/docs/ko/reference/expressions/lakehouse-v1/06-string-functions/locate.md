---
title: LOCATE (Lakehouse v1)
description: LOCATE — 첫 번째 구문은 문자열 str에서 부분 문자열 substr이 처음 나타나는 위치를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/locate.md
---

첫 번째 구문은 문자열 str에서 부분 문자열 substr이 처음 나타나는 위치를 반환합니다.
두 번째 구문은 위치 pos부터 시작하여 문자열 str에서 부분 문자열 substr이 처음 나타나는 위치를 반환합니다.
substr이 str에 없으면 0을 반환합니다. 인수 중 하나라도 NULL이면 NULL을 반환합니다.

## Analyze 구문

```python
func.locate(<substr>, <str>, <pos>)
```

## Analyze 예제

```python
func.locate('bar', 'foobarbar')
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar') │
├────────────────────────────────────┤
│                                  5 │
└────────────────────────────────────┘
```

```python
func.locate('bar', 'foobarbar', 5)
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar', 5) │
├────────────────────────────────────┤
│                                  7 │
└────────────────────────────────────┘
```

## SQL 구문

```sql
LOCATE(<substr>, <str>)
LOCATE(<substr>, <str>, <pos>)
```

## 인수

| 인수 | 설명 |
|------------|----------------|
| `<substr>` | 부분 문자열입니다. |
| `<str>`    | 문자열입니다.    |
| `<pos>`    | 위치입니다.  |

## 반환 형식

`BIGINT`

## SQL 예제

```sql
SELECT LOCATE('bar', 'foobarbar')
┌────────────────────────────┐
│ LOCATE('bar', 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT LOCATE('xbar', 'foobar')
┌──────────────────────────┐
│ LOCATE('xbar', 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘

SELECT LOCATE('bar', 'foobarbar', 5)
┌───────────────────────────────┐
│ LOCATE('bar', 'foobarbar', 5) │
├───────────────────────────────┤
│                             7 │
└───────────────────────────────┘
```
