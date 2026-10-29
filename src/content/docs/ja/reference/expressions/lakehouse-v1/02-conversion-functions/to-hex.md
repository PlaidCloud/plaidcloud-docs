---
title: TO_HEX (Lakehouse v1)
description: TO_HEX — 文字列の引数strに対して、strの各文字の各バイトを2桁の16進数に変換した、strの16進数文字列表現を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-hex.md
---

文字列の引数strに対して、TO_HEX()は、strの各文字の各バイトを2桁の16進数に変換した、strの16進数文字列表現を返します。この操作の逆は、UNHEX()関数が実行します。

数値の引数Nに対して、TO_HEX()は、Nの値をlonglong（BIGINT）の数値として扱った16進数文字列表現を返します。 

## Analyzeの構文

```python
func.to_hex(<expr>)
```

## Analyzeの例

```python
func.to_hex('abc')

┌────────────────────┐
│ func.to_hex('abc') │
├────────────────────┤
│ 616263             │
└────────────────────┘
```

## SQLの構文

```sql
TO_HEX(<expr>)
```

## エイリアス

- [HEX](../../06-string-functions/hex)

## SQLの例

```sql
SELECT HEX('abc'), TO_HEX('abc');

┌────────────────────────────┐
│ hex('abc') │ to_hex('abc') │
├────────────┼───────────────┤
│ 616263     │ 616263        │
└────────────────────────────┘

SELECT HEX(255), TO_HEX(255);

┌────────────────────────┐
│ hex(255) │ to_hex(255) │
├──────────┼─────────────┤
│ ff       │ ff          │
└────────────────────────┘
```
