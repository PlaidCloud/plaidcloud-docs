---
title: TO_HEX (Lakehouse v1)
description: TO_HEX – für ein Zeichenfolgenargument str gibt TO_HEX() eine hexadezimale Zeichenfolgendarstellung von str zurück, in der jedes Byte jedes Zeichens in str in zwei Hexadezimalziffern umgewandelt wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-hex.md
---

Für ein Zeichenfolgenargument str gibt TO_HEX() eine hexadezimale Zeichenfolgendarstellung von str zurück, in der jedes Byte jedes Zeichens in str in zwei Hexadezimalziffern umgewandelt wird. Die Umkehrung dieser Operation führt die Funktion UNHEX() aus.

Für ein numerisches Argument N gibt TO_HEX() eine hexadezimale Zeichenfolgendarstellung des Werts von N zurück, der als longlong-Zahl (BIGINT) behandelt wird. 

## Analyze-Syntax

```python
func.to_hex(<expr>)
```

## Analyze-Beispiele

```python
func.to_hex('abc')

┌────────────────────┐
│ func.to_hex('abc') │
├────────────────────┤
│ 616263             │
└────────────────────┘
```

## SQL-Syntax

```sql
TO_HEX(<expr>)
```

## Aliasse

- [HEX](../../06-string-functions/hex)

## SQL-Beispiele

```sql
SELECT HEX('abc'), TO_HEX('abc');

┌────────────────────────────┐
│ hex('abc') │ to_hex('abc') │
├────────────┼───────────────┤
│ 616263     │ 616263        │
└────────────────────────────┘

SELECT HEX(255), TO_HEX(255);

┌────────────────────────┐
│ hex(255) │ to_hex(255) │
├──────────┼─────────────┤
│ ff       │ ff          │
└────────────────────────┘
```
