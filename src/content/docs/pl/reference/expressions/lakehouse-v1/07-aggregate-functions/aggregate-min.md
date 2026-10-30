---
title: MIN (Lakehouse v1)
description: MIN — zwraca minimalną wartość w zbiorze wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min.md
---

Funkcja agregująca.

Funkcja MIN() zwraca minimalną wartość w zbiorze wartości.

## Składnia Analyze

```python
func.min(<column>)
```

## Przykłady Analyze

```python
table.station_id, func.min(table.price).alias('min_price')

| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```

## Składnia SQL

```sql
MIN(<expr>)
```

## Argumenty

| Argumenty | Opis              |
|-----------|-------------------|
| `<expr>`  | Dowolne wyrażenie |

## Typ zwracany

Minimalna wartość, w typie tej wartości.

## Przykłady SQL

---
title: MIN
---

Funkcja agregująca.

Funkcja MIN() zwraca minimalną wartość w zbiorze wartości.

## Składnia SQL

```sql
MIN(expression)
```

## Argumenty

| Argumenty   | Opis |
| ----------- | ----------- |
| expression  | Dowolne wyrażenie |

## Typ zwracany

Minimalna wartość, w typie tej wartości.

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE gas_prices (
  id INT,
  station_id INT,
  price FLOAT
);

INSERT INTO gas_prices (id, station_id, price)
VALUES (1, 1, 3.50),
       (2, 1, 3.45),
       (3, 1, 3.55),
       (4, 2, 3.40),
       (5, 2, 3.35);
```

**Przykład zapytania: znalezienie minimalnej ceny paliwa na stacji 1**
```sql
SELECT station_id, MIN(price) AS min_price
FROM gas_prices
WHERE station_id = 1
GROUP BY station_id;
```

**Wynik**
```sql
| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```
