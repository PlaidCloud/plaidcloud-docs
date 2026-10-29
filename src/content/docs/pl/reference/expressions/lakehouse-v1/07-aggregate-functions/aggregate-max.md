---
title: MAX (Lakehouse v1)
description: MAX — zwraca maksymalną wartość w zbiorze wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max.md
---

Funkcja agregująca.

Funkcja MAX() zwraca maksymalną wartość w zbiorze wartości.

## Składnia Analyze

```python
func.max(<column>)
```

## Przykłady Analyze

```python
table.city, func.max(table.temperature).alias('max_temperature')

|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```

## Składnia SQL

```sql
MAX(<expr>)
```

## Argumenty

| Argumenty | Opis |
|-----------| ----------- |
| `<expr>`  | Dowolne wyrażenie |

## Typ zwracany

Maksymalna wartość, w typie tej wartości.

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE temperatures (
  id INT,
  city VARCHAR,
  temperature FLOAT
);

INSERT INTO temperatures (id, city, temperature)
VALUES (1, 'New York', 30),
       (2, 'New York', 28),
       (3, 'New York', 32),
       (4, 'Los Angeles', 25),
       (5, 'Los Angeles', 27);
```

**Przykład zapytania: znalezienie maksymalnej temperatury w Nowym Jorku**

```sql
SELECT city, MAX(temperature) AS max_temperature
FROM temperatures
WHERE city = 'New York'
GROUP BY city;
```

**Wynik**
```sql
|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```
