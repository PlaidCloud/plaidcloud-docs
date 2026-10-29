---
title: TO_HEX (Lakehouse v1)
description: TO_HEX retorna a representação hexadecimal de um argumento de string ou numérico; cada byte de cada caractere da string é convertido em dois dígitos hexadecimais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-hex.md
---

Para um argumento de string str, TO_HEX() retorna uma representação hexadecimal de str em que cada byte de cada caractere de str é convertido em dois dígitos hexadecimais. A operação inversa é executada pela função UNHEX().

Para um argumento numérico N, TO_HEX() retorna uma representação hexadecimal do valor de N tratado como um número longlong (BIGINT). 

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

## Aliases

- [HEX](../../06-string-functions/hex)

## Exemplos de SQL

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
