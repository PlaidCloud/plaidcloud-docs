---
title: UNHEX (Lakehouse v1)
description: "UNHEX : pour un argument de type chaîne str, UNHEX(str) interprète chaque paire de caractères de l'argument."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/unhex.md
---

Pour un argument de type chaîne str, UNHEX(str) interprète chaque paire de caractères de l'argument comme un nombre hexadécimal et le convertit en l'octet représenté par ce nombre. La valeur renvoyée est une chaîne binaire.

## Syntaxe Analyze

```python
func.unhex(<expr>)
```

## Exemples Analyze

```python
func.unhex('6461746162656e64')
┌────────────────────────────────┐
│ func.unhex('6461746162656e64') │
├────────────────────────────────┤
│ 6461746162656E64               │
└────────────────────────────────┘
```

## Syntaxe SQL

```sql
UNHEX(<expr>)
```

## Alias

- [FROM_HEX](../from-hex)

## Exemples SQL

```sql
SELECT UNHEX('6461746162656e64') as c1, typeof(c1),UNHEX('6461746162656e64')::varchar as c2, typeof(c2), FROM_HEX('6461746162656e64');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           c1              │     typeof(c1)         │       c2         |    typeof(c2)     |   from_hex('6461746162656e64')  |
├───────────────────────────┼────────────────────────|──────────────────┤───────────────────|─────────────────────────────────┤
│ 6461746162656E64          │      binary            │      databend    |    varchar        |   6461746162656E64              |
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT UNHEX(HEX('string')), unhex(HEX('string'))::varchar;

┌──────────────────────────────────────────────────────┐
│ unhex(hex('string')) │ unhex(hex('string'))::varchar │
├──────────────────────┼───────────────────────────────┤
│ 737472696E67         │ string                        │
└──────────────────────────────────────────────────────┘
```
