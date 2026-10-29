---
title: ST_LINEFROMTEXT (Lakehouse v2)
description: ST_LINEFROMTEXT — 根据 WKT 字符串创建线形几何对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-linefromtext.md
---

根据 WKT 字符串创建线形几何对象。

## Analyze 语法

```python
func.st_linefromtext(<wkt>)
```

## Analyze 示例

```python
func.st_linefromtext('LINESTRING (0 0, 1 1, 2 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL 语法

```sql
ST_LINEFROMTEXT(<wkt>)
```

## SQL 示例

```sql
SELECT ST_ASTEXT(ST_LINEFROMTEXT('LINESTRING (0 0, 1 1, 2 2)'));

┌────────────────────────────┐
│ LINESTRING (0 0, 1 1, 2 2)  │
└────────────────────────────┘
```
