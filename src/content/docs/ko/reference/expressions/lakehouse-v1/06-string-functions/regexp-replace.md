---
title: REGEXP_REPLACE (Lakehouse v1)
description: REGEXP_REPLACE — 문자열 expr에서 정규식과 일치하는 항목을 바꿉니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-replace.md
---

문자열 `expr`에서 패턴 `pat`로 지정한 정규식과 일치하는 항목을 대체 문자열 `repl`로 바꾸고 결과 문자열을 반환합니다. `expr`, `pat` 또는 `repl`이 NULL이면 반환 값은 NULL입니다.

## Analyze 구문

```python
func.regexp_replace(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Analyze 예제

```python
func.regexp_replace('a b c', 'b', 'X')
┌────────────────────────────────────────┐
│ func.regexp_replace('a b c', 'b', 'X') │
├────────────────────────────────────────┤
│ a X c                                  │
└────────────────────────────────────────┘
```

## SQL 구문

```sql
REGEXP_REPLACE(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## 인수

| 인수 | 설명 |
|------------|-------------------------------------------------------------------------------------------------------------------------|
| expr       | 일치 여부를 검사할 문자열 expr                                                                                      |
| pat        | 정규식                                                                                                  |
| repl       | 대체 문자열                                                                                                  |
| pos        | 선택 사항입니다. expr에서 검색을 시작할 위치입니다. 생략하면 기본값은 1입니다.                              |
| occurrence | 선택 사항입니다. 바꿀 일치 항목의 순번입니다. 생략하면 기본값은 0이며, 이는 "일치하는 모든 항목 바꾸기"를 의미합니다. |
| match_type | 선택 사항입니다. 일치 방식을 지정하는 문자열입니다. 의미는 REGEXP_LIKE()에 설명된 것과 같습니다.               |

## 반환 형식

`VARCHAR`

## SQL 예제

```sql
SELECT REGEXP_REPLACE('a b c', 'b', 'X');
┌───────────────────────────────────┐
│ REGEXP_REPLACE('a b c', 'b', 'X') │
├───────────────────────────────────┤
│ a X c                             │
└───────────────────────────────────┘

SELECT REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3);
┌────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3) │
├────────────────────────────────────────────────────┤
│ abc def X                                          │
└────────────────────────────────────────────────────┘

SELECT REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2);
┌───────────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2)        │
├───────────────────────────────────────────────────────────┤
│ 周 周周 X                                                 │
└───────────────────────────────────────────────────────────┘
```
