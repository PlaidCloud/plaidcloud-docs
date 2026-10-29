---
title: TRIM_TRAILING (Lakehouse v1)
description: TRIM_TRAILING — 文字列の末尾から、指定したトリム文字列をすべて削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-trailing.md
---

文字列の末尾から、指定したトリム文字列をすべて削除します。

関連項目:

- [RTRIM](../rtrim)
- [TRIM_LEADING](../trim-leading)

## Analyzeの構文

```python
func.trim_trailing(<string>, <trim_string>)
```

## Analyzeの例

```python
func.trim_trailing('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_trailing('xxdatabendxx', 'x')  │
├──────────────────────────────────────────┤
│ xxdatabend                               │
└──────────────────────────────────────────┘
```

## SQLの構文

```sql
TRIM_TRAILING(<string>, <trim_string>)
```

## SQLの例

```sql
SELECT TRIM_TRAILING('databendxx', 'xxx'), TRIM_TRAILING('databendxx', 'xx'), TRIM_TRAILING('databendxx', 'x');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_trailing('databendxx', 'xxx') │ trim_trailing('databendxx', 'xx') │ trim_trailing('databendxx', 'x') │
├────────────────────────────────────┼───────────────────────────────────┼──────────────────────────────────┤
│ databendxx                         │ databend                          │ databend                         │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
