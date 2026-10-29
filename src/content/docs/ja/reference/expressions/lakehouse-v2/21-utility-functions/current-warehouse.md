---
title: CURRENT_WAREHOUSE（Lakehouse v2）
description: CURRENT_WAREHOUSE — 現在のウェアハウスの名前を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-warehouse.md
---

現在のウェアハウスの名前を返します。

## Analyze 構文

```python
func.current_warehouse()
```

## Analyze の例

```python
func.current_warehouse()

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```

## SQL 構文

```sql
CURRENT_WAREHOUSE()
```

## SQL の例

```sql
SELECT CURRENT_WAREHOUSE();

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```
