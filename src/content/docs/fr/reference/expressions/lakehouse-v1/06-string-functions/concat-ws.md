---
title: CONCAT_WS (Lakehouse v1)
description: CONCAT_WS (Concatenate With Separator) est une forme particulière de CONCAT() qui concatène des chaînes avec un séparateur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat-ws.md
---

CONCAT_WS() signifie « Concatenate With Separator » (concaténer avec un séparateur) et constitue une forme particulière de CONCAT(). Le premier argument est le séparateur appliqué aux autres arguments. Le séparateur est inséré entre les chaînes à concaténer. Le séparateur peut être une chaîne, tout comme les autres arguments. Si le séparateur est NULL, le résultat est NULL.

CONCAT_WS() ne saute pas les chaînes vides. En revanche, elle ignore toutes les valeurs NULL qui suivent l'argument séparateur.

## Syntaxe Analyze

```python
func.concat_ws(<separator>, <expr1>, ...)
```

## Exemples Analyze

```python
func.concat_ws(',', 'data', 'fuse', 'labs', '2021')
┌─────────────────────────────────────────────────────┐
│ func.concat_ws(',', 'data', 'fuse', 'labs', '2021') │
├─────────────────────────────────────────────────────┤
│ data,fuse,labs,2021                                 │
└─────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
CONCAT_WS(<separator>, <expr1>, ...)
```

## Arguments

| Arguments     | Description          |
|---------------| -------------------- |
| `<separator>` | colonne de chaînes   |
| `<expr1>`     | colonne de valeurs   |

## Type de retour

Une valeur de type de données `VARCHAR` ou `NULL`.

## Exemples SQL

```sql
SELECT CONCAT_WS(',', 'data', 'fuse', 'labs', '2021');
┌────────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', 'fuse', 'labs', '2021') │
├────────────────────────────────────────────────┤
│ data,fuse,labs,2021                            │
└────────────────────────────────────────────────┘

SELECT CONCAT_WS(',', 'data', NULL, 'bend');
┌──────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, 'bend') │
├──────────────────────────────────────┤
│ data,bend                            │
└──────────────────────────────────────┘


SELECT CONCAT_WS(',', 'data', NULL, NULL, 'bend');
┌────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, NULL, 'bend') │
├────────────────────────────────────────────┤
│ data,bend                                  │
└────────────────────────────────────────────┘


SELECT CONCAT_WS(NULL, 'data', 'fuse', 'labs');
┌─────────────────────────────────────────┐
│ CONCAT_WS(NULL, 'data', 'fuse', 'labs') │
├─────────────────────────────────────────┤
│                                    NULL │
└─────────────────────────────────────────┘

SELECT CONCAT_WS(',', NULL);
┌──────────────────────┐
│ CONCAT_WS(',', NULL) │
├──────────────────────┤
│                      │
└──────────────────────┘
```
