---
title: H3_IS_PENTAGON（Lakehouse v1）
description: H3_IS_PENTAGON — 检查给定 H3 索引是否表示五边形单元。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-pentagon.md
---

检查给定 [H3](https://eng.uber.com/h3/) 索引是否表示五边形单元。

## Analyze 语法

```python
func.h3_is_pentagon(h3)
```

## Analyze 示例

```python
func.h3_is_pentagon(599119489002373119)

┌─────────────────────────────────────────┐
│ func.h3_is_pentagon(599119489002373119) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_IS_PENTAGON(h3)
```

## SQL 示例

```sql
SELECT H3_IS_PENTAGON(599119489002373119);

┌────────────────────────────────────┐
│ h3_is_pentagon(599119489002373119) │
├────────────────────────────────────┤
│ true                               │
└────────────────────────────────────┘
```
