---
title: H3_IS_VALID（Lakehouse v1）
description: H3_IS_VALID — 指定したH3インデックスが有効かどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-valid.md
---

指定した[H3](https://eng.uber.com/h3/)インデックスが有効かどうかを確認します。

## Analyze Syntax

```python
func.h3_is_valid(h3)
```

## Analyze Examples

```python
func.h3_is_valid(644325524701193974)

┌──────────────────────────────────────┐
│ func.h3_is_valid(644325524701193974) │
├──────────────────────────────────────┤
│ true                                 │
└──────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_IS_VALID(h3)
```

## SQL Examples

```sql
SELECT H3_IS_VALID(644325524701193974);

┌─────────────────────────────────┐
│ h3_is_valid(644325524701193974) │
├─────────────────────────────────┤
│ true                            │
└─────────────────────────────────┘
```
