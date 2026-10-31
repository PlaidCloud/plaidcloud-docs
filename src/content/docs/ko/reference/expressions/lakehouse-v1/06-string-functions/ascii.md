---
title: ASCII (Lakehouse v1)
description: ASCII — 문자열 str의 가장 왼쪽 문자의 숫자 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ascii.md
---

문자열 str의 가장 왼쪽 문자의 숫자 값을 반환합니다.

## Analyze 구문

```python
func.ascii(<expr>)
```

## Analyze 예제

```python
func.ascii('2')
┌─────────────────┐
│ func.ascii('2') │
├─────────────────┤
│              50 │
└─────────────────┘
```

## SQL 구문

```sql
ASCII(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|-------------|
| `<expr>`  | 문자열입니다. |

## 반환 형식

`TINYINT`

## SQL 예제

```sql
SELECT ASCII('2');
┌────────────┐
│ ASCII('2') │
├────────────┤
│         50 │
└────────────┘
```
