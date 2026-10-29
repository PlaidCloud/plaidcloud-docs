---
title: TO_DATE (Lakehouse v1)
description: TO_DATE — konwertuje wyrażenie na datę, w tym:.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-date.md
---

Konwertuje wyrażenie na datę, w tym:

- **Konwersja ciągu w formacie znacznika czasu na datę**: wyodrębnia datę z podanego ciągu.

- **Konwersja liczby całkowitej na datę**: interpretuje liczbę całkowitą jako liczbę dni przed (dla liczb ujemnych) lub po (dla liczb dodatnich) epoce Uniksa (północ 1 stycznia 1970 r.). Uwaga: wartość typu Date mieści się w zakresie od `1000-01-01` do `9999-12-31`. PlaidCloud Lakehouse zwróci błąd, jeśli uruchomisz „SELECT TO_DATE(9999999999999999999)”.

- **Konwersja ciągu na datę z użyciem określonego formatu**: funkcja przyjmuje dwa argumenty i konwertuje pierwszy ciąg na datę zgodnie z formatem podanym w drugim ciągu. Aby dostosować format daty i czasu w PlaidCloud Lakehouse, można użyć specyfikatorów. Pełną listę obsługiwanych specyfikatorów znajdziesz w sekcji Formatowanie daty i czasu.

Formaty dat są wyrażane za pomocą specyfikacji `strftime`. Zobacz [krótkie zestawienie](https://devhints.io/strftime).

Zobacz też: [TO_TIMESTAMP](../to-timestamp)

## Parametry strftime

### Krótkie zestawienie

#### Data

| Przykład        | Wynik                  |
| ---             | ---                    |
| `%m/%d/%Y`      | `06/05/2013`           |
| `%A, %B %e, %Y` | `Sunday, June 5, 2013` |
| `%b %e %a`      | `Jun 5 Sun`            |

#### Czas

| Przykład        | Wynik                  |
| ---             | ---                    |
| `%H:%M`         | `23:05`                |
| `%I:%M %p`      | `11:05 PM`             |


### Data

| Symbol | Przykład                 | Obszar            |
| ---    | ---                      | ---               |
| `%a`   | `Sun`                    | **Dzień tygodnia** |
| `%A`   | `Sunday`                 |                   |
| `%w`   | `0`..`6` _(niedziela to 0)_ |                |
| ---    | ---                      | ---               |
| `%y`   | `13`                     | **Rok**           |
| `%Y`   | `2013`                   |                   |
| ---    | ---                      | ---               |
| `%b`   | `Jan`                    | **Miesiąc**       |
| `%B`   | `January`                |                   |
| `%m`   | `01`..`12`               |                   |
| ---    | ---                      | ---               |
| `%d`   | `01`..`31`               | **Dzień**         |
| `%e`   | `1`..`31`                |                   |


### Czas

| Symbol | Przykład     | Obszar                |
| ---    | ---          | ---                   |
| `%l`   | `1`          | Godzina               |
| `%H`   | `00`..`23`   | Godzina (24h)         |
| `%I`   | `01`..`12`   | Godzina (12h)         |
| --     | ---          | ---                   |
| `%M`   | `00`..`59`   | Minuta                |
| `%S`   | `00`..`60`   | Sekunda               |
| ---    | ---          | ---                   |
| `%p`   | `AM`         | AM lub PM             |
| `%Z`   | `+08`        | Strefa czasowa        |
| ---    | ---          | ---                   |
| `%j`   | `001`..`366` | Dzień roku            |
| `%%`   | `%`          | Dosłowny znak %       |


## Składnia Analyze

```python
func.to_date('<timestamp_expr>')
func.to_date(<integer>)
func.to_date('<string>', '<format>')
```

## Przykłady Analyze

```python
func.typeof(func.to_date('2022-01-02')), func.typeof(func.str_to_date('2022-01-02'))

┌───────────────────────────────────────────────────────────────────────────────────────┐
│ func.typeof(func.to_date('2022-01-02')) │ func.typeof(func.str_to_date('2022-01-02')) │
├─────────────────────────────────────────┼─────────────────────────────────────────────┤
│ DATE                                    │ DATE                                        │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
-- Convert a timestamp-format string
TO_DATE('<timestamp_expr>')

-- Convert an integer
TO_DATE(<integer>)

-- Convert a string using the given format
TO_DATE('<string>', '<format>')
```

## Aliasy

- [DATE](../date)
- [STR_TO_DATE](../str-to-date)

## Zwracany typ

Funkcja zwraca datę w formacie „YYYY-MM-DD”:

```sql
SELECT TYPEOF(TO_DATE('2022-01-02')), TYPEOF(STR_TO_DATE('2022-01-02'));

┌───────────────────────────────────────────────────────────────────┐
│ typeof(to_date('2022-01-02')) │ typeof(str_to_date('2022-01-02')) │
├───────────────────────────────┼───────────────────────────────────┤
│ DATE                          │ DATE                              │
└───────────────────────────────────────────────────────────────────┘
```

Aby przekonwertować zwróconą datę z powrotem na ciąg, użyj funkcji [DATE_FORMAT](../date-format):

```sql
SELECT DATE_FORMAT(TO_DATE('2022-01-02')) AS dt, TYPEOF(dt);

┌─────────────────────────┐
│     dt     │ typeof(dt) │
├────────────┼────────────┤
│ 2022-01-02 │ VARCHAR    │
└─────────────────────────┘
```

## Przykłady SQL

### Przykłady SQL 1: konwersja ciągu w formacie znacznika czasu

```sql
SELECT TO_DATE('2022-01-02T01:12:00+07:00'), STR_TO_DATE('2022-01-02T01:12:00+07:00');

┌─────────────────────────────────────────────────────────────────────────────────┐
│ to_date('2022-01-02t01:12:00+07:00') │ str_to_date('2022-01-02t01:12:00+07:00') │
├──────────────────────────────────────┼──────────────────────────────────────────┤
│ 2022-01-01                           │ 2022-01-01                               │
└─────────────────────────────────────────────────────────────────────────────────┘

SELECT TO_DATE('2022-01-02'), STR_TO_DATE('2022-01-02');

┌───────────────────────────────────────────────────┐
│ to_date('2022-01-02') │ str_to_date('2022-01-02') │
├───────────────────────┼───────────────────────────┤
│ 2022-01-02            │ 2022-01-02                │
└───────────────────────────────────────────────────┘
```

### Przykłady SQL 2: konwersja liczby całkowitej

```sql
SELECT TO_DATE(1), STR_TO_DATE(1), TO_DATE(-1), STR_TO_DATE(-1);

┌───────────────────────────────────────────────────────────────────┐
│ to_date(1) │ str_to_date(1) │ to_date((- 1)) │ str_to_date((- 1)) │
│    Date    │      Date      │      Date      │        Date        │
├────────────┼────────────────┼────────────────┼────────────────────┤
│ 1970-01-02 │ 1970-01-02     │ 1969-12-31     │ 1969-12-31         │
└───────────────────────────────────────────────────────────────────┘
```

### Przykłady SQL 3: konwersja ciągu z użyciem podanego formatu

```sql
SELECT TO_DATE('12/25/2022','%m/%d/%Y'), STR_TO_DATE('12/25/2022','%m/%d/%Y');

┌───────────────────────────────────────────────────────────────────────────┐
│ to_date('12/25/2022', '%m/%d/%y') │ str_to_date('12/25/2022', '%m/%d/%y') │
├───────────────────────────────────┼───────────────────────────────────────┤
│ 2022-12-25                        │ 2022-12-25                            │
└───────────────────────────────────────────────────────────────────────────┘
```
