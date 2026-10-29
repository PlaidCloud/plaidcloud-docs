---
title: LTRIM (Lakehouse v1)
description: LTRIM — 지정한 제거 문자열에 포함된 모든 문자를 문자열의 왼쪽에서 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ltrim.md
---

지정한 제거 문자열에 포함된 모든 문자를 문자열의 왼쪽에서 모두 제거합니다.

참고: 

- [TRIM_LEADING](../trim-leading)
- [RTRIM](../rtrim)

## Analyze 구문

```python
func.ltrim(<string>, <trim_string>)
```

## Analyze 예제

```python
func.ltrim('xxdatabend', 'x')
┌────────────────────────────────┐
│ func.ltrim('xxdatabend', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## SQL 구문

```sql
LTRIM(<string>, <trim_string>)
```

## SQL 예제

```sql
SELECT LTRIM('xxdatabend', 'xx'), LTRIM('xxdatabend', 'xy');

┌───────────────────────────────────────────────────────┐
│ ltrim('xxdatabend', 'xx') │ ltrim('xxdatabend', 'xy') │
├───────────────────────────┼───────────────────────────┤
│ databend                  │ databend                  │
└───────────────────────────────────────────────────────┘
```
