---
title: TO_NULLABLE (Lakehouse v1)
description: TO_NULLABLE — converte um valor em seu equivalente anulável.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/to-nullable.md
---

Converte um valor em seu equivalente anulável.

Ao aplicar essa função a um valor, ela verifica se ele já é capaz de conter valores NULL. Se o valor já for capaz de conter valores NULL, a função o retorna sem fazer alterações.

No entanto, se o valor não for capaz de conter valores NULL, a função TO_NULLABLE o modifica para que ele passe a ser capaz de conter valores NULL. Ela faz isso envolvendo o valor em uma estrutura que pode conter valores NULL, o que significa que o valor poderá conter valores NULL daqui em diante.

## Sintaxe no Analyze

```python
func.to_nullable(x);
```

## Exemplos no Analyze

```python
func.typeof(3), func.to_nullable(3), func.typeof(func.to_nullable(3))

func.typeof(3)   | func.to_nullable(3) | func.typeof(func.to_nullable(3)) |
-----------------+---------------------+----------------------------------+
TINYINT UNSIGNED |                   3 | TINYINT UNSIGNED NULL            |

```

## Sintaxe SQL

```sql
TO_NULLABLE(x);
```

## Argumentos

| Argumentos | Descrição                  |
|-----------|----------------------------|
| x         | O valor original.          |


## Tipo de retorno

Retorna um valor do mesmo tipo de dados que o valor de entrada, mas envolvido em um contêiner anulável se o valor de entrada ainda não for anulável.

## Exemplos de SQL

```sql
SELECT typeof(3), TO_NULLABLE(3), typeof(TO_NULLABLE(3));

typeof(3)       |to_nullable(3)|typeof(to_nullable(3))|
----------------+--------------+----------------------+
TINYINT UNSIGNED|             3|TINYINT UNSIGNED NULL |

```
