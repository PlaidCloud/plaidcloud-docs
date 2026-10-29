---
title: SPACE（Lakehouse v1）
description: SPACE——返回由 N 个空格字符组成的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/space.md
---

返回由 N 个空格字符组成的字符串。

## Analyze 语法

```python
func.space(<n>)
```

## Analyze 示例

```python
func.space(20)
┌─────────────────┐
│ func.space(20)  │
├─────────────────┤
│                 │
└─────────────────┘
```

## SQL 语法

```sql
SPACE(<n>);
```

## 参数

| 参数 | 说明          |
|-----------|----------------------|
| `<n>`     | 空格数量 |

## 返回类型

字符串数据类型的值。

## SQL 示例

```sql
SELECT SPACE(20)
┌──────────────────────┐
│ SPACE(20)            │
├──────────────────────┤
│                      │
└──────────────────────┘
```
