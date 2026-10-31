---
title: LOWER (Lakehouse v1)
description: LOWER — すべての文字を小文字に変換した文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lower.md
---

すべての文字を小文字に変換した文字列を返します。

## Analyze の構文

```python
func.lower(<str>)
```

## Analyze の例

```python
func.lower('Hello, PlaidCloud!')
┌──────────────────────────────────┐
│ func.lower('Hello, PlaidCloud!') │
├──────────────────────────────────┤
│ hello, plaidcloud!               │
└──────────────────────────────────┘
```

## SQL構文

```sql
LOWER(<str>)
```

## エイリアス

- [LCASE](../lcase)

## 戻り値の型

VARCHAR

## SQLの例

```sql
SELECT LOWER('Hello, Databend!'), LCASE('Hello, Databend!');

┌───────────────────────────────────────────────────────┐
│ lower('hello, databend!') │ lcase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ hello, databend!          │ hello, databend!          │
└───────────────────────────────────────────────────────┘
```
