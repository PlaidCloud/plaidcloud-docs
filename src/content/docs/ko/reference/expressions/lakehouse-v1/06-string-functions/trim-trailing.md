---
title: TRIM_TRAILING (Lakehouse v1)
description: TRIM_TRAILING — 문자열의 끝 부분에서 지정한 트림 문자열을 모두 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-trailing.md
---

문자열의 끝 부분에서 지정한 트림 문자열을 모두 제거합니다.

관련 항목:

- [RTRIM](../rtrim)
- [TRIM_LEADING](../trim-leading)

## Analyze 구문

```python
func.trim_trailing(<string>, <trim_string>)
```

## Analyze 예제

```python
func.trim_trailing('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_trailing('xxdatabendxx', 'x')  │
├──────────────────────────────────────────┤
│ xxdatabend                               │
└──────────────────────────────────────────┘
```

## SQL 구문

```sql
TRIM_TRAILING(<string>, <trim_string>)
```

## SQL 예제

```sql
SELECT TRIM_TRAILING('databendxx', 'xxx'), TRIM_TRAILING('databendxx', 'xx'), TRIM_TRAILING('databendxx', 'x');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_trailing('databendxx', 'xxx') │ trim_trailing('databendxx', 'xx') │ trim_trailing('databendxx', 'x') │
├────────────────────────────────────┼───────────────────────────────────┼──────────────────────────────────┤
│ databendxx                         │ databend                          │ databend                         │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
