---
title: H3_GET_FACES（Lakehouse v1）
description: H3_GET_FACES — 查找与给定 H3 索引相交的所有二十面体面。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-faces.md
---

查找与给定 [H3](https://eng.uber.com/h3/) 索引相交的所有二十面体面。面以 0-19 的整数表示。

## Analyze 语法

```python
func.h3_get_faces(h3)
```

## Analyze 示例

```python
func.h3_get_faces(599119489002373119)

┌───────────────────────────────────────┐
│ func.h3_get_faces(599119489002373119) │
├───────────────────────────────────────┤
│ [0,1,2,3,4]                           │
└───────────────────────────────────────┘
```

## SQL 语法

```sql
H3_GET_FACES(h3)
```

## SQL 示例

```sql
SELECT H3_GET_FACES(599119489002373119);

┌──────────────────────────────────┐
│ h3_get_faces(599119489002373119) │
├──────────────────────────────────┤
│ [0,1,2,3,4]                      │
└──────────────────────────────────┘
```
