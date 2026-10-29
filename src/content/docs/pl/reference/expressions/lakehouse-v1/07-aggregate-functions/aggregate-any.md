---
title: ANY (Lakehouse v1)
description: ANY — zwraca pierwszą napotkaną wartość różną od NULL z zestawu; wynik jest nieokreślony, gdy kolejność wykonania się zmienia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-any.md
---

Funkcja agregująca.

Funkcja ANY() wybiera pierwszą napotkaną wartość (różną od NULL), chyba że wszystkie wiersze mają w tej kolumnie wartości NULL. Zapytanie może być wykonywane w dowolnej kolejności, a nawet w innej kolejności przy każdym uruchomieniu, dlatego wynik tej funkcji jest nieokreślony. Aby uzyskać wynik określony, zamiast funkcji „any” można użyć funkcji „min” lub „max”.

## Składnia Analyze

```python
func.any(<expr>)
```

## Przykłady Analyze

```python
func.any(table.product_name).alias('any_product_name')

| any_product_name |
|------------------|
| Laptop           |
```

## Składnia SQL

```sql
ANY(<expr>)
```

## Argumenty

| Argumenty | Opis           |
|-----------|----------------|
| `<expr>`  | Dowolne wyrażenie |

## Typ zwracany

Pierwsza napotkana wartość (różna od NULL), w typie tej wartości. Jeśli wszystkie wartości mają wartość NULL, zwracana jest wartość NULL.

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE product_data (
  id INT,
  product_name VARCHAR NULL,
  price FLOAT NULL
);

INSERT INTO product_data (id, product_name, price)
VALUES (1, 'Laptop', 1000),
       (2, NULL, 800),
       (3, 'Keyboard', NULL),
       (4, 'Mouse', 25),
       (5, 'Monitor', 150);
```

**Przykład zapytania: pobranie pierwszej napotkanej nazwy produktu różnej od NULL**
```sql
SELECT ANY(product_name) AS any_product_name
FROM product_data;
```

**Wynik**
```sql
| any_product_name |
|------------------|
| Laptop           |
```
