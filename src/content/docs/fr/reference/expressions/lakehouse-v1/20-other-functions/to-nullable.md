---
title: TO_NULLABLE (Lakehouse v1)
description: TO_NULLABLE — convertit une valeur en son équivalent nullable.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/to-nullable.md
---

Convertit une valeur en son équivalent nullable.

Lorsque vous appliquez cette fonction à une valeur, elle vérifie si cette valeur peut déjà contenir des valeurs NULL. Si c'est le cas, la fonction renvoie la valeur sans y apporter de modification.

En revanche, si la valeur ne peut pas contenir de valeurs NULL, la fonction TO_NULLABLE la modifie pour qu'elle le puisse. Pour cela, elle encapsule la valeur dans une structure capable de contenir des valeurs NULL, ce qui signifie que la valeur pourra désormais contenir des valeurs NULL.

## Syntaxe Analyze

```python
func.to_nullable(x);
```

## Exemples Analyze

```python
func.typeof(3), func.to_nullable(3), func.typeof(func.to_nullable(3))

func.typeof(3)   | func.to_nullable(3) | func.typeof(func.to_nullable(3)) |
-----------------+---------------------+----------------------------------+
TINYINT UNSIGNED |                   3 | TINYINT UNSIGNED NULL            |

```

## Syntaxe SQL

```sql
TO_NULLABLE(x);
```

## Arguments

| Arguments | Description                |
|-----------|----------------------------|
| x         | La valeur d'origine.       |


## Type de retour

Renvoie une valeur du même type de données que la valeur d'entrée, mais encapsulée dans un conteneur nullable si la valeur d'entrée n'est pas déjà nullable.

## Exemples SQL

```sql
SELECT typeof(3), TO_NULLABLE(3), typeof(TO_NULLABLE(3));

typeof(3)       |to_nullable(3)|typeof(to_nullable(3))|
----------------+--------------+----------------------+
TINYINT UNSIGNED|             3|TINYINT UNSIGNED NULL |

```
