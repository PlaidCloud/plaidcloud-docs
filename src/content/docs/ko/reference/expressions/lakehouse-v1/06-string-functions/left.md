---
title: LEFT (Lakehouse v1)
description: LEFT — 문자열 str의 왼쪽에서 len개의 문자를 반환하며, 인수 중 하나라도 NULL이면 NULL을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/left.md
---

문자열 str의 왼쪽에서 len개의 문자를 반환하며, 인수 중 하나라도 NULL이면 NULL을 반환합니다.

## Analyze 구문

```python
func.left(<str>, <len>)
```

## Analyze 예제

```python
func.left('foobarbar', 5)
┌───────────────────────────┐
│ func.left('foobarbar', 5) │
├───────────────────────────┤
│ fooba                     │
└───────────────────────────┘
```

## SQL 구문

```sql
LEFT(<str>, <len>);
```

## 인수

| 인수 | 설명 |
|-----------|----------------------------------------------------------|
| `<str>`   | 문자를 추출할 원본 문자열 |
| `<len>`   | 문자 수                                  |

## 반환 형식

`VARCHAR`

## SQL 예제

```sql
SELECT LEFT('foobarbar', 5);
┌──────────────────────┐
│ LEFT('foobarbar', 5) │
├──────────────────────┤
│ fooba                │
└──────────────────────┘
```
