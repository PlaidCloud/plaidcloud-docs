---
title: BIN (Lakehouse v1)
description: BIN — N の2進数値を表す文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bin.md
---

N の2進数値を表す文字列を返します。

## Analyze の構文

```python
func.bin(<expr>)
```

## Analyze の例

```python
func.bin(12)
┌──────────────┐
│ func.bin(12) │
├──────────────┤
│ 1100         │
└──────────────┘
```

## SQL構文

```sql
BIN(<expr>)
```

## 引数

| 引数 | 説明 |
|-----------|-------------|
| `<expr>`  | 数値。 |

## 戻り値の型

`VARCHAR`

## SQLの例

```sql
SELECT BIN(12);
┌─────────┐
│ BIN(12) │
├─────────┤
│ 1100    │
└─────────┘
```
