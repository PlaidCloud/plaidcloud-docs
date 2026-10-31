---
title: SUBSTR (Lakehouse v1)
description: SUBSTR extrait une chaîne contenant un nombre précis de caractères à partir d'une position donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/substr.md
---

Extrait une chaîne contenant un nombre précis de caractères à partir d'une position donnée d'une chaîne.

- Les formes sans argument `len` renvoient une sous-chaîne de la chaîne `str` à partir de la position `pos`.
- Les formes avec un argument `len` renvoient une sous-chaîne de `len` caractères de la chaîne `str`, à partir de la position `pos`.

Il est également possible d'utiliser une valeur négative pour `pos`. Dans ce cas, le début de la sous-chaîne se situe à pos caractères de la fin de la chaîne, et non du début. Une valeur négative peut être utilisée pour `pos` dans toutes les formes de cette fonction. Une valeur de 0 pour `pos` renvoie une chaîne vide. La position du premier caractère de la chaîne dont la sous-chaîne est extraite est comptée comme 1.

## Syntaxe Analyze

```python
func.substr(<str>, <pos>, <len>)
```

## Exemples Analyze

```python
func.substr('Quadratically', 5, 6)
┌────────────────────────────────────┐
│ func.substr('Quadratically', 5, 6) │
├────────────────────────────────────┤
│ ratica                             │
└────────────────────────────────────┘
```

## Syntaxe SQL

```sql
SUBSTR(<str>, <pos>)

SUBSTR(<str>, <pos>, <len>)
```

## Arguments

| Arguments | Description                                                                                                  |
|-----------|--------------------------------------------------------------------------------------------------------------|
| `<str>`   | La chaîne principale dont les caractères sont à extraire                                                     |
| `<pos>`   | La position (à partir de 1) à laquelle la sous-chaîne commence. Si elle est négative, le décompte part de la fin |
| `<len>`   | La longueur maximale de la sous-chaîne à extraire                                                            |

## Alias

- [SUBSTRING](../substring)
- [MID](../mid)

## Type de retour

VARCHAR

## Exemples SQL

```sql
SELECT
  SUBSTRING('Quadratically', 5),
  SUBSTR('Quadratically', 5),
  MID('Quadratically', 5);

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5) │ substring('quadratically' from 5) │ mid('quadratically', 5) │
├───────────────────────────────────┼───────────────────────────────────┼─────────────────────────┤
│ ratically                         │ ratically                         │ ratically               │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  SUBSTRING('Quadratically', 5, 6),
  SUBSTR('Quadratically', 5, 6),
  MID('Quadratically', 5, 6);

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5 for 6) │ substring('quadratically' from 5 for 6) │ mid('quadratically', 5, 6) │
├─────────────────────────────────────────┼─────────────────────────────────────────┼────────────────────────────┤
│ ratica                                  │ ratica                                  │ ratica                     │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
