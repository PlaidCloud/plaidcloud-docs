---
title: OCT (Lakehouse v1)
description: OCT — retorna uma representação em string do valor octal de N.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/oct.md
---

Retorna uma representação em string do valor octal de N.

## Sintaxe do Analyze

```python
func.oct(<expr>)
```

## Exemplos do Analyze

```python
func.oct(12)
┌─────────────────┐
│ func.oct(12)    │
├─────────────────┤
│ 014             │
└─────────────────┘
```

## Sintaxe SQL

```sql
OCT(<expr>)
```

## Exemplos de SQL

```sql
SELECT OCT(12);
┌─────────┐
│ OCT(12) │
├─────────┤
│ 014     │
└─────────┘
```
