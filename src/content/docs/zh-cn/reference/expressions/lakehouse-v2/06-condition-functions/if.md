---
title: IF (Lakehouse v2)
description: IF：根据条件为 TRUE 还是 FALSE，返回两个值中的一个。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/if.md
---

根据条件为 TRUE 还是 FALSE，返回两个值中的一个。

## Analyze 语法

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Analyze 示例

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## SQL 语法

```sql
IF(<score> >= 60, 'Pass', 'Fail')
```

## SQL 示例

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
