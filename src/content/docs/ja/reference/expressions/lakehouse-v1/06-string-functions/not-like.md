---
title: NOT LIKE (Lakehouse v1)
description: NOT LIKE — SQL パターンを使って、パターンに一致しないことを判定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-like.md
---

SQL パターンを使って、パターンに一致しないことを判定します。1（TRUE）または 0（FALSE）を返します。expr または pat のいずれかが NULL の場合、結果は NULL になります。

## Analyze の構文

```python
<column>.not_like(<pattern>)
```

## Analyze の例

```python
my_clothes.not_like('%pants)
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants XL  │
│ plaid hat       │
│ plaid shirt     │
└─────────────────┘
```

## SQL構文

```sql
<expr> NOT LIKE <pattern>
```

## SQLの例

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' AND name not like '%64' ORDER BY name;
┌──────────┬────────────┐
│ name     │ category   │
├──────────┼────────────┤
│ touint16 │ conversion │
│ touint32 │ conversion │
│ touint8  │ conversion │
└──────────┴────────────┘
```
