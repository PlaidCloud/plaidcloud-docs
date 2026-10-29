---
title: HOST_NAME（Lakehouse v2）
description: HOST_NAME — 現在のバックエンドノードのホスト名を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/host-name.md
---

現在のバックエンドノードのホスト名を返します。

## Analyze 構文

```python
func.host_name()
```

## Analyze の例

```python
func.host_name()

┌─────────────┐
│ 'be-node-1'  │
└─────────────┘
```

## SQL 構文

```sql
HOST_NAME()
```

## SQL の例

```sql
SELECT HOST_NAME();

┌───────────┐
│ be-node-1  │
└───────────┘
```
