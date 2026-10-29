---
title: INSERT (Lakehouse v1)
description: INSERT — 문자열 str에서 위치 pos부터 시작하는 len 길이의 부분 문자열을 newstr로 바꾼 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/insert.md
---

문자열 str에서 위치 pos부터 시작하는 len 길이의 부분 문자열을 문자열 newstr로 바꾼 결과를 반환합니다. pos가 문자열 길이 범위를 벗어나면 원래 문자열을 반환합니다. len이 위치 pos 이후 나머지 문자열의 길이 범위를 벗어나면 위치 pos부터 문자열의 나머지 부분을 모두 바꿉니다. 인수 중 하나라도 NULL이면 NULL을 반환합니다.

## Analyze 구문

```python
func.insert(<str>, <pos>, <len>, <newstr>)
```

## Analyze 예제

```python
func.insert('Quadratic', 3, 4, 'What')
┌────────────────────────────────────────┐
│ func.insert('Quadratic', 3, 4, 'What') │
├────────────────────────────────────────┤
│ QuWhattic                              │
└────────────────────────────────────────┘
```

## SQL 구문

```sql
INSERT(<str>, <pos>, <len>, <newstr>)
```

## 인수

| 인수 | 설명 |
|------------|-----------------|
| `<str>`    | 문자열입니다.     |
| `<pos>`    | 위치입니다.   |
| `<len>`    | 길이입니다.     |
| `<newstr>` | 새 문자열입니다. |

## 반환 형식

`VARCHAR`

## SQL 예제

```sql
SELECT INSERT('Quadratic', 3, 4, 'What');
┌───────────────────────────────────┐
│ INSERT('Quadratic', 3, 4, 'What') │
├───────────────────────────────────┤
│ QuWhattic                         │
└───────────────────────────────────┘

SELECT INSERT('Quadratic', -1, 4, 'What');
┌───────────────────────────────────────┐
│ INSERT('Quadratic', (- 1), 4, 'What') │
├───────────────────────────────────────┤
│ Quadratic                             │
└───────────────────────────────────────┘

SELECT INSERT('Quadratic', 3, 100, 'What');
┌─────────────────────────────────────┐
│ INSERT('Quadratic', 3, 100, 'What') │
├─────────────────────────────────────┤
│ QuWhat                              │
└─────────────────────────────────────┘

┌────────────────────────────────────────────┬────────┐
│ INSERT('123456789', number, number, 'aaa') │ number │
├────────────────────────────────────────────┼────────┤
│ 123456789                                  │      0 │
│ aaa23456789                                │      1 │
│ 1aaa456789                                 │      2 │
│ 12aaa6789                                  │      3 │
│ 123aaa89                                   │      4 │
│ 1234aaa                                    │      5 │
│ 12345aaa                                   │      6 │
│ 123456aaa                                  │      7 │
│ 1234567aaa                                 │      8 │
│ 12345678aaa                                │      9 │
│ 123456789                                  │     10 │
│ 123456789                                  │     11 │
│ 123456789                                  │     12 │
└────────────────────────────────────────────┴────────┘
```
