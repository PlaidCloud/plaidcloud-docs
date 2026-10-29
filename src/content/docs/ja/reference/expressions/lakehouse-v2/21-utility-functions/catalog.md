---
title: CATALOG（Lakehouse v2）
description: CATALOG — 現在のカタログの名前を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/catalog.md
---

現在のカタログの名前を返します。

## Analyze 構文

```python
func.catalog()
```

## Analyze の例

```python
func.catalog()

┌───────────────────┐
│ 'default_catalog'  │
└───────────────────┘
```

## SQL 構文

```sql
CATALOG()
```

## SQL の例

```sql
SELECT CATALOG();

┌─────────────────┐
│ default_catalog  │
└─────────────────┘
```
