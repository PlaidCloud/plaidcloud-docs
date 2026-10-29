---
title: REGEXP_REPLACE (Lakehouse v1)
description: REGEXP_REPLACE remplace les occurrences de la chaîne expr qui correspondent à l'expression régulière.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-replace.md
---

Remplace les occurrences de la chaîne `expr` qui correspondent à l'expression régulière définie par le motif `pat` par la chaîne de remplacement `repl`, et renvoie la chaîne obtenue. Si `expr`, `pat` ou `repl` est NULL, la valeur renvoyée est NULL.

## Syntaxe Analyze

```python
func.regexp_replace(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Exemples Analyze

```python
func.regexp_replace('a b c', 'b', 'X')
┌────────────────────────────────────────┐
│ func.regexp_replace('a b c', 'b', 'X') │
├────────────────────────────────────────┤
│ a X c                                  │
└────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
REGEXP_REPLACE(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Arguments

| Arguments  | Description                                                                                                                       |
|------------|-----------------------------------------------------------------------------------------------------------------------------------|
| expr       | La chaîne expr à faire correspondre                                                                                               |
| pat        | L'expression régulière                                                                                                            |
| repl       | La chaîne de remplacement                                                                                                         |
| pos        | Facultatif. La position dans expr à laquelle commencer la recherche. Si omis, la valeur par défaut est 1.                         |
| occurrence | Facultatif. L'occurrence de correspondance à remplacer. Si omis, la valeur par défaut est 0 (ce qui signifie « remplacer toutes les occurrences »). |
| match_type | Facultatif. Une chaîne qui indique comment effectuer la correspondance. La signification est celle décrite pour REGEXP_LIKE().    |

## Type de retour

`VARCHAR`

## Exemples SQL

```sql
SELECT REGEXP_REPLACE('a b c', 'b', 'X');
┌───────────────────────────────────┐
│ REGEXP_REPLACE('a b c', 'b', 'X') │
├───────────────────────────────────┤
│ a X c                             │
└───────────────────────────────────┘

SELECT REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3);
┌────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3) │
├────────────────────────────────────────────────────┤
│ abc def X                                          │
└────────────────────────────────────────────────────┘

SELECT REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2);
┌───────────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2)        │
├───────────────────────────────────────────────────────────┤
│ 周 周周 X                                                 │
└───────────────────────────────────────────────────────────┘
```
