---
title: AVG (Lakehouse v1)
description: AVG — zwraca średnią wartość wyrażenia, ignorując wartości NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg.md
---

Funkcja agregująca.

Funkcja AVG() zwraca średnią wartość wyrażenia.

**Uwaga:** wartości NULL nie są liczone.


## Składnia Analyze

```python
func.avg(<column>)
```

## Przykłady Analyze

```python
func.avg(table.price).alias('avg_price')

| avg_price |
| --------- |
| 20.4      |
```

## Składnia SQL

```sql
AVG(<expr>)
```

## Argumenty

| Argumenty | Opis                     |
|-----------|--------------------------|
| `<expr>`  | Dowolne wyrażenie liczbowe |

## Typ zwracany

double

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**

Utwórzmy tabelę o nazwie „sales” i wstawmy do niej przykładowe dane:
```sql
CREATE TABLE sales (
  id INTEGER,
  product VARCHAR(50),
  price FLOAT
);

INSERT INTO sales (id, product, price)
VALUES (1, 'Product A', 10.5),
       (2, 'Product B', 20.75),
       (3, 'Product C', 30.0),
       (4, 'Product D', 15.25),
       (5, 'Product E', 25.5);
```

**Zapytanie: użycie funkcji AVG()**

Użyjmy teraz funkcji AVG(), aby znaleźć średnią cenę wszystkich produktów w tabeli „sales”:
```sql
SELECT AVG(price) AS avg_price
FROM sales;
```

Wynik powinien wyglądać następująco:
```sql
| avg_price |
| --------- |
| 20.4      |
```
