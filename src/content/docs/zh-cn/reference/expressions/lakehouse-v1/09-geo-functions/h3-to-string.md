---
title: H3_TO_STRING（Lakehouse v1）
description: H3_TO_STRING — 将给定 H3 索引的表示形式转换为字符串表示形式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-string.md
---

将给定 [H3](https://eng.uber.com/h3/) 索引的表示形式转换为字符串表示形式。

## Analyze 语法

```python
func.h3_to_string(h3)
```

## Analyze 示例

```python
func.h3_to_string(635318325446452991)

┌───────────────────────────────────────┐
│ func.h3_to_string(635318325446452991) │
├───────────────────────────────────────┤
│ 8d11aa6a38826ff                       │
└───────────────────────────────────────┘
```

## SQL 语法

```sql
H3_TO_STRING(h3)
```

## SQL 示例

```sql
SELECT H3_TO_STRING(635318325446452991);

┌──────────────────────────────────┐
│ h3_to_string(635318325446452991) │
├──────────────────────────────────┤
│ 8d11aa6a38826ff                  │
└──────────────────────────────────┘
```
