---
title: HISTOGRAM (Lakehouse v1)
description: HISTOGRAM — generuje histogram rozkładu danych przy użyciu strategii grupowania o równej wysokości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-histogram.md
---

Generuje histogram rozkładu danych przy użyciu strategii grupowania „o równej wysokości”.

## Składnia Analyze

```python
func.histogram(<expr>)
```

## Przykłady Analyze
Szczegóły znajdziesz w przykładzie SQL

## Składnia SQL

```sql
HISTOGRAM(<expr>)

-- The following two forms are equivalent:
HISTOGRAM(<max_num_buckets>)(<expr>)
HISTOGRAM(<expr> [, <max_num_buckets>])
```

| Parametr          | Opis                                                                                |
|-------------------|-------------------------------------------------------------------------------------|
| `expr`            | Typ danych `expr` powinien umożliwiać sortowanie.                                   |
| `max_num_buckets` | Opcjonalna dodatnia liczba całkowita określająca maksymalną liczbę zasobników. Domyślnie 128. |

## Typ zwracany

Zwraca pusty ciąg znaków albo obiekt JSON o następującej strukturze:

- **buckets**: lista zasobników ze szczegółowymi informacjami:
  - **lower**: dolna granica zasobnika.
  - **upper**: górna granica zasobnika.
  - **count**: liczba elementów w zasobniku.
  - **pre_sum**: skumulowana liczba elementów do bieżącego zasobnika włącznie.
  - **ndv**: liczba unikatowych wartości w zasobniku.

## Przykłady SQL

Ten przykład pokazuje, jak funkcja HISTOGRAM analizuje rozkład wartości `c_int` w tabeli `histagg`, zwracając granice zasobników, liczby unikatowych wartości, liczby elementów i liczby skumulowane:

```sql
CREATE TABLE histagg (
  c_id INT,
  c_tinyint TINYINT,
  c_smallint SMALLINT,
  c_int INT
);

INSERT INTO histagg VALUES
  (1, 10, 20, 30),
  (1, 11, 21, 33),
  (1, 11, 12, 13),
  (2, 21, 22, 23),
  (2, 31, 32, 33),
  (2, 10, 20, 30);

SELECT HISTOGRAM(c_int) FROM histagg;

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                              histogram(c_int)                                                                                                             │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [{"lower":"13","upper":"13","ndv":1,"count":1,"pre_sum":0},{"lower":"23","upper":"23","ndv":1,"count":1,"pre_sum":1},{"lower":"30","upper":"30","ndv":1,"count":2,"pre_sum":2},{"lower":"33","upper":"33","ndv":1,"count":2,"pre_sum":4}] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Wynik jest zwracany jako tablica JSON:

```json
[
  {
    "lower": "13",
    "upper": "13",
    "ndv": 1,
    "count": 1,
    "pre_sum": 0
  },
  {
    "lower": "23",
    "upper": "23",
    "ndv": 1,
    "count": 1,
    "pre_sum": 1
  },
  {
    "lower": "30",
    "upper": "30",
    "ndv": 1,
    "count": 2,
    "pre_sum": 2
  },
  {
    "lower": "33",
    "upper": "33",
    "ndv": 1,
    "count": 2,
    "pre_sum": 4
  }
]
```

Ten przykład pokazuje, jak `HISTOGRAM(2)` grupuje wartości c_int w dwa zasobniki:

```sql
SELECT HISTOGRAM(2)(c_int) FROM histagg;
-- Or
SELECT HISTOGRAM(c_int, 2) FROM histagg;

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                  histogram(2)(c_int)                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [{"lower":"13","upper":"30","ndv":3,"count":4,"pre_sum":0},{"lower":"33","upper":"33","ndv":1,"count":2,"pre_sum":4}] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Wynik jest zwracany jako tablica JSON:

```json
[
  {
    "lower": "13",
    "upper": "30",
    "ndv": 3,
    "count": 4,
    "pre_sum": 0
  },
  {
    "lower": "33",
    "upper": "33",
    "ndv": 1,
    "count": 2,
    "pre_sum": 4
  }
]
```
