---
title: ASCII (Lakehouse v1)
description: ASCII — 文字列 str の左端の文字の数値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ascii.md
---

文字列 str の左端の文字の数値を返します。

## Analyze の構文

```python
func.ascii(<expr>)
```

## Analyze の例

```python
func.ascii('2')
┌─────────────────┐
│ func.ascii('2') │
├─────────────────┤
│              50 │
└─────────────────┘
```

## SQL構文

```sql
ASCII(<expr>)
```

## 引数

| 引数 | 説明 |
|-----------|-------------|
| `<expr>`  | 文字列。 |

## 戻り値の型

`TINYINT`

## SQLの例

```sql
SELECT ASCII('2');
┌────────────┐
│ ASCII('2') │
├────────────┤
│         50 │
└────────────┘
```
