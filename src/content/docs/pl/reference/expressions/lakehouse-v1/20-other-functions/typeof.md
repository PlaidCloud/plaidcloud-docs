---
title: TYPEOF (Lakehouse v1)
description: TYPEOF — funkcja TYPEOF zwraca nazwę typu danych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/typeof.md
---

Funkcja TYPEOF zwraca nazwę typu danych.

## Składnia Analyze

```python
func.typeof( <expr> )
```

## Przykłady Analyze

```python
func.typeof(1)
┌──────────────────┐
│ func.typeof(1)   │
├──────────────────┤
│ INT              │
└──────────────────┘
```

## Składnia SQL

```sql
TYPEOF( <expr> )
```

## Argumenty

| Argumenty   | Opis |
| ----------- | ----------- |
| `<expr>` | Dowolne wyrażenie. <br /> Może to być nazwa kolumny, wynik innej funkcji lub operacja matematyczna.

## Zwracany typ

Ciąg znaków

## Przykłady SQL

```sql
SELECT typeof(1::INT);
┌──────────────────┐
│ typeof(1::Int32) │
├──────────────────┤
│ INT              │
└──────────────────┘
```
