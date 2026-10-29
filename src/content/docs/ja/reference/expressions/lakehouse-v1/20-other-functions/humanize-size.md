---
title: HUMANIZE_SIZE（Lakehouse v1）
description: HUMANIZE_SIZE — 接尾辞（KiB、MiBなど）付きの読みやすい形式のサイズを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-size.md
---

接尾辞（KiB、MiBなど）付きの読みやすい形式のサイズを返します。

## Analyzeの構文

```python
func.humanize_size(x);
```

## Analyzeの例

```python
func.humanize_size(1024 * 1024)
┌────────────────────────────────────────┐
│ func.func.humanize_size((1024 * 1024)) │
├────────────────────────────────────────┤
│ 1 MiB                                  │
└────────────────────────────────────────┘
```

## SQLの構文

```sql
HUMANIZE_SIZE(x);
```

## 引数

| 引数 | 説明                |
|-----------|----------------------------|
| x         | 数値のサイズ。        |


## 戻り値の型

文字列。

## SQLの例

```sql
SELECT HUMANIZE_SIZE(1024 * 1024)
┌─────────────────────────┐
│ HUMANIZE_SIZE((1024 * 1024)) │
├─────────────────────────┤
│ 1 MiB                    │
└─────────────────────────┘
```
