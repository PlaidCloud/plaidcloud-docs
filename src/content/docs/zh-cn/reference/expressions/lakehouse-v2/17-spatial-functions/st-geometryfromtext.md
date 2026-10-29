---
title: ST_GEOMETRYFROMTEXT (Lakehouse v2)
description: ST_GEOMETRYFROMTEXT — 根据 WKT（Well-Known Text）字符串创建几何对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-geometryfromtext.md
---

根据 WKT（Well-Known Text）字符串创建几何对象。

## Analyze 语法

```python
func.st_geometryfromtext(<wkt>)
```

## Analyze 示例

```python
func.st_geometryfromtext('POINT (1 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 语法

```sql
ST_GEOMETRYFROMTEXT(<wkt>)
```

## SQL 示例

```sql
SELECT ST_ASTEXT(ST_GEOMETRYFROMTEXT('POINT (1 2)'));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
