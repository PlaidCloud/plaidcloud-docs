---
title: Ścieżka nauki Analityka
description: Co przeczytać przed laboratoriami Praktyk i Ekspert z analityki PlaidCloud i czego wymaga każde laboratorium.
sidebar:
  label: Analityka
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/analytics.md
---

Ścieżka Analityka dotyczy metryk, które dają jedną właściwą odpowiedź niezależnie od podziału, oraz wspólnych znaczeń w tabelach. Zacznij od ścieżki [Podstawy](/pl/guides/certification/foundations/). Informacje o tym, jak działają laboratoria, znajdziesz w [Certyfikacja PlaidCloud](/pl/guides/certification/).

## Praktyk

### Czytaj w tej kolejności

1. [Uruchamianie przepływu pracy](/pl/guides/workflows/run-a-workflow/)
2. [Wyświetlanie dziennika przepływu pracy](/pl/guides/workflows/viewing-workflow-log/)
3. [Definicje metryk](/pl/integrations/ai-coding-agents/metric-definitions/), w tym jak wyprowadzić metrykę z innych
4. [Zbuduj pulpit z opublikowanej tabeli](/pl/get-started/tutorials/build-a-dashboard/), dla opcjonalnego pulpitu

### Czego wymaga laboratorium

Laboratorium nosi nazwę *Analityka: zdefiniuj metryki dla trzech pytań*.

Uruchamiasz przepływ pracy, który przygotowuje tabelę sprzedaży, a następnie definiujesz na tej tabeli metryki, każdą z regionem i kanałem w ziarnistości: przychód według regionu, średnią wartość zamówienia według kanału, wyprowadzoną z liczby zamówień, oraz koszt jako udział w przychodzie według regionu, wyprowadzony z metryki kosztu. Każda metryka jest zbudowana na przygotowanej tabeli, a nie na surowej. Pulpit z trzema odpowiedziami to dobry następny krok, ale nie jest oceniany.

Laboratorium sprawdza, czy przepływ pracy się uruchamia i czy każda z trzech metryk daje prawidłową odpowiedź.

## Ekspert

Laboratorium Ekspert jest na czas: masz 4 godziny od chwili jego rozpoczęcia.

### Czytaj w tej kolejności

1. [Definicje metryk](/pl/integrations/ai-coding-agents/metric-definitions/)
2. [Model danych i elementy projektu](/pl/guides/projects/data-model/)
3. [Ścieżki analizy](/pl/integrations/ai-coding-agents/analysis-paths/)

### Czego wymaga laboratorium

Laboratorium nosi nazwę *Analityka Ekspert: spójne metryki*.

Dwie metryki dają różne odpowiedzi w zależności od podziału, a suma przychodu jest większa niż suma zamówień. Naprawiasz je tak, aby każda zwracała jedną prawidłową odpowiedź według regionu i według produktu, zachowując ich nazwy. Następnie kolumny o tym samym znaczeniu łączysz we wspólny element: jeden dla regionu, w tabelach, które przechowują go pod różnymi nazwami kolumn, i jeden dla produktu.

Laboratorium sprawdza, czy przepływ pracy się uruchamia, czy przychód według regionu i produktu oraz liczba sztuk według produktu są prawidłowe, a także czy elementy obejmują właściwe kolumny.
