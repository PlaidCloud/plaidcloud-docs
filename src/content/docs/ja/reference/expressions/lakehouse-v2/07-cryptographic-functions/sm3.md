---
title: SM3 (Lakehouse v2)
description: SM3 — 文字列の SM3 ハッシュを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sm3.md
---

文字列の SM3 ハッシュを返します。

## Analyzeの構文

```python
func.sm3(<str>)
```

## Analyzeの例

```python
func.sm3('hello')

┌───────────────┐
│ 'becbbfaa...'  │
└───────────────┘
```

## SQLの構文

```sql
SM3(<str>)
```

## SQLの例

```sql
SELECT SM3('hello');

┌──────────────────────────────────────────────────────────────────┐
│ becbbfaae6548b8bf0cfcad5a27183cd1be6093b1cceccc303d9c61d0a645268  │
└──────────────────────────────────────────────────────────────────┘
```
