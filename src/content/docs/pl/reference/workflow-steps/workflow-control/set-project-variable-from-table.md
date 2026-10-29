---
title: Set Project Variable Values from Table (krok)
description: Odczytuje wartości z tabeli projektu i przypisuje je do zmiennych projektu, które utrzymują się między uruchomieniami przepływów pracy.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable-from-table.md
---

## Opis

Odczytuje wartości z tabeli projektu i przypisuje je do zmiennych *projektu*. W odróżnieniu od kroku [Set Workflow Variable Values from Table (krok)](/pl/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/) wartości te utrzymują się po zakończeniu uruchomienia — każdy przepływ pracy w projekcie widzi je, dopóki coś ich ponownie nie zmieni.

Użyj go do stanu, który przetrwa pojedyncze uruchomienie: ostatniego pomyślnie załadowanego okresu, znacznika czasu (watermark) lub nazwy bieżącego scenariusza.

## Konfiguracja

### Kolumny źródłowe

Zmapuj każdą kolumnę źródłową na zmienną projektu, którą wypełnia. Krok odczytuje pojedynczy wiersz, więc przed jego uruchomieniem zawęź tabelę do jednego wiersza.

### Wybierz podzbiór danych

Wyrażenie filtru zawężające wiersze źródłowe.

### Zastosuj filtr dodatkowy do danych wynikowych

Filtr w stylu `HAVING` stosowany po agregacji.

### Końcowe wycinanie tabeli danych (limit)

Domyślnie wyłączone, a po włączeniu ograniczone do jednego wiersza. Włącz je z jawnym uporządkowaniem, gdy źródło może zwrócić kilka wierszy kandydujących.

## Powiązane

- [Kroki sterowania przepływem pracy](/pl/reference/workflow-steps/workflow-control/)
- [Set Project Variable (krok)](/pl/reference/workflow-steps/workflow-control/set-project-variable/)
- [Set Workflow Variable Values from Table (krok)](/pl/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)
