---
title: UPPER (Lakehouse v1)
description: UPPER — すべての文字を大文字に変換した文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/upper.md
---

すべての文字を大文字に変換した文字列を返します。

## Analyzeの構文

```python
func.unhex(<expr>)
```

## Analyzeの例

```python
func.upper('hello, plaidcloud lakehouse!')
┌────────────────────────────────────────────┐
│ func.upper('hello, plaidcloud lakehouse!') │
├────────────────────────────────────────────┤
│ 'HELLO, PLAIDCLOUD LAKEHOUSE!'             │
└────────────────────────────────────────────┘
```

## SQLの構文

```sql
UPPER(<str>)
```

## エイリアス

- [UCASE](../ucase)

## 戻り値の型

VARCHAR

## SQLの例

```sql
SELECT UPPER('hello, databend!'), UCASE('hello, databend!');

┌───────────────────────────────────────────────────────┐
│ upper('hello, databend!') │ ucase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ HELLO, DATABEND!          │ HELLO, DATABEND!          │
└───────────────────────────────────────────────────────┘
```
