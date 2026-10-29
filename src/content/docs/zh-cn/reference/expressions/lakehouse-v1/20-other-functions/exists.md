---
title: EXISTS (Lakehouse v1)
description: EXISTS：exists 条件与子查询结合使用，当子查询至少返回一行时，视为条件“已满足”。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/exists.md
---

exists 条件与子查询结合使用，当子查询至少返回一行时，视为条件“已满足”。

## SQL 语法

```sql
WHERE EXISTS ( <subquery> );
```

## SQL 示例
```sql
SELECT number FROM numbers(5) AS A WHERE exists (SELECT * FROM numbers(3) WHERE number=1); 
┌────────┐
│ number │
├────────┤
│      0 │
│      1 │
│      2 │
│      3 │
│      4 │
└────────┘
```
