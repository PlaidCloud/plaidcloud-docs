---
title: H3_TO_STRING（Lakehouse v1）
description: H3_TO_STRING — 指定したH3インデックスの表現を文字列表現に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-string.md
---

指定した[H3](https://eng.uber.com/h3/)インデックスの表現を文字列表現に変換します。

## Analyze Syntax

```python
func.h3_to_string(h3)
```

## Analyze Examples

```python
func.h3_to_string(635318325446452991)

┌───────────────────────────────────────┐
│ func.h3_to_string(635318325446452991) │
├───────────────────────────────────────┤
│ 8d11aa6a38826ff                       │
└───────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_TO_STRING(h3)
```

## SQL Examples

```sql
SELECT H3_TO_STRING(635318325446452991);

┌──────────────────────────────────┐
│ h3_to_string(635318325446452991) │
├──────────────────────────────────┤
│ 8d11aa6a38826ff                  │
└──────────────────────────────────┘
```
