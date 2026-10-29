---
title: INSTR (Lakehouse v1)
description: INSTR — 문자열 str에서 부분 문자열 substr이 처음 나타나는 위치를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/instr.md
---

문자열 str에서 부분 문자열 substr이 처음 나타나는 위치를 반환합니다.
인수의 순서가 반대라는 점을 제외하면 LOCATE()의 인수 두 개짜리 형식과 같습니다.

## Analyze 구문

```python
func.instr(<str>, <substr>)
```

## Analyze 예제

```python
func.instr('foobarbar', 'bar')
┌────────────────────────────────┐
│ func.instr('foobarbar', 'bar') │
├────────────────────────────────┤
│                              4 │
└────────────────────────────────┘
```

## SQL 구문

```sql
INSTR(<str>, <substr>)
```

## 인수

| 인수 | 설명 |
|------------|----------------|
| `<str>`    | 문자열입니다.    |
| `<substr>` | 부분 문자열입니다. |

## 반환 형식

`BIGINT`

## SQL 예제

```sql
SELECT INSTR('foobarbar', 'bar');
┌───────────────────────────┐
│ INSTR('foobarbar', 'bar') │
├───────────────────────────┤
│                         4 │
└───────────────────────────┘

SELECT INSTR('xbar', 'foobar');
┌─────────────────────────┐
│ INSTR('xbar', 'foobar') │
├─────────────────────────┤
│                       0 │
└─────────────────────────┘
```
