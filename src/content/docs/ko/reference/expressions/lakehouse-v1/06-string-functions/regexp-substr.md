---
title: REGEXP_SUBSTR (Lakehouse v1)
description: REGEXP_SUBSTR — 문자열 expr에서 정규식과 일치하는 부분 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-substr.md
---

문자열 `expr`에서 패턴 `pat`로 지정한 정규식과 일치하는 부분 문자열을 반환하며, 일치하는 항목이 없으면 NULL을 반환합니다. expr 또는 pat가 NULL이면 반환 값은 NULL입니다.

## Analyze 구문

```python
func.regexp_substr(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Analyze 예제

```python
func.regexp_substr('abc def ghi', '[a-z]+')
┌─────────────────────────────────────────────┐
│ func.regexp_substr('abc def ghi', '[a-z]+') │
├─────────────────────────────────────────────┤
│ abc                                         │
└─────────────────────────────────────────────┘
```

## SQL 구문

```sql
REGEXP_SUBSTR(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## 인수

| 인수 | 설명 |
|------------|-----------------------------------------------------------------------------------------------------------|
| expr       | 일치 여부를 검사할 문자열 expr                                                                        |
| pat        | 정규식                                                                                    |
| pos        | 선택 사항입니다. expr에서 검색을 시작할 위치입니다. 생략하면 기본값은 1입니다.                |
| occurrence | 선택 사항입니다. 검색할 일치 항목의 순번입니다. 생략하면 기본값은 1입니다.                        |
| match_type | 선택 사항입니다. 일치 방식을 지정하는 문자열입니다. 의미는 REGEXP_LIKE()에 설명된 것과 같습니다. |

## 반환 형식

`VARCHAR`

## SQL 예제

```sql
SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+');
┌────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+') │
├────────────────────────────────────────┤
│ abc                                    │
└────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3);
┌──────────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3) │
├──────────────────────────────────────────────┤
│ ghi                                          │
└──────────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3);
┌──────────────────────────────────────────────────────────────────┐
│ REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3)            │
├──────────────────────────────────────────────────────────────────┤
│ 周周周周                                                         │
└──────────────────────────────────────────────────────────────────┘

```
