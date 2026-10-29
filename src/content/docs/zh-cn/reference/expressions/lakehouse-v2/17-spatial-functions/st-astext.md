---
title: ST_ASTEXT (Lakehouse v2)
description: ST_ASTEXT — 将几何对象转换为其 WKT（Well-Known Text）表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-astext.md
---

将几何对象转换为其 WKT（Well-Known Text）表示。

## Analyze 语法

```python
func.st_astext(<geometry>)
```

## Analyze 示例

```python
func.st_astext(func.st_point(1, 2))

┌───────────────┐
│ 'POINT (1 2)'  │
└───────────────┘
```

## SQL 语法

```sql
ST_ASTEXT(<geometry>)
```

## SQL 示例

```sql
SELECT ST_ASTEXT(ST_POINT(1, 2));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
