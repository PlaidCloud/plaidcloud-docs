---
title: TYPEOF (Lakehouse v1)
description: TYPEOF gibt den Namen eines Datentyps zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/typeof.md
---

Die Funktion TYPEOF gibt den Namen eines Datentyps zurück.

## Analyze-Syntax

```python
func.typeof( <expr> )
```

## Analyze-Beispiele

```python
func.typeof(1)
┌──────────────────┐
│ func.typeof(1)   │
├──────────────────┤
│ INT              │
└──────────────────┘
```

## SQL-Syntax

```sql
TYPEOF( <expr> )
```

## Argumente

| Argumente   | Beschreibung |
| ----------- | ----------- |
| `<expr>` | Ein beliebiger Ausdruck. <br /> Das kann ein Spaltenname, das Ergebnis einer anderen Funktion oder eine mathematische Operation sein.

## Rückgabetyp

Zeichenfolge

## SQL-Beispiele

```sql
SELECT typeof(1::INT);
┌──────────────────┐
│ typeof(1::Int32) │
├──────────────────┤
│ INT              │
└──────────────────┘
```
