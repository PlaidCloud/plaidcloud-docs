---
title: Get Workspace Members (krok)
description: Zapisz członków obszaru roboczego w tabeli projektu, wybierając, które pola tożsamości i aktywności uwzględnić.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## Opis

Zapisuje członków obszaru roboczego w tabeli projektu. Użyj go do raportowania dostępu, uzgadniania listy członków z danymi z systemu kadrowego lub sterowania krokiem następnym na podstawie tego, kto aktualnie ma dostęp.

## Konfiguracja

### Informacje do uwzględnienia

Domyślnie włączone: **Nazwisko**, **Imię**, **E-mail**, **Nazwa użytkownika**, **Data utworzenia elementu** i **Znacznik czasu ostatniego logowania**.

### Ustawienia dodatkowe

Domyślnie wyłączone:

- **Uwzględnij dezaktywowane elementy** — rozszerza wynik poza aktywnych członków.
- **Tryb historii logowania** — zwraca historię logowania, a nie tylko ostatnie logowanie.

## Dziennik Zabezpieczeń

Każde uruchomienie zapisuje w Dzienniku zabezpieczeń wpis z zapisanymi kolumnami, tabelą docelową, przepływem pracy, krokiem i uruchomieniem.

## Powiązane

- [Kroki ogólne](/pl/reference/workflow-steps/general/)
- [Deactivate Workspace Members (krok)](/pl/reference/workflow-steps/general/deactivate-workspace-members/)
- [Get Workspace Usage (krok)](/pl/reference/workflow-steps/general/get-workspace-usage/)
- [Zarządzanie członkami](/pl/administration/access/)
