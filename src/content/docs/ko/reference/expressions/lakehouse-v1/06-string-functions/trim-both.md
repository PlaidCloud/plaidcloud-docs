---
title: TRIM_BOTH (Lakehouse v1)
description: TRIM_BOTH — 지정한 제거 문자열이 문자열의 시작, 끝 또는 양쪽에 나타나는 모든 항목을 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-both.md
---

지정한 제거 문자열이 문자열의 시작, 끝 또는 양쪽에 나타나는 모든 항목을 제거합니다.

참고: [TRIM](../trim)

## Analyze 구문

```python
func.trim_both(<string>, <trim_string>)
```

## Analyze 예제

```python
func.trim_both('xxdatabendxx', 'x')
┌──────────────────────────────────────┐
│ func.trim_both('xxdatabendxx', 'x')  │
├──────────────────────────────────────┤
│ databend                             │
└──────────────────────────────────────┘
```

## SQL 구문

```sql
TRIM_BOTH(<string>, <trim_string>)
```

## SQL 예제

```sql
SELECT TRIM_BOTH('xxdatabendxx', 'xxx'), TRIM_BOTH('xxdatabendxx', 'xx'), TRIM_BOTH('xxdatabendxx', 'x');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_both('xxdatabendxx', 'xxx') │ trim_both('xxdatabendxx', 'xx') │ trim_both('xxdatabendxx', 'x') │
├──────────────────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ xxdatabendxx                     │ databend                        │ databend                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
