---
title: REGEXP（Lakehouse v1）
description: REGEXP——如果字符串 <expr> 与 <pattern> 指定的正则表达式匹配，则返回 true，否则返回 false。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp.md
---

如果字符串 `<expr>` 与 `<pattern>` 指定的正则表达式匹配，则返回 `true`，否则返回 `false`。

## Analyze 语法

```python
<column>.regexp_match(<pattern>)
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

my_clothes.regexp_match('p*')
┌───────────────────────────────┐
│ my_clothes.regexp_match('p*') │
├───────────────────────────────┤
│ true                          │
│ true                          │
│ true                          │
│ false                         │
└───────────────────────────────┘
```

## SQL 语法

```sql
<expr> REGEXP <pattern>
```

## 别名

- [RLIKE](../rlike)

## SQL 示例

```sql
SELECT 'databend' REGEXP 'd*', 'databend' RLIKE 'd*';

┌────────────────────────────────────────────────────┐
│ ('databend' regexp 'd*') │ ('databend' rlike 'd*') │
├──────────────────────────┼─────────────────────────┤
│ true                     │ true                    │
└────────────────────────────────────────────────────┘
```
