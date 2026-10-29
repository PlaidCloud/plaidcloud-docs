---
title: CONNECTION_ID（Lakehouse v1）
description: CONNECTION_ID — 現在の接続の接続IDを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/connection-id.md
---

現在の接続の接続IDを返します。

## Analyzeの構文

```python
func.connection_id()
```

## Analyzeの例

```python
func.connection_id()

┌──────────────────────────────────────┐
│       func.connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```

## SQLの構文

```sql
CONNECTION_ID()
```

## SQLの例

```sql
SELECT CONNECTION_ID();

┌──────────────────────────────────────┐
│            connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```
