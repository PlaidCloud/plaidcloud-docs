---
title: TO_NULLABLE (Lakehouse v1)
description: TO_NULLABLE — konwertuje wartość na jej odpowiednik dopuszczający NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/to-nullable.md
---

Konwertuje wartość na jej odpowiednik dopuszczający NULL.

Po zastosowaniu tej funkcji do wartości sprawdzane jest, czy wartość może już przechowywać NULL. Jeśli wartość może już przechowywać NULL, funkcja zwraca ją bez zmian.

Jeśli jednak wartość nie może przechowywać NULL, funkcja TO_NULLABLE modyfikuje ją tak, aby mogła. Robi to, opakowując wartość w strukturę, która może przechowywać NULL, co oznacza, że wartość może od tego momentu przyjmować NULL.

## Składnia Analyze

```python
func.to_nullable(x);
```

## Przykłady Analyze

```python
func.typeof(3), func.to_nullable(3), func.typeof(func.to_nullable(3))

func.typeof(3)   | func.to_nullable(3) | func.typeof(func.to_nullable(3)) |
-----------------+---------------------+----------------------------------+
TINYINT UNSIGNED |                   3 | TINYINT UNSIGNED NULL            |

```

## Składnia SQL

```sql
TO_NULLABLE(x);
```

## Argumenty

| Argumenty | Opis                |
|-----------|----------------------------|
| x         | Oryginalna wartość.        |


## Zwracany typ

Zwraca wartość tego samego typu danych co wartość wejściowa, ale opakowaną w kontener dopuszczający NULL, jeśli wartość wejściowa nie dopuszcza jeszcze NULL.

## Przykłady SQL

```sql
SELECT typeof(3), TO_NULLABLE(3), typeof(TO_NULLABLE(3));

typeof(3)       |to_nullable(3)|typeof(to_nullable(3))|
----------------+--------------+----------------------+
TINYINT UNSIGNED|             3|TINYINT UNSIGNED NULL |

```
