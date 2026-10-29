---
title: TRIM_LEADING (Lakehouse v1)
description: TRIM_LEADING — 문자열의 시작 부분에서 지정한 트림 문자열을 모두 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-leading.md
---

문자열의 시작 부분에서 지정한 트림 문자열을 모두 제거합니다.

관련 항목:

- [LTRIM](../ltrim)
- [TRIM_TRAILING](../trim-trailing)

## Analyze 구문

```python
func.trim_leading(<string>, <trim_string>)
```

## Analyze 예제

```python
func.trim_leading('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_leading('xxdatabendxx', 'x')   │
├──────────────────────────────────────────┤
│ databendxx                               │
└──────────────────────────────────────────┘
```

## SQL 구문

```sql
TRIM_LEADING(<string>, <trim_string>)
```

## SQL 예제

```sql
SELECT TRIM_LEADING('xxdatabend', 'xxx'), TRIM_LEADING('xxdatabend', 'xx'), TRIM_LEADING('xxdatabend', 'x');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_leading('xxdatabend', 'xxx') │ trim_leading('xxdatabend', 'xx') │ trim_leading('xxdatabend', 'x') │
├───────────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ xxdatabend                        │ databend                         │ databend                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
