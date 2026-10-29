---
title: ORD (Lakehouse v1)
description: ORD – gibt den Zeichencode des ganz links stehenden Zeichens einer Zeichenfolge zurück (ASCII-Wert bei Einzelbyte-Zeichen, berechneter Wert bei Mehrbyte-Zeichen).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ord.md
---

Ist das ganz links stehende Zeichen kein Mehrbyte-Zeichen, gibt ORD() denselben Wert zurück wie die Funktion ASCII().

Ist das ganz links stehende Zeichen der Zeichenfolge str ein Mehrbyte-Zeichen, gibt die Funktion den Code dieses Zeichens zurück,
berechnet aus den numerischen Werten seiner einzelnen Bytes nach dieser Formel:

```sql
  (1st byte code)
+ (2nd byte code * 256)
+ (3rd byte code * 256^2) ...
```

## Analyze-Syntax

```python
func.ord(<str>)
```

## Analyze-Beispiele

```python
func.ord('2')
┌────────────────┐
│ func.ord('2)   │
├────────────────┤
│             50 │
└────────────────┘
```

## SQL-Syntax

```sql
ORD(<str>)
```

## Argumente

| Argumente | Beschreibung      |
|-----------|-------------------|
| `<str>`   | Die Zeichenfolge. |

## Rückgabetyp

`BIGINT`

## SQL-Beispiele

```sql
SELECT ORD('2')
┌────────┐
│ ORD(2) │
├────────┤
│     50 │
└────────┘
```
