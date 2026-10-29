---
title: INSERT (Lakehouse v1)
description: INSERT renvoie la chaîne str dont la sous-chaîne commençant à la position pos et longue de len caractères est remplacée par newstr.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/insert.md
---

Renvoie la chaîne str dont la sous-chaîne commençant à la position pos et longue de len caractères est remplacée par la chaîne newstr. Renvoie la chaîne d'origine si pos ne se trouve pas dans la longueur de la chaîne. Remplace le reste de la chaîne à partir de la position pos si len dépasse la longueur du reste de la chaîne. Renvoie NULL si l'un des arguments est NULL.

## Syntaxe Analyze

```python
func.insert(<str>, <pos>, <len>, <newstr>)
```

## Exemples Analyze

```python
func.insert('Quadratic', 3, 4, 'What')
┌────────────────────────────────────────┐
│ func.insert('Quadratic', 3, 4, 'What') │
├────────────────────────────────────────┤
│ QuWhattic                              │
└────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
INSERT(<str>, <pos>, <len>, <newstr>)
```

## Arguments

| Arguments  | Description            |
|------------|------------------------|
| `<str>`    | La chaîne.             |
| `<pos>`    | La position.           |
| `<len>`    | La longueur.           |
| `<newstr>` | La nouvelle chaîne.    |

## Type de retour

`VARCHAR`

## Exemples SQL

```sql
SELECT INSERT('Quadratic', 3, 4, 'What');
┌───────────────────────────────────┐
│ INSERT('Quadratic', 3, 4, 'What') │
├───────────────────────────────────┤
│ QuWhattic                         │
└───────────────────────────────────┘

SELECT INSERT('Quadratic', -1, 4, 'What');
┌───────────────────────────────────────┐
│ INSERT('Quadratic', (- 1), 4, 'What') │
├───────────────────────────────────────┤
│ Quadratic                             │
└───────────────────────────────────────┘

SELECT INSERT('Quadratic', 3, 100, 'What');
┌─────────────────────────────────────┐
│ INSERT('Quadratic', 3, 100, 'What') │
├─────────────────────────────────────┤
│ QuWhat                              │
└─────────────────────────────────────┘

┌────────────────────────────────────────────┬────────┐
│ INSERT('123456789', number, number, 'aaa') │ number │
├────────────────────────────────────────────┼────────┤
│ 123456789                                  │      0 │
│ aaa23456789                                │      1 │
│ 1aaa456789                                 │      2 │
│ 12aaa6789                                  │      3 │
│ 123aaa89                                   │      4 │
│ 1234aaa                                    │      5 │
│ 12345aaa                                   │      6 │
│ 123456aaa                                  │      7 │
│ 1234567aaa                                 │      8 │
│ 12345678aaa                                │      9 │
│ 123456789                                  │     10 │
│ 123456789                                  │     11 │
│ 123456789                                  │     12 │
└────────────────────────────────────────────┴────────┘
```
