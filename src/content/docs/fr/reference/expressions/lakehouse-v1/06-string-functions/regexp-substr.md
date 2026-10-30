---
title: REGEXP_SUBSTR (Lakehouse v1)
description: REGEXP_SUBSTR renvoie la sous-chaîne de la chaîne expr qui correspond à l'expression régulière.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-substr.md
---

Renvoie la sous-chaîne de la chaîne `expr` qui correspond à l'expression régulière définie par le motif `pat`, ou NULL s'il n'y a aucune correspondance. Si expr ou pat est NULL, la valeur renvoyée est NULL.

## Syntaxe Analyze

```python
func.regexp_substr(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Exemples Analyze

```python
func.regexp_substr('abc def ghi', '[a-z]+')
┌─────────────────────────────────────────────┐
│ func.regexp_substr('abc def ghi', '[a-z]+') │
├─────────────────────────────────────────────┤
│ abc                                         │
└─────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
REGEXP_SUBSTR(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Arguments

| Arguments  | Description                                                                                                                    |
|------------|--------------------------------------------------------------------------------------------------------------------------------|
| expr       | La chaîne expr à faire correspondre                                                                                            |
| pat        | L'expression régulière                                                                                                         |
| pos        | Facultatif. La position dans expr à laquelle commencer la recherche. Si omis, la valeur par défaut est 1.                      |
| occurrence | Facultatif. L'occurrence de correspondance à rechercher. Si omis, la valeur par défaut est 1.                                  |
| match_type | Facultatif. Une chaîne qui indique comment effectuer la correspondance. La signification est celle décrite pour REGEXP_LIKE(). |

## Type de retour

`VARCHAR`

## Exemples SQL

```sql
SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+');
┌────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+') │
├────────────────────────────────────────┤
│ abc                                    │
└────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3);
┌──────────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3) │
├──────────────────────────────────────────────┤
│ ghi                                          │
└──────────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3);
┌──────────────────────────────────────────────────────────────────┐
│ REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3)            │
├──────────────────────────────────────────────────────────────────┤
│ 周周周周                                                         │
└──────────────────────────────────────────────────────────────────┘

```
