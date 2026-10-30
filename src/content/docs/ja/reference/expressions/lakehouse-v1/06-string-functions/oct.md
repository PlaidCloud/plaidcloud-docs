---
title: OCT (Lakehouse v1)
description: OCT — N の8進数値を表す文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/oct.md
---

N の8進数値を表す文字列を返します。

## Analyze の構文

```python
func.oct(<expr>)
```

## Analyze の例

```python
func.oct(12)
┌─────────────────┐
│ func.oct(12)    │
├─────────────────┤
│ 014             │
└─────────────────┘
```

## SQL構文

```sql
OCT(<expr>)
```

## SQLの例

```sql
SELECT OCT(12);
┌─────────┐
│ OCT(12) │
├─────────┤
│ 014     │
└─────────┘
```
