---
title: CURRENT_ROLE（Lakehouse v2）
description: CURRENT_ROLE — 現在アクティブなロールを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-role.md
---

現在アクティブなロールを返します。

## Analyze 構文

```python
func.current_role()
```

## Analyze の例

```python
func.current_role()

┌─────────┐
│ 'admin'  │
└─────────┘
```

## SQL 構文

```sql
CURRENT_ROLE()
```

## SQL の例

```sql
SELECT CURRENT_ROLE();

┌───────┐
│ admin  │
└───────┘
```
