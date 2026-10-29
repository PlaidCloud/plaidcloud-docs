---
title: ST_X（Lakehouse v2）
description: ST_X — ポイントジオメトリのX座標（経度）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-x.md
---

ポイントジオメトリのX座標（経度）を返します。

## Analyze 構文

```python
func.st_x(<point>)
```

## Analyze の例

```python
func.st_x(func.st_point(1.5, 2.5))

┌─────┐
│ 1.5  │
└─────┘
```

## SQL 構文

```sql
ST_X(<point>)
```

## SQL の例

```sql
SELECT ST_X(ST_POINT(1.5, 2.5));

┌─────┐
│ 1.5  │
└─────┘
```
