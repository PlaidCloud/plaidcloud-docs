---
title: TO_HEX (Lakehouse v1)
description: TO_HEX — para um argumento de cadeia de caracteres str, TO_HEX() devolve uma representação hexadecimal de str em que cada byte de cada carácter é convertido em dois dígitos hexadecimais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-hex.md
---

Para um argumento de cadeia de caracteres str, TO_HEX() devolve uma representação hexadecimal de str em que cada byte de cada carácter de str é convertido em dois dígitos hexadecimais. A operação inversa é realizada pela função UNHEX().

Para um argumento numérico N, TO_HEX() devolve uma representação hexadecimal do valor de N tratado como um número longlong (BIGINT).

## Sintaxe do Analyze

```python
func.to_hex(<expr>)
```

## Exemplos do Analyze

```python
func.to_hex('abc')

┌────────────────────┐
│ func.to_hex('abc') │
├────────────────────┤
│ 616263             │
└────────────────────┘
```

## Sintaxe SQL

```sql
TO_HEX(<expr>)
```

## Alias

- [HEX](../../06-string-functions/hex)

## Exemplos SQL

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
