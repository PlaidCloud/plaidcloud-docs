---
title: TYPEOF（Lakehouse v1）
description: TYPEOF — TYPEOF関数は、データ型の名前を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/typeof.md
---

TYPEOF関数は、データ型の名前を返します。

## Analyzeの構文

```python
func.typeof( <expr> )
```

## Analyzeの例

```python
func.typeof(1)
┌──────────────────┐
│ func.typeof(1)   │
├──────────────────┤
│ INT              │
└──────────────────┘
```

## SQLの構文

```sql
TYPEOF( <expr> )
```

## 引数

| 引数   | 説明 |
| ----------- | ----------- |
| `<expr>` | 任意の式。 <br /> 列名、別の関数の結果、または算術演算を指定できます。

## 戻り値の型

文字列

## SQLの例

```sql
SELECT typeof(1::INT);
┌──────────────────┐
│ typeof(1::Int32) │
├──────────────────┤
│ INT              │
└──────────────────┘
```
