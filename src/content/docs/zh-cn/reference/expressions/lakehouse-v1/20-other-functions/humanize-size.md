---
title: HUMANIZE_SIZE (Lakehouse v1)
description: HUMANIZE_SIZE：返回带后缀（KiB、MiB 等）的易读大小。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-size.md
---

返回带后缀（KiB、MiB 等）的易读大小。

## Analyze 语法

```python
func.humanize_size(x);
```

## Analyze 示例

```python
func.humanize_size(1024 * 1024)
┌────────────────────────────────────────┐
│ func.func.humanize_size((1024 * 1024)) │
├────────────────────────────────────────┤
│ 1 MiB                                  │
└────────────────────────────────────────┘
```

## SQL 语法

```sql
HUMANIZE_SIZE(x);
```

## 参数

| 参数 | 说明 |
|-----------|----------------------------|
| x | 数值大小。 |


## 返回类型

字符串。

## SQL 示例

```sql
SELECT HUMANIZE_SIZE(1024 * 1024)
┌─────────────────────────┐
│ HUMANIZE_SIZE((1024 * 1024)) │
├─────────────────────────┤
│ 1 MiB                    │
└─────────────────────────┘
```
