---
title: SKEWNESS (Lakehouse v1)
description: SKEWNESS — zwraca skośność (asymetrię rozkładu) wszystkich wartości wejściowych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-skewness.md
---

Funkcja agregująca.

Funkcja `SKEWNESS()` zwraca skośność wszystkich wartości wejściowych.

## Składnia Analyze

```python
func.skewness(<expr>)
```

## Przykłady Analyze

```python
func.skewness(table.temperature).alias('temperature_skewness')

| temperature_skewness |
|----------------------|
|      0.68            |
```

## Składnia SQL

```sql
SKEWNESS(<expr>)
```

## Argumenty

| Argumenty | Opis                            |
|-----------| -----------                     |
| `<expr>`  | Dowolne wyrażenie liczbowe      |

## Typ zwracany

Nullable Float64.

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE temperature_data (
                                  id INT,
                                  city_id INT,
                                  temperature FLOAT
);

INSERT INTO temperature_data (id, city_id, temperature)
VALUES (1, 1, 60),
       (2, 1, 65),
       (3, 1, 62),
       (4, 2, 70),
       (5, 2, 75);
```

**Przykład zapytania: obliczenie skośności danych o temperaturze**

```sql
SELECT SKEWNESS(temperature) AS temperature_skewness
FROM temperature_data;
```

**Wynik**
```sql
| temperature_skewness |
|----------------------|
|      0.68            |
```
