---
title: ST_ASTEXT (Lakehouse v2)
description: ST_ASTEXT — ジオメトリをWKT（Well-Known Text）表現に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-astext.md
---

ジオメトリをWKT（Well-Known Text）表現に変換します。

## Analyzeの構文

```python
func.st_astext(<geometry>)
```

## Analyzeの例

```python
func.st_astext(func.st_point(1, 2))

┌───────────────┐
│ 'POINT (1 2)'  │
└───────────────┘
```

## SQLの構文

```sql
ST_ASTEXT(<geometry>)
```

## SQLの例

```sql
SELECT ST_ASTEXT(ST_POINT(1, 2));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
