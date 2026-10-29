---
title: TO_HEX (Lakehouse v1)
description: TO_HEX — para un argumento de cadena str, TO_HEX() devuelve una representación de str como cadena hexadecimal en la que cada byte de cada carácter de str se convierte en dos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-hex.md
---

Para un argumento de cadena str, TO_HEX() devuelve una representación de str como cadena hexadecimal en la que cada byte de cada carácter de str se convierte en dos dígitos hexadecimales. La función UNHEX() realiza la operación inversa.

Para un argumento numérico N, TO_HEX() devuelve una representación como cadena hexadecimal del valor de N, tratado como un número longlong (BIGINT).

## Sintaxis de Analyze

```python
func.to_hex(<expr>)
```

## Ejemplos de Analyze

```python
func.to_hex('abc')

┌────────────────────┐
│ func.to_hex('abc') │
├────────────────────┤
│ 616263             │
└────────────────────┘
```

## Sintaxis de SQL

```sql
TO_HEX(<expr>)
```

## Alias

- [HEX](../../06-string-functions/hex)

## Ejemplos de SQL

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
