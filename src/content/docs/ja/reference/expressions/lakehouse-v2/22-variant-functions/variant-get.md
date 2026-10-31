---
title: VARIANT_GET（Lakehouse v2）
description: VARIANT_GET — VARIANT オブジェクトの指定したパスから、型指定された値を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-get.md
---

VARIANT オブジェクトの指定したパスから、型指定された値を抽出します。

## Analyze 構文

```python
func.variant_get(<variant>, <path>, <type>)
```

## Analyze の例

```python
func.variant_get(get_column(table, 'data'), '$.name', 'STRING')

┌─────────┐
│ 'Alice'  │
└─────────┘
```

## SQL 構文

```sql
VARIANT_GET(<variant>, <path>, <type>)
```

## SQL の例

```sql
SELECT VARIANT_GET(data, '$.name', 'STRING') FROM events;

┌───────┐
│ Alice  │
└───────┘
```
