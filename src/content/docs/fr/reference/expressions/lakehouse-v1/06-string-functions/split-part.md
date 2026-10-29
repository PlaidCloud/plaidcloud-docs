---
title: SPLIT_PART (Lakehouse v1)
description: SPLIT_PART découpe une chaîne selon un délimiteur donné et renvoie la partie demandée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/split-part.md
---

Découpe une chaîne selon un délimiteur donné et renvoie la partie demandée.

Voir aussi : [SPLIT](../split)

## Syntaxe Analyze

```python
func.split_part('<input_string>', '<delimiter>', '<position>')
```

## Exemples Analyze

```python
func.split_part('PlaidCloud Lakehouse', ' ', 1)
┌─────────────────────────────────────────────────┐
│ func.split_part('PlaidCloud Lakehouse', ' ', 1) │
├─────────────────────────────────────────────────┤
│ PlaidCloud                                      │
└─────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
SPLIT_PART('<input_string>', '<delimiter>', '<position>')
```

L'argument *position* indique quelle partie renvoyer. Il utilise un indice commençant à 1, mais accepte aussi des valeurs positives, négatives ou nulles :

- Si *position* est un nombre positif, la fonction renvoie la partie située à cette position de gauche à droite, ou NULL si elle n'existe pas.
- Si *position* est un nombre négatif, la fonction renvoie la partie située à cette position de droite à gauche, ou NULL si elle n'existe pas.
- Si *position* vaut 0, elle est traitée comme 1, ce qui renvoie en pratique la première partie de la chaîne.

## Type de retour

Chaîne. SPLIT_PART renvoie NULL lorsque la chaîne d'entrée, le délimiteur ou la position est NULL.

## Exemples SQL

```sql
-- Use a space as the delimiter
-- SPLIT_PART returns a specific part.
SELECT SPLIT_PART('PlaidCloud Lakehouse', ' ', 1);

split_part('PlaidCloud Lakehouse', ' ', 1)|
------------------------------------------+
PlaidCloud Lakehouse                      |

-- Use an empty string as the delimiter or a delimiter that does not exist in the input string
-- SPLIT_PART returns the entire input string.
SELECT SPLIT_PART('PlaidCloud Lakehouse', '', 1);

split_part('PlaidCloud Lakehouse', '', 1)|
-----------------------------------+
PlaidCloud Lakehouse                     |

SELECT SPLIT_PART('PlaidCloud Lakehouse', ',', 1);

split_part('PlaidCloud Lakehouse', ',', 1)|
------------------------------------+
PlaidCloud Lakehouse                      |

-- Use '    ' (tab) as the delimiter
-- SPLIT_PART returns individual fields.
SELECT SPLIT_PART('2023-10-19 15:30:45   INFO   Log message goes here', '   ', 3);

split_part('2023-10-19 15:30:45   info   log message goes here', '   ', 3)|
--------------------------------------------------------------------------+
Log message goes here                                                     |

-- SPLIT_PART returns an empty string as the specified part does not exist at all.
SELECT SPLIT_PART('2023-10-19 15:30:45   INFO   Log message goes here', '   ', 4);

split_part('2023-10-19 15:30:45   info   log message goes here', '   ', 4)|
--------------------------------------------------------------------------+
                                                                          |
```
