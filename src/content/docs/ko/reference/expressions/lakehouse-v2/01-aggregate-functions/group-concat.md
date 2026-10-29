---
title: "GROUP_CONCAT (집계, Lakehouse v2)"
description: GROUP_CONCAT — 그룹의 값을 구분자로 연결하여 하나의 문자열로 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/group-concat.md
---

그룹의 값을 구분자로 연결하여 하나의 문자열로 만듭니다.

## Analyze 구문

```python
func.group_concat(get_column(table, 'name'), literal(','))
```

## Analyze 예제

```python
func.group_concat(get_column(table, 'name'))
```

## SQL 구문

```sql
GROUP_CONCAT(<name>, literal(','))
```

## SQL 예제

```sql
SELECT department, GROUP_CONCAT(name ORDER BY name SEPARATOR ', ')
FROM employees GROUP BY department;

┌────────────┬──────────────────────────┐
│ department │ group_concat(name)       │
├────────────┼──────────────────────────┤
│ Sales      │ Alice, Bob, Charlie      │
│ IT         │ Dave, Eve                │
└────────────┴──────────────────────────┘
```
