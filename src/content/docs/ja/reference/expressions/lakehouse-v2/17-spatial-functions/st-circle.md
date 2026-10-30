---
title: ST_CIRCLE (Lakehouse v2)
description: ST_CIRCLE — 中心の経度、緯度、およびメートル単位の半径から円のジオメトリを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-circle.md
---

中心の経度、緯度、およびメートル単位の半径から円のジオメトリを作成します。

## Analyzeの構文

```python
func.st_circle(<lng>, <lat>, <radius>)
```

## Analyzeの例

```python
func.st_circle(0, 0, 100)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQLの構文

```sql
ST_CIRCLE(<lng>, <lat>, <radius>)
```

## SQLの例

```sql
SELECT ST_ASTEXT(ST_CIRCLE(0, 0, 100));

┌─────────────────────┐
│ CIRCLE((0, 0), 100)  │
└─────────────────────┘
```
