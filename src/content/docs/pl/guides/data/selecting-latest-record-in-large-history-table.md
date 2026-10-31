---
title: Wybieranie najnowszego rekordu w dużej tabeli historii wersji
description: Dowiedz się, jak efektywnie wybrać najnowszy rekord z dużych tabel historii w PlaidCloud za pomocą zoptymalizowanych technik zapytań.
sidebar:
  label: Wybieranie najnowszego rekordu w dużej tabeli historii wersji
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/selecting-latest-record-in-large-history-table.md
---

## Wyzwanie

Masz tabelę zawierającą wiele wersji każdego rekordu, ale musisz użyć najnowszej wersji.

## Omówienie

Ten problem można rozwiązać, wybierając identyfikator i MAX daty aktualizacji do tabeli tymczasowej. Następnie tę tabelę tymczasową można połączyć za pomocą INNER JOIN z tabelą historii, aby uzyskać wynik. Niestety wymaga to dwóch kroków i przechowywania tabeli pośredniej, która służy wyłącznie do znalezienia najnowszej aktualizacji.

Bardziej eleganckie rozwiązanie, które wykonuje tę operację w jednym zapytaniu, wykorzystuje funkcję okna z sortowaniem oraz filtr.

## Rozwiązanie

### Tabela historii wersji

| employee_id | department | salary    | update_date  |
|-------------|------------|-----------|--------------|
| 3           | IT         | 90000     | 2024-09-17   |
| 2           | HR         | 85000     | 2024-09-17   |
| 5           | HR         | 82000     | 2024-09-17   |
| 3           | IT         | 77000     | 2023-10-01   |
| 3           | IT         | 75000     | 2022-10-04   |
| 5           | IT         | 72000     | 2024-07-12   |
| 2           | IT         | 67000     | 2024-03-18   |
| 1           | Sales      | 62000     | 2022-02-28   |
| 5           | Sales      | 60000     | 2023-01-14   |
| 4           | Sales      | 58000     | 2021-11-19   |

### Konfiguracja kroku
W kroku wyodrębniania (extract) utwórz wyrażenie funkcji okna w kolumnie o nazwie `Rank`, na przykład:

```python
func.rank().over(order_by=table.updated_date.desc(), partition_by=table.employee_id)
```

Na karcie filtra w kroku Extract ustaw filtr, na przykład:

```python
table.Rank == 1
```

### Wynik

| employee_id | department | salary    | update_date  | Rank |
|-------------|------------|-----------|--------------|------|
| 3           | IT         | 90000     | 2024-09-17   | 1    |
| 2           | HR         | 85000     | 2024-09-17   | 1    |
| 5           | HR         | 82000     | 2024-09-17   | 1    |
| 1           | Sales      | 62000     | 2022-02-28   | 1    |
| 4           | Sales      | 58000     | 2021-11-19   | 1    |

To podejście jest bardzo wydajne i pozwala wybrać najnowszy rekord w wielowersyjnej tabeli historii w jednym kroku. Działa ono przez uszeregowanie każdego rekordu w grupie `employee_id` według `update_date`, a następnie wybranie tylko pierwszego rekordu.

Jeśli unikatowy klucz wiersza składa się z wielu kolumn, możesz dodać je do argumentu `partition_by` jako listę, na przykład:

```python
partition_by=[table.first_column, table.second_column, table.third_column]
```

Jeśli potrzebujesz sortowania według wielu kolumn, możesz również zastosować je za pomocą listy kolumn, na przykład:

```python
order_by=[table.first_column.desc(), table.second_column, table.third_column.desc()]
```
