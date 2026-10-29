---
title: HOST_NAME (Lakehouse v2)
description: HOST_NAME：返回当前后端节点的主机名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/host-name.md
---

返回当前后端节点的主机名。

## Analyze 语法

```python
func.host_name()
```

## Analyze 示例

```python
func.host_name()

┌─────────────┐
│ 'be-node-1'  │
└─────────────┘
```

## SQL 语法

```sql
HOST_NAME()
```

## SQL 示例

```sql
SELECT HOST_NAME();

┌───────────┐
│ be-node-1  │
└───────────┘
```
