---
title: MONEY_FORMAT（Lakehouse v2）
description: MONEY_FORMAT — 数値を、カンマ区切りで小数点以下2桁の通貨形式の文字列に書式設定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/money-format.md
---

数値を、カンマ区切りで小数点以下2桁の通貨形式の文字列に書式設定します。

## Analyze 構文

```python
func.money_format(<num>)
```

## Analyze の例

```python
func.money_format(1234567.89)

┌────────────────┐
│ '1,234,567.89'  │
└────────────────┘
```

## SQL 構文

```sql
MONEY_FORMAT(<num>)
```

## SQL の例

```sql
SELECT MONEY_FORMAT(1234567.89);

┌──────────────┐
│ 1,234,567.89  │
└──────────────┘
```
