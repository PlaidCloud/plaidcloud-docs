---
title: IF (Lakehouse v2)
description: IF — 조건이 TRUE인지 FALSE인지에 따라 두 값 중 하나를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/if.md
---

조건이 TRUE인지 FALSE인지에 따라 두 값 중 하나를 반환합니다.

## Analyze 구문

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Analyze 예제

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## SQL 구문

```sql
IF(<score> >= 60, 'Pass', 'Fail')
```

## SQL 예제

```sql
SELECT name, IF(score >= 60, 'Pass', 'Fail') AS result FROM students;

┌─────────┬────────┐
│ name    │ result │
├─────────┼────────┤
│ Alice   │ Pass   │
│ Bob     │ Fail   │
│ Charlie │ Pass   │
└─────────┴────────┘
```
