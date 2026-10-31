---
title: "GROUP_CONCAT (String, Lakehouse v2)"
description: GROUP_CONCAT — 그룹의 값을 구분자로 연결하여 하나의 문자열로 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/group-concat.md
---

그룹의 값을 구분자로 연결하여 하나의 문자열로 만듭니다.

## Analyze 구문

```python
func.group_concat(<expr> [SEPARATOR '<sep>'])
```

## Analyze 예제

```python
func.group_concat(get_column(table, 'name'))

┌─────────────────────┐
│ 'Alice,Bob,Charlie'  │
└─────────────────────┘
```

## SQL 구문

```sql
GROUP_CONCAT(<expr> [SEPARATOR '<sep>'])
```

## SQL 예제

```sql
SELECT GROUP_CONCAT(name ORDER BY name SEPARATOR ', ') FROM employees;

┌─────────────────────┐
│ Alice, Bob, Charlie  │
└─────────────────────┘
```
