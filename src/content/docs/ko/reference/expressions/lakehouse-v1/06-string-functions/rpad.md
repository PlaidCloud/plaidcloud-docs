---
title: RPAD (Lakehouse v1)
description: RPAD — 문자열 str의 오른쪽을 문자열 padstr로 채워 len 문자 길이로 만든 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rpad.md
---

문자열 str의 오른쪽을 문자열 padstr로 채워 len 문자 길이로 만든 문자열을 반환합니다.
str이 len보다 길면 반환 값은 len 문자로 잘립니다.

## Analyze 구문

```python
func.rpad(<str>, <len>, <padstr>)
```

## Analyze 예제

```python
func.rpad('hi',5,'?')
┌───────────────────────┐
│ func.rpad('hi',5,'?') │
├───────────────────────┤
│ hi???                 │
└───────────────────────┘

func.rpad('hi',1,'?')
┌───────────────────────┐
│ func.rpad('hi',1,'?') │
├───────────────────────┤
│ h                     │
└───────────────────────┘
```

## SQL 구문

```sql
RPAD(<str>, <len>, <padstr>)
```

## 인수

| 인수 | 설명 |
|------------|-----------------|
| `<str>`    | 문자열입니다.     |
| `<len>`    | 길이입니다.     |
| `<padstr>` | 채움 문자열입니다. |

## 반환 형식

`VARCHAR`

## SQL 예제

```sql
SELECT RPAD('hi',5,'?');
┌────────────────────┐
│ RPAD('hi', 5, '?') │
├────────────────────┤
│ hi???              │
└────────────────────┘

SELECT RPAD('hi',1,'?');
┌────────────────────┐
│ RPAD('hi', 1, '?') │
├────────────────────┤
│ h                  │
└────────────────────┘
```
