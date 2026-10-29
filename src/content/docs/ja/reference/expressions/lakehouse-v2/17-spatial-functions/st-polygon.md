---
title: ST_POLYGON（Lakehouse v2）
description: ST_POLYGON — WKT文字列からポリゴンジオメトリを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-polygon.md
---

WKT文字列からポリゴンジオメトリを作成します。

## Analyze 構文

```python
func.st_polygon(<wkt>)
```

## Analyze の例

```python
func.st_polygon('POLYGON((0 0,10 0,10 10,0 10,0 0))')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 構文

```sql
ST_POLYGON(<wkt>)
```

## SQL の例

```sql
SELECT ST_ASTEXT(ST_POLYGON('POLYGON((0 0,10 0,10 10,0 10,0 0))'));

┌─────────────────────────────────────────┐
│ POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))  │
└─────────────────────────────────────────┘
```
