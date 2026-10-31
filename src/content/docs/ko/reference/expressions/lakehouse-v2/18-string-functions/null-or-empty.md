---
title: NULL_OR_EMPTY (Lakehouse v2)
description: NULL_OR_EMPTY — 문자열이 NULL이거나 비어 있는지 확인합니다. 해당하면 1을, 아니면 0을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/null-or-empty.md
---

문자열이 NULL이거나 비어 있는지 확인합니다. 해당하면 1을, 아니면 0을 반환합니다.

## Analyze 구문

```python
func.null_or_empty(<str>)
```

## Analyze 예제

```python
func.null_or_empty('')

┌───┐
│ 1  │
└───┘
```

## SQL 구문

```sql
NULL_OR_EMPTY(<str>)
```

## SQL 예제

```sql
SELECT NULL_OR_EMPTY('');

┌───┐
│ 1  │
└───┘
```
