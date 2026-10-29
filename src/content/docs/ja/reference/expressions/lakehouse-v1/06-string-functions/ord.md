---
title: ORD (Lakehouse v1)
description: ORD — 文字列の左端の文字の文字コードを返します（シングルバイト文字は ASCII 値、マルチバイト文字は計算された値）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ord.md
---

左端の文字がマルチバイト文字でない場合、ORD() は ASCII() 関数と同じ値を返します。

文字列 str の左端の文字がマルチバイト文字の場合は、その文字を構成する各バイトの数値から次の式で計算したコードを返します。

```sql
  (1st byte code)
+ (2nd byte code * 256)
+ (3rd byte code * 256^2) ...
```

## Analyze の構文

```python
func.ord(<str>)
```

## Analyze の例

```python
func.ord('2')
┌────────────────┐
│ func.ord('2)   │
├────────────────┤
│             50 │
└────────────────┘
```

## SQL構文

```sql
ORD(<str>)
```

## 引数

| 引数 | 説明 |
|-----------|-------------|
| `<str>`   | 文字列。 |

## 戻り値の型

`BIGINT`

## SQLの例

```sql
SELECT ORD('2')
┌────────┐
│ ORD(2) │
├────────┤
│     50 │
└────────┘
```
