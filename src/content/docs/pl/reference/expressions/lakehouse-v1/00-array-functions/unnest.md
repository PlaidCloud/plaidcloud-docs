---
title: UNNEST (Lakehouse v1)
description: UNNEST — rozwija tablicę i zwraca zbiór jej elementów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/unnest.md
---

Rozwija tablicę i zwraca zbiór jej elementów.

## Składnia Analyze

```python
func.unnest( <array> )
```

## Przykłady Analyze

```python
func.unnest([1, 2])

┌──────────────────────┐
│  func.unnest([1, 2]) │
├──────────────────────┤
│                    1 │
│                    2 │
└──────────────────────┘
```

## Składnia SQL

```sql
UNNEST( <array> )
```

## Przykłady SQL

```sql
SELECT UNNEST([1, 2]);

┌─────────────────┐
│  unnest([1, 2]) │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘

-- UNNEST(array) can be used as a table function.
SELECT * FROM UNNEST([1, 2]);

┌─────────────────┐
│      value      │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘
```

## Praktyczny przykład
W poniższych przykładach użyjemy tabeli o nazwie contacts z kolumną phones zdefiniowaną jako tablica tekstów.

```python
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (100), 
  phones TEXT []
);
```

Kolumna phones jest tablicą jednowymiarową, która przechowuje różne numery telefonów, jakie może mieć kontakt.

Aby zdefiniować tablicę wielowymiarową, dodaj nawiasy kwadratowe.

Na przykład tablicę dwuwymiarową można zdefiniować w następujący sposób:

```python
column_name data_type [][]
```

Przykład wstawiania danych do tej tabeli:
```python
INSERT INTO contacts (name, phones)
VALUES('John Doe',ARRAY [ '(408)-589-5846','(408)-589-5555' ]);
```
lub
```python
INSERT INTO contacts (name, phones)
VALUES('Lily Bush','{"(408)-589-5841"}'),
      ('William Gate','{"(408)-589-5842","(408)-589-5843"}');
```

Funkcja unnest() rozwija tablicę do listy wierszy. Na przykład poniższe zapytanie rozwija wszystkie numery telefonów z tablicy phones.

```python
SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;
```

Wynik:
|     name     |     unnest     |
|--------------|----------------|
| John Doe     | (408)-589-5846 |
| John Doe     | (408)-589-5555 |
| Lily Bush    | (408)-589-5841 |
| William Gate | (408)-589-5843 |
