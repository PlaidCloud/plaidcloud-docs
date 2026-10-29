---
title: DATABASE（Lakehouse v2）
description: DATABASE — 現在のデータベースの名前を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/database.md
---

現在のデータベースの名前を返します。

## Analyze 構文

```python
func.database()
```

## Analyze の例

```python
func.database()

┌───────────────┐
│ 'my_database'  │
└───────────────┘
```

## SQL 構文

```sql
DATABASE()
```

## SQL の例

```sql
SELECT DATABASE();

┌─────────────┐
│ my_database  │
└─────────────┘
```
