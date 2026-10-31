---
title: ORD (Lakehouse v1)
description: ORD renvoie le code du caractère le plus à gauche d'une chaîne (valeur ASCII pour un octet unique, valeur calculée pour un caractère multioctet).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ord.md
---

Si le caractère le plus à gauche n'est pas un caractère multioctet, ORD() renvoie la même valeur que la fonction ASCII().

Si le caractère le plus à gauche de la chaîne str est un caractère multioctet, la fonction renvoie le code de ce caractère,
calculé à partir des valeurs numériques de ses octets constitutifs selon la formule suivante :

```sql
  (1st byte code)
+ (2nd byte code * 256)
+ (3rd byte code * 256^2) ...
```

## Syntaxe Analyze

```python
func.ord(<str>)
```

## Exemples Analyze

```python
func.ord('2')
┌────────────────┐
│ func.ord('2)   │
├────────────────┤
│             50 │
└────────────────┘
```

## Syntaxe SQL

```sql
ORD(<str>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<str>`   | La chaîne.  |

## Type de retour

`BIGINT`

## Exemples SQL

```sql
SELECT ORD('2')
┌────────┐
│ ORD(2) │
├────────┤
│     50 │
└────────┘
```
