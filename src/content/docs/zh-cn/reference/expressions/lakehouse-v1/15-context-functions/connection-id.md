---
title: CONNECTION_ID (Lakehouse v1)
description: CONNECTION_ID：返回当前连接的连接 ID。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/connection-id.md
---

返回当前连接的连接 ID。

## Analyze 语法

```python
func.connection_id()
```

## Analyze 示例

```python
func.connection_id()

┌──────────────────────────────────────┐
│       func.connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```

## SQL 语法

```sql
CONNECTION_ID()
```

## SQL 示例

```sql
SELECT CONNECTION_ID();

┌──────────────────────────────────────┐
│            connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```
