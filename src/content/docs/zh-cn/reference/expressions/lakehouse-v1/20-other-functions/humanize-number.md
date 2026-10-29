---
title: HUMANIZE_NUMBER (Lakehouse v1)
description: HUMANIZE_NUMBER：返回易读的数字。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-number.md
---

返回易读的数字。

## Analyze 语法

```python
func.humanize_number(x);
```

## Analyze 示例

```python
func.humanize_number(1000 * 1000)
┌─────────────────────────────────────┐
│ func.humanize_number((1000 * 1000)) │
├─────────────────────────────────────┤
│ 1 million                           │
└─────────────────────────────────────┘
```

## SQL 语法

```sql
HUMANIZE_NUMBER(x);
```

## 参数

| 参数 | 说明 |
|-----------|----------------------------|
| x | 数值大小。 |


## 返回类型

字符串。

## SQL 示例

```sql
SELECT HUMANIZE_NUMBER(1000 * 1000)
┌─────────────────────────┐
│ HUMANIZE_NUMBER((1000 * 1000)) │
├─────────────────────────┤
│ 1 million               │
└─────────────────────────┘
```
