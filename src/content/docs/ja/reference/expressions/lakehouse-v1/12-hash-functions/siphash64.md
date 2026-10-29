---
title: SIPHASH64（Lakehouse v1）
description: SIPHASH64 — 64ビットのSipHashハッシュ値を生成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/siphash64.md
---

64ビットの[SipHash](https://en.wikipedia.org/wiki/SipHash)ハッシュ値を生成します。

## Analyzeの構文

```python
func.siphash64(<expr>)
```

## Analyzeの例

```python
func.siphash64('1234567890')

┌───────────────────────────────┐
│ func.siphash64('1234567890')  │
├───────────────────────────────┤
│          18110648197875983073 │
└───────────────────────────────┘
```

## SQLの構文

```sql
SIPHASH64(<expr>)
```

## エイリアス

- [SIPHASH](../siphash)

## SQLの例

```sql
SELECT SIPHASH('1234567890'), SIPHASH64('1234567890');

┌─────────────────────────────────────────────────┐
│ siphash('1234567890') │ siphash64('1234567890') │
├───────────────────────┼─────────────────────────┤
│  18110648197875983073 │    18110648197875983073 │
└─────────────────────────────────────────────────┘
```
