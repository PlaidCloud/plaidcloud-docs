---
title: UUID（Lakehouse v2）
description: UUID — ランダムな UUID の文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid.md
---

ランダムな UUID の文字列を返します。

## Analyze 構文

```python
func.uuid()
```

## Analyze の例

```python
func.uuid()

┌────────────────────────────────────────┐
│ '550e8400-e29b-41d4-a716-446655440000'  │
└────────────────────────────────────────┘
```

## SQL 構文

```sql
UUID()
```

## SQL の例

```sql
SELECT UUID();

┌──────────────────────────────────────┐
│ 550e8400-e29b-41d4-a716-446655440000  │
└──────────────────────────────────────┘
```
