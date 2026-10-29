---
title: TO_BOOLEAN (Lakehouse v1)
description: TO_BOOLEAN — 値をBOOLEANデータ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-boolean.md
---

値をBOOLEANデータ型に変換します。

## Analyzeの構文

```python
func.to_boolean( <expr> )
```

## Analyzeの例

```python
func.to_boolean('true')

┌──────────────────────────┐
│ func.to_boolean('true')  │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## SQLの構文

```sql
TO_BOOLEAN( <expr> )
```

## SQLの例

```sql
SELECT TO_BOOLEAN('true');

┌────────────────────┐
│ to_boolean('true') │
├────────────────────┤
│ true               │
└────────────────────┘
```
