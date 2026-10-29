---
title: ST_Y（Lakehouse v2）
description: ST_Y — ポイントジオメトリのY座標（緯度）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-y.md
---

ポイントジオメトリのY座標（緯度）を返します。

## Analyze 構文

```python
func.st_y(<point>)
```

## Analyze の例

```python
func.st_y(func.st_point(1.5, 2.5))

┌─────┐
│ 2.5  │
└─────┘
```

## SQL 構文

```sql
ST_Y(<point>)
```

## SQL の例

```sql
SELECT ST_Y(ST_POINT(1.5, 2.5));

┌─────┐
│ 2.5  │
└─────┘
```
