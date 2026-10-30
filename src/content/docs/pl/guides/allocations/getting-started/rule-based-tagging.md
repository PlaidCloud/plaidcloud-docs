---
title: Tagowanie według reguł
description: Skonfiguruj tagowanie według reguł w alokacjach PlaidCloud, aby automatycznie kategoryzować i oznaczać rekordy danych na podstawie zdefiniowanych kryteriów.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/rule-based-tagging.md
---

Tagowanie według reguł pozwala oznaczyć wiersze źródłowe metadanymi, których mechanizm alokacji używa do ustalenia, *dokąd* te wiersze trafiają. Użyj go, gdy zachowanie alokacji ma zależeć od wiersza — na przykład gdy koszty jednego centrum kosztów mają być rozdzielone według liczby pracowników, a koszty innego według przychodów.

## Kiedy z niego korzystać

- Jedna płaska reguła alokacji nie oddaje tego, jak koszt powinien faktycznie zostać rozdzielony (różne reguły dla różnych rodzajów kosztów).
- Chcesz skierować niektóre wiersze źródłowe do określonych celów, a pozostałe rozdzielić w zwykły sposób.
- Modelujesz alokację z wieloma pulami, w której każda pula używa innego klucza alokacji.

## Jak działa tagowanie

1. **Otaguj źródło.** Tabela wartości otrzymuje jedną lub więcej kolumn tagów, które klasyfikują każdy wiersz.
2. **Odwołaj się do tagów w regule alokacji.** Podczas konfigurowania kroku alokacji wyrażasz reguły w postaci *„jeśli tag źródła X = wartość Y, alokuj według klucza D i wymiaru docelowego T”*.
3. **Mechanizm kieruje wiersze.** Każdy wiersz źródłowy jest dopasowywany do reguł po kolei; o zachowaniu alokacji decyduje pierwsza pasująca reguła.

## Wzorce źródeł przyjazne tagowaniu

- Kolumna o nazwie `cost_category` z wartościami takimi jak `payroll`, `facilities`, `it`, `marketing`
- Kolumna o nazwie `pool`, która wskazuje pulę alokacji, do której należy wiersz
- Kolumna logiczna, taka jak `is_overhead`, która uruchamia odmienne traktowanie

## Przykład

Tabela kosztów z kolumnami `cost_center` i `cost_category`:

| cost_center | cost_category | amount |
|---|---|---|
| 1010 | payroll | 50,000 |
| 1010 | it | 8,000 |
| 1020 | payroll | 35,000 |

Możesz skonfigurować dwie reguły alokacji:

- **Wiersze payroll** rozdzielane według klucza liczby pracowników
- **Wiersze it** rozdzielane według klucza liczby użytkowników

Obie reguły działają na tej samej tabeli źródłowej; tagi decydują, która z nich dotyczy danego wiersza.

## Powiązane

- [Szybki start z alokacjami](/pl/guides/allocations/getting-started/allocations-quick-start/) — podstawowy przebieg przed dodaniem tagowania
- [Konfigurowanie alokacji](/pl/guides/allocations/setup/configure-an-allocation/) — pełny opis kroku
- [Krok reguł alokacji](/pl/reference/workflow-steps/allocation/allocation-rules/) — krok przepływu pracy, który wykorzystuje otagowane dane
