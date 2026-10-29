---
title: LIKE (Lakehouse v1)
description: LIKE — SQL パターンを使ってパターンマッチングを行います。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/like.md
---

SQL パターンを使ってパターンマッチングを行います。1（TRUE）または 0（FALSE）を返します。expr または pat のいずれかが NULL の場合、結果は NULL になります。

## Analyze の構文

```python
<column>.like('plaid%')
```

## Analyze の例

```python
my_clothes.like('plaid%)
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants     │
│ plaid hat       │
│ plaid shirt     │
└─────────────────┘
```

## SQL構文

```sql
<expr> LIKE <pattern>
```

## SQLの例

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' ORDER BY name;
┌──────────┬────────────┐
│ name     │ category   │
├──────────┼────────────┤
│ touint16 │ conversion │
│ touint32 │ conversion │
│ touint64 │ conversion │
│ touint8  │ conversion │
└──────────┴────────────┘
```
