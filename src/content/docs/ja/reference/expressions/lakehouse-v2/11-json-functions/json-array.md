---
title: JSON_ARRAY (Lakehouse v2)
description: JSON_ARRAY — 値のリストからJSON配列を作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-array.md
---

値のリストからJSON配列を作成します。

## Analyzeの構文

```python
func.json_array(1, 'hello', None)
```

## Analyzeの例

```python
func.json_array(1, 'hello', None)

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```

## SQLの構文

```sql
JSON_ARRAY(1, 'hello', None)
```

## SQLの例

```sql
SELECT JSON_ARRAY(1, 'hello', NULL);

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```
