---
title: NOT REGEXP（Lakehouse v1）
description: NOT REGEXP——如果字符串 expr 与模式 pat 指定的正则表达式不匹配，则返回 1，否则返回 0。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-regexp.md
---

如果字符串 expr 与模式 pat 指定的正则表达式不匹配，则返回 1，否则返回 0。

## Analyze 语法

```python
not_(<column>.regexp_match(<pattern>))
```

## Analyze 示例

```python

With an input table of:
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants     │
│ plaid hat       │
│ plaid shirt     │
│ shoes           │
└─────────────────┘

not_(my_clothes.regexp_match('p*'))
┌─────────────────────────────────────┐
│ not_(my_clothes.regexp_match('p*')) │
├─────────────────────────────────────┤
│ false                               │
│ false                               │
│ false                               │
│ true                                │
└─────────────────────────────────────┘
```

## SQL 语法

```sql
<expr> NOT REGEXP <pattern>
```

## SQL 示例

```sql
SELECT 'databend' NOT REGEXP 'd*';
┌──────────────────────────────┐
│ ('databend' not regexp 'd*') │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```
