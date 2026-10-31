---
title: CURRENT_CATALOG（Lakehouse v1）
description: CURRENT_CATALOG — セッションで現在使用しているカタログの名前を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-catalog.md
---

セッションで現在使用しているカタログの名前を返します。

## SQLの構文

```sql
CURRENT_CATALOG()
```

## SQLの例

```sql
SELECT CURRENT_CATALOG();

┌───────────────────┐
│ current_catalog() │
├───────────────────┤
│ default           │
└───────────────────┘
```
