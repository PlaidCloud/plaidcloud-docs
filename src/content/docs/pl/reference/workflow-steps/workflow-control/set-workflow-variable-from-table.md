---
title: Set Workflow Variable Values from Table (krok)
description: Odczytuje wartości z tabeli projektu i przypisuje je do zmiennych przepływu pracy, aby kolejne kroki rozgałęziały się lub filtrowały na podstawie danych, a nie wartości zapisanych na stałe.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable-from-table.md
---

## Opis

Odczytuje wartości z tabeli projektu i przypisuje je do zmiennych przepływu pracy. Użyj go, aby sterować przepływem pracy jego własnymi danymi — odczytaj z tabeli kontrolnej ostatni zamknięty okres, liczbę wierszy lub ścieżkę pliku i pozwól kolejnym krokom się do nich odwoływać.

Zmienne ustawione tutaj istnieją przez czas uruchomienia przepływu pracy. Aby ustawić wartości utrzymujące się we wszystkich przepływach pracy w projekcie, użyj kroku [Set Project Variable Values from Table (krok)](/pl/reference/workflow-steps/workflow-control/set-project-variable-from-table/).

## Konfiguracja

### Kolumny źródłowe

Zmapuj każdą kolumnę źródłową na zmienną przepływu pracy, którą wypełnia. Krok odczytuje pojedynczy wiersz, więc przed jego uruchomieniem zawęź tabelę do jednego wiersza.

### Wybierz podzbiór danych

Wyrażenie filtru zawężające wiersze źródłowe — zwykle do jednego wiersza zawierającego potrzebne wartości.

### Zastosuj filtr dodatkowy do danych wynikowych

Filtr w stylu `HAVING` stosowany po agregacji, gdy wartość pochodzi z obliczenia grupowanego.

### Końcowe wycinanie tabeli danych (limit)

Domyślnie wyłączone, a po włączeniu ograniczone do jednego wiersza. Włącz je z jawnym uporządkowaniem, gdy źródło może zwrócić kilka wierszy kandydujących, a potrzebny jest konkretny z nich.

## Powiązane

- [Kroki sterowania przepływem pracy](/pl/reference/workflow-steps/workflow-control/)
- [Set Workflow Variable (krok)](/pl/reference/workflow-steps/workflow-control/set-workflow-variable/)
- [Set Project Variable Values from Table (krok)](/pl/reference/workflow-steps/workflow-control/set-project-variable-from-table/)
- [Zarządzaj zmiennymi przepływu pracy](/pl/guides/workflows/manage-workflow-variables/)
