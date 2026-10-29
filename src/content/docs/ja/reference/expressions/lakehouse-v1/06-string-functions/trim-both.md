---
title: TRIM_BOTH (Lakehouse v1)
description: TRIM_BOTH — 指定したトリム文字列を、文字列の先頭、末尾、または両側からすべて削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-both.md
---

指定したトリム文字列を、文字列の先頭、末尾、または両側からすべて削除します。

関連項目: [TRIM](../trim)

## Analyze の構文

```python
func.trim_both(<string>, <trim_string>)
```

## Analyze の例

```python
func.trim_both('xxdatabendxx', 'x')
┌──────────────────────────────────────┐
│ func.trim_both('xxdatabendxx', 'x')  │
├──────────────────────────────────────┤
│ databend                             │
└──────────────────────────────────────┘
```

## SQL構文

```sql
TRIM_BOTH(<string>, <trim_string>)
```

## SQLの例

```sql
SELECT TRIM_BOTH('xxdatabendxx', 'xxx'), TRIM_BOTH('xxdatabendxx', 'xx'), TRIM_BOTH('xxdatabendxx', 'x');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_both('xxdatabendxx', 'xxx') │ trim_both('xxdatabendxx', 'xx') │ trim_both('xxdatabendxx', 'x') │
├──────────────────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ xxdatabendxx                     │ databend                        │ databend                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
