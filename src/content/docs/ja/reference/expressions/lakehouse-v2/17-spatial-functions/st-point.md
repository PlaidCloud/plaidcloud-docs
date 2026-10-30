---
title: ST_POINT（Lakehouse v2）
description: ST_POINT — 経度と緯度の値からポイントジオメトリを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-point.md
---

経度と緯度の値からポイントジオメトリを作成します。

## Analyze 構文

```python
func.st_point(<lng>, <lat>)
```

## Analyze の例

```python
func.st_point(-73.9857, 40.7484)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 構文

```sql
ST_POINT(<lng>, <lat>)
```

## SQL の例

```sql
SELECT ST_ASTEXT(ST_POINT(-73.9857, 40.7484));

┌──────────────────────────┐
│ POINT (-73.9857 40.7484)  │
└──────────────────────────┘
```
