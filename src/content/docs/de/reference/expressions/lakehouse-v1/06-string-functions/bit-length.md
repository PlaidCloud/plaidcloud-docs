---
title: BIT_LENGTH (Lakehouse v1)
description: BIT_LENGTH – gibt die Länge einer Zeichenfolge in Bit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bit-length.md
---

Gibt die Länge einer Zeichenfolge in Bit zurück.

## Analyze-Syntax

```python
func.bit_length(<expr>)
```

## Analyze-Beispiele

```python
func.bit_length('Word')
┌─────────────────────────┐
│ func.bit_length('Word') │
├─────────────────────────┤
│                      32 │
└─────────────────────────┘
```

## SQL-Syntax

```sql
BIT_LENGTH(<expr>)
```

## Argumente

| Argumente | Beschreibung      |
|-----------| ----------------- |
| `<expr>`  | Die Zeichenfolge. |

## Rückgabetyp

`BIGINT`

## SQL-Beispiele

```sql
SELECT BIT_LENGTH('Word');
┌────────────────────────────┐
│ SELECT BIT_LENGTH('Word'); │
├────────────────────────────┤
│ 32                         │
└────────────────────────────┘
```
