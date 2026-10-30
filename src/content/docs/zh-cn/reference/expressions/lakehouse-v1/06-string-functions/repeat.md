---
title: REPEAT（Lakehouse v1）
description: REPEAT——返回由字符串 str 重复 count 次组成的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/repeat.md
---

返回由字符串 str 重复 count 次组成的字符串。如果 count 小于 1，则返回空字符串。如果 str 或 count 为 NULL，则返回 NULL。

## Analyze 语法

```python
func.repeat(<str>, <count>)
```

## Analyze 示例

```python
func.repeat(<str>, <count>)
┌─────────────────────────┐
│ func.repeat('plaid', 3) │
├─────────────────────────┤
│ plaidplaidplaid         │
└─────────────────────────┘
```

## SQL 语法

```sql
REPEAT(<str>, <count>)
```

## 参数

| 参数 | 说明 |
|-----------|-------------|
| `<str>`   | 字符串。 |
| `<count>` | 数字。 |

## SQL 示例

```sql
SELECT REPEAT('databend', 3);
┌──────────────────────────┐
│ REPEAT('databend', 3)    │
├──────────────────────────┤
│ databenddatabenddatabend │
└──────────────────────────┘

SELECT REPEAT('databend', 0);
┌───────────────────────┐
│ REPEAT('databend', 0) │
├───────────────────────┤
│                       │
└───────────────────────┘

SELECT REPEAT('databend', NULL);
┌──────────────────────────┐
│ REPEAT('databend', NULL) │
├──────────────────────────┤
│                     NULL │
└──────────────────────────┘
```
