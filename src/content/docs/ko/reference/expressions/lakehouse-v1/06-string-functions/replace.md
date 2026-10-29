---
title: REPLACE (Lakehouse v1)
description: REPLACE — 문자열 str에서 문자열 from_str이 나타나는 모든 위치를 문자열 to_str로 바꾼 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/replace.md
---

문자열 str에서 문자열 from_str이 나타나는 모든 위치를 문자열 to_str로 바꾼 문자열을 반환합니다.

## Analyze 구문

```python
func.replace(<str>, <from_str>, <to_str>)
```

## Analyze 예제

```python
func.replace(<str>, <from_str>, <to_str>)
┌──────────────────────────────────────┐
│ func.replace('plaidCloud', 'p', 'P') │
├──────────────────────────────────────┤
│ PlaidCloud                           │
└──────────────────────────────────────┘
```

## SQL 구문

```sql
REPLACE(<str>, <from_str>, <to_str>)
```

## 인수

| 인수 | 설명 |
|--------------|------------------|
| `<str>`      | 문자열입니다.      |
| `<from_str>` | 바꿀 대상 문자열입니다. |
| `<to_str>`   | 대체할 문자열입니다.   |

## 반환 형식

`VARCHAR`

## SQL 예제

```sql
SELECT REPLACE('www.mysql.com', 'w', 'Ww');
┌─────────────────────────────────────┐
│ REPLACE('www.mysql.com', 'w', 'Ww') │
├─────────────────────────────────────┤
│ WwWwWw.mysql.com                    │
└─────────────────────────────────────┘
```
