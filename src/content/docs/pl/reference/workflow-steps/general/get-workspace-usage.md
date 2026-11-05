---
title: Get Workspace Usage (krok)
description: Zapisz sumy użycia obszaru roboczego z Raportów użycia w tabeli projektu, według dni lub miesięcy, aby tworzyć wykresy adopcji lub zasilać kolejny krok.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Opis

Zapisuje podsumowanie sposobu korzystania z obszaru roboczego w tabeli projektu. Użyj go do śledzenia adopcji w czasie, budowania własnych pulpitów użycia lub sygnalizowania spadku aktywności w zaplanowanym przepływie pracy. Dane są takie same jak te, które pokazują [Raporty użycia](/pl/administration/access/usage-reports/).

Wynik zawiera wyłącznie sumy. Żaden wiersz nie wskazuje członka, a ścieżki notatników są zastąpione znakiem `*`. Członkowie, których dane użycia zostały usunięte, są pomijani.

## Konfiguracja

### Dane użycia

**Zbiór danych** określa, co zawiera każdy wiersz:

| Zbiór danych | Jeden wiersz dla każdego | Kolumny |
|---|---|---|
| **Dzienne według elementu** | dnia, dziedziny, zdarzenia i podmiotu | `day`, `source`, `event`, `subject`, `events` |
| **Miesięczne według elementu** | miesiąca, dziedziny, zdarzenia i podmiotu | `month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial` |
| **Sumy miesięczne** (domyślnie) | miesiąca i dziedziny | `month`, `source`, `active_users`, `coverage_start`, `partial` |

`partial` ma wartość true dla miesiąca, którego historia nie obejmuje w całości, a `coverage_start` to data rozpoczęcia zbierania danych.

**Dziedzina** ogranicza wiersze do jednej dziedziny: **Aplikacja PlaidCloud**, **Pulpity**, **Aplikacje**, **Odwiedziny aplikacji** lub **Notatniki**. Pozostaw **Wszystkie dziedziny**, aby uwzględnić wszystkie.

### Zakres dat

**Zakres** określa dni do odczytania:

- **Ostatnia liczba dni** (domyślnie 30) odczytuje ostatnie dni, łącznie z dzisiejszym.
- **Poprzedni miesiąc** odczytuje ostatni pełny miesiąc kalendarzowy.
- **Od początku miesiąca** odczytuje dane od pierwszego dnia bieżącego miesiąca do dziś.
- **Między datami** odczytuje dane od **Data początkowa** do **Data końcowa**. Pozostaw pole **Data końcowa** puste, aby czytać do dziś.

Dni i daty są w UTC. Pola **Dni**, **Data początkowa** i **Data końcowa** akceptują [zmienną](/pl/guides/workflows/manage-workflow-variables/), taką jak `{report_start}`, a także liczbę lub datę w formacie `YYYY-MM-DD`. Początek nie może przypadać po końcu.

### Cel użycia

**Tabela docelowa** otrzymuje wynik. Krok zastępuje wszystko, co zawierała tabela, i zawsze zapisuje kolumny zbioru danych, nawet gdy nie ma wierszy.

## Ostrzeżenia

Nie powodują one niepowodzenia kroku. Krok kończy się ostrzeżeniem, które mówi, co się stało, i nadal zapisuje tabelę:

- Zbieranie danych użycia nie zostało jeszcze skonfigurowane dla obszaru roboczego.
- W zakresie nie było użycia.
- Zakres zaczyna się przed okresem przechowywania danych, więc został skrócony do początku historii. Dane dzienne są przechowywane przez 180 dni, a miesięczne przez 25 miesięcy.

## Dziennik zabezpieczeń

Każde uruchomienie zapisuje w Dzienniku zabezpieczeń wpis ze zbiorem danych, zakresem, tabelą docelową, przepływem pracy, krokiem i uruchomieniem oraz liczbą zapisanych wierszy.

## Powiązane

- [Kroki ogólne](/pl/reference/workflow-steps/general/)
- [Raporty użycia](/pl/administration/access/usage-reports/)
- [Get Workspace Members (krok)](/pl/reference/workflow-steps/general/get-workspace-members/)
