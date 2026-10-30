---
title: RTRIM (Lakehouse v1)
description: RTRIM — 指定したトリム文字列に含まれるいずれかの文字を、文字列の右側からすべて削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rtrim.md
---

指定したトリム文字列に含まれるいずれかの文字を、文字列の右側からすべて削除します。

関連項目: 

- [TRIM_TRAILING](../trim-trailing)
- [LTRIM](../ltrim)

## Analyze の構文

```python
func.rtrim(<string>, <trim_string>)
```

## Analyze の例

```python
func.rtrim('databend'xx, 'x')
┌────────────────────────────────┐
│ func.rtrim('databendxx', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## SQL構文

```sql
RTRIM(<string>, <trim_string>)
```

## SQLの例

```sql
SELECT RTRIM('databendxx', 'x'), RTRIM('databendxx', 'xy');

┌──────────────────────────────────────────────────────┐
│ rtrim('databendxx', 'x') │ rtrim('databendxx', 'xy') │
├──────────────────────────┼───────────────────────────┤
│ databend                 │ databend                  │
└──────────────────────────────────────────────────────┘
```
