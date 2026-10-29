---
title: TO_NULLABLE (Lakehouse v1)
description: TO_NULLABLE convierte un valor en su equivalente que admite valores nulos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/to-nullable.md
---

Convierte un valor en su equivalente que admite valores nulos.

Al aplicar esta función a un valor, comprueba si el valor ya puede contener valores NULL. Si el valor ya puede contener valores NULL, la función devuelve el valor sin realizar ningún cambio.

Sin embargo, si el valor no puede contener valores NULL, la función TO_NULLABLE modifica el valor para que pueda contenerlos. Para ello, envuelve el valor en una estructura que puede contener valores NULL, lo que significa que el valor podrá contener valores NULL en el futuro.

## Sintaxis de Analyze

```python
func.to_nullable(x);
```

## Ejemplos de Analyze

```python
func.typeof(3), func.to_nullable(3), func.typeof(func.to_nullable(3))

func.typeof(3)   | func.to_nullable(3) | func.typeof(func.to_nullable(3)) |
-----------------+---------------------+----------------------------------+
TINYINT UNSIGNED |                   3 | TINYINT UNSIGNED NULL            |

```

## Sintaxis de SQL

```sql
TO_NULLABLE(x);
```

## Argumentos

| Argumentos | Descripción                |
|-----------|----------------------------|
| x         | El valor original.         |


## Tipo de retorno

Devuelve un valor del mismo tipo de dato que el valor de entrada, pero envuelto en un contenedor que admite valores nulos si el valor de entrada aún no los admite.

## Ejemplos de SQL

```sql
SELECT typeof(3), TO_NULLABLE(3), typeof(TO_NULLABLE(3));

typeof(3)       |to_nullable(3)|typeof(to_nullable(3))|
----------------+--------------+----------------------+
TINYINT UNSIGNED|             3|TINYINT UNSIGNED NULL |

```
