---
title: TO_HEX (Lakehouse v1)
description: TO_HEX — dla argumentu tekstowego str funkcja TO_HEX() zwraca szesnastkową reprezentację tekstową str, w której każdy bajt każdego znaku str jest zamieniany na dwie cyfry szesnastkowe.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-hex.md
---

Dla argumentu tekstowego str funkcja TO_HEX() zwraca szesnastkową reprezentację tekstową str, w której każdy bajt każdego znaku str jest zamieniany na dwie cyfry szesnastkowe. Operację odwrotną wykonuje funkcja UNHEX().

Dla argumentu liczbowego N funkcja TO_HEX() zwraca szesnastkową reprezentację tekstową wartości N traktowanej jako liczba typu longlong (BIGINT). 

## Składnia Analyze

```python
func.to_hex(<expr>)
```

## Przykłady Analyze

```python
func.to_hex('abc')

┌────────────────────┐
│ func.to_hex('abc') │
├────────────────────┤
│ 616263             │
└────────────────────┘
```

## Składnia SQL

```sql
TO_HEX(<expr>)
```

## Aliasy

- [HEX](../../06-string-functions/hex)

## Przykłady SQL

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
