---
title: APPROX_COUNT_DISTINCT (Lakehouse v1)
description: APPROX_COUNT_DISTINCT — szacuje liczbę unikatowych wartości w zbiorze danych za pomocą algorytmu HyperLogLog.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-approx-count-distinct.md
---

Szacuje liczbę unikatowych wartości w zbiorze danych za pomocą algorytmu [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog). 

Algorytm HyperLogLog zapewnia przybliżenie liczby unikatowych elementów przy niewielkim zużyciu pamięci i czasu. Warto użyć tej funkcji przy dużych zbiorach danych, gdy akceptowalny jest wynik szacunkowy. Kosztem pewnej dokładności jest to szybka i wydajna metoda zwracania liczby unikatowych wartości.

Aby uzyskać dokładny wynik, użyj funkcji [COUNT_DISTINCT](../aggregate-count-distinct). Dodatkowe wyjaśnienia znajdziesz w sekcji [Przykłady](#przykłady-sql).

## Składnia Analyze

```python
func.approx_count_distinct(<expr>)
```

## Przykłady Analyze

```python
func.approx_count_distinct(table.user_id).alias('approx_distinct_user_count')

| approx_distinct_user_count |
|----------------------------|
|             4              |
```

## Składnia SQL

```sql
APPROX_COUNT_DISTINCT(<expr>)
```

## Typ zwracany

Liczba całkowita.

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_name VARCHAR
);

INSERT INTO user_events (id, user_id, event_name)
VALUES (1, 1, 'Login'),
       (2, 2, 'Login'),
       (3, 3, 'Login'),
       (4, 1, 'Logout'),
       (5, 2, 'Logout'),
       (6, 4, 'Login'),
       (7, 1, 'Login');
```

**Przykład zapytania: oszacowanie liczby unikatowych identyfikatorów użytkowników**
```sql
SELECT APPROX_COUNT_DISTINCT(user_id) AS approx_distinct_user_count
FROM user_events;
```

**Wynik**
```sql
| approx_distinct_user_count |
|----------------------------|
|             4              |
```
