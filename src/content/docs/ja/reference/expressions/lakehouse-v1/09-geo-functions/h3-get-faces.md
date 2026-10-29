---
title: H3_GET_FACES（Lakehouse v1）
description: H3_GET_FACES — 指定したH3インデックスと交差する二十面体のすべての面を検索します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-faces.md
---

指定した[H3](https://eng.uber.com/h3/)インデックスと交差する二十面体のすべての面を検索します。面は0〜19の整数で表されます。

## Analyze Syntax

```python
func.h3_get_faces(h3)
```

## Analyze Examples

```python
func.h3_get_faces(599119489002373119)

┌───────────────────────────────────────┐
│ func.h3_get_faces(599119489002373119) │
├───────────────────────────────────────┤
│ [0,1,2,3,4]                           │
└───────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_GET_FACES(h3)
```

## SQL Examples

```sql
SELECT H3_GET_FACES(599119489002373119);

┌──────────────────────────────────┐
│ h3_get_faces(599119489002373119) │
├──────────────────────────────────┤
│ [0,1,2,3,4]                      │
└──────────────────────────────────┘
```
