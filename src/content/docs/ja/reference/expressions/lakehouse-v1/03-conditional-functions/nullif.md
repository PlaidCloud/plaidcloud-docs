---
title: NULLIF（Lakehouse v1）
description: NULLIF — 2 つの式が等しい場合に NULL を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nullif.md
---

2 つの式が等しい場合は NULL を返します。等しくない場合は expr1 を返します。2 つの式は同じデータ型である必要があります。

## Analyze 構文

```python
func.nullif(<expr1>, <expr2>)
```

## Analyze の例

```python
func.nullif(0, null) 

┌──────────────────────┐
│ func.nullif(0, null) │
├──────────────────────┤
│                    0 │
└──────────────────────┘
```

## SQL 構文

```sql
NULLIF(<expr1>, <expr2>)
```

## SQL の例

```sql
SELECT NULLIF(0, NULL);

┌─────────────────┐
│ nullif(0, null) │
├─────────────────┤
│               0 │
└─────────────────┘
```
