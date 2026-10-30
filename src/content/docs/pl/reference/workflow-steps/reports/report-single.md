---
title: Report Single
description: Generuj pojedynczy raport PDF z kroku przepływu pracy PlaidCloud, używając szablonów, źródeł danych i konfigurowalnych opcji układu.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/report-single.md
---

## Opis



Renderuje raport PDF z szablonu RML (Report Markup Language), wypełnionego danymi z jednej lub kilku tabel PlaidCloud. Używaj go do formalnych, sformatowanych raportów — faktur, sprawozdań finansowych, zgłoszeń regulacyjnych, markowych zestawień.

Szablon RML definiuje układ (rozmiar strony, czcionki, stały tekst, rozmieszczenie tabel); tabele wejściowe dostarczają dane zmienne. Porównaj z [Reports Batch](/pl/reference/workflow-steps/reports/reports-batch/), gdy jeden szablon ma wygenerować wiele raportów (np. po jednym na klienta).


## Nazwy odczytywane przez szablon

Szablon odczytuje według nazwy każde źródło na karcie **Dane raportu** oraz każdą stałą w sekcji **Stałe raportu (wartości stałe)**. Nowe źródła mają nazwy `new_source`, `new_source_2` itd., które szablon może odczytać bez zmian; zmień je tak, aby mówiły, co zawierają.


## Co jest sprawdzane przy zapisie

Każda nazwa źródła i stałej musi być:

- **Podana** — pusta nazwa jest odrzucana.
- **Unikatowa** — dwa źródła, dwie stałe ani źródło i stała nie mogą mieć tej samej nazwy, ponieważ szablon zobaczyłby tylko jedną z nich: *Source name 'sales' is also a constant name; rename one of them.*
- **Możliwa do odczytania przez szablon** — litery, cyfry i podkreślenia, zaczynając od litery lub podkreślenia: *Constant name 'fiscal year' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*
- **Nie słowem zastrzeżonym przez szablon** — `True`, `False`, `None`, `true`, `false`, `none`, `not` i `self` są odczytywane jako coś innego niż Twoje dane: *Source name 'self' is a word the template reserves, so it can't be read as a name.*


## Przykłady

Brak przykładów...
