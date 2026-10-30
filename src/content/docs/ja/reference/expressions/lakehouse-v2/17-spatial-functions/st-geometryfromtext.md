---
title: ST_GEOMETRYFROMTEXT (Lakehouse v2)
description: ST_GEOMETRYFROMTEXT — WKT（Well-Known Text）文字列からジオメトリを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-geometryfromtext.md
---

WKT（Well-Known Text）文字列からジオメトリを作成します。

## Analyzeの構文

```python
func.st_geometryfromtext(<wkt>)
```

## Analyzeの例

```python
func.st_geometryfromtext('POINT (1 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQLの構文

```sql
ST_GEOMETRYFROMTEXT(<wkt>)
```

## SQLの例

```sql
SELECT ST_ASTEXT(ST_GEOMETRYFROMTEXT('POINT (1 2)'));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
