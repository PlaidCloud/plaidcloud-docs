---
title: REGEXP_LIKE (Lakehouse v1)
description: REGEXP_LIKE vérifie si la chaîne correspond à l'expression régulière.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-like.md
---

La fonction REGEXP_LIKE vérifie si la chaîne correspond à l'expression régulière.

## Syntaxe Analyze

```python
func.regexp_like(<expr>, <pat[, match_type]>)
```

## Exemples Analyze

```python
func.regexp_like('a', '^[a-d]')
┌─────────────────────────────────┐
│ func.regexp_like('a', '^[a-d]') │
├─────────────────────────────────┤
│                               1 │
└─────────────────────────────────┘
```

## Syntaxe SQL

```sql
REGEXP_LIKE(<expr>, <pat[, match_type]>)
```

## Arguments

| Arguments      | Description                                                                                  |
|----------------|----------------------------------------------------------------------------------------------|
| `<expr>`       | La chaîne expr à faire correspondre                                                          |
| `<pat>`        | L'expression régulière                                                                       |
| `[match_type]` | Facultatif. L'argument match_type est une chaîne qui indique comment effectuer la correspondance |

`match_type` peut contenir tout ou partie des caractères suivants :

* `c` : correspondance sensible à la casse.
* `i` : correspondance insensible à la casse.
* `m` : mode multiligne. Reconnaît les terminateurs de ligne au sein de la chaîne. Par défaut, les terminateurs de ligne ne sont reconnus qu'au début et à la fin de la chaîne.
* `n` : le caractère `.` correspond aux terminateurs de ligne. Par défaut, la correspondance de `.` s'arrête à la fin d'une ligne.
* `u` : fins de ligne Unix uniquement. Non pris en charge actuellement.

## Type de retour

`BIGINT`
Renvoie `1` si la chaîne expr correspond à l'expression régulière définie par le motif pat, `0` sinon. Si expr ou pat est NULL, la valeur renvoyée est NULL.

## Exemples SQL

```sql
SELECT REGEXP_LIKE('a', '^[a-d]');
┌────────────────────────────┐
│ REGEXP_LIKE('a', '^[a-d]') │
├────────────────────────────┤
│                          1 │
└────────────────────────────┘

SELECT REGEXP_LIKE('abc', 'ABC');
┌───────────────────────────┐
│ REGEXP_LIKE('abc', 'ABC') │
├───────────────────────────┤
│                         1 │
└───────────────────────────┘

SELECT REGEXP_LIKE('abc', 'ABC', 'c');
┌────────────────────────────────┐
│ REGEXP_LIKE('abc', 'ABC', 'c') │
├────────────────────────────────┤
│                              0 │
└────────────────────────────────┘

SELECT REGEXP_LIKE('new*\n*line', 'new\\*.\\*line');

┌───────────────────────────────────────────┐
│ REGEXP_LIKE('new*\n*line', 'new\*.\*line')│
├───────────────────────────────────────────┤
│                                         0 │
└───────────────────────────────────────────┘

SELECT REGEXP_LIKE('new*\n*line', 'new\\*.\\*line', 'n');

┌────────────────────────────────────────────────┐
│ REGEXP_LIKE('new*\n*line', 'new\*.\*line', 'n')│
├────────────────────────────────────────────────┤
│                                              1 │
└────────────────────────────────────────────────┘
```
