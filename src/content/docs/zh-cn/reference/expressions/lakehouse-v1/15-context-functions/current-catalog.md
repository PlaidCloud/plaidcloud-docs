---
title: CURRENT_CATALOG (Lakehouse v1)
description: CURRENT_CATALOG：返回会话当前使用的目录名称。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-catalog.md
---

返回会话当前使用的目录名称。

## SQL 语法

```sql
CURRENT_CATALOG()
```

## SQL 示例

```sql
SELECT CURRENT_CATALOG();

┌───────────────────┐
│ current_catalog() │
├───────────────────┤
│ default           │
└───────────────────┘
```
