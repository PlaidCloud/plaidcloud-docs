---
title: OCT (Lakehouse v1)
description: OCT — zwraca tekstową reprezentację wartości ósemkowej liczby N.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/oct.md
---

Zwraca tekstową reprezentację wartości ósemkowej liczby N.

## Składnia Analyze

```python
func.oct(<expr>)
```

## Przykłady Analyze

```python
func.oct(12)
┌─────────────────┐
│ func.oct(12)    │
├─────────────────┤
│ 014             │
└─────────────────┘
```

## Składnia SQL

```sql
OCT(<expr>)
```

## Przykłady SQL

```sql
SELECT OCT(12);
┌─────────┐
│ OCT(12) │
├─────────┤
│ 014     │
└─────────┘
```
