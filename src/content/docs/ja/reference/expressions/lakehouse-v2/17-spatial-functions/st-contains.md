---
title: ST_CONTAINS (Lakehouse v2)
description: ST_CONTAINS — あるジオメトリが別のジオメトリを含むかどうかをチェックします。含む場合は1を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-contains.md
---

あるジオメトリが別のジオメトリを含むかどうかをチェックします。含む場合は1を返します。

## Analyzeの構文

```python
func.st_contains(<geometry1>, <geometry2>)
```

## Analyzeの例

```python
func.st_contains(get_column(table, 'area'), func.st_point(1, 1))

┌───┐
│ 1  │
└───┘
```

## SQLの構文

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## SQLの例

```sql
SELECT ST_CONTAINS(ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0))'), ST_POINT(5, 5));

┌───┐
│ 1  │
└───┘
```
