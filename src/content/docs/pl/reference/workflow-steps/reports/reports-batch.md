---
title: Reports Batch
description: Generuj wsadowo raporty PDF z kroku przepływu pracy PlaidCloud, aby tworzyć wiele raportów z szablonów przy zmiennych danych wejściowych.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/reports-batch.md
---

## Opis



Renderuje wiele raportów PDF z jednego szablonu RML, sterowanych tabelą kontrolną. Dla każdego wiersza tabeli kontrolnej powstaje jeden raport, a wartości kolumn tego wiersza są używane jako parametry jego renderowania.

Typowe zastosowania: wyciągi klientów (jeden PDF na klienta), sprawozdania finansowe jednostek (jeden PDF na jednostkę biznesową), faktury (jeden PDF na zamówienie). Porównaj z [Report Single](/pl/reference/workflow-steps/reports/report-single/) do jednorazowego generowania raportów.


## Nazwy odczytywane przez szablon

Szablon odczytuje według nazwy każde źródło na karcie **Dane raportu** oraz każdą kolumnę docelową mapowania **Źródło danych wartości rekordów partii**. Nie ma sekcji stałych: każdy wiersz partii dostarcza szablonowi wartości dla swojego raportu. Nowe źródła mają nazwy `new_source`, `new_source_2` itd., które szablon może odczytać bez zmian.


## Co jest sprawdzane przy zapisie

Każda nazwa źródła i kolumny partii musi być podana, unikatowa i możliwa do odczytania przez szablon — obowiązują te same reguły co w [Report Single](/pl/reference/workflow-steps/reports/report-single/), z kolumnami partii zamiast stałych: *Batch column name 'unit id' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*

Zapis z wybraną tabelą źródłową partii, ale pustym mapowaniem partii, wypełnia mapowanie na podstawie tej tabeli, tak jak zrobiłoby to Populate.


## Pusta tabela partii

Gdy tabela źródłowa partii nie ma wierszy, krok kończy się powodzeniem z ostrzeżeniem wskazującym tabelę partii, a żadne raporty nie są tworzone.


## Przykłady

Brak przykładów...
