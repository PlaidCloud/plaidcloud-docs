---
title: IF (Lakehouse v2)
description: IF — 条件が TRUE か FALSE かに応じて、2 つの値のいずれかを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/if.md
---

条件が TRUE か FALSE かに応じて、2 つの値のいずれかを返します。

## Analyzeの構文

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Analyzeの例

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## SQLの構文

```sql
IF(<score> >= 60, 'Pass', 'Fail')
```

## SQLの例

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
