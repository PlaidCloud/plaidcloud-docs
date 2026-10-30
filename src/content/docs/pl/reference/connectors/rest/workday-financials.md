---
title: Łącznik Workday Financials
description: Skonfiguruj połączenie Workday Financials w PlaidCloud z użytkownikiem systemu integracji, aby importować dane przez raport RaaS i księgować zapisy dziennika przez SOAP.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday-financials.md
---

## Dokumentacja API

Interfejsy używane przez ten łącznik opisują [usługi sieciowe SOAP](https://community.workday.com/sites/default/files/file-hosting/productionapi/) oraz [Report-as-a-Service (RaaS)](https://doc.workday.com/) firmy Workday.

## Jak działa uwierzytelnianie

Połączenie uwierzytelnia się jako **użytkownik systemu integracji (ISU)** — typ użytkownika Workday przeznaczony do integracji między systemami, zabezpieczony przez Integration System Security Group, która przyznaje mu wyłącznie dostęp potrzebny temu łącznikowi (dostęp do raportów przy odczycie, proces biznesowy Submit Accounting Journal przy księgowaniu). Żądania zawierają nazwę użytkownika i hasło ISU; nie ma interaktywnego logowania.

## Konfiguracja

| Pole | Typ | Opis |
|---|---|---|
| Name | Tekst | Wyświetlana nazwa tego połączenia. |
| Tenant Host | Tekst | Host Workday, np. `wd5-impl.workday.com`. |
| Tenant Name | Tekst | Nazwa Twojego tenanta Workday. |
| ISU Username | Tekst | Nazwa użytkownika systemu integracji. |
| ISU Password | Tekst | Hasło użytkownika systemu integracji. Przechowywane w postaci zaszyfrowanej. |

## Importowanie danych

Workday Financials nie ma stałego zestawu gotowych jednostek. Zamiast tego krok **Import Workday Entity** wywołuje **raport Report-as-a-Service (RaaS)**, który budujesz w Workday i publikujesz z dostępem Web Service — podajesz jego adres URL. Krok obsługuje filtry `company`, `ledger`, `period`, `accounting_date` (zakres), `ledger_account` (zakres) i `cost_center`, z których każdy jest przekazywany jako parametr raportu, więc filtr działa tylko wtedy, gdy raport definiuje odpowiedni monit. Pełny opis pól znajdziesz w [Import Workday Entity](/pl/reference/workflow-steps/workday-financials/import-workday-entity/).

## Księgowanie zapisów dziennika

Krok **Workday Financials: Post Journal Entry** księguje zapisy księgowe przez wspólny potok zapisu ERP PlaidCloud, używając operacji SOAP `Submit_Accounting_Journal` w Workday i odpytując stan procesu biznesowego zapisu aż do stanu końcowego, zanim zgłosi go jako zaksięgowany. Korekta księguje nowy zapis odwracający z zamienionymi stronami Wn/Ma zamiast edytować oryginał. Opis pól znajdziesz w [Workday Financials: Post Journal Entry](/pl/reference/workflow-steps/workday-financials/workday-post/), a pełny opis księgowania w [Połączenie z Workday Financials](/pl/guides/connections/workday-financials/).

## Znane ograniczenia

| Ograniczenie | Co oznacza |
|---|---|
| Kształt importu zależy od Twojego raportu RaaS | PlaidCloud nie ma gotowych jednostek dla Workday Financials — pola raportu, monity i kontrola dostępu znajdują się w Workday. Zmiana raportu w Workday może zmienić kształt importu bez żadnej zmiany po stronie PlaidCloud. |
| Zatwierdzanie w procesie biznesowym wydłuża czas | Zapis przekazany do kroku zatwierdzania w procesie biznesowym Submit Accounting Journal pozostaje w stanie `pending` do czasu zatwierdzenia w Workday; odpytywanie stanu końcowego czeka na to zatwierdzenie. |
## Powiązane

- [Połączenie z Workday Financials (przewodnik)](/pl/guides/connections/workday-financials/) — krok po kroku: utwórz połączenie, przetestuj je, zaimportuj raport i zaksięguj zapis dziennika.
- [Import Workday Entity](/pl/reference/workflow-steps/workday-financials/import-workday-entity/)
- [Workday Financials: Post Journal Entry](/pl/reference/workflow-steps/workday-financials/workday-post/)
- [Przegląd historii księgowań ERP](/pl/guides/connections/erp-post-history/)
- [Łącznik Workday REST](/pl/reference/connectors/rest/workday/) — osobny, ogólny łącznik Workday dla danych REST HR i płac.
