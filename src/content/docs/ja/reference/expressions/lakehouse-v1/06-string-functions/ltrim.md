---
title: LTRIM (Lakehouse v1)
description: LTRIM — 指定したトリム文字列に含まれるいずれかの文字を、文字列の左側からすべて削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ltrim.md
---

指定したトリム文字列に含まれるいずれかの文字を、文字列の左側からすべて削除します。

関連項目: 

- [TRIM_LEADING](../trim-leading)
- [RTRIM](../rtrim)

## Analyze の構文

```python
func.ltrim(<string>, <trim_string>)
```

## Analyze の例

```python
func.ltrim('xxdatabend', 'x')
┌────────────────────────────────┐
│ func.ltrim('xxdatabend', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## SQL構文

```sql
LTRIM(<string>, <trim_string>)
```

## SQLの例

```sql
SELECT LTRIM('xxdatabend', 'xx'), LTRIM('xxdatabend', 'xy');

┌───────────────────────────────────────────────────────┐
│ ltrim('xxdatabend', 'xx') │ ltrim('xxdatabend', 'xy') │
├───────────────────────────┼───────────────────────────┤
│ databend                  │ databend                  │
└───────────────────────────────────────────────────────┘
```
