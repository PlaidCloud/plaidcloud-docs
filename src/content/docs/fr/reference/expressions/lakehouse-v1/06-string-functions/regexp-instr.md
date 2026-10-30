---
title: REGEXP_INSTR (Lakehouse v1)
description: REGEXP_INSTR renvoie l'indice de départ de la sous-chaîne de la chaîne expr qui correspond à l'expression régulière définie par le motif pat, ou 0 s'il n'y a aucune correspondance.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-instr.md
---

Renvoie l'indice de départ de la sous-chaîne de la chaîne `expr` qui correspond à l'expression régulière définie par le motif `pat`, ou `0` s'il n'y a aucune correspondance. Si `expr` ou `pat` est NULL, la valeur renvoyée est NULL. Les indices de caractères commencent à `1`.

## Syntaxe Analyze

```python
func.regexp_instr(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Exemples Analyze

```python
func.regexp_instr('dog cat dog', 'dog')
┌─────────────────────────────────────────┐
│ func.regexp_instr('dog cat dog', 'dog') │
├─────────────────────────────────────────┤
│                                       1 │
└─────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
REGEXP_INSTR(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Arguments

| Arguments     | Description                                                                                                                                                                                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expr          | La chaîne expr à faire correspondre                                                                                                                                                                                                                                    |
| pat           | L'expression régulière                                                                                                                                                                                                                                                 |
| pos           | Facultatif. La position dans expr à laquelle commencer la recherche. Si omis, la valeur par défaut est 1.                                                                                                                                                              |
| occurrence    | Facultatif. L'occurrence de correspondance à rechercher. Si omis, la valeur par défaut est 1.                                                                                                                                                                          |
| return_option | Facultatif. Le type de position à renvoyer. Si cette valeur est 0, REGEXP_INSTR() renvoie la position du premier caractère de la sous-chaîne trouvée. Si cette valeur est 1, REGEXP_INSTR() renvoie la position qui suit la sous-chaîne trouvée. Si omis, la valeur par défaut est 0. |
| match_type    | Facultatif. Une chaîne qui indique comment effectuer la correspondance. La signification est celle décrite pour REGEXP_LIKE().                                                                                                                                         |

## Type de retour

Une valeur de type numérique.

## Exemples SQL

```sql
SELECT REGEXP_INSTR('dog cat dog', 'dog');
┌────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog') │
├────────────────────────────────────┤
│                                  1 │
└────────────────────────────────────┘

SELECT REGEXP_INSTR('dog cat dog', 'dog', 2);
┌───────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog', 2) │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{2}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{2}') │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{4}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{4}') │
├─────────────────────────────────────┤
│                                   8 │
└─────────────────────────────────────┘
```
