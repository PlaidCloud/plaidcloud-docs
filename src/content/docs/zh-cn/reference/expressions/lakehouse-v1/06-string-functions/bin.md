---
title: BIN（Lakehouse v1）
description: BIN——返回 N 的二进制值的字符串表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bin.md
---

返回 N 的二进制值的字符串表示。

## Analyze 语法

```python
func.bin(<expr>)
```

## Analyze 示例

```python
func.bin(12)
┌──────────────┐
│ func.bin(12) │
├──────────────┤
│ 1100         │
└──────────────┘
```

## SQL 语法

```sql
BIN(<expr>)
```

## 参数

| 参数 | 说明 |
|-----------|-------------|
| `<expr>`  | 数字。 |

## 返回类型

`VARCHAR`

## SQL 示例

```sql
SELECT BIN(12);
┌─────────┐
│ BIN(12) │
├─────────┤
│ 1100    │
└─────────┘
```
