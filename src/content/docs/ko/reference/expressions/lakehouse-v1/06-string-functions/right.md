---
title: RIGHT (Lakehouse v1)
description: RIGHT — 문자열 str의 오른쪽에서 len개의 문자를 반환하며, 인수 중 하나라도 NULL이면 NULL을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/right.md
---

문자열 str의 오른쪽에서 len개의 문자를 반환하며, 인수 중 하나라도 NULL이면 NULL을 반환합니다.

## Analyze 구문

```python
func.right(<str>, <len>)
```

## Analyze 예제

```python
func.right('foobarbar', 4)
┌────────────────────────────┐
│ func.right('foobarbar', 4) │
├────────────────────────────┤
│ rbar                       │
└────────────────────────────┘
```

## SQL 구문

```sql
RIGHT(<str>, <len>);
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
SELECT RIGHT('foobarbar', 4);
┌───────────────────────┐
│ RIGHT('foobarbar', 4) │
├───────────────────────┤
│ rbar                  │
└───────────────────────┘
```
