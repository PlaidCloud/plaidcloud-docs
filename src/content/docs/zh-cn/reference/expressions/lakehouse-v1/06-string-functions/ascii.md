---
title: ASCII（Lakehouse v1）
description: ASCII——返回字符串 str 最左侧字符的数值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ascii.md
---

返回字符串 str 最左侧字符的数值。

## Analyze 语法

```python
func.ascii(<expr>)
```

## Analyze 示例

```python
func.ascii('2')
┌─────────────────┐
│ func.ascii('2') │
├─────────────────┤
│              50 │
└─────────────────┘
```

## SQL 语法

```sql
ASCII(<expr>)
```

## 参数

| 参数 | 说明 |
|-----------|-------------|
| `<expr>`  | 字符串。 |

## 返回类型

`TINYINT`

## SQL 示例

```sql
SELECT ASCII('2');
┌────────────┐
│ ASCII('2') │
├────────────┤
│         50 │
└────────────┘
```
