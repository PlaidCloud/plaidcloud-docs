---
title: OCT（Lakehouse v1）
description: OCT——返回 N 的八进制值的字符串表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/oct.md
---

返回 N 的八进制值的字符串表示。

## Analyze 语法

```python
func.oct(<expr>)
```

## Analyze 示例

```python
func.oct(12)
┌─────────────────┐
│ func.oct(12)    │
├─────────────────┤
│ 014             │
└─────────────────┘
```

## SQL 语法

```sql
OCT(<expr>)
```

## SQL 示例

```sql
SELECT OCT(12);
┌─────────┐
│ OCT(12) │
├─────────┤
│ 014     │
└─────────┘
```
