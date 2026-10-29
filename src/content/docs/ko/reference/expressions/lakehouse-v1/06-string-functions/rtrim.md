---
title: RTRIM (Lakehouse v1)
description: RTRIM — 지정한 제거 문자열에 포함된 모든 문자를 문자열의 오른쪽에서 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rtrim.md
---

지정한 제거 문자열에 포함된 모든 문자를 문자열의 오른쪽에서 모두 제거합니다.

참고: 

- [TRIM_TRAILING](../trim-trailing)
- [LTRIM](../ltrim)

## Analyze 구문

```python
func.rtrim(<string>, <trim_string>)
```

## Analyze 예제

```python
func.rtrim('databend'xx, 'x')
┌────────────────────────────────┐
│ func.rtrim('databendxx', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## SQL 구문

```sql
RTRIM(<string>, <trim_string>)
```

## SQL 예제

```sql
SELECT RTRIM('databendxx', 'x'), RTRIM('databendxx', 'xy');

┌──────────────────────────────────────────────────────┐
│ rtrim('databendxx', 'x') │ rtrim('databendxx', 'xy') │
├──────────────────────────┼───────────────────────────┤
│ databend                 │ databend                  │
└──────────────────────────────────────────────────────┘
```
