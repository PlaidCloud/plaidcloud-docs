---
title: LOOKUP_STRING (Lakehouse v2)
description: LOOKUP_STRING — 사전에서 문자열을 조회하여 해당 ID를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/lookup-string.md
---

사전에서 문자열을 조회하여 해당 ID를 반환합니다.

## Analyze 구문

```python
func.lookup_string(<dict_table>, <value>)
```

## Analyze 예제

```python
func.lookup_string('status_dict', 'Active')

┌───┐
│ 1  │
└───┘
```

## SQL 구문

```sql
LOOKUP_STRING(<dict_table>, <value>)
```

## SQL 예제

```sql
SELECT LOOKUP_STRING('status_dict', 'Active');

┌───┐
│ 1  │
└───┘
```
