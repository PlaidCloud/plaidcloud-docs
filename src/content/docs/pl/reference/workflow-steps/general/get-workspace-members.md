---
title: Get Workspace Members
description: Zapisz członków obszaru roboczego do tabeli projektu, wybierając pola tożsamości i aktywności do uwzględnienia.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## Opis

Zapisuje członków obszaru roboczego do tabeli projektu. Użyj tego kroku, aby raportować dostęp, uzgadniać listę członków z danymi z systemu kadrowego lub sterować kolejnym krokiem na podstawie tego, kto ma obecnie dostęp.

## Konfiguracja

### Informacje do uwzględnienia

Domyślnie włączone: **Nazwisko**, **Imię**, **E-mail**, **Nazwa użytkownika**, **Data utworzenia elementu** i **Znacznik czasu ostatniego logowania**.

### Ustawienia dodatkowe

Domyślnie wyłączone:

- **Uwzględnij dezaktywowane elementy** — rozszerza wynik poza aktywnych członków.
- **Tryb historii logowania** — zwraca historię logowania zamiast tylko ostatniego logowania.

## Dziennik zabezpieczeń

Każde uruchomienie zapisuje w Dzienniku zabezpieczeń wpis z zapisanymi kolumnami, tabelą docelową, przepływem pracy, krokiem i uruchomieniem.

## Powiązane

- [Kroki ogólne](/pl/reference/workflow-steps/general/)
- [Deactivate Workspace Members](/pl/reference/workflow-steps/general/deactivate-workspace-members/)
- [Get Workspace Usage](/pl/reference/workflow-steps/general/get-workspace-usage/)
- [Zarządzanie członkami](/pl/administration/access/)
