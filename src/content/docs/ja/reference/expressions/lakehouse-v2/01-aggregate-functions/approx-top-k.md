---
title: APPROX_TOP_K (Lakehouse v2)
description: APPROX_TOP_K — 出現頻度の高い上位 k 個の値と、そのおおよその件数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-top-k.md
---

出現頻度の高い上位 k 個の値と、そのおおよその件数を返します。

## Analyze の構文

```python
func.approx_top_k(get_column(table, 'city'), 3)
```

## Analyze の例

```python
func.approx_top_k(get_column(table, 'city'), 3)

┌──────────────────────────────┐
│ [{"item":"NYC","count":150}] │
└──────────────────────────────┘
```

## SQL の構文

```sql
APPROX_TOP_K(<city>, 3)
```

## SQL の例

```sql
SELECT APPROX_TOP_K(city, 3) FROM customers;

┌───────────────────────────────────┐
│ [{"item":"New York","count":150}] │
└───────────────────────────────────┘
```
