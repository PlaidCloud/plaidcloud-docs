---
title: HUMANIZE_NUMBER（Lakehouse v1）
description: HUMANIZE_NUMBER — 読みやすい形式の数値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-number.md
---

読みやすい形式の数値を返します。

## Analyzeの構文

```python
func.humanize_number(x);
```

## Analyzeの例

```python
func.humanize_number(1000 * 1000)
┌─────────────────────────────────────┐
│ func.humanize_number((1000 * 1000)) │
├─────────────────────────────────────┤
│ 1 million                           │
└─────────────────────────────────────┘
```

## SQLの構文

```sql
HUMANIZE_NUMBER(x);
```

## 引数

| 引数 | 説明                |
|-----------|----------------------------|
| x         | 数値のサイズ。        |


## 戻り値の型

文字列。

## SQLの例

```sql
SELECT HUMANIZE_NUMBER(1000 * 1000)
┌─────────────────────────┐
│ HUMANIZE_NUMBER((1000 * 1000)) │
├─────────────────────────┤
│ 1 million               │
└─────────────────────────┘
```
