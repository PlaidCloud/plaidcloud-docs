---
title: TO_NULLABLE (Lakehouse v1)
description: TO_NULLABLE — converte um valor no seu equivalente anulável.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/to-nullable.md
---

Converte um valor no seu equivalente anulável.

Quando aplica esta função a um valor, esta verifica se o valor já pode conter valores NULL. Se o valor já puder conter valores NULL, a função devolve-o sem fazer alterações.

No entanto, se o valor não puder conter valores NULL, a função TO_NULLABLE modifica-o para que possa conter valores NULL. Fá-lo envolvendo o valor numa estrutura que pode conter valores NULL, o que significa que o valor passa a poder conter valores NULL no futuro.

## Sintaxe do Analyze

```python
func.to_nullable(x);
```

## Exemplos do Analyze

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

Devolve um valor do mesmo tipo de dados que o valor de entrada, mas envolvido num contentor anulável se o valor de entrada ainda não for anulável.

## Exemplos de SQL

```sql
SELECT typeof(3), TO_NULLABLE(3), typeof(TO_NULLABLE(3));

typeof(3)       |to_nullable(3)|typeof(to_nullable(3))|
----------------+--------------+----------------------+
TINYINT UNSIGNED|             3|TINYINT UNSIGNED NULL |

```
