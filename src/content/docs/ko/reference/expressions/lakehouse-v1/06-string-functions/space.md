---
title: SPACE (Lakehouse v1)
description: SPACE — N개의 공백 문자로 구성된 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/space.md
---

N개의 공백 문자로 구성된 문자열을 반환합니다.

## Analyze 구문

```python
func.space(<n>)
```

## Analyze 예제

```python
func.space(20)
┌─────────────────┐
│ func.space(20)  │
├─────────────────┤
│                 │
└─────────────────┘
```

## SQL 구문

```sql
SPACE(<n>);
```

## 인수

| 인수 | 설명 |
|-----------|----------------------|
| `<n>`     | 공백의 수 |

## 반환 형식

문자열 데이터 형식 값입니다.

## SQL 예제

```sql
SELECT SPACE(20)
┌──────────────────────┐
│ SPACE(20)            │
├──────────────────────┤
│                      │
└──────────────────────┘
```
