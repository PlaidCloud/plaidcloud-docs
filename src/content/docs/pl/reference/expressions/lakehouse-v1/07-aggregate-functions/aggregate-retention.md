---
title: RETENTION (Lakehouse v1)
description: RETENTION — funkcja agregująca.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-retention.md
---

Funkcja agregująca

Funkcja RETENTION() przyjmuje jako argumenty zestaw od 1 do 32 warunków typu UInt8, które wskazują, czy dla zdarzenia spełniono dany warunek.

Jako argument można podać dowolny warunek (jak w klauzuli WHERE).

Warunki, z wyjątkiem pierwszego, są stosowane parami: wynik drugiego jest prawdziwy, jeśli prawdziwy jest pierwszy i drugi, wynik trzeciego — jeśli prawdziwy jest pierwszy i trzeci itd.

## Składnia Analyze

```python
func.retention(<cond1> , <cond2> , ..., <cond32>)
```

## Przykłady Analyze

```python
table.user_id, func.retention(table.event_type=='signup', table.event_type='login', table.event_type='purchase').alias('sales_amounts')

| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```

## Składnia SQL

```sql
RETENTION( <cond1> , <cond2> , ..., <cond32> );
```

## Argumenty

| Argumenty | Opis                                        |
|-----------|---------------------------------------------|
| `<cond>`  | Wyrażenie zwracające wynik logiczny         |

## Typ zwracany

Tablica wartości 1 lub 0.

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_date DATE,
  event_type VARCHAR
);

INSERT INTO user_events (id, user_id, event_date, event_type)
VALUES (1, 1, '2022-01-01', 'signup'),
       (2, 1, '2022-01-02', 'login'),
       (3, 2, '2022-01-01', 'signup'),
       (4, 2, '2022-01-03', 'purchase'),
       (5, 3, '2022-01-01', 'signup'),
       (6, 3, '2022-01-02', 'login');
```

**Przykład zapytania: obliczenie retencji użytkowników na podstawie zdarzeń rejestracji, logowania i zakupu**
```sql
SELECT
  user_id,
  RETENTION(event_type = 'signup', event_type = 'login', event_type = 'purchase') AS retention
FROM user_events
GROUP BY user_id;
```

**Wynik**
```sql
| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```
