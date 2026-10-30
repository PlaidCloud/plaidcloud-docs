---
title: TRIM_LEADING (Lakehouse v1)
description: TRIM_LEADING — 文字列の先頭から、指定したトリム文字列をすべて削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-leading.md
---

文字列の先頭から、指定したトリム文字列をすべて削除します。

関連項目:

- [LTRIM](../ltrim)
- [TRIM_TRAILING](../trim-trailing)

## Analyzeの構文

```python
func.trim_leading(<string>, <trim_string>)
```

## Analyzeの例

```python
func.trim_leading('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_leading('xxdatabendxx', 'x')   │
├──────────────────────────────────────────┤
│ databendxx                               │
└──────────────────────────────────────────┘
```

## SQLの構文

```sql
TRIM_LEADING(<string>, <trim_string>)
```

## SQLの例

```sql
SELECT TRIM_LEADING('xxdatabend', 'xxx'), TRIM_LEADING('xxdatabend', 'xx'), TRIM_LEADING('xxdatabend', 'x');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_leading('xxdatabend', 'xxx') │ trim_leading('xxdatabend', 'xx') │ trim_leading('xxdatabend', 'x') │
├───────────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ xxdatabend                        │ databend                         │ databend                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
