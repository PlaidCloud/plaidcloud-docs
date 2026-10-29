---
title: STRING_TO_H3（Lakehouse v1）
description: STRING_TO_H3 — 将字符串表示形式转换为 H3（uint64）表示形式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/string-to-h3.md
---

将字符串表示形式转换为 [H3](https://eng.uber.com/h3/)（uint64）表示形式。

## Analyze 语法

```python
func.string_to_h3(h3)
```

## Analyze 示例

```python
func.string_to_h3('8d11aa6a38826ff')

┌──────────────────────────────────────┐
│ func.string_to_h3('8d11aa6a38826ff') │
├──────────────────────────────────────┤
│                   635318325446452991 │
└──────────────────────────────────────┘
```

## SQL 语法

```sql
STRING_TO_H3(h3)
```

## SQL 示例

```sql
SELECT STRING_TO_H3('8d11aa6a38826ff');

┌─────────────────────────────────┐
│ string_to_h3('8d11aa6a38826ff') │
├─────────────────────────────────┤
│              635318325446452991 │
└─────────────────────────────────┘
```
