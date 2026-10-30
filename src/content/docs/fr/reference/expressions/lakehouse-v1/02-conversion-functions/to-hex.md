---
title: TO_HEX (Lakehouse v1)
description: "TO_HEX : pour un argument de type chaîne str, TO_HEX() renvoie une représentation hexadécimale de str dans laquelle chaque octet de chaque caractère de str est converti en deux chiffres hexadécimaux."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-hex.md
---

Pour un argument de type chaîne str, TO_HEX() renvoie une représentation hexadécimale de str dans laquelle chaque octet de chaque caractère de str est converti en deux chiffres hexadécimaux. L'opération inverse est réalisée par la fonction UNHEX().

Pour un argument numérique N, TO_HEX() renvoie une représentation hexadécimale de la valeur de N traitée comme un nombre longlong (BIGINT). 

## Syntaxe Analyze

```python
func.to_hex(<expr>)
```

## Exemples Analyze

```python
func.to_hex('abc')

┌────────────────────┐
│ func.to_hex('abc') │
├────────────────────┤
│ 616263             │
└────────────────────┘
```

## Syntaxe SQL

```sql
TO_HEX(<expr>)
```

## Alias

- [HEX](../../06-string-functions/hex)

## Exemples SQL

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
