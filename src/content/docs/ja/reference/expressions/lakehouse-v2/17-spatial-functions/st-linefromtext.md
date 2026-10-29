---
title: ST_LINEFROMTEXT (Lakehouse v2)
description: ST_LINEFROMTEXT — WKT文字列から線のジオメトリを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-linefromtext.md
---

WKT文字列から線のジオメトリを作成します。

## Analyzeの構文

```python
func.st_linefromtext(<wkt>)
```

## Analyzeの例

```python
func.st_linefromtext('LINESTRING (0 0, 1 1, 2 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQLの構文

```sql
ST_LINEFROMTEXT(<wkt>)
```

## SQLの例

```sql
SELECT ST_ASTEXT(ST_LINEFROMTEXT('LINESTRING (0 0, 1 1, 2 2)'));

┌────────────────────────────┐
│ LINESTRING (0 0, 1 1, 2 2)  │
└────────────────────────────┘
```
