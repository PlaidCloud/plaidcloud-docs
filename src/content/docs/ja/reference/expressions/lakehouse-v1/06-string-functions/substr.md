---
title: SUBSTR (Lakehouse v1)
description: SUBSTR — 指定した位置から、指定した文字数分の文字列を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/substr.md
---

指定した文字列の特定の位置から、指定した文字数分の文字列を抽出します。

- `len` 引数のない形式は、文字列 `str` の位置 `pos` から始まる部分文字列を返します。
- `len` 引数のある形式は、文字列 `str` の位置 `pos` から始まる `len` 文字分の部分文字列を返します。

`pos` に負の値を指定することもできます。この場合、部分文字列の開始位置は、文字列の先頭ではなく末尾から pos 文字目になります。負の値は、この関数のどの形式でも `pos` に使用できます。`pos` が 0 の場合は空文字列を返します。部分文字列を抽出する元の文字列では、先頭の文字の位置を 1 と数えます。

## Analyze の構文

```python
func.substr(<str>, <pos>, <len>)
```

## Analyze の例

```python
func.substr('Quadratically', 5, 6)
┌────────────────────────────────────┐
│ func.substr('Quadratically', 5, 6) │
├────────────────────────────────────┤
│ ratica                             │
└────────────────────────────────────┘
```

## SQL構文

```sql
SUBSTR(<str>, <pos>)

SUBSTR(<str>, <pos>, <len>)
```

## 引数

| 引数 | 説明                                                                                |
|-----------|--------------------------------------------------------------------------------------------|
| `<str>`   | 文字を抽出する元の文字列                                   |
| `<pos>`   | 部分文字列を開始する位置（1から始まります）。負の値の場合は末尾から数えます |
| `<len>`   | 抽出する部分文字列の最大長                                             |

## エイリアス

- [SUBSTRING](../substring)
- [MID](../mid)

## 戻り値の型

VARCHAR

## SQLの例

```sql
SELECT
  SUBSTRING('Quadratically', 5),
  SUBSTR('Quadratically', 5),
  MID('Quadratically', 5);

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5) │ substring('quadratically' from 5) │ mid('quadratically', 5) │
├───────────────────────────────────┼───────────────────────────────────┼─────────────────────────┤
│ ratically                         │ ratically                         │ ratically               │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  SUBSTRING('Quadratically', 5, 6),
  SUBSTR('Quadratically', 5, 6),
  MID('Quadratically', 5, 6);

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5 for 6) │ substring('quadratically' from 5 for 6) │ mid('quadratically', 5, 6) │
├─────────────────────────────────────────┼─────────────────────────────────────────┼────────────────────────────┤
│ ratica                                  │ ratica                                  │ ratica                     │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
