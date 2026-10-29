---
title: HEX（Lakehouse v2）
description: HEX — 文字列または数値の16進数表現を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex.md
---

文字列または数値の16進数表現を返します。

## Analyze 構文

```python
func.hex(<expr>)
```

## Analyze の例

```python
func.hex(255)

┌──────┐
│ 'FF'  │
└──────┘
```

## SQL 構文

```sql
HEX(<expr>)
```

## SQL の例

```sql
SELECT HEX(255);

┌────┐
│ FF  │
└────┘
```
