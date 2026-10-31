---
title: ASCII（Lakehouse v2）
description: ASCII — 文字列の先頭文字のASCIIコードを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ascii.md
---

文字列の先頭文字のASCIIコードを返します。

## Analyze 構文

```python
func.ascii(<str>)
```

## Analyze の例

```python
func.ascii('A')

┌────┐
│ 65  │
└────┘
```

## SQL 構文

```sql
ASCII(<str>)
```

## SQL の例

```sql
SELECT ASCII('A');

┌────┐
│ 65  │
└────┘
```
