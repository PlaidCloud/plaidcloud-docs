---
title: Ścieżka nauki Inżynieria danych
description: Co przeczytać przed laboratoriami Praktyk i Ekspert z inżynierii danych PlaidCloud i czego wymaga każde laboratorium.
sidebar:
  label: Inżynieria danych
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/data-engineering.md
---

Ścieżka Inżynieria danych dotyczy budowania przepływów pracy, które są poprawne, sterowane zmiennymi i szybkie. Zacznij od ścieżki [Podstawy](/pl/guides/certification/foundations/). Informacje o tym, jak działają laboratoria, znajdziesz w [Certyfikacja PlaidCloud](/pl/guides/certification/).

## Praktyk

### Czytaj w tej kolejności

1. [Utwórz przepływ pracy](/pl/guides/workflows/create-workflow/)
2. [Kroki przepływu pracy](/pl/reference/workflow-steps/), w szczególności [Table Inner Join](/pl/reference/workflow-steps/tables/table-inner-join/) i [Table Extract](/pl/reference/workflow-steps/tables/table-extract/)
3. [Zarządzanie zmiennymi przepływu pracy](/pl/guides/workflows/manage-workflow-variables/)
4. [Używaj ponownie swojej pracy: zmienne, makra i UDF](/pl/get-started/tutorials/reuse-variables-macros-udfs/)
5. [Uruchamianie przepływu pracy](/pl/guides/workflows/run-a-workflow/)
6. [Wyświetlanie dziennika przepływu pracy](/pl/guides/workflows/viewing-workflow-log/)

### Czego wymaga laboratorium

Laboratorium nosi nazwę *Inżynieria danych: miesięczne budowanie sprzedaży*.

Załadowane są trzy surowe tabele: wiersze sprzedaży, sklepy i produkty. W przepływie pracy laboratorium budujesz miesięczne podsumowanie z jednym wierszem na region i kategorię produktu, z liczbą sztuk i przychodem, dla sprzedanych wierszy jednego miesiąca. Miesiąc pochodzi ze zmiennej projektu, a nie z wartości wpisanej w kroku: laboratorium zmienia zmienną i uruchamia przepływ pracy ponownie. Używaj wyłącznie standardowych kroków, bez kroków SQL ani kodu.

Laboratorium sprawdza, czy przepływ pracy się uruchamia, czy używa tylko standardowych kroków oraz czy podsumowanie jest prawidłowe dla danego miesiąca i ponownie dla innego miesiąca.

## Ekspert

Laboratorium Ekspert jest na czas: masz 4 godziny od chwili jego rozpoczęcia.

### Czytaj w tej kolejności

1. [Debugowanie przepływu pracy](/pl/get-started/tutorials/debug-a-workflow/)
2. [Wyświetlanie dziennika przepływu pracy](/pl/guides/workflows/viewing-workflow-log/)
3. [Zarządzanie błędami kroków](/pl/guides/workflows/managing-step-errors/)
4. [Podgląd danych kroku](/pl/guides/workflows/preview-step-data/)
5. [Optymalizacja przepływu pracy](/pl/guides/workflows/optimize-a-workflow/)
6. [Kroki przepływu pracy](/pl/reference/workflow-steps/), w szczególności [Table Inner Join](/pl/reference/workflow-steps/tables/table-inner-join/)

### Czego wymaga laboratorium

Laboratorium nosi nazwę *Inżynieria danych Ekspert: napraw i przyspiesz nocną budowę*.

Nocny przepływ pracy przestał się uruchamiać, a wcześniej był stanowczo zbyt wolny. Czytasz dziennik uruchomienia, znajdujesz każdą przyczynę i naprawiasz przepływ pracy tak, aby kończył się powodzeniem, tworzył prawidłowe podsumowanie i działał w niewielkim ułamku dawnego czasu. Wiersze bez konta są pomijane, a konta wymienione dwukrotnie nie mogą zawyżać liczników. Używaj wyłącznie standardowych kroków i pozostaw tabele wejściowe bez zmian.

Laboratorium sprawdza, czy przepływ pracy się uruchamia, czy używa tylko standardowych kroków, czy podsumowanie jest prawidłowe, czy tabele wejściowe pozostały bez zmian oraz czy przepływ pracy jest wystarczająco szybki.
