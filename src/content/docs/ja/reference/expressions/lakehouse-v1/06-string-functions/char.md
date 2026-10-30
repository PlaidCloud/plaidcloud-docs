---
title: CHAR (Lakehouse v1)
description: CHAR — 渡された各整数に対応する文字を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/char.md
---

渡された各整数に対応する文字を返します。

## Analyze の構文

```python
func.char(N,...)
```

## Analyze の例

```python
func.char(77,121,83,81,76)
┌─────────────────────────────┐
│ func.char(77,121,83,81,76) │
├─────────────────────────────┤
│ 4D7953514C                  │
└─────────────────────────────┘
```

## SQL構文

```sql
CHAR(N, ...)
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| N         | 数値列 |

## 戻り値の型

`BINARY`

## SQLの例

次の例では、返されるバイナリ値と、その文字列表現の両方を示します。

```sql
SELECT CHAR(77,121,83,81,76) as a, a::String;
┌────────────────────────┐
│      a     │ a::string │
│   Binary   │   String  │
├────────────┼───────────┤
│ 4D7953514C │ MySQL     │
└────────────────────────┘
```
