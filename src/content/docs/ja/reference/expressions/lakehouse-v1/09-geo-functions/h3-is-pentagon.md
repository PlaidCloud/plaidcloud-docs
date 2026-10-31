---
title: H3_IS_PENTAGON（Lakehouse v1）
description: H3_IS_PENTAGON — 指定したH3インデックスが五角形のセルを表しているかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-pentagon.md
---

指定した[H3](https://eng.uber.com/h3/)インデックスが五角形のセルを表しているかどうかを確認します。

## Analyze Syntax

```python
func.h3_is_pentagon(h3)
```

## Analyze Examples

```python
func.h3_is_pentagon(599119489002373119)

┌─────────────────────────────────────────┐
│ func.h3_is_pentagon(599119489002373119) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_IS_PENTAGON(h3)
```

## SQL Examples

```sql
SELECT H3_IS_PENTAGON(599119489002373119);

┌────────────────────────────────────┐
│ h3_is_pentagon(599119489002373119) │
├────────────────────────────────────┤
│ true                               │
└────────────────────────────────────┘
```
