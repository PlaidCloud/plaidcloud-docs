---
title: REGEXP_INSTR (Lakehouse v1)
description: REGEXP_INSTR — 문자열 expr에서 패턴 pat로 지정한 정규식과 일치하는 부분 문자열의 시작 인덱스를 반환하며, 일치하는 항목이 없으면 0을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-instr.md
---

문자열 `expr`에서 패턴 `pat`로 지정한 정규식과 일치하는 부분 문자열의 시작 인덱스를 반환하며, 일치하는 항목이 없으면 `0`을 반환합니다. `expr` 또는 `pat`가 NULL이면 반환 값은 NULL입니다. 문자 인덱스는 `1`부터 시작합니다.

## Analyze 구문

```python
func.regexp_instr(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Analyze 예제

```python
func.regexp_instr('dog cat dog', 'dog')
┌─────────────────────────────────────────┐
│ func.regexp_instr('dog cat dog', 'dog') │
├─────────────────────────────────────────┤
│                                       1 │
└─────────────────────────────────────────┘
```

## SQL 구문

```sql
REGEXP_INSTR(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## 인수

| 인수 | 설명 |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expr          | 일치 여부를 검사할 문자열 expr                                                                                                                                                                                                                                     |
| pat           | 정규식                                                                                                                                                                                                                                                 |
| pos           | 선택 사항입니다. expr에서 검색을 시작할 위치입니다. 생략하면 기본값은 1입니다.                                                                                                                                                                             |
| occurrence    | 선택 사항입니다. 검색할 일치 항목의 순번입니다. 생략하면 기본값은 1입니다.                                                                                                                                                                                     |
| return_option | 선택 사항입니다. 반환할 위치의 유형입니다. 이 값이 0이면 REGEXP_INSTR()는 일치한 부분 문자열의 첫 번째 문자 위치를 반환합니다. 이 값이 1이면 REGEXP_INSTR()는 일치한 부분 문자열 바로 다음 위치를 반환합니다. 생략하면 기본값은 0입니다. |
| match_type    | 선택 사항입니다. 일치 방식을 지정하는 문자열입니다. 의미는 REGEXP_LIKE()에 설명된 것과 같습니다.                                                                                                                                                              |

## 반환 형식

숫자 데이터 형식 값입니다.

## SQL 예제

```sql
SELECT REGEXP_INSTR('dog cat dog', 'dog');
┌────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog') │
├────────────────────────────────────┤
│                                  1 │
└────────────────────────────────────┘

SELECT REGEXP_INSTR('dog cat dog', 'dog', 2);
┌───────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog', 2) │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{2}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{2}') │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{4}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{4}') │
├─────────────────────────────────────┤
│                                   8 │
└─────────────────────────────────────┘
```
