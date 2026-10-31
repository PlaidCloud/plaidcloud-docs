---
title: Deactivate Workspace Members
description: Dezaktywuj członków obszaru roboczego wymienionych w tabeli projektu, dopasowanych według adresu e-mail lub nazwy użytkownika.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/deactivate-workspace-members.md
---

import { Aside } from '@astrojs/starlight/components';

## Opis

Dezaktywuje członków obszaru roboczego wskazanych w tabeli źródłowej. Używaj go do automatyzacji odejść z organizacji na podstawie wiarygodnej listy — wyciągu z HR lub przeglądu dostępów — zamiast dezaktywować osoby ręcznie.

Połącz go z krokiem [Get Workspace Members](/pl/reference/workflow-steps/general/get-workspace-members/), aby zbudować listę osób, które nie powinny już mieć dostępu.

<Aside type="caution" title="Odbiera dostęp">
  Każdy dopasowany członek traci dostęp po uruchomieniu kroku. Przed
  zaplanowaniem tego kroku sprawdź, czy tabela źródłowa zawiera tylko te osoby, które zamierzasz dezaktywować.
</Aside>

## Administratorzy obszaru roboczego na liście

[Administratora obszaru roboczego może dezaktywować tylko administrator obszaru roboczego](/pl/administration/access/member-management/#zmiana-administratora-obszaru-roboczego). Gdy krok jest uruchamiany bez uprawnień administratora obszaru roboczego, a jego lista zawiera administratorów, pozostawia ich aktywnych, dezaktywuje wszystkich pozostałych, a następnie kończy się błędem z komunikatem podającym, ilu członków zdezaktywował, i wymieniającym każdego pozostawionego jako aktywnego administratora. Członkowie, których zdezaktywował, pozostają zdezaktywowani. Aby zdezaktywować administratora, poproś administratora obszaru roboczego, aby zrobił to w Identity.

## Konfiguracja

### Parametr wyszukiwania elementów

Sposób dopasowania wierszy tabeli źródłowej do członków. Wybierz jedną z opcji:

- **E-mail** (domyślnie)
- **Nazwa użytkownika**

## Powiązane

- [Kroki ogólne](/pl/reference/workflow-steps/general/)
- [Get Workspace Members](/pl/reference/workflow-steps/general/get-workspace-members/)
- [Zarządzanie członkami](/pl/administration/access/)
